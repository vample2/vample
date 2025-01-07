from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


def de(e, n, a):
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


# 示例用法
L = "kEyOA02sa7d8dUYr"  # 密钥
data = "Kl2_X6P85gZp7jT9A1seUPqhGIV8StkyonEH0KUikYlxbIzokUVoI57unNaNtDoPkKks0xoHtorAw3SfjLeOve9dQT9oOtVGMdowXSYtQ-9l5s69bwkE8AiOSuawhVBhEbyxVqFIW7zPCP4qXuRlXP1VDvWM4dGXRdNBDO-v1tpPwNum6TgQ8ABlOuweo6d-VpG-oSI9QzLaaK2zfNOL1UcdG3DeYEFqj4_B5aPXG6pc3Et8JZ0nTSuJPVsIHqtfxrZchae7V8fTbHgXYqWTgbL17SEI8RSIobY1r6Wu3PbsPknWyis-T79-NP6j_LqbQr0SpPMj5LR1umIUIOgiPUU_kTsH7au5EnVcUyv2LLXKxCBa3q_P6A23OD3GGToHAnDpZNnerMjcKDLcU04pvSWIh-kUGDJKvSr52-2AoLSyZEpJNrtrE2NRQG3PpcglRWQUg0M1cdrJIZP37UFoX9k4IYLmxc241JjvBR3BnzoIJ6Zwai2_gOHct10LiQY8xVdxuQUrC3Mq41t8pFjngv86-peEA6gD8OSMwRXRF8Ikmzd9H9ln_R_tCInzlOyxMHOY5KG15BF7o1ka0hvcD2t1xff__tOfobVUW-Z5WLkAwx9QZvfsRaBEtxRTKoGLzldEh36C2p-8xFWwRnX1neskpJvDoCfS5iBVqO0c1K9LqTrZOLF699e2cXpBCsdHcm0h1kx9qdoqJGkA4tP9s9dXEl9oVnNzvXiaFF5_xCyEWIkXx5KY9fmQuiyknipcGD4qPptcxt6dTvQNRHPYhGUcVYlT5Xmzu1KjW11HjQaxcd--8GiekBVwxG78Vns-JDqoDEolUM12ejNyuAak_JOMKhoiJpgEVqM_zv3x70wktQ2_q5NteMHQ_XfWcqvZ0utZoV95RtT1efUrHNh4f66KYfIHeNkMDE-C-n-8-gxxgoqN0J9yAW2_QzhIWWDcHh7GCFNP3jHGSsoAiLyr5loCtzCcm0gQk1sjIujJkWFZf-Z-JSu0lFOqmfKR77XleRVK_r67_DcmjVAFZtas56EeLj6ZP87qB4UHxf-PimK5n7RqGiAlinhSES5wMf5GY4qO35ewzey2j1Daa6FHj_deEmj97u9HjkrhkeXOHc9D6cIntpmjL5JqXo59gsMSJ1LEWzxAgPomZWYuCw84yp6xRV_-Zmd48rhwlw0_lOw9itf9U7p-i-byE7jtU5sZxaS9HUsWtM_DNXa5igQiTHeFMFpXwYwE7Qy0R8Re9p52Z2E8OMaazxOAU65KlkCi3WNREfUdRHo-VXdxCFJ9QEZmQGztU7Qg9dgPmYe2MsqVo8gh7ylIHnjYwfam4nhomoMoqV1dV7ItiRc5QYpa37JRctjiPrFjpDctOd3X_GjCquUphaosb61igWYayLSXWUG-ndsyYtca59rGSQOSnCtrxdjah2nyRjsFVlflcujDIzaguUBICc_fZYJqFPoOGUN3z9Nlajlbyupv_k5r4A=="  # 数据

result = de(data, L, True)
print(result)
