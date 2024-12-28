import base64
import os
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from urllib3.exceptions import InsecureRequestWarning
import urllib3
import json
import logging
import requests
import re
import subprocess
from functools import partial
import time

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs

# import CHERWIN_TOOLS
# 禁用安全请求警告
urllib3.disable_warnings(InsecureRequestWarning)

# 配置 logging 模块
logging.basicConfig(level=logging.INFO,
                    format='\033[33m[%(asctime)s][%(levelname)s]:\033[0m%(message)s')






def JD_shop_point(login_rl):
    session = requests.Session()
    headers = {
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                }

    response = session.get(url=login_rl, headers=headers)
    # print(response)
    # print(response.text)
    # print(session.cookies.get_dict())
    if response.status_code == 200:
        print("登录成功")
        message = getTokenKeyStr(session)
        # print(message)
        key = get_key(message)
        # print(key)
        duiba_token_str = get_keytoken(key, session)
        orderNum = JD_shop_query(session, duiba_token_str)
    #     if orderNum is not None:
    #         Log("查询积分商店签到结果")
    #         time.sleep(2)
    #         get_shop_result(session, orderNum)


def get_key(data):
    # 使用正则表达式提取 script 标签中的内容
    ctx = execjs.compile(data)
    duiba_token_str = ctx.eval('ohjaiohdf.toString()')
    # print(duiba_token_str)
    key_match = re.search(r"var\s+key\s+=\s+'([^']+)';", duiba_token_str)
    if key_match:
        key = key_match.group(1)
        print(f"获取 key:{key}")
        # Log(key)
        return key
    else:
        print("未找到 key")
    return None
    # pattern = r'<script type="text/javascript">\s*/\*\s*\*\s*获取token\s*\*/\s*[\s\S]*?<\/script>'
    # match = re.search(pattern, data)

    # if match:
    #     # 提取匹配到的脚本内容
    #     text = match.group(0)

    #     # 替换 <script> 和 </script>
    #     code = text.replace('<script type="text/javascript">', '').replace('</script>', '')
    #     # print(code)
    #     ctx = execjs.compile(code)
    #     duiba_token_str = ctx.eval('ohjaiohdf.toString()')
    #     key_match = re.search(r"var\s+key\s+=\s+'([^']+)';", duiba_token_str)
    #     if key_match:
    #         key = key_match.group(1)
    #         Log(f"获取 key:{key}")
    #         # Log(key)
    #         return key
    #     else:
    #         print("未找到 key")
    #     return None
    # else:
    #     print("未找到匹配的脚本")
    #     return None


