import json
import hashlib
import time
import subprocess
import requests



def get_Timestamp(json_data):

    result = subprocess.run(['node', './index.js',json.dumps(json_data)], capture_output=True, text=True,encoding='utf-8')
    print(result.stdout)
    return result.stdout

def completeBrowseTask(type,token):
    url = "https://www.hotkidclub.com/api/cpn/year2025/getFragments.ctrl"

    payload = json.dumps({
        "getWay": type,
        "adid": "2025festival-hotkidclub-click-2025_festival-1j8"
    })

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'Content-Type': "application/json",
        'sec-ch-ua': "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        'Timestamp': "1732889190472",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Windows\"",
        'Origin': "https://www.hotkidclub.com",
        'Sec-Fetch-Site': "same-origin",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Dest': "empty",
        'Referer': "https://www.hotkidclub.com/",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': token
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response)

    print(response.text)
def startGame(token):
    

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': token,
        'Referer': 'https://www.hotkidclub.com/cpn/2025year/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Timestamp': '1735189648064',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://www.hotkidclub.com/api/cpn/year2025/startGame.ctrl',  headers=headers)
    print("开始游戏")
    print(response)
    print(response.text)
    return response.json()["Response"]["data"]["grade"]

def grabGameGetFragment(grade,token):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': token,
        'Origin': 'https://www.hotkidclub.com',
        'Referer': 'https://www.hotkidclub.com/cpn/2025year/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Timestamp': '1735188280977',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'grade': grade,
        'score': 50,
        'channel': '其他H5',
        'isPass': 1,
        'adid': '2025festival-campaign_self-click-link-1i6',
    }
    if grade == 1:
        json_data["score"]=30
    elif grade == 2:
        json_data['score'] = 50
    Timestamp=get_Timestamp(json_data)
    print(Timestamp)
    headers["Timestamp"]=Timestamp.replace("\n","").replace(" ","")
    # print(headers)
    response = requests.post(
        'https://www.hotkidclub.com/api/cpn/year2025/grabGameGetFragment.ctrl',
        headers=headers,
        json=json_data,
    )
    print(response)
    print(response.text)




def getFragments(type, token):
    import requests
    import json

    url = "https://www.hotkidclub.com/api/cpn/year2025/getFragments.ctrl"

    payload = json.dumps({
        "getWay": type,
        "adid": "2025festival-hotkidclub-click-2025_festival-1j8"
    })

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'Content-Type': "application/json",
        'sec-ch-ua': "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        'Timestamp': "1732971346278",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Windows\"",
        'Origin': "https://www.hotkidclub.com",
        'Sec-Fetch-Site': "same-origin",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Dest': "empty",
        'Referer': "https://www.hotkidclub.com/",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': token
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)


def cpnSign(token):
    url = "https://www.hotkidclub.com/api/cpn/year2025/cpnSign.ctrl"

    payload = {
        "adid": "2025festival-hotkidclub-click-2025_festival-1j8"
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 13; IN2010 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.102 Mobile Safari/537.36 XWEB/1300073 MMWEBSDK/20240501 MMWEBID/4970 MicroMessenger/8.0.50.2701(0x2800325B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxe2c4192bf307ccff",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/json",
        'sec-ch-ua-platform': "\"Android\"",
        'Timestamp': "1732887953869",
        'sec-ch-ua': "\"Chromium\";v=\"130\", \"Android WebView\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        'sec-ch-ua-mobile': "?1",
        'Origin': "https://www.hotkidclub.com",
        'X-Requested-With': "com.tencent.mm",
        'Sec-Fetch-Site': "same-origin",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Dest': "empty",
        'Referer': "https://www.hotkidclub.com/",
        'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        'Cookie': token
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # print(response.text)


def get_tasklist(token):
    url = "https://www.hotkidclub.com/api/cpn/year2025/taskList.ctrl"

    payload = {
        "platformType": 1
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 13; IN2010 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.102 Mobile Safari/537.36 XWEB/1300073 MMWEBSDK/20240501 MMWEBID/4970 MicroMessenger/8.0.50.2701(0x2800325B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxe2c4192bf307ccff",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/json",
        'sec-ch-ua-platform': "\"Android\"",
        'Timestamp': "1732887296942",
        'sec-ch-ua': "\"Chromium\";v=\"130\", \"Android WebView\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        'sec-ch-ua-mobile': "?1",
        'Origin': "https://www.hotkidclub.com",
        'X-Requested-With': "com.tencent.mm",
        'Sec-Fetch-Site': "same-origin",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Dest': "empty",
        'Referer': "https://www.hotkidclub.com/",
        'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        'Cookie': token
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # print(response.text)
    return response.json()


def cpnInfo(token):
    url = "https://www.hotkidclub.com/api/cpn/year2025/cpnInfo.ctrl"

    payload = json.dumps({
        "adid": "2025festival-hotkidclub-click-2025_festival-1j8",
        "channel": "HKCMP",
        "joinChannel": "微信MP"
    })

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'Content-Type': "application/json",
        'sec-ch-ua': "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        'Timestamp': "1734147867185",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Windows\"",
        'Origin': "https://www.hotkidclub.com",
        'Sec-Fetch-Site': "same-origin",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Dest': "empty",
        'Referer': "https://www.hotkidclub.com/",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': token
    }

    response = requests.post(url, data=payload, headers=headers)
    res_json = response.json()

    # print(response.text)
    return res_json


def draw2025Year6(token, drawType):
    url = "https://www.hotkidclub.com/api/draw_centre/draw2025Year.ctrl"

    payload = json.dumps({
        "drawType": drawType,
        "acType": 1,
        "platform": "WEB",
        "channel": "WEIXINMP",
        "adid": "2025festival-hotkidclub-click-2025_festival-1j8"
    })

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
        'Content-Type': "application/json",
        'sec-ch-ua': "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        'Timestamp': "1734148447551",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Windows\"",
        'Origin': "https://www.hotkidclub.com",
        'Sec-Fetch-Site': "same-origin",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Dest': "empty",
        'Referer': "https://www.hotkidclub.com/",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': token
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)


if __name__ == '__main__':
    token_list = [
    
    ]
    for index, token in enumerate(token_list):
        task_list_json = get_tasklist(token)
        task_list = task_list_json["Response"]["data"]["taskList"]
        # print(task_list)
        print('任务列表')
        for task in task_list:
            mNumber = task["mNumber"]
            sNumber = task["sNumber"]
            taskName = task["taskName"]
            status = task["status"]
            task_type = task["type"]
            print(f"[{mNumber}/{sNumber}]   {taskName}")
            if taskName == "每日签到":
                if status == 0:
                    cpnSign(token)
            elif taskName == "每日游戏":
                    for _ in range(3):
                        grade=startGame(token)
                        print("游戏中")
                        time.sleep(150)
                        grabGameGetFragment(grade,token)
                        

