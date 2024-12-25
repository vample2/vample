import base64
from ctypes import *
import time

DllSunny = CDLL("./Sunny64.dll")

# Go语言回调函数声明
Go_callback = CFUNCTYPE(c_int64, c_int64, c_int64, c_char_p, c_char_p, c_int64, c_int64)
Go_Tcpcallback = CFUNCTYPE(None, c_char_p, c_char_p, c_int64, c_int64, c_int64, c_int64)

DllSunny.GetRequestBody.restype = c_int64
DllSunny.GetResponseBody.restype = c_int64

DllSunny.GetRequestAllHeader.restype = c_char_p
# DllSunny.GetRequestData.restype = c_char_p  # 没用上
DllSunny.GetRequestHeader.restype = c_char_p
DllSunny.GetRequestCookie.restype = c_char_p
DllSunny.GetRequestALLCookie.restype = c_char_p

# DllSunny.GetResponseData.restype = c_char_p  # 没用上
DllSunny.GetResponseHeader.restype = c_char_p
DllSunny.GetResponseAllHeader.restype = c_char_p
DllSunny.GetRequestCookie.restype = c_char_p
DllSunny.GetWebsocketBody.restype = c_char_p

MsgType_Request = 1  # 收到请求
MsgType_Response = 2  # 请求返回
MsgType_Wss_Connection = 3  # WSS连接成功
MsgType_Wss_send = 4  # wss 发送数据
MsgType_Wss_received = 5  # wss 收到数据
MsgType_Wss_Disconnect = 6  # wss 断开连接
MsgType_Ws_Connection = 7  # ws连接成功
MsgType_Ws_send = 8  # ws  发送数据
MsgType_Ws_received = 9  # ws 收到数据
MsgType_Ws_Disconnect = 10  # ws 断开连接


# WSS 测试地址 https://www.idcd.com/tool/socket
# Ws  测试地址 http://coolaf.com/tool/chattest

