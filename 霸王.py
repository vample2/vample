import hashlib
import time
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import requests
import execjs

def generate_type(js_file,url,data):
    with open(js_file, "r", encoding="utf-8") as f:
        js_code = f.read()

    # 使用 execjs 执行 JavaScript
    ctx = execjs.compile(js_code)
    generatetype__1475 = ctx.call("type",url,data)

    return generatetype__1475
def generate_x(activityId,userId):
    Mt_key = '8FgH3kJ1NpP5rQ9sTuV7WxY2ZbL4'
    St = {
        "appId": "wxafec6f8422cb357b",
        "activityId": activityId,
        "sellerId": "49006",
        "timestamp": time.time()*1000,  
        "userId": userId
    }
    key = Mt_key[::-1]
    # print(f"Reversed key: {key}")

    sorted_keys = sorted(St.keys())
    query_string = '&'.join([f"{key}={St[key]}" for key in sorted_keys])
    query_string += f"&key={key}"

    md5_hash = hashlib.md5(query_string.encode('utf-8')).hexdigest().upper()
    # print(f"MD5 Hash: {md5_hash}")
    return md5_hash


def generate_signature(activityId,userId,signature):
    Ce_key='A7b3C9D2eF1G8H4iJ6k5L7Mn3Op2Q4R9S'
    Kt={
        "appId": "wxafec6f8422cb357b",
        "activityId": activityId,
        "sellerId": "49006",
        "timestamp": int(time.time()*1000),
        "userId": userId,
        "x": signature
    }
    key = Ce_key[::-1]
    # print(f"Reversed key: {key}")

    sorted_keys = sorted(Kt.keys())
    query_string = '&'.join([f"{key}={Kt[key]}" for key in sorted_keys])
    query_string += f"&key={key}"
    print(query_string)

    md5_hash = hashlib.md5(query_string.encode('utf-8')).hexdigest().upper()
    # print(f"MD5 Hash: {md5_hash}")
    return md5_hash

def generate_data(payload,encryptKey,iv):
    payload=json.dumps(payload,ensure_ascii=False).replace(" ", "")
    print(payload)
        # 将密钥和 IV 转换为字节
    key_bytes = encryptKey.encode('utf-8')
    iv_bytes = iv.encode('utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv=iv_bytes)
    padded_data = pad(payload.encode('utf-8'), AES.block_size)
    encrypt_data = cipher.encrypt(padded_data)
    # print(base64.b64encode(encrypt_data).decode('utf-8'))
    return base64.b64encode(encrypt_data).decode('utf-8')



if __name__ == '__main__':
    activityId="1103738389171855360"
    userId="980429855913132033"
    keyWords="随春醒"
    encryptKey="DgGgY9EJ9zvySa4eImlnGA=="
    iv="06e556bd14e7b10f"
    version=17


    X=generate_x(activityId,userId)
    print(X)
    signature=generate_signature(activityId,userId,X)
    print(signature)
    
    url = "https://miniapp.qmai.cn/web/cmk-center/receive/takePartInReceive"

    payload = {
        "activityId": activityId,
        "keyWords": keyWords,
        "qzGtd": "",
        "gdtVid": "",
        "appid": "wxafec6f8422cb357b",
        "timestamp": int(time.time()*1000),
        "signature": signature,
        "x": X,
    }
    payload ={
    "activityId": "1103738389171855360",
    "keyWords": "随春醒",
    "qzGtd": "",
    "gdtVid": "",
    "appid": "wxafec6f8422cb357b",
    "timestamp": "1741341199377",
    "signature": "53093A93EF3AAAC0F15DBE878779DF97",
    "x": "8A33443472A54CDF88B435D32BD3A68F"
    }
    data=generate_data(payload,encryptKey,iv)
    payload['data']=data
    payload['version']=version

    
    type__1475=generate_type("type_1475.js",url,payload)
    params = {
        'type__1475': type__1475
    }
    print(params)
    payload=json.dumps(payload, separators=(',', ':'),ensure_ascii=False).encode('utf-8')
    print(payload)

    


    # HTTP 头
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
        'Accept': "v=1.0",
        'Content-Type': "application/json",
        'qm-user-token': "",
        'store-id': "49006",
        'qm-from': "wechat",
        'qm-trace-store-id': "49006",
        'xweb_xhr': "1",
        'qm-from-type': "catering",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://servicewechat.com/wxafec6f8422cb357b/224/page-frame.html",
        'accept-language': "zh-CN,zh;q=0.9",
    }

    # 发送请求
    response = requests.post(url, data=payload,params=params, headers=headers)

    # 输出返回数据
    print(response.text)

