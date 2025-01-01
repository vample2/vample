import time
import os
import requests
from datetime import datetime

##获取账号名称
def login(apitoken):
  url = 'https://gateway.jmhd8.com/geement.usercenter/api/v1/user/information'

  headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
    'content-type': "application/x-www-form-urlencoded",
    'apitoken': apitoken,
    'xweb_xhr': "1",
    'unique_identity': "223a474b-5eb7-43c6-8eb9-38c6a03bb75b",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://servicewechat.com/wxd79ec05386a78727/86/page-frame.html",
    'accept-language': "zh-CN,zh;q=0.9"
  }

  params = {
    'levelprocessinfo': "false",
    'gpslocationinfo': "false",
    'popularizeinfo': "false",
    'disablequery_extra_field': "true",
    'disablequery_location': "true",
    'disablequery_memberinfo': "true",
    'disablequery_customfield': "true",
    'disablequery_levelinfo': "true",
    'disablequery_perfectinfo_status': "true",
    'disablequery_extrainformation': "true"
  }

  response = requests.get(url, headers=headers, params=params).json()
  # print(response)
  data = response['data']
  user_id = data['user_no']
  nick_name = data['nick_name']
  return user_id,nick_name


### 任务列表
def getTaskList(apitoken):
  url = 'https://gateway.jmhd8.com/geement.marketingplay/api/v1/task'

  headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
    'content-type': "application/x-www-form-urlencoded",
    'apitoken': apitoken,
    'xweb_xhr': "1",
    'unique_identity': "b78effb9-789e-416c-8e2b-84f7d9dadbb6",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://servicewechat.com/wxd79ec05386a78727/86/page-frame.html",
    'accept-language': "zh-CN,zh;q=0.9"
  }

  params = {
      'pageNum': '1',
      'pageSize': '10',
      'task_status': '2',
      'status': '1',
      'group_id': '24121016331837',
  }

  response = requests.get(url, headers=headers, params=params).json()
  return response['data']




def doTask(taskId,apitoken):
  url = 'https://gateway.jmhd8.com/geement.marketingplay/api/v1/task/join'

  headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
    'content-type': "application/x-www-form-urlencoded",
    'apitoken': apitoken,
    'xweb_xhr': "1",
    'unique_identity': "b78effb9-789e-416c-8e2b-84f7d9dadbb6",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://servicewechat.com/wxd79ec05386a78727/86/page-frame.html",
    'accept-language': "zh-CN,zh;q=0.9"
  }
  current_time = datetime.now()

  # 格式化为字符串
  time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')

  params = {
      'action_time': time_str,
      'task_id': taskId,
  }

  response = requests.get(url, headers=headers, params=params).json()
  print(response)
  # return response


def lottery(apitoken):

  url = "https://thirtypro.jmhd8.com/api/v1/nongfuwater/snake/checkerboard/lottery"

  payload = {
    "code": "SCENE-24121018362724",
    "provice_name": "上海市", 
    "city_name": "上海市",
    "area_name": "浦东新区", 
    "address": "上海市浦东新区东方路121号", 
    "longitude": 121.520630, 
    "dimension": 31.239136
  }

  headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
    'Content-Type': "application/json",
    'apitoken': apitoken,
    'xweb_xhr': "1",
    'unique_identity': "b78effb9-789e-416c-8e2b-84f7d9dadbb6",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://servicewechat.com/wxd79ec05386a78727/86/page-frame.html",
    'accept-language': "zh-CN,zh;q=0.9"
  }

  response = requests.post(url, data=payload, headers=headers)

  print(response.text)



def marketinglottery(apitoken,code):
  ##SCENE-24121018345681    每日赠送抽奖
  ##SCENE-24121018352070  任务抽奖
  url = 'https://gateway.jmhd8.com/geement.marketinglottery/api/v1/marketinglottery'

  headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
    'Content-Type': "application/json",
    'apitoken': apitoken,
    'xweb_xhr': "1",
    'unique_identity': "b78effb9-789e-416c-8e2b-84f7d9dadbb6",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://servicewechat.com/wxd79ec05386a78727/86/page-frame.html",
    'accept-language': "zh-CN,zh;q=0.9"
  }

  data = {"code": f"{code}", "provice_name": "上海市", "city_name": "上海市",
          "area_name": "浦东新区", "address": "上海市浦东新区东方路121号", "longitude": 121.520630, "dimension": 31.239136}
  
  # print(data)
  response = requests.post(url, headers=headers, json=data).json()
  if response['code'] == 500:
    print(response['msg'])
  else:
    print(response['data']['prizedto']['prize_name'])


