import requests
import execjs
import subprocess
import json
import re

def get_h5st_from_js(args):
    try:
        # 将参数字典转换为 JSON 字符串
        args_json = json.dumps(args)
        
        # 执行 Node.js 脚本，传入参数，并指定编码为 utf-8
        result = subprocess.run(['node', 'js_security_v3_0.1.5.js',args_json], capture_output=True, text=True,encoding='utf-8')
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error executing Node.js script:", e.output)
        return None

# 参数字典
params = {
    'functionId': 'm_search_couponSearch',
    'appid': 'jd-cphdeveloper-m',
    'body': '{"tenantCode":"jgm","bizModelCode":5,"bizModeClientType":"M","externalLoginType":"1","coupon_batch":"1003364890","coupon_aggregation":"yes","neverpop":"yes","datatype":"1","page":"1","pagesize":"10","ext_attr":"no","brand_col":"no","price_col":"no","color_col":"no","size_col":"no","ext_attr_sort":"no","multi_suppliers":"yes","rtapi":"no","debug":"false"}',
    'loginType': '2',
    'x-api-eid-token': 'jdd035YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5IAAAAMTZ7Q47XQAAAAACT4KH2X3XI6I5UX',
    # 'h5st': '20241217142738681;fffy5ey5iez491u9;f6336;tk03wc97e1cef18naTBnGJsnCRNzJ6fBbbe0irbygGTd8lZiyBK5WCionWK2_nvqrEbbL2QlpRU--ollAuQLvc_sG5MN;03e13c62f7ce29418363d55ac83663a8;4.9;1734416858681;pjbMhjZd2mYd3DUSCWYNGWYNFSFSJrJdJrESJrpjh7Jf6rJdJz1TIipjLDrgJj4e3r4fzHIT0n1T5roeznFf6bldFelSHeIT3roSzrYTJrJdJrEa-OFTGOEjLrJp-jZSFS1T0bIT4XVeKaYf1T4f2T1f6HIfGiFf4PYe2fYS4jpjxj5PKSEQKeFjLrJp-j5e9HIg3T0UG6VRFuWeDipjxjJOJrpjh7Jj0eFP5SWbEila47nNJrJdJ31QHyVT5ipjLDrgJj4f9G1WJrJdJTlPJrpjh7ZMLrJp7rJdJLYOJipjLrpjh7JjJrJdJPYOJipjLrpjh7pd5rJdJTYOJipjLrpjh7pfLDIj2XETJrpjLrJp-rojxjpe2iFjLrpjLDrg5fojxj5f2iFjLrpjLDrg53pjxjJf2iFjLrpjLDrgJXIg6zpfJrJdJnYOJipjLrpjh7pfLDIjAOEjLrpjLDrg7rJdJfkQJrpjLrJp-rojxjpQJrpjLrJp-rojxjpS0ipjLrpjh-kjxjpS9WlOzWFjLrJp-3kjLDLjj_VYfm2X4CWOESHXMaFRJrJdJjoPJrpjLrJp-j5PGCEZBu3OUKUQ9m0UHCFjLDIj6rEjLrpjLD7NLDIj7qEjLrJp-jJYzXYbZ23gH6VR2inj2r5P2KUSdq5d7zJeLbVR8ikS9mnjwLUO9GlYJrJdJnVO4ipjLD7N;6401394ab08aff97a57648135e2d0f76',
}

# 调用函数并打印结果
result = get_h5st_from_js(params)

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
headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'origin': 'https://so.m.jd.com',
    'priority': 'u=1, i',
    'referer': 'https://so.m.jd.com/',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0',
    'x-referer-page': 'https://so.m.jd.com/list/couponSearch.action',
    'x-rp-client': 'h5_1.0.0',
}

params = {
    "functionId": "m_search_couponSearch",
    "appid": "jd-cphdeveloper-m",
    "body": "{\"tenantCode\":\"jgm\",\"bizModelCode\":5,\"bizModeClientType\":\"M\",\"externalLoginType\":\"1\",\"coupon_batch\":\"1003364890\",\"coupon_aggregation\":\"yes\",\"neverpop\":\"yes\",\"datatype\":\"1\",\"page\":\"1\",\"pagesize\":\"10\",\"ext_attr\":\"no\",\"brand_col\":\"no\",\"price_col\":\"no\",\"color_col\":\"no\",\"size_col\":\"no\",\"ext_attr_sort\":\"no\",\"multi_suppliers\":\"yes\",\"rtapi\":\"no\",\"debug\":\"false\"}",
    "loginType": 2,
    "x-api-eid-token": "jdd035YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5IAAAAMTZ7Q47XQAAAAACT4KH2X3XI6I5UX",
    'h5st': '20241217143752718;5qf8e8hvzi4eiil5;f6336;tk04wc4ebc7cc41lMiszKzNkYmwwpjbe-GVRGaYRxSkRzXldFmUerrbrYd_WPuPeEmYgoynM07YZ1iWdznFSGeFSFiYf;e211e27aeccb4f10a094f760de5302ad;4.9;1734417472718;of7ruCLj27VRCWleCCEODKYSzTVP2jpjxjpPFipjLDrg5nojxjJQIeFjLrJp-jJjLDIj7SnQEiVS0ipjLDrgJjpjxj5PKSEQKeFjLrJp-j5e9HIg3T0UG6VRFuWeDipjxjJOJrpjh7JjVm3f1fle0PnebiHNJrJdJ31QHyVT5ipjLDrgJj4f9G1WJrJdJTlPJrpjh7ZMLrJp7rJdJLYOJipjLrpjh7JjJrJdJPYOJipjLrpjh7pd5rJdJTYOJipjLrpjh7pfLDIj2XETJrpjLrJp-rojxjpe2iFjLrpjLDrg5fojxj5f2iFjLrpjLDrg53pjxjJf2iFjLrpjLDrgJXIg6zpfJrJdJnYOJipjLrpjh7pfLDIjAOEjLrpjLDrg7rJdJfkQJrpjLrJp-rojxjpQJrpjLrJp-rojxjpS0ipjLrpjh-kjxjpS9WlOzWFjLrJp-3kjLDLjj_VYfm2X4CWOESHXMaFRJrJdJjoPJrpjLrJp-j5PGCEZBu3OUKUQ9m0UHCFjLDIj6rEjLrpjLD7NLDIj7qEjLrJp-jJYzXYbZ23gH6VR2inj2r5P2KUSdq5d7zJeLbVR8ikS9mnjwLUO9GlYJrJdJnVO4ipjLD7N;07116d8628862e016df535c9779ec10d',
}

response = requests.get('https://api.m.jd.com/api', params=params, headers=headers)
print(response.text)
print(response)