class SunnyClass:
    def __init__(self, MessageId):
        self.MessageId = c_void_p(MessageId)

    def GetRequestBody(self):
        """
        获取请求的Body  bytes
        """
        Len = DllSunny.GetRequestBodyLen(self.MessageId)
        bodyPtr = DllSunny.GetRequestBody(self.MessageId)
        return string_at(bodyPtr, Len)

    def GetRequestData(self, coding):
        """
        获取请求的Body  字符串
        """
        return self.GetRequestBody().decode(coding)

    def SetRequestUrl(self, Url):
        """
        修改URL 或重定向URL
        """
        DllSunny.SetRequestUrl(self.MessageId, create_string_buffer(Url.encode("utf-8")))

    def SetRequestHeader(self, name, val):
        """
        设置一个请求的请求头
        """
        DllSunny.SetRequestHeader(self.MessageId,
                                  create_string_buffer(name.encode("utf-8")),
                                  create_string_buffer(val.encode("utf-8")))

    def SetResponseHeader(self, name, val):
        """
        设置请求返回的Head 可添加 可修改
        """
        DllSunny.SetResponseHeader(self.MessageId,
                                   create_string_buffer(name.encode("utf-8")),
                                   create_string_buffer(val.encode("utf-8")))

    def SetRequestCookie(self, name, val):
        """
        设置一个请求的一个Cookie
        """
        DllSunny.SetRequestCookie(self.MessageId,
                                  create_string_buffer(name.encode("utf-8")),
                                  create_string_buffer(val.encode("utf-8")))

    def GetRequestBodyLen(self):
        """
        获取请求的POST数据长度
        """
        return DllSunny.GetRequestBodyLen(self.MessageId)

    def GetWebsocketBodyLen(self):
        """
        获取请Websocket消息长度
        """
        return DllSunny.GetWebsocketBodyLen(self.MessageId)

    def GetWebsocketBody(self):
        """
        获取请Websocket消息Body
        """
        return DllSunny.GetWebsocketBody(self.MessageId, self.GetWebsocketBodyLen())

    def GetWebsocketBody_Str(self):
        """
        获取请Websocket消息Body
        """
        return self.GetWebsocketBody().decode("UTF-8")

    def SetWebsocketBody(self, val):
        """
        修改Websocket消息
        本命令 只接受Bytes 类型参数
        """
        if type(val) is bytes:
            DllSunny.SetWebsocketBody(self.MessageId, create_string_buffer(base64.b64encode(val)))

    def SetWebsocketStr(self, val, coding):
        """
        修改Websocket消息
        本命令 只接受 str  类型参数
        """
        if type(val) is str:
            DllSunny.SetWebsocketBody(self.MessageId, create_string_buffer(base64.b64encode(val.encode(coding))))

    def GetRequestCookie(self, name):
        """
        获取请求的Cookie
        """
        return DllSunny.GetRequestCookie(self.MessageId, create_string_buffer(name.encode("utf-8"))).decode(
            'utf-8')

    def GetRequestALLCookie(self):
        """
        获取请求的全部Cookie
        """
        return DllSunny.GetRequestALLCookie(self.MessageId).decode('utf-8')

    def GetRequestHeader(self, name):
        """
        获取请求头的一个Head
        """
        return DllSunny.GetRequestHeader(self.MessageId, create_string_buffer(name.encode("utf-8"))).decode(
            'utf-8')

    def GetRequestAllHeader(self):
        """
        获取全部请求头
        """
        return DllSunny.GetRequestAllHeader(self.MessageId).decode('utf-8')

    def DelRequestHeader(self, name):
        """
        删除请求的一个请求头
        """
        DllSunny.DelRequestHeader(self.MessageId, create_string_buffer(name.encode("utf-8")))

    def DelResponseHeader(self, name):
        """
        删除返回的一个请求头
        """
        DllSunny.DelResponseHeader(self.MessageId, create_string_buffer(name.encode("utf-8")))

    def SetRequestDataStr(self, val, coding):
        """
        设置请求POST提交的字符串Body
        本命令 只接受  str 类型参数
        """
        if type(val) is str:
            DllSunny.SetRequestData(self.MessageId, create_string_buffer(base64.b64encode(val.encode(coding))))

    def SetRequestAllCookie(self, val):
        """
        设置请求的全部Cookie
        """
        DllSunny.SetRequestAllCookie(self.MessageId, create_string_buffer(val.encode("utf-8")))

    def SetRequestDataBytes(self, val):
        """
        设置请求POST提交的字符串Body
        本命令 只接受Bytes 类型参数
        """
        if type(val) is bytes:
            DllSunny.SetRequestData(self.MessageId, create_string_buffer(base64.b64encode(val)))

    def GetResponseBody(self):
        """
        获取返回数据的Body  bytes
        """
        Len = DllSunny.GetResponseBodyLen(self.MessageId)
        bodyPtr = DllSunny.GetResponseBody(self.MessageId)
        return string_at(bodyPtr, Len)

    def GetResponseBodyLen(self):
        """
        获取返回数据长度
        """
        return DllSunny.GetResponseBodyLen(self.MessageId)

    def GetResponseData(self, coding):
        """
        获取返回的Body  字符串
        """
        s = self.GetResponseHeader("Content-Type")
        if s.find("image/") != -1:
            return ""
        return self.GetResponseBody().decode(coding)

    def GetResponseHeader(self, name):
        """
        获取返回的一个Head
        """
        return DllSunny.GetResponseHeader(self.MessageId, create_string_buffer(name.encode("utf-8"))).decode(
            'utf-8')

    def GetResponseAllHeader(self):
        """
        获取返回的全部请求头
        """
        return DllSunny.GetResponseAllHeader(self.MessageId).decode('utf-8')

    def GetResponseType(self):
        """
        获取返回文档类型
        """
        return self.GetResponseHeader("Content-Type")

    def SetResponseDataBytes(self, val):
        """
        设置请求返回的Body
        本命令 只接受Bytes   类型参数
        """
        if type(val) is bytes:
            DllSunny.SetResponseData(self.MessageId, create_string_buffer(base64.b64encode(val)))

    def SetResponseDataStr(self, val, coding):
        """
        设置请求POST提交的字符串Body
        本命令 只接受 str  类型参数
        """
        if type(val) is str:
            DllSunny.SetResponseData(self.MessageId, create_string_buffer(base64.b64encode(val.encode(coding))))


