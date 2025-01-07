import hashlib
import time
import requests
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64


def aes_encrypt(at, key, iv):
    # 将密钥和 IV 转换为字节
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')

    # 确保密钥和 IV 的长度符合 AES 要求
    if len(key_bytes) not in [16, 24, 32]:
        raise ValueError("密钥长度必须是 16、24 或 32 字节")
    if len(iv_bytes) != 16:
        raise ValueError("IV 长度必须是 16 字节")

    print(key_bytes)
    print(iv_bytes)

    # 创建 AES cipher 对象
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)

    # 数据需要 PKCS7 填充到 16 字节的倍数
    at_bytes = at.encode('utf-8')
    padded_data = pad(at_bytes, AES.block_size)

    # 加密数据
    encrypted_data = cipher.encrypt(padded_data)

    # 将加密后的数据转换为 base64 字符串输出
    return base64.b64encode(encrypted_data).decode('utf-8')


def generate_signature(uerId, activityId='1081946741727342593', appId='wxd92a2d29f8022f40', sellerId='201424'):
    aw = '8FgH3kJ1NpP5rQ9sTuV7WxY2ZbL4'
    # Reverse the aw string
    J = aw[::-1]

    # Create the data dictionary
    _t = {
        "activityId": activityId,
        "appId": appId,
        "sellerId": sellerId,
        "timestamp": str(int(time.time()*1000)),  # Current timestamp in milliseconds
        "userId": uerId
    }
    modified_entries = [f"{key}={value}" for key, value in _t.items()]

    it = "&".join(modified_entries) + "&key=" + J

    # Generate the MD5 signature
    print(it)
    signature = hashlib.md5(it.encode('utf-8')).hexdigest().upper()

    print(signature)
    return signature, _t["timestamp"]


def generate_payload(uerId, key, iv, version):
    signature, timestamp = generate_signature(uerId)
    payload = {
        "activityId": "1081946741727342593",
        "keyWords": "护嗓",
        "qzGtd": "",
        "gdtVid": "",
        "appid": "wxd92a2d29f8022f40",
        "timestamp": timestamp,
        "signature": signature,
    }
    data = aes_encrypt(json.dumps(payload, ensure_ascii=False).replace(" ", ""), key, iv)
    print(data)
    payload["data"] = data
    payload["version"] = version
    return payload



# Example usage:
if __name__ == "__main__":
    uerId = ""
    key = ""
    iv = ""
    version = 

    payload = generate_payload(uerId, key, iv, version)

