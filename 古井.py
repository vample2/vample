



import requests
import json
def shareClick(token,shareMemberId):
    """
    助力
    """

    url = "https://scrm.gujing.com/gujing_scrm/wxclient/mkt/activities/collectCards:shareClick"

    payload = json.dumps({
    "activityId": 110001353,
    "shareMemberId": shareMemberId
    })

    headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
    'Content-Type': "application/json",
    'xweb_xhr': "1",
    'Access-Token': token,
    'Sec-Fetch-Site': "cross-site",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Dest': "empty",
    'Referer': "https://servicewechat.com/wxba9855bdb1a45c8e/143/page-frame.html",
    'Accept-Language': "zh-CN,zh;q=0.9"
    }

    response = requests.post(url, data=payload, headers=headers)
    print(response)
    print(response.text)
            


def token_info(token):
    """
    获取账号信息和助力码
    """
    url = "https://scrm.gujing.com/gujing_scrm/wxclient/member/info"

    headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
    'xweb_xhr': "1",
    'Access-Token': token,
    'Content-Type': "application/json",
    'Sec-Fetch-Site': "cross-site",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Dest': "empty",
    'Referer': "https://servicewechat.com/wxba9855bdb1a45c8e/143/page-frame.html",
    'Accept-Language': "zh-CN,zh;q=0.9"
    }

    response = requests.get(url, headers=headers).json()
    mobile=response["content"]["mobile"]
    mobile = mobile[:3] + "*" * 4 + mobile[7:]
    id=response["content"]["id"]
    with open("help_codes.json", "w") as f:
        json.dump(id, f)
    return mobile,id
    # print(response.text)
def get_sign(token):
    url = "https://scrm.gujing.com/gujing_scrm/wxclient/mkt/activities/collectCards:sign"

    payload = json.dumps({
    "activityId": 110001353
    })

    headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
    'Content-Type': "application/json",
    'xweb_xhr': "1",
    'Access-Token': token,
    'Sec-Fetch-Site': "cross-site",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Dest': "empty",
    'Referer': "https://servicewechat.com/wxba9855bdb1a45c8e/143/page-frame.html",
    'Accept-Language': "zh-CN,zh;q=0.9"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)



def ruleInfoList(token):
    url = "https://scrm.gujing.com/gujing_scrm/wxclient/mkt/activities/collectCards/ruleInfoList"

    payload = json.dumps({
    "activityId": 110001353
    })

    headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
    'Content-Type': "application/json",
    'xweb_xhr': "1",
    'Access-Token': token,
    'Sec-Fetch-Site': "cross-site",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Dest': "empty",
    'Referer': "https://servicewechat.com/wxba9855bdb1a45c8e/143/page-frame.html",
    'Accept-Language': "zh-CN,zh;q=0.9"
    }

    response = requests.post(url, data=payload, headers=headers).json()
    content=response["content"]
    # print(response.text)
    return content
def load_help_codes(file_name="help_codes.json"):
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"文件 {file_name} 不存在！")
        return {}
def get_help_list_for_task(all_help_codes, current_id):
    """
    获取去除当前账号助力码后的列表
    :param all_help_codes: 包含所有账号助力码的字典
    :param current_id: 当前账号的助力码
    :return: 去除当前账号助力码后的列表
    """
    return [code for code in all_help_codes.values() if code != current_id] 

if __name__ == '__main__':
    all_help_codes = load_help_codes()
    help_codes={}
    token_list=[

    ]
    for token in token_list:
        mobile,id=token_info(token)
        if id not in help_codes:
            # help_codes[mobile]=[]
            help_codes[mobile]=id
        print("登录账号：",mobile,"助力码：",id)

        content=ruleInfoList(token)
        for index,info in enumerate(content):
            ruleName=info["ruleName"]
            numberSetting=info['numberSetting']
            currentNumber=info['currentNumber']
            if ruleName == '签到获得卡片':
                if int(numberSetting) != int(currentNumber):
                    print("执行签到任务")
                    
                    get_sign(token)
            if ruleName == '分享活动':
                print("执行助力任务")
                print(info)
                if int(info['everyDayLimitNumber']) != int(currentNumber):
                    help_list = get_help_list_for_task(all_help_codes, id)
                    for helpid in help_list:
                        print("助力：",helpid)
                        shareClick(token,helpid)
    with open("help_codes.json", "w") as f:
        json.dump(help_codes, f)
    print("保存助力码")