def Go_callback_Func(MessageId, Type, ptr_mod, ptr_Url, id, report):
    """
        函数参数说明
        MessageId           |       消息id
        Type                |       消息类型
        ptr_mod             |       mod 例如 GET / POST
        ptr_Url             |       URL链接
        id                  |       消息唯一id 请求前，请求后不会变 就是同一个请求的消息不会变
        report              |       是否预报告 如果启动之前调用了 NoticeTheRequest 命令
                                    并且 Type = MsgType_Response（ 2 ） 的情况下
                                    report 的值是 1 或者 2 为 1 时 表示是预报告 只能获取到返回数据的协议头。
                                    report 为1时候 再处理 MsgType_Response 请求时 如果 rteurn 1 表示不再接收这个请求的返回正文 详细见下方例子
                                    如果用来过滤屏蔽一些不需要的类型文件
    """
    Mod = ptr_mod.decode('utf-8')
    Url = ptr_Url.decode('utf-8')

    Sunny = SunnyClass(MessageId)
    if Type == MsgType_Request:
        print(Mod + " | " + Url)
        # 这里是请求前
        '''
        把协议头中这个删除，不然无法解析返回数据 
        因为 例如 Accept-Encoding: gzip, deflate, br 
        他可能是要求服务器返回数据时 使用  gzip, deflate, br 
        这3种任意1种压缩方式压缩数据,如果不删除这个协议头的话，我们得到的是压缩后的数据无法解析
        '''
        Sunny.DelRequestHeader("Accept-Encoding")

        # Sunny.SetRequestData("123456") # 设置字符串类型的Body
        # Sunny.SetRequestDataBytes(bytes([57, 56, 55, 54, 53, 52, 51, 50, 49])) #设置bytes 的Body
        Sunny.GetRequestBody()  # 获取请求的bytes数据
        # Sunny.GetRequestData("UTF-8")                 # 获取请求的字符串数据
        # Sunny.SetRequestUrl("http://baidu.com")        # 修改URL 或重定向URL
        Sunny.GetRequestAllHeader()  # 修改请求的全部请求头
        Sunny.GetRequestHeader("User-Agent")  # 修改请求的一个请求头
        Sunny.GetRequestALLCookie()  # 获取提交的全部Cookie
        Sunny.GetRequestCookie("BIDUPSID")  # 获取指定名称的Cookie
        Sunny.GetRequestBodyLen()  # 获取POST提交数据长度
        # Sunny.SetRequestHeader("Ser", "1.0.0")
        # Sunny.SetRequestCookie("VER", "1.2.3")
        # Sunny.SetRequestAllCookie("v=1;b=2")
        pass
    elif Type == MsgType_Response:
        # 这里是请求后
        # report == 1 表示是预报告请求
        if report == 1:
            """
            这里是预报告的请求
            """
            HtmlType = Sunny.GetResponseHeader("Content-Type")
            # 如果预报告的时候 发现 这个请求是一个图片 return 1 忽略它，Sunny 将不会收到这个请求的返回正文(Body)
            if HtmlType.find("image/") != -1:
                print("请求被过滤，目标类型是：" + HtmlType)
                return 1
            # 如果预报告的时候 发现 这个请求是一个视频 return 1 忽略它，Sunny 将不会收到这个请求的返回正文(Body)
            if HtmlType.find("video") != -1:
                print("请求被过滤，目标类型是：" + HtmlType)
                return 1
            # 否则 如果表示我们要获取这个请求的正文，
            return 0

        # 这里将获取的上方预报告 return 0 时 的返回数据 或没有 启动事情 没有调用 NoticeTheRequest 命令时的数据
        print("请求正文：" + Sunny.GetResponseData("GBK"))
        print(report)
        Sunny.GetResponseBody()  # 获取返回的Beyts 数据
        Sunny.GetResponseBodyLen()  # 获取返回数据的长度
        # Sunny.GetResponseData("GBK")  # 获取返回的Str UTF8编码的数据
        Sunny.GetResponseHeader("Server")  # 从返回数据中取一个Head
        Sunny.GetResponseAllHeader()  # 获取返回的全部Head
        Sunny.GetResponseType()  # 获取返回文档类型
        # Sunny.DelResponseHeader("Server")  # 从返回数据中删除一个Head
        # Sunny.SetResponseDataStr("123456789", "UTF-8")  # 设置返回数据 字符串
        # Sunny.SetResponseDataBytes(bytes([1, 2, 3, 0, 4, 5, 6]))  # 设置返回数据 bytes 类型
        # Sunny.SetResponseHeader("v", "1.0.0")
        pass
    elif Type == MsgType_Wss_Connection:
        print("wss 连接成功")
        pass
    elif Type == MsgType_Wss_send:
        print("wss 发送数据", Sunny.GetWebsocketBody_Str())
        Sunny.SetWebsocketStr("wss发送的数据被修改了", "UTF-8")
        pass
    elif Type == MsgType_Wss_received:
        print("wss 收到数据", Sunny.GetWebsocketBody_Str())
        Sunny.SetWebsocketStr("wss收到的数据被修改了", "UTF-8")
        pass
    elif Type == MsgType_Wss_Disconnect:
        print("wss 断开连接了")
        pass
    elif Type == MsgType_Ws_Connection:
        print("ws 连接成功")
        pass
    elif Type == MsgType_Ws_send:
        print("ws 发送数据", Sunny.GetWebsocketBody_Str())
        Sunny.SetWebsocketStr("ws发送的数据被修改了", "UTF-8")
        pass
    elif Type == MsgType_Ws_received:
        print("ws 收到数据", Sunny.GetWebsocketBody_Str())
        Sunny.SetWebsocketStr("ws收到的数据被修改了", "UTF-8")
        pass
    elif Type == MsgType_Ws_Disconnect:
        print("ws 断开连接了")
        pass

    return 0


