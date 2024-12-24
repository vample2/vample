import requests
import execjs
with open('getse.js', 'r', encoding='utf-8') as file:
    js_code = file.read()

# Create a context for executing JavaScript
context = execjs.compile(js_code)

session_id = "QC8VPgACAAAAADlmTXMAMGBqpVusT3Mlrp3xbTZyMf_CDKFXagU18K_T6OlOYaySbs8T9rASumtKaAooNVMrcAAAAAA"
token = "F61EAk47nIAXBCTG"
secret_key = "23130303037303236454145424647333930364347354831453137323142373636383333363233303033333234454636454541433246344546333730344346493333373831483530334233303035313030303"

cookies = {
    'webp': '1',
    'mba_muid': '17347068363441128009992',
    'visitkey': '5514370210242925836',
    'sc_width': '2048',
    'shshshfpa': '3e921303-5be3-5642-2ea4-ba8004a2a74f-1734706781',
    'shshshfpx': '3e921303-5be3-5642-2ea4-ba8004a2a74f-1734706781',
    '3AB9D23F7A4B3C9B': '54O76KCJDXDYZY6AZTCSVRRZEAYCKS67FFIUMCZX4MXSK5CEZWJESHRJ6P3YHPSACIWQJOL6XBCZYTUKWCNYZJZUOE',
    '__jdv': '122270672%7Clianmeng__10__www.99yes.com%7Ct_28140094_%7Cjingfen%7Cfcb895ab3f9941dda9bc011d93cfef15%7C1734764827042',
    'b_dw': '2040',
    'b_dh': '1039',
    'b_dpr': '1.25',
    'b_webp': '1',
    'b_avif': '1',
    'autoOpenApp_downCloseDate_auto': '1734764828383_1800000',
    'joyya': '1734764826.1734764829.36.00q00wrw2',
    'cid': '9',
    'equipmentId': '54O76KCJDXDYZY6AZTCSVRRZEAYCKS67FFIUMCZX4MXSK5CEZWJESHRJ6P3YHPSACIWQJOL6XBCZYTUKWCNYZJZUOE',
    'fingerprint': 'VO5Jc1I8NmNwEc0CtK4lk7r8Kt13mRjW',
    'deviceVersion': '131.0.0.0',
    'deviceOS': '',
    'deviceOSVersion': '',
    'deviceName': 'Chrome',
    'jcap_dvzw_fp': 'WoZ79dPNsqhPCBnf1J8jt4jKfY7euJd8L4LqaIA8WCsbJS1DUJB6fClEuQIMdoygDAXydZhzhKPS3zxBY60r1g==',
    'whwswswws': '',
    'cartNum': '0',
    'kplTitleShow': '1',
    'e_wq_addr': 'DNU1CJuyENC4DIU3GzPpDzTpCtqnEV8mTJdNTXU1CzO3TXU0HUPNXyV1DtcnHMV1EJYzCyV1DJCzGV8vdJHPCNuvdJczGUYvdJUyCzKvdJU2HOSvdJczGUYvdJHPDOSvdJu1HtHpTJdNTXU1CzO3TXU0HUPNTXU2DzPOTXU5DtCzTXU1CzDLTXU0HJK5TXU3C0PQTXU1CtCmTXU1DuHMTXU3C0PQTXU0HJHMTXU5DUY0TJdNCJO2BtG0DMUyGzC5BtuyCJu=',
    'wq_addr': '4551928385%7C1_72_2819_0%7C%u5317%u4EAC_%u671D%u9633%u533A_%u4E09%u73AF%u5230%u56DB%u73AF%u4E4B%u95F4_%7C%u5317%u4EAC%u671D%u9633%u533A%u4E09%u73AF%u5230%u56DB%u73AF%u4E4B%u95F4%7C116.444%2C39.9219',
    'jdAddrId': '1_72_2819_0',
    'jdAddrName': '%u5317%u4EAC_%u671D%u9633%u533A_%u4E09%u73AF%u5230%u56DB%u73AF%u4E4B%u95F4_',
    'commonAddress': '4551928385',
    'regionAddress': '1%2C72%2C2819%2C0',
    'mitemAddrId': '1_72_2819_0',
    'mitemAddrName': '%u5317%u4EAC%u671D%u9633%u533A%u4E09%u73AF%u5230%u56DB%u73AF%u4E4B%u95F4',
    'autoOpenApp_downCloseDate_jd_homePage': '1734764878324_1',
    'autoOpenApp_downCloseDate_autoOpenApp_handler': '1734765012355_1',
    'TrackerID': 'gydR9IkDbWEnFHgEP1AcVlCOoPnFAZip5juhySjmgQswQxESJ853O5gd-ww0kqxU-PVKRpLtxzXDek5MNhRJA6Sipvq4slXTU1DHPy_CA8TK70FnYMbW__mHln4-BEc7',
    'pt_key': 'AAJnZn8mADAKwH8Va5sbsnKh-w_NVQjcc_-KZhSuXhflXdUo8iZO62cgbUIdR0FSL2NmGDqzL1g',
    'pt_pin': 'jd_uTaLohrdhwQz',
    'pt_token': 'l9iegihs',
    'pwdt_id': 'jd_uTaLohrdhwQz',
    'sfstoken': 'tk01mae801b5fa8sMSsyeDJ4MXgzNifZ3fPz9z+YWGzMzKPcb1BISlOb4cXnhK/N39z9Q3VxPPB43B5O7aIAuq4LQp9a',
    'x-rp-evtoken': 'mGW9U4qbzsaBdCMe70m9pLKDgP2w4wOh7Z58kzvy4v9WP3NlyumEXz8eJTnBztR-jEsPRMjHGr2xdqRoCTLQvQ%3D%3D',
    'retina': '0',
    '3AB9D23F7A4B3CSS': 'jdd0354O76KCJDXDYZY6AZTCSVRRZEAYCKS67FFIUMCZX4MXSK5CEZWJESHRJ6P3YHPSACIWQJOL6XBCZYTUKWCNYZJZUOEAAAAMT5BQOFUAAAAAACLWODBUF4YNM3EX',
    'warehistory': '"100148274436,100148274436,100148274436,100148274436,100148274436,100148274436,100148274436,100148274436,100148274436,7504707,1067048,"',
    '__wga': '1734770492021.1734770484515.1734768123075.1734763615221.2.3',
    'PPRD_P': 'UUID.17347068363441128009992-LOGID.1734770492023.145276126',
    'autoOpenApp_downCloseDate_autoOpenApp_autoPromptly': '1734770492127_1',
    '__jdc': '122270672',
    '__jda': '122270672.17347068363441128009992.1734706836.1735004913.1735015496.12',
    '__jdb': '122270672.1.17347068363441128009992|12.1735015496',
    'mba_sid': '17350154962011174395014804279.1',
    'shshshfpb': 'BApXSt-nz9fZAZL0TqaS49pxt0_e_ZBaVBnYxYK5q9xJ1PdZfQpPikzbkhDn-O5FCaYq-s6Zi8qJVR4A',
    '__jd_ref_cls': 'LoginDisposition_Go',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'webp=1; mba_muid=17347068363441128009992; visitkey=5514370210242925836; sc_width=2048; shshshfpa=3e921303-5be3-5642-2ea4-ba8004a2a74f-1734706781; shshshfpx=3e921303-5be3-5642-2ea4-ba8004a2a74f-1734706781; 3AB9D23F7A4B3C9B=54O76KCJDXDYZY6AZTCSVRRZEAYCKS67FFIUMCZX4MXSK5CEZWJESHRJ6P3YHPSACIWQJOL6XBCZYTUKWCNYZJZUOE; __jdv=122270672%7Clianmeng__10__www.99yes.com%7Ct_28140094_%7Cjingfen%7Cfcb895ab3f9941dda9bc011d93cfef15%7C1734764827042; b_dw=2040; b_dh=1039; b_dpr=1.25; b_webp=1; b_avif=1; autoOpenApp_downCloseDate_auto=1734764828383_1800000; joyya=1734764826.1734764829.36.00q00wrw2; cid=9; equipmentId=54O76KCJDXDYZY6AZTCSVRRZEAYCKS67FFIUMCZX4MXSK5CEZWJESHRJ6P3YHPSACIWQJOL6XBCZYTUKWCNYZJZUOE; fingerprint=VO5Jc1I8NmNwEc0CtK4lk7r8Kt13mRjW; deviceVersion=131.0.0.0; deviceOS=; deviceOSVersion=; deviceName=Chrome; jcap_dvzw_fp=WoZ79dPNsqhPCBnf1J8jt4jKfY7euJd8L4LqaIA8WCsbJS1DUJB6fClEuQIMdoygDAXydZhzhKPS3zxBY60r1g==; whwswswws=; cartNum=0; kplTitleShow=1; e_wq_addr=DNU1CJuyENC4DIU3GzPpDzTpCtqnEV8mTJdNTXU1CzO3TXU0HUPNXyV1DtcnHMV1EJYzCyV1DJCzGV8vdJHPCNuvdJczGUYvdJUyCzKvdJU2HOSvdJczGUYvdJHPDOSvdJu1HtHpTJdNTXU1CzO3TXU0HUPNTXU2DzPOTXU5DtCzTXU1CzDLTXU0HJK5TXU3C0PQTXU1CtCmTXU1DuHMTXU3C0PQTXU0HJHMTXU5DUY0TJdNCJO2BtG0DMUyGzC5BtuyCJu=; wq_addr=4551928385%7C1_72_2819_0%7C%u5317%u4EAC_%u671D%u9633%u533A_%u4E09%u73AF%u5230%u56DB%u73AF%u4E4B%u95F4_%7C%u5317%u4EAC%u671D%u9633%u533A%u4E09%u73AF%u5230%u56DB%u73AF%u4E4B%u95F4%7C116.444%2C39.9219; jdAddrId=1_72_2819_0; jdAddrName=%u5317%u4EAC_%u671D%u9633%u533A_%u4E09%u73AF%u5230%u56DB%u73AF%u4E4B%u95F4_; commonAddress=4551928385; regionAddress=1%2C72%2C2819%2C0; mitemAddrId=1_72_2819_0; mitemAddrName=%u5317%u4EAC%u671D%u9633%u533A%u4E09%u73AF%u5230%u56DB%u73AF%u4E4B%u95F4; autoOpenApp_downCloseDate_jd_homePage=1734764878324_1; autoOpenApp_downCloseDate_autoOpenApp_handler=1734765012355_1; TrackerID=gydR9IkDbWEnFHgEP1AcVlCOoPnFAZip5juhySjmgQswQxESJ853O5gd-ww0kqxU-PVKRpLtxzXDek5MNhRJA6Sipvq4slXTU1DHPy_CA8TK70FnYMbW__mHln4-BEc7; pt_key=AAJnZn8mADAKwH8Va5sbsnKh-w_NVQjcc_-KZhSuXhflXdUo8iZO62cgbUIdR0FSL2NmGDqzL1g; pt_pin=jd_uTaLohrdhwQz; pt_token=l9iegihs; pwdt_id=jd_uTaLohrdhwQz; sfstoken=tk01mae801b5fa8sMSsyeDJ4MXgzNifZ3fPz9z+YWGzMzKPcb1BISlOb4cXnhK/N39z9Q3VxPPB43B5O7aIAuq4LQp9a; x-rp-evtoken=mGW9U4qbzsaBdCMe70m9pLKDgP2w4wOh7Z58kzvy4v9WP3NlyumEXz8eJTnBztR-jEsPRMjHGr2xdqRoCTLQvQ%3D%3D; retina=0; 3AB9D23F7A4B3CSS=jdd0354O76KCJDXDYZY6AZTCSVRRZEAYCKS67FFIUMCZX4MXSK5CEZWJESHRJ6P3YHPSACIWQJOL6XBCZYTUKWCNYZJZUOEAAAAMT5BQOFUAAAAAACLWODBUF4YNM3EX; warehistory="100148274436,100148274436,100148274436,100148274436,100148274436,100148274436,100148274436,100148274436,100148274436,7504707,1067048,"; __wga=1734770492021.1734770484515.1734768123075.1734763615221.2.3; PPRD_P=UUID.17347068363441128009992-LOGID.1734770492023.145276126; autoOpenApp_downCloseDate_autoOpenApp_autoPromptly=1734770492127_1; __jdc=122270672; __jda=122270672.17347068363441128009992.1734706836.1735004913.1735015496.12; __jdb=122270672.1.17347068363441128009992|12.1735015496; mba_sid=17350154962011174395014804279.1; shshshfpb=BApXSt-nz9fZAZL0TqaS49pxt0_e_ZBaVBnYxYK5q9xJ1PdZfQpPikzbkhDn-O5FCaYq-s6Zi8qJVR4A; __jd_ref_cls=LoginDisposition_Go',
    'origin': 'https://cfe.m.jd.com',
    'priority': 'u=1, i',
    'referer': 'https://cfe.m.jd.com/',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0',
}



# Execute JavaScript function and get the result
while True:
    data = context.call("generateRequestData", session_id, token, secret_key)
    response = requests.post('https://jcap.m.jd.com/cgi-bin/api/refresh', cookies=cookies, headers=headers, data=data)
    print(response)
    print(response.text)
    res_json=response.json()
    token=res_json.get("st")
