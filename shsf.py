import hashlib
import time
import requests
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64


def qiang(payload):
    url = "https://webapi.qmai.cn/web/cmk-center/receive/takePartInReceive"

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'Accept': "v=1.0",
        'Content-Type': "application/json",
        'qm-user-token': "",
        'store-id': "201424",
        'qm-from': "wechat",
        'qm-trace-store-id': "201424",
        'xweb_xhr': "1",
        'qm-from-type': "catering",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://servicewechat.com/wxd92a2d29f8022f40/358/page-frame.html",
        'accept-language': "zh-CN,zh;q=0.9"
    }


    try:
        # 发送 POST 请求
        response = requests.post(url, data=json.dumps(payload), headers=headers,  timeout=2)

        # print({'a': token["mobile_phone"], "b": proxies})
        print("状态码:", response.status_code)
        print("响应内容:", response.text)
    except requests.exceptions.RequestException as e:
        pass


def getNowTime():
    return int(round(time.time() * 1000))


def get_updated_time(minute=59, second=59, microsecond=800):
    """
    获取下一个完整小时的时间，用户可以指定分钟、秒和微秒。

    :param minute: 分钟（默认为59）
    :param second: 秒（默认为59）
    :param microsecond: 微秒（默认为700,000）
    :return: 完整小时的时间
    """
    # 获取当前时间
    now = datetime.datetime.now()

    # 计算完整小时的时间
    updated_hour = now.replace(minute=minute, second=second, microsecond=microsecond * 1000)

    # 如果时间已经过去当前小时，则将时间设置为下一个小时
    if now > updated_hour:
        updated_hour += datetime.timedelta(hours=1)

    printf("抢购时间：{}".format(updated_hour))
    return updated_hour


def datetime_to_timestamp(dt):
    """
    将 datetime 对象转换为毫秒级时间戳。

    :param dt: datetime 对象
    :return: 时间戳（以毫秒为单位）
    """
    # 将 datetime 对象转换为时间元组
    time_tuple = dt.timetuple()

    # 将时间元组转换为秒级时间戳
    timestamp_sec = time.mktime(time_tuple)

    # 转换为毫秒级时间戳，并加上微秒部分
    timestamp_ms = int(timestamp_sec * 1000 + dt.microsecond / 1000)
    # logging.info(timestamp_ms)
    return timestamp_ms


def printf(text, userId=''):
    ti = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    if userId == '':
        print(f'[{ti}]: {text}')
    else:
        print(f'[{ti}][{userId}]: {text}')
    sys.stdout.flush()


def aes_encrypt(at, key, iv):
    # 将密钥和 IV 转换为字节
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')

    # 确保密钥和 IV 的长度符合 AES 要求
    if len(key_bytes) not in [16, 24, 32]:
        raise ValueError("密钥长度必须是 16、24 或 32 字节")
    if len(iv_bytes) != 16:
        raise ValueError("IV 长度必须是 16 字节")

    # 创建 AES cipher 对象
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)

    # 数据需要 PKCS7 填充到 16 字节的倍数
    at_bytes = at.encode('utf-8')
    padded_data = pad(at_bytes, AES.block_size)

    # 加密数据
    encrypted_data = cipher.encrypt(padded_data)

    # 将加密后的数据转换为 base64 字符串输出
    return base64.b64encode(encrypted_data).decode('utf-8')


def generate_signature(uerId, activityId='1101206695629893633', appId='wxd92a2d29f8022f40', sellerId='201424'):
    aw = '8FgH3kJ1NpP5rQ9sTuV7WxY2ZbL4'
    # Reverse the aw string
    J = aw[::-1]

    # Create the data dictionary
    _t = {
        "activityId": activityId,
        "appId": appId,
        "sellerId": sellerId,
        "timestamp": str(int(time.time() * 1000)),  # Current timestamp in milliseconds
        "userId": uerId
    }
    modified_entries = [f"{key}={value}" for key, value in _t.items()]

    it = "&".join(modified_entries) + "&key=" + J

    # Generate the MD5 signature
    signature = hashlib.md5(it.encode('utf-8')).hexdigest().upper()

    print(signature)
    return signature, _t["timestamp"]


def generate_payload(uerId, key, iv, version):
    signature, timestamp = generate_signature(uerId)
    payload = {
        "activityId": "1101206695629893633",
        "qzGtd": "",
        "gdtVid": "",
        "appid": "wxd92a2d29f8022f40",
        "timestamp": timestamp,
        "signature": signature,
    }
    data = aes_encrypt(json.dumps(payload).replace(" ", ""), key, iv)
    print(data)
    payload["data"] = data
    payload["version"] = version
    return payload

if __name__ == '__main__':
    uerId = ""
    key = ""
    iv = ""
    version = 
    payload = generate_payload(uerId, key, iv, version)
    qiang(payload)
    