def getSeniority():
  url = 'https://gateway.jmhd8.com/geement.usercenter/api/v1/user/seniority'

  headers = {
      'Host': 'gateway.jmhd8.com',
      'Connection': 'keep-alive',
      'Content-Type': 'application/x-www-form-urlencoded',
      'apitoken': apitoken,
      'xweb_xhr': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
      'unique_identity': '26bce5ae-e346-40f6-92ad-946294bf9bc6',
      'Accept': '*/*',
      'Sec-Fetch-Site': 'cross-site',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Dest': 'empty',
      'Referer': 'https://servicewechat.com/wxd79ec05386a78727/65/page-frame.html',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'zh-CN,zh;q=0.9',
  }

  params = {
      'sencodes': 'SEN42583085600829603841600711680',
  }

  response = requests.get(url, headers=headers, params=params).json()

  return response['data'][0]['total_count'] - response['data'][0]['used_count']


def seniority(apitoken):
  '''
  任务次数
  '''
  url = "https://gateway.jmhd8.com/geement.usercenter/api/v1/user/seniority"

  params = {
    'sencodes': "SEN24121014343942"
  }

  headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8461",
    'content-type': "application/x-www-form-urlencoded",
    'apitoken': apitoken,
    'xweb_xhr': "1",
    'unique_identity': "4d7e5ccb-4c9f-45b0-9ba7-d8701e766abf",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://servicewechat.com/wxd79ec05386a78727/86/page-frame.html",
    'accept-language': "zh-CN,zh;q=0.9"
  }

  response = requests.get(url, params=params, headers=headers)

  print(response.text)



def todaycount(apitoken):
  '''
    赠送次数情况
  '''

  url = "https://gateway.jmhd8.com/geement.actjextra/api/v1/act/lottery/data/todaycount"

  params = {
    'act_code': "ACT2412101428048"
  }

  headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581",
    'content-type': "application/x-www-form-urlencoded",
    'apitoken': apitoken,
    'xweb_xhr': "1",
    'unique_identity': "b78effb9-789e-416c-8e2b-84f7d9dadbb6",
    'sec-fetch-site': "cross-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://servicewechat.com/wxd79ec05386a78727/86/page-frame.html",
    'accept-language': "zh-CN,zh;q=0.9"
  }

  response = requests.get(url, params=params, headers=headers)

  # print(response.text)
  return response.json()["data"]




if __name__ == '__main__':
  # if os.environ.get("nfsq"):
  #   tokenString = os.environ["nfsq"]
  #   if tokenString != '':
  #     apitokenList = tokenString.split("#")
  #   else:
  #     print('没有配置nfsq')
  #     exit()
  # else:
  #   print('没有配置nfsq')
  #   exit()
  apitokenList=[
    ''
  ]
  for index,apitoken in enumerate(apitokenList):
    user_no,nick_name=login(apitoken)
    if nick_name == '':
      print(f"============账号user_id:{user_no}============")
    else:
      print(f"============账号nick_name:{nick_name}============")
    # print(user_id)
    everydata_counted=todaycount(apitoken)
  # print(everydata_counted)

    if everydata_counted < 3:
      code = "SCENE-24121018345681"
      for _ in range(3-everydata_counted):
        marketinglottery(apitoken,code)
        time.sleep(1)
    print("每日赠送抽奖",f"[{everydata_counted}/3]")
    # marketinglottery(api)
    taskList = getTaskList(apitoken)
    # print(taskList)
    print("======任务列表======")
    for task in taskList:
      task_name=task["name"]
      task_status=task["complete_status"]
      taskId = task['id']
      ##游戏次数
      allow_complete_count=task["allow_complete_count"]
      complete_count=task["complete_count"]
      if complete_count < allow_complete_count:
        print("时来运转游戏")
        for _ in range(allow_complete_count - complete_count):
          lottery(apitoken)
          time.sleep(1)
      else:
        print("时来运转游戏 [√]")
      if task_status == 1:
        print(task_name,"[√]")
      elif task_status == 0:
        doTask(taskId,apitoken)
        print(task_name,"[×]")
        time.sleep(1)



      
