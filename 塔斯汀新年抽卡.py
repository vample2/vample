import requests
import random
import time
import base64
import hashlib
import execjs
import json
from urllib.parse import parse_qs, urlparse

import requests
def getUserToken(session,login_url):
    host = login_url.split('/')[0] + '//' + login_url.split('/')[2]
    url = host+"/xm/token/getUserToken"
    params = {
    'timestamp': "1737023703618",
    'nonceStr': "2ff483589a6371f998f60c152dd76bad",
    'tokenSign': "3a5e5f526923504c0e8c27038dcb318a"
    }
    parsed_url = urlparse(login_url)
    query_params = parse_qs(parsed_url.query)

    # 获取 'li' 参数值
    li_value = query_params.get('li', [None])[0]
    nonceStr=get_nonceStr()
    timestamp=str(int(time.time()*1000))
    tokenSign=calculate_md5_2(li_value+nonceStr+timestamp)
    params['nonceStr']=nonceStr
    params['timestamp']=timestamp
    params['tokenSign']=tokenSign

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': login_url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/131.0.0.0',
        'bdrk': 'null',
        'functionId': '0',
        'ri': '',
        'xmToken': '',
    }
    nonceStr=get_nonceStr()
    xmTimestamp=str(int(time.time()*1000))
    xmSign=calculate_md5(nonceStr+xmTimestamp+tokenSign)
    headers['nonceStr']=nonceStr
    headers['xmTimestamp']=xmTimestamp
    headers['xmSign']=xmSign

    response = session.get(url, params=params, headers=headers).json()

    return response['data']


def task_finish(session,login_url,taskId,xmToken,actOpId):
    host = login_url.split('/')[0] + '//' + login_url.split('/')[2]
    url = host+"/activity/function/task/finish"
    print(host)
    print(url)
    
    payload = {
    "actOpId": actOpId,
    "actionId": 0,
    "actionParams": {},
    "taskId": taskId,
    "timestamp": str(int(time.time()*1000)),
    "functionId": ""
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': host,
        'Pragma': 'no-cache',
        'Referer': login_url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/131.0.0.0',
        'bdrk': 'null',
        'functionId': '200460003',
        'ri': '',
        'xmToken': xmToken,
    }
    print(headers)
# '497642710{}1662486689000109100185923eee442a51dcb571805ad4565e803f7b173708246652217370824665228071021730503878021@1e25576999548f948b7bae75012eca74'
# '443494060{}076be840e224719a82ef6e91758b1fbd166248668900010910018592173708162234517370818319358071021730503878021@338f93c205b3cec13cfd4cba3b30e317'
# '497642710{}c6fbcb6110ad9658be956bf53e32d67c166248668900010910018592173708259282817370825928288071021730503878021@8680ec44675bc7a475caa3f6c915099f'
    nonceStr=get_nonceStr()
    xmTimestamp=str(int(time.time()*1000))
    m=payload['actOpId']+str(payload['actionId'])+str(payload['actionParams'])+nonceStr+payload['taskId']+payload['timestamp']+xmTimestamp+xmToken
    print(m)
    xmSign=calculate_md5(m)
    headers['nonceStr']=nonceStr
    headers['xmTimestamp']=xmTimestamp
    headers['xmSign']=xmSign

    response = session.post(url, data=json.dumps(payload), headers=headers)

    print(response.text)


def get_task(session,login_url):
    host = login_url.split('/')[0] + '//' + login_url.split('/')[2]

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': login_url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/131.0.0.0',
        'bdrk': 'null',
        'functionId': '200460003',
        'ri': '',
        'xmToken': '',
    }
    nonceStr=get_nonceStr()
    xmTimestamp=str(int(time.time()*1000))
    xmSign=calculate_md5(nonceStr+xmTimestamp)
    headers['nonceStr']=nonceStr
    headers['xmTimestamp']=xmTimestamp
    headers['xmSign']=xmSign

    response = session.get(
        host+'/activity/function/task/get',
        headers=headers,
    ).json()
    return response["data"]["taskList"]

