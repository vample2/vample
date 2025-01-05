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


def get_task(token, openId):
    url = "https://wx-camp-180-cny-api.mscampapi.digitalyili.com/fragment/ticket/ticket-info"

    params = {
        'openId': openId
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'content-type': "application/json",
        'timestamp': f"{int(time.time() * 1000)}",
        'xweb_xhr': "1",
        'access_token': token,
        'token': token,
        'app-version': "1.1.1",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://servicewechat.com/wx06af0ef532292cd3/586/page-frame.html",
        'accept-language': "zh-CN,zh;q=0.9"
    }

    # 加载 JavaScript 文件
    # with open("伊利.js", "r", encoding="utf-8") as f:
    #     js_code = f.read()

    # # 使用 execjs 执行 JavaScript
    # ctx = execjs.compile(js_code)
    # generateSignature = ctx.call("generateSignature", headers["timestamp"])
    generateSignature = generate_signature("伊利.js", headers["timestamp"], type1, type2)
    # print(generateSignature)

    # print("Generated Signature:", generateSignature['signature'],generateSignature['uniqueCode'])

    headers["signature"] = generateSignature['signature']
    headers["uniqueCode"] = generateSignature['uniqueCode']
    # print(headers)

    response = requests.get(url, params=params, headers=headers)

    # print(response.text)
    return response.json()


def get_sign(token, openId):
    url = "https://wx-camp-180-cny-api.mscampapi.digitalyili.com/fragment/ticket/sign"

    params = {
        'openId': openId
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'content-type': "application/json",
        'timestamp': f"{int(time.time() * 1000)}",
        'xweb_xhr': "1",
        'access_token': token,
        'token': token,
        'app-version': "1.1.1",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://servicewechat.com/wx06af0ef532292cd3/586/page-frame.html",
        'accept-language': "zh-CN,zh;q=0.9"
    }

    generateSignature = generate_signature("伊利.js", headers["timestamp"], type1, type2)

    # print("Generated Signature:", generateSignature['signature'],generateSignature['uniqueCode'])

    headers["signature"] = generateSignature['signature']
    headers["uniqueCode"] = generateSignature['uniqueCode']

    response = requests.get(url, params=params, headers=headers)

    # print(response.text)


def get_seePage(token, openId):
    url = "https://wx-camp-180-cny-api.mscampapi.digitalyili.com/fragment/ticket/see-page"

    params = {
        'openId': openId
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'content-type': "application/json",
        'timestamp': f"{int(time.time() * 1000)}",
        'xweb_xhr': "1",
        'access_token': token,
        'token': token,
        'app-version': "1.1.1",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://servicewechat.com/wx06af0ef532292cd3/586/page-frame.html",
        'accept-language': "zh-CN,zh;q=0.9"
    }

    generateSignature = generate_signature("伊利.js", headers["timestamp"], type1, type2)

    # print("Generated Signature:", generateSignature['signature'],generateSignature['uniqueCode'])

    headers["signature"] = generateSignature['signature']
    headers["uniqueCode"] = generateSignature['uniqueCode']

    response = requests.get(url, params=params, headers=headers)

    # print(response.text)


def get_lottery(token, openId):
    url = "https://wx-camp-180-cny-api.mscampapi.digitalyili.com/fragmentActivity/lottery"

    params = {
        'activityId': "1",
        'openId': openId
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'content-type': "application/json",
        'timestamp': f"{int(time.time() * 1000)}",
        'xweb_xhr': "1",
        'access_token': token,
        'token': token,
        'app-version': "1.1.1",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://servicewechat.com/wx06af0ef532292cd3/586/page-frame.html",
        'accept-language': "zh-CN,zh;q=0.9"
    }
    generateSignature = generate_signature("伊利.js", headers["timestamp"], type1, type2)

    # print("Generated Signature:", generateSignature['signature'],generateSignature['uniqueCode'])

    headers["signature"] = generateSignature['signature']
    headers["uniqueCode"] = generateSignature['uniqueCode']

    response = requests.get(url, params=params, headers=headers)

    # print(response.text)
    return response.json()


