from curl_cffi import requests
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
        result = subprocess.run(['node', 'js_security_v3_0.1.5.js',args_json], capture_output=True, text=True,encoding='utf-8')
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error executing Node.js script:", e.output)
        return None

# 参数字典
# params = {
#     'functionId': 'm_search_couponSearch',
#     'appid': 'jd-cphdeveloper-m',
#     'body': '{"tenantCode":"jgm","bizModelCode":5,"bizModeClientType":"M","externalLoginType":"1","coupon_batch":"1003364890","coupon_aggregation":"yes","neverpop":"yes","datatype":"1","page":"5","pagesize":"40","ext_attr":"no","brand_col":"no","price_col":"no","color_col":"no","size_col":"no","ext_attr_sort":"no","multi_suppliers":"yes","rtapi":"no","debug":"false"}',
#     'loginType': '2',
#     "x-api-eid-token": "jdd035YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5IAAAAMTZ7Q47XQAAAAACT4KH2X3XI6I5UX",
#      # 'h5st': '20241217153152626;vf0qq85e1e9zilr6;f6336;tk03w65ef1ab518n1AM31X0tbo5URi9AXj4G_KpiH2DbXfdvE1Moi9W2UBhN_AEfrTvZ0wTqX127_IkQGD3KqOC0fTEu;3c6b9453199147f465819ab5bde2799d;4.9;1734420712626;pjbMhjJe56VRxGYS6XVeznUP7TFOJrJdJrESJrpjh7Jf6rJdJz1TIipjLDrgJj4e3r4fzHIT0n1T5roeznFf6bldFelSHeIT3roSzrYTJrJdJrEa-OFTGOEjLrJp-jZSFS1T0bIT4XVeKaYf1T4f2T1f6HIfGiFf4PYe2fYS4jpjxj5PKSEQKeFjLrJp-j5e9HIg3T0UG6VRFuWeDipjxjJOJrpjh7JjKG2fBC1Y5O1SMe0TJrJdJ31QHyVT5ipjLDrgJj4f9G1WJrJdJTlPJrpjh7ZMLrJp7rJdJLYOJipjLrpjh7JjJrJdJPYOJipjLrpjh7pe4rJdJTYOJipjLrpjh7pfLDIj2XETJrpjLrJp-rojxjpe2iFjLrpjLDrg6fojxj5f2iFjLrpjLDrg53pjxjJf2iFjLrpjLDrgJXIg6zpfJrJdJnYOJipjLrpjh7pfLDIjAOEjLrpjLDrg7rJdJfkQJrpjLrJp-rojxjpQJrpjLrJp-rojxjpS0ipjLrpjh-kjxjpS9WlOzWFjLrJp-3kjLDLjj_VYfm2X4CWOESHXMaFRJrJdJjoPJrpjLrJp-j5PGCEZBu3OUKUQ9m0UHCFjLDIj6rEjLrpjLD7NLDIj7qEjLrJp-jJYzXYbZ23gH6VR2inj2r5P2KUSdq5d7zJeLbVR8ikS9mnjwLUO9GlYJrJdJnVO4ipjLD7N;b40248ef2cf007b124d1e21cb4a9adf6',
# }

# # 调用函数并打印结果
# result = get_h5st_from_js(params)
# print(result)
# # Now perform the search on the decoded output
# match = re.search(r'\$\$(.*?)\$\$', result)