# JavaScript 代码
def action(session,login_url,xmToken,actOpId):
    """
    抽卡
    """

    host = login_url.split('/')[0] + '//' + login_url.split('/')[2]
    url = host+"/activity/function/action"
    print(url)

    payload = {
    "functionId": 100460001,
    "actOpId": actOpId,
    "timestamp": int(time.time()*1000)
    }
    print(payload)

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': host,
        'Pragma': 'no-cache',
        'Referer': login_url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/131.0.0.0',
        'bdrk': 'null',
        'functionId': '100460001',
        'nonceStr': '02f6a6e7161b7afdb9e7175fe095c2c7',
        'ri': '',
        'xmSign': '31072cae79d9416b967e233fa38feee4',
        'xmTimestamp': '1737093855397',
        'xmToken': xmToken,
    }
    print(headers)
    nonceStr=get_nonceStr()
    xmTimestamp=str(int(time.time()*1000))

    m=str(payload['actOpId'])+str(payload['functionId'])+nonceStr+str(payload['timestamp'])+xmTimestamp+xmToken
    print(m)
    xmSign=calculate_md5(m)
    headers['nonceStr']=nonceStr
    headers['xmTimestamp']=xmTimestamp
    headers['xmSign']=xmSign

    response = session.post(url, data=json.dumps(payload), headers=headers).json()

    print(response)
    return response["code"]

def calculate_md5_2(m):
    # 解码 Base64 字符串为 UTF-8
    base64_string = "eG1wc0Bub2Nlc3RyIzEyM15QT0kmTW5w"
    decoded_string = base64.b64decode(base64_string).decode('utf-8')
    
    # 拼接字符串并计算 MD5
    combined_string = m + decoded_string
    md5_hash = hashlib.md5(combined_string.encode('utf-8')).hexdigest()
    
    return md5_hash
def calculate_md5(m):
    # 解码 Base64 字符串为 UTF-8
    base64_string = "eG1TaWduU2VjcmV0QDEyMyQlXjc4KDBRQVolNGZCfjk="
    decoded_string = base64.b64decode(base64_string).decode('utf-8')
    
    # 拼接字符串并计算 MD5
    combined_string = m + decoded_string
    md5_hash = hashlib.md5(combined_string.encode('utf-8')).hexdigest()
    
    return md5_hash

def get_nonceStr():
    return "".join(
        [
            hex(random.randint(0, 15))[2:] if char == "x" else hex((random.randint(0, 15) & 3) | 8)[2:]
            for char in "xxxxxxxxxxxx7xxxyxxxxxxxxxxxxxxx"
        ]
    )

def login(url):
    session = requests.Session()  # 创建 Session 对象
    headers = {
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/131.0.0.0",
        'xmToken': "",
        'bdrk': "null",
        'ri': "",
        'functionId': "0",
        'Sec-Fetch-Site': "same-origin",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Dest': "empty",
        'Accept-Language': "zh-CN,zh;q=0.9",
        }
    response = session.get(url, headers=headers)
    # response = session.get(response.url, headers=headers)
    return session,response.url


def getConfig(session,login_url):
    host = login_url.split('/')[0] + '//' + login_url.split('/')[2]

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': login_url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/131.0.0.0',
        'bdrk': 'null',
        'functionId': '0',
        'ri': '',
        'xmToken': '',
    }
    nonceStr=get_nonceStr()
    xmTimestamp=str(int(time.time()*1000))
    xmSign=calculate_md5(nonceStr+xmTimestamp)
    headers['nonceStr']=nonceStr
    headers['xmTimestamp']=xmTimestamp
    headers['xmSign']=xmSign

    response = session.get(
        host+'/activity/function/getConfig',
        headers=headers,
    ).json()
    return response["data"]["actOpId"]

def getBaseParams(session,login_url):
    host = login_url.split('/')[0] + '//' + login_url.split('/')[2]
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': login_url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/131.0.0.0',
        'bdrk': 'null',
        'functionId': '0',
        'nonceStr': '623e7c7ebb9c7fbc86a622f5d9182476',
        'ri': '',
        'xmSign': '6dc447cb35be0b22862d918fc4f70c44',
        'xmTimestamp': '1737092664182',
        'xmToken': '',
    }
    params = {
        'pageUrl': login_url,
    }

    nonceStr=get_nonceStr()
    xmTimestamp=str(int(time.time()*1000))
    xmSign=calculate_md5(params['pageUrl']+nonceStr+xmTimestamp)
    headers['nonceStr']=nonceStr
    headers['xmTimestamp']=xmTimestamp
    headers['xmSign']=xmSign


    response = session.get(
        host+'/xm/auth/getBaseParams',
        params=params,
        headers=headers,
    )
    print(response.text)


