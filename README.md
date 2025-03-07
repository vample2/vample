学习逆向记录（互相学习）
仅用于学习！！！
- jd补环境(更新的话尝试替换)
   - 狗洞获取验证图片(se参数，其中Module['getEncryptData']，直接拿源文件可以运行)
   - jdfingerprint纯算
- 麋鹿
- 塔司厅
- 毅力
- 农夫三拳
- 旺牢记游戏（没有易盾通杀，只能999分）
- 汪汪每日游戏（验证时间戳，需要通过wasm获取，直接扣代码）
- 上海少妇
- 库底
- 塔斯汀福卡
- 古井（简单写下，助力逻辑没写10个号内没问题）
- 雪王（幸运卡）系列
- 上海少妇口令(多线程) key可以使用cheat engine 搜索\"encrypt_key\":获得;提前包需要修改时间和"receiveStatus":0
```
 response_text = response_text.replace('"receiveStatus":1', '"receiveStatus":0')
 response_text = response_text.replace('11:00:00','08:00:00')


 on xweb callback. operateWXData {"data":{"data":"{\"encrypt_key\":\"\",\"version\":,\"expire_in\":3600,\"iv\":\"\",\"create_time\":1740532888}","err_no":0},"errMsg":"operateWXData:ok","errno":0,"errorCode":0}
```
- 古茗refer参数（
encoded_params = urllib.parse.urlencode(params)