# # Check if the match is found
# if match:
#     h5st_value = match.group(1)
#     print("h5st value:", h5st_value)
#     print("h5st length:", len(h5st_value))
# else:
#     print("h5st not found")
# # print("----------------------------", h5st)
# # print("h5st:", h5st)
# params['h5st']=h5st_value
# print(params)
# headers = {
#     'accept': 'application/json',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'cookie': 'shshshfpa=6c8165a2-c1ba-1fed-ed1b-2435212deff6-1695291512; shshshfpx=6c8165a2-c1ba-1fed-ed1b-2435212deff6-1695291512; jcap_dvzw_fp=G_jilqTZxGOFoyiKs4CbWvb9twZmFaOpqH9jhRF6Drc6tJymTDFyV2q2VemscVp3C9HJnQYA7YP5U-WjcrFd_A==; whwswswws=; TrackID=1gAPp4BdypGDOURSeMBye4FoEb4G8ZZ69LK5H-jf5Kz9Q8uFHeDs_AkNeAyDGC7OhM2RiD9LOQCc9SDGJMrm43_vI7dc83_cXXdGIzUaM3ck; light_key=AASBKE7rOxgWQziEhC_QY6yappPLxNKcFskARK5KkUvJA9o4IhkLpMKOkMr1sViuWO5-FRJ1; pinId=zKNkEUXVM7WAc2lkmNayQw; pin=jd_RFguZsSQLMkH; unick=%E6%A1%91%E6%A6%86%E9%9D%9E%E6%99%9A%E6%9F%A0%E6%9C%88%E5%A6%82%E9%A3%8Ec; b_webp=1; b_avif=1; b_dpr=1.25; __jdu=17143788493461841221692; autoOpenApp_downCloseDate_jd_homePage=1733535635432_1; mba_muid=17143788493461841221692; b_dw=1018; b_dh=1034; autoOpenApp_downCloseDate_auto=1733725464733_1800000; webp=1; visitkey=4644584812236839534; joyya=1733725472.1733725473.41.1jt0r14w2; sc_width=2048; mt_xid=V2_52007VwMUUlhaVFMWTBFeAGADG1ddW1FaGEEabFVvV0ZRWwsHRksaSw4ZYgBFBkELUVkcVU0LDWcHR1YNC1cKT3kaXQZiHxJRQVlaSx9MEl8AbAcSYl9oUmoWQRxaBGQDFFZaWFJdF0kZVABkMxdTVF4%3D; ipLoc-djd=14-1127-1129-49140; 3AB9D23F7A4B3C9B=5YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5I; TrackerID=NyuaNCn6q-qic0mFPP4IXZaA2CK_NQmj1RHA2OYqQ4gZNwRJx79vCn1dhQ2o3M311S93P8pBOH5Qh4N4dclGbJnvdj6-QxlWfpDZTCkQWDGoTIsEyi9bMUu5-b1lfUzt; pt_key=AAJnVo4pADCV4zMqMNHo0-BasaYgDBp-Im6R5Uij0SraTyvWaZrFZ9zowmcWXt5BFm-Nd6A01OE; pt_pin=jd_qnmxWwOjJzes; pt_token=2q1d7g8i; pwdt_id=jd_qnmxWwOjJzes; abtest=20241209194227337_12; cid=9; warehistory="100120894416,100145676660,100138662730,100120894416,100091180530,100120894416,100006341283,100120894416,100077085270,100077085270,"; autoOpenApp_downCloseDate_autoOpenApp_autoPromptly=1733744570671_1; __jdv=181111935%7Candroidapp%7Ct_335139774%7Cappshare%7CCopyURL%7C1734062714695; addrId_1=6129929309; mitemAddrId=7_412_63461_63474; mitemAddrName=%u6CB3%u5357%u90D1%u5DDE%u5E02%u90D1%u5DDE%u822A%u7A7A%u6E2F%u7ECF%u6D4E%u7EFC%u5408%u5B9E%u9A8C%u533A%u9F99%u6E2F%u8857%u9053%u9F99%u738B%u4E61%u601D%u5B58%u8DEF%u9F99%u5B89%u793E%u533A%u4E94%u53F7%u9662%u897F%u4FA7%u9F99%u5B89%u793E%u533A3%u53F7%u9662; wq_addr=6129929309%7C7_412_63461_63474%7C%u6CB3%u5357_%u90D1%u5DDE%u5E02_%u90D1%u5DDE%u822A%u7A7A%u6E2F%u7ECF%u6D4E%u7EFC%u5408%u5B9E%u9A8C%u533A_%u9F99%u6E2F%u8857%u9053%7C%u6CB3%u5357%u90D1%u5DDE%u5E02%u90D1%u5DDE%u822A%u7A7A%u6E2F%u7ECF%u6D4E%u7EFC%u5408%u5B9E%u9A8C%u533A%u9F99%u6E2F%u8857%u9053%u9F99%u738B%u4E61%u601D%u5B58%u8DEF%u9F99%u5B89%u793E%u533A%u4E94%u53F7%u9662%u897F%u4FA7%u9F99%u5B89%u793E%u533A3%u53F7%u9662%7C113.854646%2C34.437974; wxa_level=1; PPRD_P=UUID.17143788493461841221692; jxsid_s_u=https%3A//so.m.jd.com/list/couponSearch.action; shshshfpb=BApXS3oqMzPZAd8uyM_3xWV_STUKa614sB9doEj1v9xJ1PdZfQpfYnwLcmwTwGZx2YKJg-afn; jxsid=17343547602129236876; __jda=181111935.17143788493461841221692.1714378849.1734356571.1734416847.47; __jdc=181111935; cd_eid=jdd035YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5IAAAAMTZ7Q47XQAAAAACT4KH2X3XI6I5UX; 3AB9D23F7A4B3CSS=jdd035YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5IAAAAMT2NGNMOQAAAAADTGUMBEA4D2V7UX; _gia_d=1; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; appCode=ms0ca95114; jxsid_s_t=1734416856369; retina=1; wqmnx1=MDEyNjM1NHNvZC8vb3JjP29jMDg0ODI5b2EgdW5kO3VCLzhwZS8zSCAgb3IxLk1lYTMgMS40cjJmLTJLV1VJIyYoKQ%3D%3D; __jdb=181111935.2.17143788493461841221692|47.1734416847; mba_sid=17344168474449306899780510090.3; __wga=1734416858774.1734416847971.1734353361281.1733725483935.2.8',
#     'origin': 'https://so.m.jd.com',
#     'priority': 'u=1, i',
#     'referer': 'https://so.m.jd.com/',
#     'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     'sec-ch-ua-mobile': '?1',
#     'sec-ch-ua-platform': '"Android"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0',
#     'x-referer-page': 'https://so.m.jd.com/list/couponSearch.action',
#     'x-rp-client': 'h5_1.0.0',
# }
# h5st_params = {
#     "ver": "4.9.7",
#     "ai": "f6336",
#     "sua": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0",
#     "appid": params["appid"],  # 假设 `params` 字典中已有这个键
#     "functionId": params["functionId"],  # 同上
#     "body": params['body']  # 假设 `body` 已定义
# }