def getTokenKeyStr(session):
    # 获取 key 的请求
    key_url = 'https://96126.activity-19.m.duiba.com.cn/projectx/p71c499de/getTokenKey'
    headers = {
        'accept': '*/*',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'referer': 'https://96126.activity-19.m.duiba.com.cn/projectx/p71c499de/index.html?&app_key=zd49bb086bcfdf8ae4&appId=97276&channel=0&from=login&spm=97276.1.1.1',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    timestamp_str=str(int(time.time()*1000))
    params = {
    '_t': [
        timestamp_str,
        timestamp_str,
    ],
}
    response = session.get(key_url, headers=headers,params=params)
    # print(response)
    # print(response.text)
    return response.text


# 获取 token 值
# 获取 token 值
def get_token(session):
    params = {
        '_': int(time.time() * 1000)
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'priority': 'u=1, i',
        'referer': 'https://96126.activity-19.m.duiba.com.cn/projectx/p71c499de/index.html?&app_key=zd49bb086bcfdf8ae4&appId=97276&channel=0&from=login&spm=97276.1.1.1',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    response = session.get(f'https://96126.activity-19.m.duiba.com.cn/projectx/p71c499de/getToken', params=params,
                            headers=headers)
    print(response)
    # print(response.text)
    if response.status_code == 200:
        # print(response.text)
        win_info = response.json()
        win_data = win_info["data"]

        return win_data


def simulate_window_and_execute(js_code):
    # 模拟 `window` 对象和创建一个环境来执行 JavaScript 代码
    js_env = """
    var window = {};  // 创建一个简化的 window 对象
    function runCode(code) {
        eval(code);  // 执行传入的 JavaScript 代码
        return window;  // 返回模拟的 window 对象
    }
    """
    ctx = execjs.compile(js_env)
    return ctx.call('runCode', js_code)


def get_keytoken(key, session):
    # 获取 token
    win_token = get_token(session)

    # 执行并模拟 `window`
    result = simulate_window_and_execute(win_token)

    # 获取 token 值
    duiba_token_str = result.get(key)  # 替换为实际的 key
    print(f"duiba_token:{duiba_token_str}")
    return duiba_token_str


def get_shop_result(session, orderNum):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/6.8.0(0x16080000) NetType/WIFI MiniProgramEnv/Mac MacWechat/WMPF MacWechat/3.8.8(0x13080812) XWEB/1216',
        'referer': "https://96108.activity-42.m.duiba.com.cn/sign/component/page?signOperatingId=275335335642857",
    }
    params = {
        'orderNum': orderNum,
        '_': int(time.time() * 1000)
    }
    response = session.get("https://96108.activity-42.m.duiba.com.cn/sign/component/signResult", params=params,
                           headers=headers)
    # Log(response)
    message = response.json()
    Log(message)
    signResult = message["data"]["signResult"]
    credits = message["data"]["credits"]
    if signResult == 2:
        Log(f'签到成功，获得【{credits}】个幸运币')



def JD_shop_query(session, duiba_token_str):
    url = "https://96126.activity-19.m.duiba.com.cn/projectx/p71c499de/scrape/draw.do"

    params = {
    'token': str(duiba_token_str),
    'user_type': '1',
    'is_from_share': '1',
    '_t': str(int(time.time()*1000)),
}

    # payload = f"signOperatingId=275335335642857&token={duiba_token_str}"

    headers = {
        'accept': '*/*',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    response = session.post(url, params=params, headers=headers)
    if response.status_code == 200:
        message = response.json()
        print(message)
        # if message.get('data') is None or message['data'].get('orderNum') is None:
        #     print(message.get('desc'))  # Print the description if 'orderNum' is missing
        # else:
        #     orderNum = message['data']['orderNum']
        #     print(f"Order number: {orderNum}")
        #     return orderNum


def Log(cont):
    global send_msg
    logging.info(cont)
    if cont:
        send_msg += f'{cont}\n'


def pushplus(send_msg):
    token = 'b8b60c4c66224859b140b786e504b837'  # 在pushpush网站中可以找到
    title = '幸运咖签到'  # 改成你要的标题内容 # 改成你要的正文内容
    url = 'http://www.pushplus.plus/send'
    data = {
        "token": token,
        "title": title,
        "content": send_msg
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=body, headers=headers)

def get_code(token):
    url = "https://msmarket.msx.digitalyili.com/developer/oauth2/buyer/authorize"

    params = {
    'app_key': "zd49bb086bcfdf8ae4"
    }

    headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
    'register-source': "",
    'access-token': token,
    'forward-appid': "",
    'source-type': "",
    'content-type': "application/json",
    'atv-page': "",
    'shareid': "oWT3_49LZ3yMNfOouEs-p43ihpJk",
    'scene': "1007",
    'xweb_xhr': "1",
    'tenant-id': "1718857849685876737",
    'channel': "message",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://servicewechat.com/wxf32616183fb4511e/648/page-frame.html",
    'accept-language': "zh-CN,zh;q=0.9"
    }

    response = requests.get(url, params=params, headers=headers)

    # print(response.text)
    code=response.json()["data"]
    return code

def get_loginurl(code):
    url = "https://96126.activity-19.m.duiba.com.cn/wechat/yili/autoLogin"

    params = {
    'code': code,
    'appId': "97276",
    'redirectUrl': "https://96126.activity-19.m.duiba.com.cn/projectx/p71c499de/index.html?appID=97276&app_key=zd49bb086bcfdf8ae4&appId=97276&channel=0"
    }

    headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
    'sec-ch-ua': "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
    'x-requested-with': "XMLHttpRequest",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "\"Windows\"",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'accept-language': "zh-CN,zh;q=0.9",
    }

    response = requests.get(url, params=params, headers=headers)

    # print(response.text)
    login_url = response.json()['data']['redirectUrl']
    return login_url
if __name__ == '__main__':
    # login_url="https://96126.activity-19.m.duiba.com.cn/autoLogin/autologin?dcustom=unionId%253Do6QWL1OEF71Vca4gSMzIkRo36Qy0%2526openId%253DoWT3_49LZ3yMNfOouEs-p43ihpJk%2526registerTimestamp%253D1672632705000%2526ip%253D111.38.164.29%2526mobile%253D18156199271%2526accessTokenExpireTime%253D1735392974928%2526avatar%253Dhttps%253A%252F%252Fyshop-cos.yili.com%252Fassets%252Fauth%252Fyshop%252F11.png%2526accessToken%253D8id7NZKISVBf3JpGH%25252BKkDlFPtCyZdC%25252BEpFOJhYZglmwgNW8Gh8gnNUYzPbaJjZ92Mc%25252Bpjvx9SNLXpNsGs7NIHA%25253D%25253D%2526userId%253D1552928644285122338%2526registerSource%253D1563%2526refreshTokenExpireTime%253D1735394774928%2526openWxStep%253Dfalse%2526nickname%253D%25E5%25BF%25A7%25E9%2583%2581%25E7%259A%2584%25E6%259C%258D%25E9%25A5%25B0%2526tenantId%253D1718857849685876737%2526refreshToken%253DXYdBLL%25252FDvGyVtBAtx7%25252FwCbC9c2biSu7td4eU42rRCIaQ7UJwTNhJQRTmGVFtGkVwHpxV0IeR4%25252FtGAx773GXlau%25252B93u%25252BqiTeuYF%25252BzR8649UO9nSKDduKT5wx%25252FF0a%25252FlcD8%25252FnWDNl6dib0jCTTpqfoFOzHTctkPK74h5G8j3CmgRbI%25253D&redirect=https%3A%2F%2F96126.activity-19.m.duiba.com.cn%2Fprojectx%2Fp71c499de%2Findex.html%3FappID%3D97276%26app_key%3Dzd49bb086bcfdf8ae4%26appId%3D97276%26channel%3D0&uid=1552928644285122338&credits=35&sourceType=4&sign=dfbb72cc700163c45e59cbc22dd789c1&appKey=CXaq2gmukK99fVGYgnFmmc4t1jG&timestamp=1735389375152&"
    # 
    tokens=[

    ]
    for token in tokens:
        code=get_code(token)
        login_url=get_loginurl(code)
        JD_shop_point(login_url)




    
