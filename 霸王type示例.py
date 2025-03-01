import execjs


def generate_type(js_file,url,data):
    with open(js_file, "r", encoding="utf-8") as f:
        js_code = f.read()

    # 使用 execjs 执行 JavaScript
    ctx = execjs.compile(js_code)
    generatetype__1475 = ctx.call("type",url,data)

    return generatetype__1475



import requests
import json
url='https://miniapp.qmai.cn/web/catering2-apiserver/coupon/wx-coupon-list'
headers = {
    'authority': 'miniapp.qmai.cn',
    'accept': 'v=1.0',
    'accept-language': 'zh-CN',
    'channelcode': '',
    'content-type': 'application/json',
    'gdt-vid': '',
    'multi-store-id': '',
    'promotion-code': '',
    'qm-from': 'wechat',
    'qm-from-type': 'catering',
    'qm-user-token': '',
    'qz-gtd': '',
    'referer': 'https://servicewechat.com/wxafec6f8422cb357b/222/page-frame.html',
    'scene': '1256',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'store-id': '49006',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555',
    'work-staff-id': '',
    'work-staff-name': '',
    'work-wechat-userid': '',
    'xweb_xhr': '1',
}

params = {
    'appid': 'wxafec6f8422cb357b',
}
type__1475=generate_type("type_1475.js",url,params)
params['type__1475']=type__1475
print(params)

response = requests.get(url=url, params=params, headers=headers)
print(response)
print(response.text)
