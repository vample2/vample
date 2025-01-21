import execjs
import subprocess
import json
import re
import time
def get_h5st_from_js(args):
    try:
        # 将参数字典转换为 JSON 字符串
        args_json = json.dumps(args)
        
        # 执行 Node.js 脚本，传入参数，并指定编码为 utf-8
        result = subprocess.run(['node', 'h5st5_0_4.js',args_json], capture_output=True, text=True,encoding='utf-8')
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error executing Node.js script:", e.output)
        return None


if __name__ == '__main__':
        params = {
            'appid': '',
            'functionId': '',
            'body': body,
            'loginType': 2,
            'x-api-eid-token': '',

        }
        # 调用函数并打印结果
        h5st_params={
            "appId":"f6336",
            "params":params
        }
        if headers.get('cookie'):
            h5st_params['cookie'] = headers['cookie']

        if headers.get('user-agent'):
            h5st_params['useragent'] = headers['user-agent']
        # print(h5st_params)
        print("获取h5st")
        result = get_h5st_from_js(h5st_params)
        # print(result)
        # Now perform the search on the decoded output
        match = re.search(r'\$\$(.*?)\$\$', result)

        # Check if the match is found
        if match:
            h5st_value = match.group(1)
            print("h5st value:", h5st_value)
            print("h5st length:", len(h5st_value))
        else:
            print("h5st not found")
        # print("----------------------------", h5st)
        # print("h5st:", h5st)
        params['h5st']=h5st_value
