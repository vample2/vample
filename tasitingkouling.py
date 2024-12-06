import time

import requests
import json

import json
import base64
import urllib.parse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def exchange(param, token):
    url = "https://sss-web.tastientech.com/api/selfCoupon/watchword/exchange"
    payload = param
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'Content-Type': "application/json",
        'version': "3.1.0",
        'xweb_xhr': "1",
        'user-token': token,
        'channel': "1",
        'Sec-Fetch-Site': "cross-site",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Dest': "empty",
        'Referer': "https://servicewechat.com/wx557473f23153a429/368/page-frame.html",
        'Accept-Language': "zh-CN,zh;q=0.9"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    print(response.text)


def aes_cbc_encrypt(e):
    """
    模拟 JavaScript 的加密函数
    :param e: 包含 aesKey, ivSeed 和 content 的字典
    :return: 加密后的 URL 安全字符串
    """
    try:
        # 参数完整性检查
        if not e.get("aesKey") or not e.get("ivSeed") or not e.get("content"):
            raise ValueError("参数不完整")

        # 转换为字节
        aes_key = e["aesKey"].encode("utf-8")
        iv_seed = e["ivSeed"].encode("utf-8")
        content = e["content"].encode("utf-8")

        # 初始化 AES 加密器
        cipher = AES.new(aes_key, AES.MODE_CBC, iv_seed)
        encrypted = cipher.encrypt(pad(content, AES.block_size))

        # Base64 编码并 URL 安全替换
        encrypted_base64 = base64.b64encode(encrypted).decode("utf-8")
        encrypted_url_safe = encrypted_base64.replace("+", "%2B").replace("/", "%2F")

        return encrypted_url_safe

    except Exception as t:
        print("AES CbcEncrypt Error!", {
            "param": json.dumps(e, ensure_ascii=False),
            "error": str(t)
        })
        return ""


def Sign(payload):
    e = {
        "aesKey": "aZ3uXd2hXupRxvHZ",
        "ivSeed": "1513D520B9C1459C",
        "content": json.dumps(payload, separators=(",", ":"))  # 转换为 JSON 字符串
    }

    sign = aes_cbc_encrypt(e)
    return sign


token_list = [
    ""
]
# 示例数据
payload = {
    "activityId": 1576,
    "randomCode": "7c3e63617eb746649320b75376c307fa",
    "watchword": "冰嬉",
    "timestamp": int(time.time() * 1000),
}

sign = Sign(payload)
print(sign)
payload["sign"] = sign
print(payload)
for index, token in enumerate(token_list):
    exchange(payload, token)
