import hashlib
import time
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import requests
import math


def generate_x(timestamp, uerId):
    X = int(timestamp)
    xt = [[3, 5, 8, 12], [7, 11, 2], [19, 23, 17]]
    mt = uerId
    Ht = int("1" + mt[-2:] + timestamp[-2:])
    Bt = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    fe = math.floor((X / 1000)) % 1000 or 1
    se = fe
    for index, st in enumerate(xt):
        me = Bt[index]
        for index, num in enumerate(st):
            we = [int(num), index, st]
            Ht ^= we[0] * me
            se += pow(we[0] % 10, 2) * fe % 1000003
    Te = int(mt[len(mt) - 1]) or 1
    Ae = mt
    _e = str(int((X + 0) % 1e4))
    for st in range(0, Te):
        Ae = hashlib.md5((str(Ae + _e)).encode('utf-8')).hexdigest()
    Mt = f"{Ht}-{se}-{X}-{Ae}"
    sha256_hex = hashlib.sha256(Mt.encode()).hexdigest()
    md5_final = hashlib.md5(sha256_hex.encode()).hexdigest()
    print(f"MD5 Hash: {md5_final}")
    return md5_final


def generate_signature(activityId, userId, signature_timestamp):
    Mt_key = '8FgH3kJ1NpP5rQ9sTuV7WxY2ZbL4'
    St = {
        "appId": "",
        "activityId": activityId,
        "sellerId": "201424",
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


def generate_data(payload, encryptKey, iv):
    payload = json.dumps(payload, ensure_ascii=False).replace(" ", "")
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
    ## appid自己添加
    timestamp = "1745035922049"
    userId = ""
    activityId = "1120071264150298625"
    keyWords = "护嗓"

    x = generate_x(timestamp, userId)
    signature = generate_signature(activityId, userId, timestamp)
    payload = {
        "activityId": activityId,
        "keyWords": keyWords,
        "qzGtd": "",
        "gdtVid": "",
        "appid": "",
        "timestamp": timestamp,
        "signature": signature,
        "x": x,
        "v": 2
    }

    encryptKey = ""
    iv = ""
    version = 
    data=generate_data(payload, encryptKey, iv)
    print(data)