def getMpOriginalId(session,login_url):
    host = login_url.split('/')[0] + '//' + login_url.split('/')[2]
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': login_url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/131.0.0.0',
        'bdrk': 'null',
        'functionId': '0',
        'nonceStr': '856611801dc774d38f7c6bda3972b1b1',
        'ri': '',
        'xmSign': '914710e57c0355cbc945aa00c18ff5f6',
        'xmTimestamp': '1737092664024',
        'xmToken': '',
    }

    nonceStr=get_nonceStr()
    xmTimestamp=str(int(time.time()*1000))
    xmSign=calculate_md5(nonceStr+xmTimestamp)
    headers['nonceStr']=nonceStr
    headers['xmTimestamp']=xmTimestamp
    headers['xmSign']=xmSign



    response = session.get(
        host+'/private/merchant/getMpOriginalId',
        headers=headers,
    )
    print(response.text)

def getUserAccount(session,login_url):
    host = login_url.split('/')[0] + '//' + login_url.split('/')[2]
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': login_url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/131.0.0.0',
        'bdrk': 'null',
        'functionId': '0',
        'nonceStr': '856611801dc774d38f7c6bda3972b1b1',
        'ri': '',
        'xmSign': '914710e57c0355cbc945aa00c18ff5f6',
        'xmTimestamp': '1737092664024',
        'xmToken': '',
    }

    nonceStr=get_nonceStr()
    xmTimestamp=str(int(time.time()*1000))
    xmSign=calculate_md5(nonceStr+xmTimestamp)
    headers['nonceStr']=nonceStr
    headers['xmTimestamp']=xmTimestamp
    headers['xmSign']=xmSign



    response = session.get(
        host+'/activity/function/getUserAccount',
        headers=headers,
    )
    print(response.text)

def getUserAccountparams(session,login_url):
    host = login_url.split('/')[0] + '//' + login_url.split('/')[2]
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': login_url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/131.0.0.0',
        'bdrk': 'null',
        'functionId': '0',
        'nonceStr': '856611801dc774d38f7c6bda3972b1b1',
        'ri': '',
        'xmSign': '914710e57c0355cbc945aa00c18ff5f6',
        'xmTimestamp': '1737092664024',
        'xmToken': '',
    }
    params = {
    'functionId': '100460001',
    }


    nonceStr=get_nonceStr()
    xmTimestamp=str(int(time.time()*1000))
    xmSign=calculate_md5(params['functionId']+nonceStr+xmTimestamp)
    headers['nonceStr']=nonceStr
    headers['xmTimestamp']=xmTimestamp
    headers['xmSign']=xmSign



    response = session.get(
        host+'/activity/function/getUserAccount',
        headers=headers,
    )
    print(response.text)


if __name__ == '__main__':
# https://p3234966655219-tasiting.xiaoman-activity.meta-xuantan.com/xm/activity/place/3234966655219/46-88548-ptmj05oyx2/v1-hdzyfzts?。。。。&avatar=
    url_list=[
        ''
    
    ]
    for url in url_list:
        session,login_url=login(url)
        # notice(session,login_url)
        print(login_url)
        getBaseParams(session,login_url)
        actOpId=getConfig(session,login_url)
        print(actOpId)
        getMpOriginalId(session,login_url)
        getUserAccount(session,login_url)
        getUserAccountparams(session,login_url)
        # task_list=get_task(session,login_url)
        # for task in task_list:
        #     if task["taskTitle"] == '每日登录':
        #         if task["status"] == 0:
        #             xmToken=getUserToken(session,login_url)
        #             print(xmToken)
        #             print(task['taskId'])
        #             task_finish(session,login_url,task['taskId'],xmToken,actOpId)
        #         else:
        #             print('每日登录：已完成')
        #     if task["taskTitle"] == '每日分享':
        #         if task["status"] == 0:
        #             for _ in range(task["taskNum"]-task["finishNum"]):
        #                 xmToken=getUserToken(session,login_url)
        #                 print(xmToken)
        #                 print(task['taskId'])
        #                 task_finish(session,login_url,task['taskId'],xmToken,actOpId)
        #                 time.sleep(1)
        #         else:
        #             print('每日分享：已完成')
        print("开始抽卡")
        while True:
            xmToken=getUserToken(session,login_url)
            print(xmToken)
            code=action(session,login_url,xmToken,actOpId)
            if code == '-1':
                break
            # time.sleep(3)
            
