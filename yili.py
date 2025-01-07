import requests
import time
import execjs
import time
import json


def generate_signature(js_file, timestamp, type1, type2):
    with open(js_file, "r", encoding="utf-8") as f:
        js_code = f.read()

    # 使用 execjs 执行 JavaScript
    ctx = execjs.compile(js_code)
    generateSignature = ctx.call("generateSignature", timestamp, type1, type2)

    return generateSignature