def SetTcpMsg(id, msgtype, msg_bytes):
    """
    :param id: 会话唯一ID
    :param msgtype:  消息类型
    :param msg_bytes:  byte[] 类型的数据，要修改的值
    """
    DllSunny.SetTcpBody(id, msgtype, create_string_buffer(base64.b64encode(msg_bytes)))


def Go_Tcpcallback_Func(LocalAddr, RemoteAddr, MsgType, id, data_prt, datalen):
    """
    :param LocalAddr:            请求地址
    :param RemoteAddr:           目标地址
    :param MsgType:              消息类型 0=连接进入 1=发送数据 2=收到数据 3=断开连接
    :param id:                   会话唯一ID
    :param data_prt:             数据指针
    :param datalen:              数据的长度
    :return:
    """

    Local = LocalAddr.decode('utf-8')
    Remote = RemoteAddr.decode('utf-8')

    if MsgType == 0:
        print(Local, Remote, "连接了")
    elif MsgType == 1:
        data = string_at(data_prt, datalen)
        print(Local, Remote, "发送了数据", data)
        SetTcpMsg(id, MsgType, "发送数据我修改了:".encode("UTF8"))
    elif MsgType == 2:
        data = string_at(data_prt, datalen)
        print(Local, Remote, "收到了数据", data)
        SetTcpMsg(id, MsgType, "收到数据我修改了:".encode("UTF8"))
    elif MsgType == 3:
        print(Local, Remote, "断开了")

    pass


callback = Go_callback(Go_callback_Func)
tcpcallback = Go_Tcpcallback(Go_Tcpcallback_Func)


