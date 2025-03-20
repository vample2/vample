import nonebot_plugin_imagetools
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.params import CommandArg
from nonebot.params import ArgPlainText
from httpx import AsyncClient
from nonebot.adapters.qq import MessageSegment,Message
import re
import json
from bs4 import BeautifulSoup
import urllib.parse
import qrcode
from pathlib import Path
from nonebot.matcher import Matcher
import validators

JDcoupon = on_command("优惠券提取", rule=to_me(), aliases={"京东优惠券", "优惠券链接"}, priority=10)


@JDcoupon.handle()
async def handle_function(matcher: Matcher, args: Message = CommandArg()):
    if args.extract_plain_text():
        matcher.set_arg("url", args)


@JDcoupon.got("url", prompt="输入网址")
async def got_location(url: str = ArgPlainText()):
    # 拆分用户输入的地名
    # 初始化变量，避免在异常处理时出现问题
    if not validators.url(url):
        await JDcoupon.reject("❌ 请输入一个有效的网址")

    async with AsyncClient(follow_redirects=True) as session:
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        }

        response = await session.get(url=url, headers=headers)
        html_content = response.text
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        # # 使用正则表达式提取 window.__react_data__ 的值
        react_data_script = soup.find('script', string=re.compile(r'window\.__react_data__'))

        if react_data_script:
            # 使用正则提取 window.__react_data__ 的内容
            react_data = re.search(r'window\.__react_data__ = ({.*?});', react_data_script.string, re.DOTALL)
            if react_data:
                # 提取的 JSON 字符串
                react_data_json = react_data.group(1)
                data = json.loads(react_data_json)  # 解析 JSON 数据["activityData"]["floorList"][6]["couponList"]
                for index,couponlist_data in enumerate(data["activityData"]["floorList"]):
                    # couponList = couponlist_data["couponList"]
                    if 'couponList' in couponlist_data:
                        for coupon_list in couponlist_data['couponList']:
                            # coupon_list = couponlist_data['couponList'][0]
                            # print(coupon_list)

                            if "flexibleData" in coupon_list:
                                args = coupon_list["args"]
                                flexibleData = coupon_list["flexibleData"]
                                scope = flexibleData['scope']
                                limit = flexibleData['limit']
                                discount = flexibleData["discount"]
                                body = json.dumps({"activityId": "3H885vA4sQj6ctYzzPVix4iiYN2P",
                                                   "scene": "1",
                                                   "args": args,
                                                   "log": "1,1"
                                                   # "log": log_list[i]['log'],
                                                   # "random": log_list[i]['random']
                                                   }
                                                  )
                                encoded_data = urllib.parse.quote(body)
                                link = f"https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&client=wh5&body={encoded_data}"
                                qr = qrcode.make(link)

                                # 本地保存二维码图片
                                qr_path = f"qr_code{index}.png"
                                qr.save(qr_path)
                                message = Message([
                                    f"📍 范围：{scope}",
                                    f"💰 门槛：{limit}",
                                    f"🔻 折扣：{discount}",
                                    MessageSegment.file_image(Path(qr_path)),
                                ])
                                await JDcoupon.send(message)

        await JDcoupon.finish("已发送完成")