# # 发起请求
# h5st = requests.get("http://101.43.103.15:6868/www/api/h5st", params=h5st_params).text
# params['h5st']=h5st
# # http://101.43.103.15:6868/api/h5st?ver=4.9.2&ai=f6336&sua=iPhone; CPU iPhone OS 13_2_3 like Mac OS X&appid={params['appid']}&functionId={params['functionId']}&body={body}
# print("h5st:", h5st)
# print(len(h5st))
# params = {
#     "functionId": "m_search_couponSearch",
#     "appid": "jd-cphdeveloper-m",
#     "body": '{"tenantCode":"jgm","bizModelCode":5,"bizModeClientType":"M","externalLoginType":"1","coupon_batch":"1003364890","coupon_aggregation":"yes","neverpop":"yes","datatype":"2","page":"1","pagesize":"1","ext_attr":"yes","brand_col":"yes","price_col":"yes","color_col":"yes","size_col":"yes","ext_attr_sort":"yes","merge_sku":"yes","multi_suppliers":"yes","rtapi":"no","new_brand_val":"yes","qp_disable":"no","attr_only":"yes","coupon_kind":"1","coupon_shopid":"0","debug":"false"}',
#     "loginType": 2,
#     "x-api-eid-token": "jdd035YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5IAAAAMTZ7Q47XQAAAAACT4KH2X3XI6I5UX",
#     'h5st': '20241217171409129;fyh8vq0qzzzelku3;f6336;tk04w637f7ff741lMiszQ0p4ak5apj7f2_lQGCENxmkf6SkdDGESrrbrYdOy86VeEmYgoynM07YZ1iWdzLYTHeVSIWod;a305ce37b1b41b12e22b70e893bd60dd;4.9;1734426849129;of7ruCLj4X0R-WFNxCUP7nEOzLVNFipjxjpPFipjLDrg5nojxjJQIeFjLrJp-jJjLDIj7SnQEiVS0ipjLDrgJjpjxj5PKSEQKeFjLrJp-j5e9HIg3T0UG6VRFuWeDipjxjJOJrpjh7JjIaUf82nY2_VfFmGSJrJdJ31QHyVT5ipjLDrgJj4f9G1WJrJdJTlPJrpjh7ZMLrJp5rJdJLYOJipjLrpjh7JjJrJdJPYOJipjLrpjh7pd5rJdJTYOJipjLrpjh7pfLDIj2XETJrpjLrJp-rojxjpe2iFjLrpjLDrg5fojxj5f2iFjLrpjLDrg53pjxjJf2iFjLrpjLDrgJXIg6zpfJrJdJnYOJipjLrpjh7pfLDIjAOEjLrpjLDrg5rJdJfkQJrpjLrJp-rojxjpQJrpjLrJp-rojxjpS0ipjLrpjh-kjxjpS9WlOzWFjLrJp-3kjLDLjj_VYfm2X4CWOESHXMaFRJrJdJjoPJrpjLrJp-j5PGCEZBu3OUKUQ9m0UHCFjLDIj6rEjLrpjLD7NLDIj7qEjLrJp-jJYzXYbZ23gH6VR2inj2r5P2KUSdq5d7zJeLbVR8ikS9mnjwLUO9GlYJrJdJnVO4ipjLD7N;5ecfdb7a09be05651d0b5d5a1544aad1',
# }

