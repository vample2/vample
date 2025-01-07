from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import requests


def decoder_response(e, n="kEyOA02sa7d8dUYr", a=True):
    """
    解密函数，模拟 JavaScript 实现逻辑。

    :param e: 加密的 base64 数据字符串
    :param n: 加密的密钥
    :param a: 是否需要替换 '-' 和 '_' 字符
    :return: 解密后的字符串
    """
    if a:
        e = e.replace("-", "+").replace("_", "/")

    # 将 base64 数据解码为字节
    o = base64.b64decode(e)

    # 密钥需要为字节类型
    key = n.encode('utf-8')

    # 初始化 AES-ECB 加密模式，带 PKCS7 填充
    cipher = AES.new(key, AES.MODE_ECB)

    # 解密数据并去除填充
    decrypted_data = unpad(cipher.decrypt(o), AES.block_size)

    # 解密后的数据转换为 UTF-8 编码的字符串
    return decrypted_data.decode('utf-8')



def aes_decrypt(encrypted_data: str, key: str, url_safe: bool = True) -> str:
    """
    AES 解密函数，支持 ECB 模式和 URL 安全的 Base64 编码。

    :param encrypted_data: Base64 编码的密文
    :param key: 解密密钥，长度不足 16 补齐，超出截断
    :param url_safe: 是否将 URL 安全格式的 Base64 转换为普通格式
    :return: 解密后的字符串
    """
    # 调整密钥长度为 16 字节
    key_bytes = key.encode('utf-8').ljust(16)[:16]

    # 如果 Base64 为 URL 安全格式，先还原为标准格式
    if url_safe:
        encrypted_data = encrypted_data.replace("-", "+").replace("_", "/")

    # Base64 解码密文
    encrypted_bytes = base64.b64decode(encrypted_data)

    # 创建 AES 解密器 (ECB 模式) 并解密
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # 去除 PKCS7 填充
    padding = decrypted_bytes[-1]
    decrypted_bytes = decrypted_bytes[:-padding]

    return decrypted_bytes.decode('utf-8')


def aes_encrypt(data: str, key: str, url_safe: bool = True) -> str:
    """
    AES 加密函数，支持 ECB 模式、PKCS7 填充和 URL 安全的 Base64 编码。

    :param data: 待加密的字符串
    :param key: 加密密钥，长度不足 16 补齐，超出截断
    :param url_safe: 是否将 Base64 编码结果转换为 URL 安全格式
    :return: 加密后的字符串
    """
    # 调整密钥长度为 16 字节
    key_bytes = key.encode('utf-8').ljust(16)[:16]

    # 转换数据为字节格式并进行 PKCS7 填充
    data_bytes = data.encode('utf-8')
    padding = 16 - len(data_bytes) % 16
    data_bytes += bytes([padding]) * padding

    # 创建 AES 加密器 (ECB 模式) 并加密
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(data_bytes)

    # Base64 编码并处理 URL 安全性
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')
    if url_safe:
        encrypted_base64 = encrypted_base64.replace("+", "-").replace("/", "_")

    return encrypted_base64


def md5_extract_integers(data: str):
    """
    计算给定字符串的 MD5 值，并从 MD5 字节数组中提取 4 个整数值（每 4 字节一个整数）。
    返回这些整数的绝对值，并拼接成字符串。

    :param data: 待加密的字符串
    :return: 四个整数的绝对值拼接成的字符串
    """
    # 计算 MD5 并获取字节数组
    md5_bytes = hashlib.md5(data.encode('utf-8')).digest()

    # 提取每 4 字节并转换为整数（小端字节序），然后取绝对值
    def n(r, e):
        result = ((255 & r[e]) << 24) | ((255 & r[e + 1]) << 16) | ((255 & r[e + 2]) << 8) | (255 & r[e + 3])
        # Simulate 32-bit signed integer overflow
        if result >= 2 ** 31:
            result -= 2 ** 32
        return result

    if len(md5_bytes) != 16:
        raise ValueError("MD5 hash result is not 16 bytes long")
    # 提取并计算绝对值
    a = abs(n(md5_bytes, 0))
    s = abs(n(md5_bytes, 4))
    o = abs(n(md5_bytes, 8))
    c = abs(n(md5_bytes, 12))

    # 返回合并的字符串结果
    result = str(a) + str(s) + str(o) + str(c)

    print(f"MD5 Bytes: {list(md5_bytes)}")
    print(f"a: {a}, s: {s}, o: {o}, c: {c}")

    return result




if __name__ == "__main__":

    data_dict = {"deptId": "1",
                 "virtualProductVOList": [
                     {"spuCode": "SPU116308775836540928", "skuCode": "SKU116308775836540930", "amount": 1}],
                 "delivery": "pick", "eatway": "eat", "useDiscount": 0, "useDefaultCafeKu": 0, "channel": "GCJ-02",
                 "blackBox": "",
                 "did": "", "miniversion": "5273"}
    key = "kEyOA02sa7d8dUYr"
    cid = "230101"
    uid = ""
    # 去除空格并转换为 JSON 字符串
    data = json.dumps(data_dict, separators=(',', ':'))

    # 执行 AES 加密
    encrypted_data = aes_encrypt(data, key)
    decrypt_data = aes_decrypt(encrypted_data, key)

    print("加密结果:", encrypted_data)
    print("解密结果:", decrypt_data)
    # 构造参数列表
    v = [
        f"cid={cid}",
        "dk=1",
        f"q={encrypted_data}",
        f"uid={uid}"
    ]

    # 按字典序排序并拼接
    sorted_string = ";".join(sorted(v)) + key
    print(sorted_string)
    # 生成签名
    sign = md5_extract_integers(sorted_string)
    # print(sign)
    # 最终参数
    params = {
        "cid": cid,
        "q": encrypted_data,
        "dk": "1",
        "sign": sign,
    }

    print("参数:", params)
