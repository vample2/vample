from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def en(result, n):
    """
    加密函数，将解密后的 result 加密生成与 data 一致的字符串。

    :param result: 原始明文字符串
    :param n: 加密密钥
    :return: 加密后的 base64 字符串
    """
    # 将 result 转换为字节
    plaintext = result.encode('utf-8')

    # 密钥需要为字节类型
    key = n.encode('utf-8')

    # 初始化 AES-ECB 加密模式，带 PKCS7 填充
    cipher = AES.new(key, AES.MODE_ECB)

    # 对明文加密并进行 base64 编码
    encrypted_data = cipher.encrypt(pad(plaintext, AES.block_size))
    encoded_data = base64.b64encode(encrypted_data).decode('utf-8')

    # 将 base64 编码字符串中的 '+' 替换为 '-'，'/' 替换为 '_'
    encoded_data = encoded_data.replace("+", "-").replace("/", "_")

    return encoded_data


# 示例用法
L = "kEyOA02sa7d8dUYr"  # 密钥
result = '{"busiCode":"BASE000","code":1,"content":{"availableStock":472,"bizType":1,"currency":{"enName":"CNY","regionCode":"CN","symbol":"¥","unit":"元"},"detailDescription":"内含：38元饮品兑换券，共1张","perLimit":1,"picUrl":"https://img03.luckincoffeecdn.com/group2/M00/24/DF/CtwiPWdNjayAcTlZAAIaFZqL7y440.jpeg","price":38.0,"selectSkuName":"【定时抢】1元限量秒杀","sellPrice":1.0,"skuCode":"SKU116308775836540930","skuDetailItemList":[{"amount":1,"bizName":"38元饮品兑换券","price":"38","tagName":""}],"skuName":"【定时抢】1元限量秒杀","spuCode":"SPU116308775836540928","totalAmount":1,"virtualActivityConfigRe":{"activityDesc":"下一场12.12日12点开始","activityLabel":"下一场12.12日12点开始","activityStatus":3,"activityToast":"已抢完，12.12日再来","applySkuCodes":[],"endTimeStamp":0,"refreshTimeInterval":3000,"requestTimeInterval":300,"startTimeStamp":0}},"handler":"CLIENT","msg":"成功","status":"SUCCESS","uid":"d3ccf300-b8f9-496e-98f7-e4cfbef849db1733799978194","version":"101","zeusId":"luckyactcapiproxy-0add6a0f-481614-12221","abTest":[]}'

# 重新生成 data
generated_data = en(result, L)
print(generated_data)