# response = requests.get('https://api.m.jd.com/api', params=params, headers=headers)
# print(response.text)
# print(response)
# page=1
# coupon_batch=1003364890
# body = f'{{"tenantCode":"jgm","bizModelCode":5,"bizModeClientType":"M","externalLoginType":"1","coupon_batch":"{coupon_batch}","coupon_aggregation":"yes","neverpop":"yes","datatype":"1","page":"{page}","pagesize":"50","ext_attr":"no","brand_col":"no","price_col":"no","color_col":"no","size_col":"no","ext_attr_sort":"no","multi_suppliers":"yes","rtapi":"no","debug":"false"}}'

# params  = {
#     "functionId": "m_search_couponSearch",
#     "appid": "jd-cphdeveloper-m",
#     "body": "{"tenantCode":"jgm\",\"bizModelCode\":5,\"bizModeClientType\":\"M\",\"externalLoginType\":\"1\",\"coupon_batch\":\"1003364890\",\"coupon_aggregation\":\"yes\",\"neverpop\":\"yes\",\"datatype\":\"1\",\"page\":\"1\",\"pagesize\":\"10\",\"ext_attr\":\"no\",\"brand_col\":\"no\",\"price_col\":\"no\",\"color_col\":\"no\",\"size_col\":\"no\",\"ext_attr_sort\":\"no\",\"multi_suppliers\":\"yes\",\"rtapi\":\"no\",\"debug\":\"false\"}",
#     "loginType": "2",
#     "x-api-eid-token": "jdd035YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5IAAAAMTZJYRGFIAAAAADMDPJ6XDSWSCTMX",
#     "h5st": "20241216133558996;fffy5ey5iez491u9;f6336;tk03wc5cd1cd618njFYHIXGqOKaIleJRYjdh3vXkjszjYgVSLc26wkeUFZWfu17rcSk019eU7eGNQX2olALMsqvwVnd7;e7f1d4c1674bba5abf6276001effc8d8;4.9;1734327358996;pjbMhjZd2mYd3DUSCWYNGWYNFSFSJrJdJrESJrpjh7Jf6rJdJz1TIipjLDrgJj4e3r4fzHIT0n1T5roeznFf6bldFelSHeIT3roSzrYTJrJdJrEa-OFTGOEjLrJp-jZSFS1T0bIT4XVeKaYf1T4f2T1f6HIfGiFf4PYe2fYS4jpjxj5PKSEQKeFjLrJp-j5e9HIg3T0UG6VRFuWeDipjxjJOJrpjh7JjDu3P6SHTyeHTimXaJrJdJ31QHyVT5ipjLDrgJj4f9G1WJrJdJTlPJrpjh7ZMLrJp7rJdJLYOJipjLrpjh7JjJrJdJPYOJipjLrpjh7pd5rJdJTYOJipjLrpjh7pfLDIj2XETJrpjLrJp-rojxjpe2iFjLrpjLDrg5fojxj5f2iFjLrpjLDrg53pjxjJf2iFjLrpjLDrgJXIg6zpfJrJdJnYOJipjLrpjh7pfLDIjAOEjLrpjLDrg7rJdJfkQJrpjLrJp-rojxjpQJrpjLrJp-rojxjpS0ipjLrpjh-kjxjpS9WlOzWFjLrJp-3kjLDLjj_VYfm2X4CWOESHXMaFRJrJdJjoPJrpjLrJp-j5PGCEZBu3OUKUQ9m0UHCFjLDIj6rEjLrpjLD7NLDIj7qEjLrJp-jJYzXYbZ23gH6VR2inj2r5P2KUSdq5d7zJeLbVR8ikS9mnjwLUO9GlYJrJdJnVO4ipjLD7N;3865c40bcaba00226e94496c964b76cb"
# }