def check_fragment(token, openId):
    url = "https://wx-camp-180-cny-api.mscampapi.digitalyili.com/fragmentActivity/fragment"

    params = {
        'activityId': "1",
        'openId': openId
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'content-type': "application/json",
        'timestamp': f"{int(time.time() * 1000)}",
        'xweb_xhr': "1",
        'access_token': token,
        'token': token,
        'app-version': "1.1.1",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://servicewechat.com/wx06af0ef532292cd3/586/page-frame.html",
        'accept-language': "zh-CN,zh;q=0.9"
    }
    generateSignature = generate_signature("伊利.js", headers["timestamp"], type1, type2)

    # print("Generated Signature:", generateSignature['signature'],generateSignature['uniqueCode'])

    headers["signature"] = generateSignature['signature']
    headers["uniqueCode"] = generateSignature['uniqueCode']

    response = requests.get(url, params=params, headers=headers)

    # print(response.text)
    return response.json()


def open_prize(token, fragmentId, openId):
    url = "https://wx-camp-180-cny-api.mscampapi.digitalyili.com/fragmentActivity/open-prize"

    params = {
        'fragmentId': fragmentId,
        'activityId': "1",
        'openId': openId
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'content-type': "application/json",
        'timestamp': f"{int(time.time() * 1000)}",

        'xweb_xhr': "1",
        'access_token': token,

        'token': token,
        'app-version': "1.1.1",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://servicewechat.com/wx06af0ef532292cd3/587/page-frame.html",
        'accept-language': "zh-CN,zh;q=0.9"
    }
    generateSignature = generate_signature("伊利.js", headers["timestamp"], type1, type2)

    # print("Generated Signature:", generateSignature['signature'],generateSignature['uniqueCode'])

    headers["signature"] = generateSignature['signature']
    headers["uniqueCode"] = generateSignature['uniqueCode']

    # response = requests.get(url, params=params, headers=headers)

    response = requests.get(url, params=params, headers=headers)

    # print(response.text)
    return response.json()


def get_newtoken(phoneNum, openId, unionId, authorizationCode, context_id):
    import requests
    import json

    url = "https://wx-camp-180-cny-api.mscampapi.digitalyili.com/v2/wechat/applet/set-user-info"

    payload = {
        "headImg": "https://wx-pubcos.yili.com/prod-msmarket/97b585bb991e4c97969abb56cd7394c7.png",
        "phoneNum": phoneNum,
        "openId": openId,
        "unionId": unionId,
        "authorizationCode": authorizationCode,
        "ciphertext": context_id
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
        'Content-Type': "application/json",
        'xweb_xhr': "1",
        'app-version': "1.1.1",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://servicewechat.com/wx06af0ef532292cd3/598/page-frame.html",
        'accept-language': "zh-CN,zh;q=0.9"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    # print(response)
    # print(response.text)
    res_json = response.json()
    res_data = res_json['data']
    num1 = res_data['num1']
    num2 = res_data['num2']
    token = res_data['token']
    return num1, num2, token


def get_userinfo(access_oken):
    url = "https://msmarket.msx.digitalyili.com/gateway/api/auth/account/user/info"

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
        'register-source': "",
        'access-token': access_oken,
        'forward-appid': "",
        'source-type': "",
        'content-type': "application/json",
        'atv-page': "",
        'scene': "1007",
        'xweb_xhr': "1",
        'x-tingyun': "c=M|wm6l1s4m4N8",
        'tenant-id': "1559474730809618433",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://servicewechat.com/wx06af0ef532292cd3/597/page-frame.html",
        'accept-language': "zh-CN,zh;q=0.9"
    }

    response = requests.get(url, headers=headers)
    # print(response.text)
    contextId = response.json()["contextId"]
    data_json = response.json()["data"]
    mobile = data_json["mobile"]
    openId = data_json["openId"]
    unionId = data_json["unionId"]

    return contextId, mobile, openId, unionId


