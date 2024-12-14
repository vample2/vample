payload = {
    'pid': 101,
    'aid': '弹窗点击',
    'a_attrs': {
        '项目名称': '金蛇福旺旺了个旺',
        '页面名称': '游戏页',
        '活动名称': '结算本局弹窗',
        '按钮名称': '立即结算',
        '跳转渠道': '固定跳转',
        'adid': '2025festival-hotkidclub-click-2025_festival-1j8',
        '参与渠道': '微信MP',
    },
    'customer': {
        'hkc_id': 26401085,
    },
    'location': {
        'ip': '39.144.238.42',
    }
}
a_attrs_str = json.dumps(payload["a_attrs"], ensure_ascii=False).replace(" ", "")
customer_str = json.dumps(payload["customer"], ensure_ascii=False).replace(" ", "")
location_str = json.dumps(payload["location"], ensure_ascii=False).replace(" ", "")

# 构建 data 字符串，确保没有空格
data = f'a_attrs={a_attrs_str}&aid="{payload["aid"]}"&customer={customer_str}&location={location_str}&pid={payload["pid"]}|vuT4cjptCf'

# 输出结果
# print(f"生成的 data 字符串：\n{data}")

# data = 'a_attrs={"项目名称":"金蛇福旺旺了个旺","页面名称":"游戏页","进入时间":"2024-11-30T17:09:58+08:00","离开时间":"2024-11-30T17:09:58+08:00","adid":"2025festival-hotkidclub-click-2025_festival-1j8","参与渠道":"微信MP"}&aid="页面浏览"&customer={"hkc_id":26401085}&location={"ip":"39.144.238.42"}&pid=101|vuT4cjptCf'

md5_hash = hashlib.md5(data.encode()).hexdigest().upper()
print(md5_hash)
payload["sign"] = md5_hash
