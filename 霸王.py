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
def generate_signature(activityId,userId,signature_timestamp):
    Mt_key = '8FgH3kJ1NpP5rQ9sTuV7WxY2ZbL4'
    St = {
        "appId": "wxafec6f8422cb357b",
        "activityId": activityId,
        "sellerId": "49006",
        "timestamp": signature_timestamp,  
        "userId": userId
    }
    key = Mt_key[::-1]
    # print(f"Reversed key: {key}")

    sorted_keys = sorted(St.keys())
    query_string = '&'.join([f"{key}={St[key]}" for key in sorted_keys])
    query_string += f"&key={key}"

    md5_hash = hashlib.md5(query_string.encode('utf-8')).hexdigest().upper()
    print(f"MD5 Hash: {md5_hash}")
    return md5_hash


def generate_x(activityId,userId,signature,signature_timestamp):
    Ce_key='A7b3C9D2eF1G8H4iJ6k5L7Mn3Op2Q4R9S'
    Kt={
        "appId": "wxafec6f8422cb357b",
        "activityId": activityId,
        "sellerId": "49006",
        "timestamp": signature_timestamp,
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
    userId=""
    keyWords="随春醒"
    encryptKey=""
    iv=""
    version=

    signature_timestamp=int(time.time()*1000)
    signature=generate_signature(activityId,userId,signature_timestamp)
    print("signature:",signature)
    X=generate_x(activityId,userId,signature,signature_timestamp)