# divs = select.xpath('//li[@class="gl-item"]')
# print(divs)
# for div in divs:
#     sku = div.xpath('string(./@data-sku)').get()
#     print(sku)
with open('2.md', 'a', encoding='utf-8') as file:
    file.write("| 名称                    | ID                  | 折扣                  | 价格                  |\n")
    file.write("|-------------------------|---------------------|-----------------------|-----------------------|\n")


class GETID:
    def __init__(self):
        self.id_list = []
        self.total_id_list = []
        self.saver = []
        self.page_id = []
    # print(name)
    # print(sku)
    # print(discount)
    # print(discount1)

    # if sku not in data_list:
    #     with open(file_path1, 'a') as file:
    #         file.write(f'{sku}\n')
    #     with open(file_path2, 'a') as filel:
    #         filel.write(f'{sku}\n')
    def get_info(self, coupon_batch, page):
        body = f'{{"tenantCode":"jgm","bizModelCode":5,"bizModeClientType":"M","externalLoginType":"1","coupon_batch":"{coupon_batch}","coupon_aggregation":"yes","neverpop":"yes","datatype":"1","page":"{page}","pagesize":"50","ext_attr":"no","brand_col":"no","price_col":"no","color_col":"no","size_col":"no","ext_attr_sort":"no","multi_suppliers":"yes","rtapi":"no","debug":"false"}}'

        params = {
            'appid': 'jd-cphdeveloper-m',
            'functionId': 'm_search_couponSearch',
            'body': body,
            'loginType': 2,
            "x-api-eid-token": "jdd035YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5IAAAAMTZ7Q47XQAAAAACT4KH2X3XI6I5UX",
        }
        # 调用函数并打印结果
        result = get_h5st_from_js(params)
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
        print(params)
        #print(params)
        headers = {
            'accept': 'application/json',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cookie': 'shshshfpa=6c8165a2-c1ba-1fed-ed1b-2435212deff6-1695291512; shshshfpx=6c8165a2-c1ba-1fed-ed1b-2435212deff6-1695291512; jcap_dvzw_fp=G_jilqTZxGOFoyiKs4CbWvb9twZmFaOpqH9jhRF6Drc6tJymTDFyV2q2VemscVp3C9HJnQYA7YP5U-WjcrFd_A==; whwswswws=; TrackID=1gAPp4BdypGDOURSeMBye4FoEb4G8ZZ69LK5H-jf5Kz9Q8uFHeDs_AkNeAyDGC7OhM2RiD9LOQCc9SDGJMrm43_vI7dc83_cXXdGIzUaM3ck; light_key=AASBKE7rOxgWQziEhC_QY6yappPLxNKcFskARK5KkUvJA9o4IhkLpMKOkMr1sViuWO5-FRJ1; pinId=zKNkEUXVM7WAc2lkmNayQw; pin=jd_RFguZsSQLMkH; unick=%E6%A1%91%E6%A6%86%E9%9D%9E%E6%99%9A%E6%9F%A0%E6%9C%88%E5%A6%82%E9%A3%8Ec; b_webp=1; b_avif=1; b_dpr=1.25; __jdu=17143788493461841221692; autoOpenApp_downCloseDate_jd_homePage=1733535635432_1; mba_muid=17143788493461841221692; b_dw=1018; b_dh=1034; autoOpenApp_downCloseDate_auto=1733725464733_1800000; webp=1; visitkey=4644584812236839534; joyya=1733725472.1733725473.41.1jt0r14w2; sc_width=2048; mt_xid=V2_52007VwMUUlhaVFMWTBFeAGADG1ddW1FaGEEabFVvV0ZRWwsHRksaSw4ZYgBFBkELUVkcVU0LDWcHR1YNC1cKT3kaXQZiHxJRQVlaSx9MEl8AbAcSYl9oUmoWQRxaBGQDFFZaWFJdF0kZVABkMxdTVF4%3D; ipLoc-djd=14-1127-1129-49140; 3AB9D23F7A4B3C9B=5YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5I; TrackerID=NyuaNCn6q-qic0mFPP4IXZaA2CK_NQmj1RHA2OYqQ4gZNwRJx79vCn1dhQ2o3M311S93P8pBOH5Qh4N4dclGbJnvdj6-QxlWfpDZTCkQWDGoTIsEyi9bMUu5-b1lfUzt; pt_key=AAJnVo4pADCV4zMqMNHo0-BasaYgDBp-Im6R5Uij0SraTyvWaZrFZ9zowmcWXt5BFm-Nd6A01OE; pt_pin=jd_qnmxWwOjJzes; pt_token=2q1d7g8i; pwdt_id=jd_qnmxWwOjJzes; abtest=20241209194227337_12; cid=9; warehistory="100120894416,100145676660,100138662730,100120894416,100091180530,100120894416,100006341283,100120894416,100077085270,100077085270,"; autoOpenApp_downCloseDate_autoOpenApp_autoPromptly=1733744570671_1; __jdv=181111935%7Candroidapp%7Ct_335139774%7Cappshare%7CCopyURL%7C1734062714695; addrId_1=6129929309; mitemAddrId=7_412_63461_63474; mitemAddrName=%u6CB3%u5357%u90D1%u5DDE%u5E02%u90D1%u5DDE%u822A%u7A7A%u6E2F%u7ECF%u6D4E%u7EFC%u5408%u5B9E%u9A8C%u533A%u9F99%u6E2F%u8857%u9053%u9F99%u738B%u4E61%u601D%u5B58%u8DEF%u9F99%u5B89%u793E%u533A%u4E94%u53F7%u9662%u897F%u4FA7%u9F99%u5B89%u793E%u533A3%u53F7%u9662; wq_addr=6129929309%7C7_412_63461_63474%7C%u6CB3%u5357_%u90D1%u5DDE%u5E02_%u90D1%u5DDE%u822A%u7A7A%u6E2F%u7ECF%u6D4E%u7EFC%u5408%u5B9E%u9A8C%u533A_%u9F99%u6E2F%u8857%u9053%7C%u6CB3%u5357%u90D1%u5DDE%u5E02%u90D1%u5DDE%u822A%u7A7A%u6E2F%u7ECF%u6D4E%u7EFC%u5408%u5B9E%u9A8C%u533A%u9F99%u6E2F%u8857%u9053%u9F99%u738B%u4E61%u601D%u5B58%u8DEF%u9F99%u5B89%u793E%u533A%u4E94%u53F7%u9662%u897F%u4FA7%u9F99%u5B89%u793E%u533A3%u53F7%u9662%7C113.854646%2C34.437974; wxa_level=1; PPRD_P=UUID.17143788493461841221692; jxsid_s_u=https%3A//so.m.jd.com/list/couponSearch.action; shshshfpb=BApXS3oqMzPZAd8uyM_3xWV_STUKa614sB9doEj1v9xJ1PdZfQpfYnwLcmwTwGZx2YKJg-afn; jxsid=17343547602129236876; __jda=181111935.17143788493461841221692.1714378849.1734356571.1734416847.47; __jdc=181111935; cd_eid=jdd035YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5IAAAAMTZ7Q47XQAAAAACT4KH2X3XI6I5UX; 3AB9D23F7A4B3CSS=jdd035YGHXAUGIDZYONNUNS7TNLR7K5APOTGKL5IQQFWW5LQCXFMVJ3LWSFLNBZDBVAVVMOVDD52PYX2IEMZZSQMDY64M5IAAAAMT2NGNMOQAAAAADTGUMBEA4D2V7UX; _gia_d=1; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; appCode=ms0ca95114; jxsid_s_t=1734416856369; retina=1; wqmnx1=MDEyNjM1NHNvZC8vb3JjP29jMDg0ODI5b2EgdW5kO3VCLzhwZS8zSCAgb3IxLk1lYTMgMS40cjJmLTJLV1VJIyYoKQ%3D%3D; __jdb=181111935.2.17143788493461841221692|47.1734416847; mba_sid=17344168474449306899780510090.3; __wga=1734416858774.1734416847971.1734353361281.1733725483935.2.8',
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

        response = requests.get("https://api.m.jd.com/", headers=headers, params=params)
        # print("Response:", response.text)
        print(response)
        return response

    def process_response(self, data):
        print(data)
        self.id_list.clear()
        self.page_id.clear()
        data_json = data.json()
        data1 = data_json['data']
        # print(data1)
        Paragraph = data1["searchm"]["Paragraph"]
        Summary = data1["searchm"]["Head"]["Summary"]
        page_info = Summary["Page"]
        ResultCount = Summary["ResultCount"]
        # print(ResultCount)
        PageCount = page_info["PageCount"]
        PageIndex = page_info["PageIndex"]
        print(f"获取第{PageIndex}页商品,共{PageCount}页")

        # print(Paragraph)
        for paragraph_item in Paragraph:
            # print(paragraph_item['pfdt'])
            wareid = paragraph_item["wareid"]
            self.page_id.append(wareid)
            if wareid not in self.total_id_list:
                self.total_id_list.append(wareid)

                item_pfdt = paragraph_item['pfdt']
                warename = paragraph_item['Content']["warename"]
                price = paragraph_item["dredisprice"]

                if item_pfdt != {'t': '', 'j': '', 'm': ''}:
                    self.id_list.append(wareid)
                    if item_pfdt['t'] == "1":
                        self.discount = "每满" + item_pfdt['m'] + "减" + item_pfdt['j']
                    elif item_pfdt['t'] == "2":
                        self.discount = "满" + item_pfdt['m'] + "减" + item_pfdt['j']
                    elif item_pfdt['t'] == "3":
                        self.discount = item_pfdt['m'] + "免" + item_pfdt['j']
                    elif item_pfdt['t'] == "4":
                        self.discount = item_pfdt['m'] + "元" + item_pfdt['j'] + "件"
                    elif item_pfdt['t'] == "5":
                        self.discount = item_pfdt['m'] + "件" + item_pfdt['j'] + "折"

                    print(f"名称:{warename:<50} id:{wareid:<20} 折扣:{self.discount:<20} 价格:{price:<20}")

                    self.saver.append({
                        "warename": warename, "wareid": wareid, "discount": self.discount, "price": price
                    })

                    with open('2.md', 'a', encoding='utf-8') as file:
                        file.write(f"|{warename:<50} | {wareid:<20} | {self.discount:<20} | {price:<20} |\n")

                    with open('2.txt', 'a', encoding='utf-8') as file1:
                        file1.write(f"名称:{warename:<50} id:{wareid:<20} 折扣:{self.discount:<20} 价格:{price:<20}")

        print("有折扣商品数量：{}/{}，商品总数:{}".format(len(self.id_list), len(self.total_id_list), ResultCount))

    def save_xlsx(self):
        for index, saver in enumerate(self.saver):
            ws.append([saver["warename"], saver["wareid"], saver["discount"], saver["price"]])
        wb.save("a1.xlsx")
        # print("已保存")

    def main(self):
        for index, coupon_batch in enumerate(coupon_batch_list):
            print(f"获取第{index + 1}张优惠券")
            page = 1
            while True:
                info = self.get_info(coupon_batch, page)
                # print(info.status_code)
                if info.status_code == 403:
                    continue
                # print(info.text)
                self.process_response(info)
                if len(self.page_id) < 50:
                    break
                page += 1
                time.sleep(3)


if __name__ == '__main__':
    coupon_batch_list = [
        # 1075495214
        #1104780306,
        1208165489
    ]

    get_id = GETID()
    get_id.main()
    