def get_authorize(access_token):
    url = "https://msmarket.msx.digitalyili.com/developer/oauth2/buyer/authorize"

    # 请求参数
    params = {
        "app_key": "zdcade261b48eb4c5e"
    }

    # 自定义 Header
    headers = {
        "content-type": "application/json",
        "access-token": access_token,
        "scene": "1256",
        # "tenant-id": "1559474730809618433",
        "atv-page": "",
        "forward-appid": "",
        "source-type": "",
        "register-source": ""
    }

    response = requests.get(url, params=params, headers=headers).json()
    # response.raise_for_status()  # 检查是否返回 HTTP 错误
    # print(response)

    return response["data"], response["context_id"]


def my_prize(token,openId):
    import requests

    url = "https://wx-camp-180-cny-api.mscampapi.digitalyili.com/fragmentActivity/my-prize"

    params = {
        'openId': openId
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
        'content-type': "application/json",
        'timestamp': f"{int(time.time() * 1000)}",
        'signature': "C1B6E4462F862505259C1371BFF78AB4",
        'xweb_xhr': "1",
        'access_token': token,
        'uniquecode': "1735806818049&937264",
        'token': token,
        'app-version': "1.1.1",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://servicewechat.com/wx06af0ef532292cd3/598/page-frame.html",
        'accept-language': "zh-CN,zh;q=0.9"
    }

    generateSignature = generate_signature("伊利.js", headers["timestamp"], type1, type2)

    # print("Generated Signature:", generateSignature['signature'],generateSignature['uniqueCode'])

    headers["signature"] = generateSignature['signature']
    headers["uniqueCode"] = generateSignature['uniqueCode']

    # response = requests.get(url, params=params, headers=headers)

    response = requests.get(url, params=params, headers=headers).json()
    return response["data"]

if __name__ == "__main__":
    token_list = [
        '',

    ]
    for index, access_token in enumerate(token_list):
        contextId, phoneNum, openId, unionId = get_userinfo(access_token)
        print(f"----------------账号:{phoneNum[:3] + '****' + phoneNum[-4:]}----------------")
        authorizationCode, context_id = get_authorize(access_token)
        type1, type2, token = get_newtoken(phoneNum, openId, unionId, authorizationCode, context_id)

        res_json = get_task(token, openId)
        task_list = res_json["data"]
        print(task_list)

        print("签到时间：{}天".format(task_list['signDays']))
        print("任务列表：")
        if task_list["sign"] == True:
            print("签到:已签到")
        else:
            get_sign(token, openId)

        if task_list["addWxByQr"] == True:
            print("添加专属导购:已完成")
        else:
            print("添加专属导购:未完成")

        if task_list["fillQuestionnaire"] == True:
            print("fillQuestionnaire:已完成")
        else:
            print("fillQuestionnaire:未完成")
        if task_list["seePage"] == True:
            print("浏览活动页面:已完成")
        else:
            print("浏览活动页面:未完成")
            get_seePage(token, openId)

        print("----------------开始抽奖----------------")
        while True:
            lottery_json = get_lottery(token, openId)
            if lottery_json.get("message") == '抽卡次数不足':
                break
            time.sleep(1)
        fragment_json = check_fragment(token, openId)
        data_list = fragment_json["data"]
        print(data_list)
        print("----------------开始翻卡----------------")
        for index, fragment in enumerate(data_list):
            fragmentName = fragment["fragmentName"]
            fragmentnum = fragment["num"]
            fragmentId = fragment["fragmentId"]
            print(f"卡片名称: {fragmentName}, 数量: {fragmentnum}")
            if fragmentnum > 1:
                for _ in range(fragmentnum - 1):
                    while True:
                        prize_json = open_prize(token, fragmentId, openId)
                        if prize_json.get('message') == '您的手速太快了~':
                            time.sleep(1)
                        else:
                            prizeName = prize_json['data']["prizeName"]
                            print(prizeName)
                            break
        print("----------------查询奖品----------------")
        prize_list=my_prize(token,openId)
        for prize in prize_list:
            print(prize["prizeName"])

