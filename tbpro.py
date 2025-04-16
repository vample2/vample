import nonebot_plugin_imagetools
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.qq import MessageSegment, Message
import re
import json
from nonebot.matcher import Matcher
import validators
import re
from urllib.parse import urlparse, parse_qs
from nonebot.params import CommandArg, ArgPlainText
import requests
import time
import qrcode
from pathlib import Path
JDcoupon = on_command("淘宝直链", rule=to_me(), aliases={"淘宝商品直链"}, priority=10, block=True)


# ================= 工具函数 ==================
# 淘宝短链判断
def is_taobao_short_link(u):
    parsed = urlparse(u)
    return parsed.netloc in {"m.tb.cn", "s.tb.cn", "e.tb.cn"}


def extract_real_url_from_short(u):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        resp = requests.get(u, headers=headers)
        html = resp.text
        match = re.search(r"url\s*=\s*'(https?://[^']+)'", html)
        if match:
            return match.group(1)
    except Exception as e:
        print("短链解析失败：", e)
    return None


def get_shopId(real_url):
    parsed = urlparse(real_url)
    query = parse_qs(parsed.query)
    item_id = query.get('itemId', [None])[0] or query.get('id', [None])[0]
    return item_id


def get_t_sign(shopId):
    current_time_millis = int(time.time() * 1000)
    shop_id_length = len(shopId)
    t_sign = str(shop_id_length * 357) + str(current_time_millis) + "aliapi@!android"

    return t_sign


def get_skuinfo(shopId):
    headers = {
        "f_client": "android",
        "f_version": "356",
        "os": "android",
        "appversion": "356",
        "Host": "101.33.242.223:5036",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9"
    }
    url = "http://101.33.242.223:5036/ali/getInfo"
    params = {
        "shopId": shopId,
        "token": "",##添加自己的浮动时间token
        "f_t": int(time.time() * 1000),
        # "f_sign": "b9674b8c4228e77c5a70f1bf2cfb64ff"
    }
    f_sign = get_t_sign(params['shopId'])
    params['f_sign'] = f_sign
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text)
    propath_map = {i["path"]: i["itemName"] for i in data["propath"][0]}
    merged_list = [{"itemName": propath_map[sku["propPath"]], "skuId": sku["skuId"], "priceText": sku["priceText"]}
                   for sku in
                   data["skuInfo"] if sku["propPath"] in propath_map]
    return merged_list



# ================= 事件响应 ==================

@JDcoupon.handle()
async def handle_function(matcher: Matcher, args: Message = CommandArg()):
    # 处理初始输入，提取商品链接
    if args.extract_plain_text():
        matcher.set_arg("url", args)


@JDcoupon.got("url", prompt="请输入淘宝商品链接")
async def got_location(matcher: Matcher, url: str = ArgPlainText()):
    # 处理商品链接，获取店铺信息和SKU列表
    if is_taobao_short_link(url):
        real_url = extract_real_url_from_short(url)
        if not real_url:
            await JDcoupon.finish("❌ 短链解析失败")
    else:
        real_url = url

    # 获取店铺 ID 和 SKU 信息
    shopId = get_shopId(real_url)
    sku_list = get_skuinfo(shopId)

    # 如果没有 SKU 列表，结束流程
    if not sku_list:
        await JDcoupon.finish("❌ 没有找到商品信息")

    # 将 SKU 列表保存到 matcher.state
    matcher.state["shopId"] = shopId
    matcher.state["sku_list"] = sku_list
    print(sku_list)

    # 展示 SKU 列表
    msg_lines = ["可选商品："]
    for idx, item in enumerate(sku_list):
        msg_lines.append(f"[{idx + 1}] {item['itemName']} - ￥{item['priceText']}")

    await matcher.send("\n".join(msg_lines))


@JDcoupon.got("sku_choice", prompt="请输入你想选择的商品序号：")
async def choose_product(matcher: Matcher, sku_choice: str = ArgPlainText()):
    # 验证用户输入的商品序号
    try:
        sku_choice = int(sku_choice)  # 将输入转换为整数
        if sku_choice < 1 or sku_choice > len(matcher.state["sku_list"]):  # 检查是否在有效范围内
            raise ValueError("无效的序号")
    except ValueError:
        await matcher.reject("❌ 请输入一个有效的商品序号！")  # 输入无效时拒绝并提示

    # 从 matcher.state 中获取选择的 SKU 信息
    selected_sku = matcher.state["sku_list"][sku_choice - 1]  # 因为索引从 0 开始，减去 1
    item_name = selected_sku["itemName"]
    price = selected_sku["priceText"]
    skuId=selected_sku["skuId"]

    # 提供反馈，告知用户选择的商品
    product_link = f"https://h5.m.taobao.com/awp/base/buy.htm?buyParam={matcher.state['shopId']}_1_{skuId}"
    print(product_link)
    qr = qrcode.make(product_link)

    # 本地保存二维码图片
    qr_path = f"tbpro_code.png"
    qr.save(qr_path)
    message = Message([
        MessageSegment.text(
            f"你选择的商品是：\n"
            f"{item_name} - ￥{price}\n"
            f"📍 直链：扫码查看 \n"
        ),
        MessageSegment.file_image(Path(qr_path))
    ])

    await matcher.send(message)
    # await JDcoupon.finish("已发送完成")
