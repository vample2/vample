from curl_cffi import requests
from Crypto.Cipher import AES
import base64
import time
import execjs
import re
import json
import urllib.parse
def decrypted(encrypted):
    key = b"3C8C48E792E9241B"  # 16 字节密钥
    iv = b"cDOiBC1n2QrkAY2P"   # 初始化向量

    # Base64 解码密文
    encrypted_bytes = base64.b64decode(encrypted)

    # 创建 AES 解密器
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 解密数据
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # 手动移除 ZeroPadding
    def zero_unpad(data):
        return data.rstrip(b'\x00')

    # 处理解密后的数据
    decrypted = zero_unpad(decrypted_bytes).decode('utf-8')

    print("解密后的明文:", decrypted)
    return decrypted

def encrypt(plaintext,key=b"3C8C48E792E9241B",iv=b"cDOiBC1n2QrkAY2P" ):

    # 定义块大小
    block_size = AES.block_size  # 通常为 16 字节

    # 手动实现 ZeroPadding
    def zero_pad(data, block_size):
        padding_len = block_size - (len(data) % block_size)
        return data + b'\x00' * padding_len

    # 明文需要先进行填充 (ZeroPadding)
    padded_plaintext = zero_pad(plaintext.encode('utf-8'), block_size)

    # 创建 AES 加密器
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 加密明文
    encrypted_bytes = cipher.encrypt(padded_plaintext)

    # 转换为 Base64 字符串
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')

    print("密文 (Base64):", encrypted_base64)
    return encrypted_base64
    
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
def getTokenKeyStr(session):
    # 获取 key 的请求
    url = "https://96984.activity-19.m.duiba.com.cn/projectx/pb9acddd2/getTokenKey"
    timestamp = str(int(time.time()))
    params = {
    '_t': timestamp,
    '_t': timestamp
    }

    headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 13; IN2010 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.103 Mobile Safari/537.36 XWEB/1300149 MMWEBSDK/20240501 MMWEBID/4970 MicroMessenger/8.0.50.2701(0x2800325B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxd25dc8ba975776e3",
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'sec-ch-ua-platform': "\"Android\"",
    'sec-ch-ua': "\"Chromium\";v=\"130\", \"Android WebView\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    'sec-ch-ua-mobile': "?1",
    'x-requested-with': "com.tencent.mm",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "no-cors",
    'sec-fetch-dest': "script",
    'referer': "https://96984.activity-19.m.duiba.com.cn/projectx/pb9acddd2/index.html?appID=96984&code=&from=&roomId=&shareCode=&propCode=8K70EX&from=login&spm=96984.1.1.1",
    'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = session.get(url, params=params, headers=headers)

    # print(response.text)
    # print(response)
    # print(response.text)
    return response.text
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
def get_token(session):
    url = "https://96984.activity-19.m.duiba.com.cn/projectx/pb9acddd2/getToken"

    params = {
    '_t': str(int(time.time()*1000))
    }

    headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 13; IN2010 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.103 Mobile Safari/537.36 XWEB/1300149 MMWEBSDK/20240501 MMWEBID/4970 MicroMessenger/8.0.50.2701(0x2800325B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxd25dc8ba975776e3",
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'sec-ch-ua-platform': "\"Android\"",
    'sec-ch-ua': "\"Chromium\";v=\"130\", \"Android WebView\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    'content-type': "application/x-www-form-urlencoded",
    'sec-ch-ua-mobile': "?1",
    'x-requested-with': "com.tencent.mm",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://96984.activity-19.m.duiba.com.cn/projectx/pb9acddd2/index.html?appID=96984&code=&from=&roomId=&shareCode=&propCode=8K70EX&from=login&spm=96984.1.1.1",
    'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=1, i",
    }

    response = session.get(url, params=params, headers=headers)

    # print(response.text)
    win_info = response.json()
    win_data = win_info["data"]

    return win_data
def startgame(session):

    url = "https://96984.activity-19.m.duiba.com.cn/projectx/pb9acddd2/game/join.do"

    params = {
    'user_type': "1",
    'is_from_share': "1",
    '_t': str(int(time.time()*1000))
    }

    headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 13; IN2010 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.103 Mobile Safari/537.36 XWEB/1300149 MMWEBSDK/20240501 MMWEBID/4970 MicroMessenger/8.0.50.2701(0x2800325B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxd25dc8ba975776e3",
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'sec-ch-ua-platform': "\"Android\"",
    'sec-ch-ua': "\"Chromium\";v=\"130\", \"Android WebView\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    'content-type': "application/x-www-form-urlencoded",
    'sec-ch-ua-mobile': "?1",
    'x-requested-with': "com.tencent.mm",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://96984.activity-19.m.duiba.com.cn/projectx/pb9acddd2/index.html?appID=96984&code=&from=&roomId=&shareCode=&propCode=8K70EX&from=login&spm=96984.1.1.1",
    'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=1, i",
    }

    response = session.get(url, params=params, headers=headers)

    print(response.text)
    return response.json().get("data").get("encryption")

def com_game(session,param,token):
    url_encoded_data = urllib.parse.quote(param)
    url = "https://96984.activity-19.m.duiba.com.cn/projectx/pb9acddd2/game/submit.do"
    params = {
    'param': url_encoded_data,
    'validate': "",
    'token': str(token),
    'user_type': "1",
    'is_from_share': "1",
    '_t': str(int(time.time()*1000))
    }
    print(params)
    

    headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 13; IN2010 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.103 Mobile Safari/537.36 XWEB/1300149 MMWEBSDK/20240501 MMWEBID/4970 MicroMessenger/8.0.50.2701(0x2800325B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxd25dc8ba975776e3",
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'sec-ch-ua-platform': "\"Android\"",
    'sec-ch-ua': "\"Chromium\";v=\"130\", \"Android WebView\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    'content-type': "application/x-www-form-urlencoded",
    'sec-ch-ua-mobile': "?1",
    'x-requested-with': "com.tencent.mm",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://96984.activity-19.m.duiba.com.cn/projectx/pb9acddd2/index.html?appID=96984&code=&from=&roomId=&shareCode=&propCode=TINP0U&from=login&spm=96984.1.1.1",
    'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=1, i",
    }

    response = session.get(url, params=params, headers=headers)

    print(response.text)


def get_login(usercode):
    session = requests.Session()


    url = "https://customer-link.duiba.com.cn/customer/96984/wlg/login"

    params = {
    'userCode': usercode,
    'activityCode': "2025cny",
    'redirectUrl': "https://96984.activity-19.m.duiba.com.cn/projectx/pb9acddd2/index.html?appID=96984&code=&from=&roomId=&shareCode=&propCode=8K70EX"
    }

    headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 13; IN2010 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.103 Mobile Safari/537.36 XWEB/1300149 MMWEBSDK/20240501 MMWEBID/4970 MicroMessenger/8.0.50.2701(0x2800325B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxd25dc8ba975776e3",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'sec-ch-ua': "\"Chromium\";v=\"130\", \"Android WebView\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    'sec-ch-ua-mobile': "?1",
    'sec-ch-ua-platform': "\"Android\"",
    'upgrade-insecure-requests': "1",
    'x-requested-with': "com.tencent.mm",
    'sec-fetch-site': "same-site",
    'sec-fetch-mode': "navigate",
    'sec-fetch-dest': "document",
    'referer': "https://96984.activity-19.m.duiba.com.cn/",
    'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=0, i",
    }



    response = session.get(url, params=params, headers=headers)

    # print(response.text)
    print(session.cookies.get_dict())

    print("开始游戏")
    encryption=startgame(session)
    if encryption is not None:
        decrypted_str = decrypted(encryption)
        startId =json.loads(decrypted_str)["startId"]
        print('游戏id：',startId)
        message = getTokenKeyStr(session)
        key = get_key(message)
        print(key)
        duiba_token_str = get_keytoken(key, session)
        param= f'{{"startId":"{startId}","timestamp":{int(time.time() * 1000)},"score":999}}'
        print(param)
        encrypt_param=encrypt(param)
        time.sleep(2)
        print("游戏结算")
        com_game(session,encrypt_param,duiba_token_str)
    # get_token(session)
if __name__ == '__main__':
    use_list=[
      ''
    ]
    for user in use_list:
        get_login(user)