def main():
    SetCa()  # 使用自定义的证书 如果留空或不调用本命令将使用默认证书 再启动前设置

    """
     开启报告返回协议头
     开启后，返回请求 将返回2次，第一次只有协议头，第二次才有正文,再启动之前调用【在启动之前调用】 详见 回调函数的参数说明
    """
    DllSunny.NoticeTheRequest(True)

    IsRunTcp = True
    if IsRunTcp:
        """
        开启TCP抓包模式 
        TCP抓包模式 只能使用S5代理
        """
        DllSunny.OpenTcp(tcpcallback)
        # 取消HTTP抓包 如果不取消 HTTP抓包不能使用S5 代理
        callback = 0

    if DllSunny.PInit(2023, callback) == 0:
        print("启动失败：" + DllSunny.Geterr())  # 如果启动错误，打印出错误信息
        exit(0)
    print("正在运行")
    # 阻止程序退出
    time.sleep(2592000)
    DllSunny.Stop()  # 停止命令


def SetCa():
    """
    使用自定义的证书 如果留空或不调用本命令将使用默认证书 再启动前设置
    """
    RootCa = """-----BEGIN CERTIFICATE-----
MIIDizCCAnOgAwIBAgIUKZuAsiiXCMz613rrURfxAHNuU7YwDQYJKoZIhvcNAQEL
BQAwVDELMAkGA1UEBhMCQ04xCzAJBgNVBAgMAkJKMQswCQYDVQQHDAJCSjENMAsG
A1UECgwEbGl2ZTENMAsGA1UECwwEUk9PVDENMAsGA1UEAwwEUk9PVDAgFw0yMTEw
MjEwMzUwNTBaGA8yMTIxMDkyNzAzNTA1MFowVDELMAkGA1UEBhMCQ04xCzAJBgNV
BAgMAkJKMQswCQYDVQQHDAJCSjENMAsGA1UECgwEbGl2ZTENMAsGA1UECwwEUk9P
VDENMAsGA1UEAwwEUk9PVDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
AMI+CTQSiFlew0i5Ir0OczDnucnHbCoCEb5m3x3VyH+KFAPdc8DltkETlSlvKbcc
C3G4Tm8IQ0lN9GpFepqbd/+06vhiZg+NU10hoXFP7pk3LwnrBXFHSHAN90y/7REP
1wPRdDUglI6WJKvEailZXdNgch+HTNXDlbpAKytqRe2m/pdzqTDWpiPu1UFQ0AtQ
rRhk+rCQe467cW7ekY/t7pEXqEwxUqKjHWvCXUAFUy6rOYe6/VZJWQF7Wo4zyidy
SYCF2t7RSpMXiwt5oEnuMT+L6g9RG+5DOpHJmg5LsqCYaQ+UWB2sthIlUni7D5E4
DFlKi+1AzV3sn6qrzAE0wlMCAwEAAaNTMFEwHQYDVR0OBBYEFL6bnl/tCNaISSbE
IZEkxBZr0kZEMB8GA1UdIwQYMBaAFL6bnl/tCNaISSbEIZEkxBZr0kZEMA8GA1Ud
EwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAIIeZjAJ1opJQnNPbarbYFTG
I1yx3IbBjwr0/TX6Ku+BFU2McLSQFYdE8mtzcKGUryz15fBnirr+Xtjp7oy+1sZp
fiJToAw0fob/hjOWrLd5Oa8ZbwCCIbqauQy75SD4T/zBGAnyUSvTvhlITKPDrvMg
q/78o+3hitOCzytPgy9njee45DyhzW3/kczTXiBObyUrgI2YnFsbBBunYu5r5atb
jflL/BPXbo2I6AUSIZBYP+sjlDugttxtm7dao61fiMREkd5sgFhFi1b7HAETESKs
YuUTLN7fP7MUIOy+1cf+uX8STUTUz5tmu4eH6NiG4+HVdQHWQ0fI/3RoZmvghOg=
-----END CERTIFICATE-----
"""
    RootKey = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAwj4JNBKIWV7DSLkivQ5zMOe5ycdsKgIRvmbfHdXIf4oUA91z
wOW2QROVKW8ptxwLcbhObwhDSU30akV6mpt3/7Tq+GJmD41TXSGhcU/umTcvCesF
cUdIcA33TL/tEQ/XA9F0NSCUjpYkq8RqKVld02ByH4dM1cOVukArK2pF7ab+l3Op
MNamI+7VQVDQC1CtGGT6sJB7jrtxbt6Rj+3ukReoTDFSoqMda8JdQAVTLqs5h7r9
VklZAXtajjPKJ3JJgIXa3tFKkxeLC3mgSe4xP4vqD1Eb7kM6kcmaDkuyoJhpD5RY
Hay2EiVSeLsPkTgMWUqL7UDNXeyfqqvMATTCUwIDAQABAoIBADAr7GJimjf3vVyC
tW/Hbp/ZSAUXlOaSHs5merzOcOvYVYBj4jobfeiDr8FX1TOZG+l2+NSmavF6CLx2
QKKpHchnmMJCvObseJknJv+QAC81NVAzXeUq9Xb8r7D0BBnwILXMsxId41m9OJj0
nBNnG1K5n3PcPRziZXaMRWh98ZuvGE2efXHO+Z+bo1O3wyBb7aH7dwMEXLRwUxMO
lRrcczLdySejcuc+z0p9jJUhCnXAuuunOhjVrv/jVsuqUaFfiuIvp0A2dLXu/Bea
mWywSr+WqTZdszErghXuEjmBMK7rFz84/fvqxUMYM+rI2PWhjIOw0K0sSkIK0SwR
wrVdFWkCgYEA9311dONQfJiwxNGpSqJaI+XdNkuzyCFollxxbJVLBrnBd5+rt3bX
4wJwttQrIDY9mlGtitijf43C5yitO9Y9z4asON8hgjfalBp2/g98Aym0oLr+GHaJ
OQhVbpHawYkrKQQUXrT2UNrUI88LJM4Ezxs1+pvB01cMVc27DxqunF0CgYEAyOvc
m0cbWS5rBLY7oTFYebMqreDY/PCXbWBeDXCuTvEa/24HRmuK3IPsv5ircOgHSxBH
imZXBMITev0MPseiMYajqcgnSUWNzEtczrBMi00ezIC2OExifWExIaYAWeF7vQoY
JAxaVAy4IVZ2gkdr2Ib4ckoH1GyUKS5/8uybbm8CgYEA08IiHOhetq1DGrS2IGj3
rZ2BgHKXmlaTkYv5dMnszw1jb0JMgAcMw20UGitB1ybx4LegQJwKkRovuPACAZ/X
dViqxWKN3kiCGpTmWY3QMzidF6XHwhCyav0pdBkSTuRZ7JdUApDd7OK//v+pbk1k
qfyDXDGnT3g80rHcKxlOa/UCgYAy8mvMC+nJYVXNqg/Qvdx7b40A7iTXboJXP7pZ
mhr49XYtEs9Rce+SHvmnU6UVSiCfTg917qFeGYArDYNPX/ump0dUw+YCVFqyVOHB
nz6pi/KlVHXgLK5EsKJur9Mi92QS+T5J1cAJ0/fUrEH8ovObwg25nUADA01Ga/4R
sSFwjQKBgQDcGD7f7dMvt5azi7/OkAc18Z7NxWwyZ52i/JwtejOoO1ZhY1R0zT1U
hu3xdcZQ98EHSzY9i/cnj8hbpRc158NRTIJ9+16XFtw4mKXwnEetw4cnotF8rUAs
EkvK5BlNCpvFCO8TKImcB/g4v8R7FNxmM4tUE1HJzSym4jbiaWtf8w==
-----END RSA PRIVATE KEY-----
"""
    DllSunny.SetCa(
        create_string_buffer(RootCa.encode("utf-8")),
        create_string_buffer(RootKey.encode("utf-8"))
    )


main()
