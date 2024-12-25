import struct
import ctypes
from ctypes import *

# 判断你的python环境是64位还是32位
__RuntimeEnvironment = struct.calcsize("P") * 8 == 64

try:
    if __RuntimeEnvironment:
        # 如果是64位加载64位DLL
        lib = CDLL("./Sunny64.dll")
        # Go语言回调函数声明
        TcpCallback = CFUNCTYPE(None, c_int64, c_char_p, c_char_p, c_int64, c_int64, c_int64, c_int64, c_int64, c_int64)
        HttpCallback = CFUNCTYPE(None, c_int64, c_int64, c_int64, c_int64, c_char_p, c_char_p, c_char_p, c_int64)
        WsCallback = CFUNCTYPE(None, c_int64, c_int64, c_int64, c_int64, c_char_p, c_char_p, c_int64, c_int64)
        UDPCallback = CFUNCTYPE(None, c_int64, c_char_p, c_char_p, c_int64, c_int64, c_int64, c_int64)

    else:
        # 如果不是64位加载32位DLL
        lib = CDLL("./Sunny.dll")
        # Go语言回调函数声明
        TcpCallback = CFUNCTYPE(None, c_int, c_char_p, c_char_p, c_int, c_int, c_int, c_int, c_int, c_int)
        HttpCallback = CFUNCTYPE(None, c_int, c_int, c_int, c_int, c_char_p, c_char_p, c_char_p, c_int)
        WsCallback = CFUNCTYPE(None, c_int, c_int, c_int, c_int, c_char_p, c_char_p, c_int, c_int)
        UDPCallback = CFUNCTYPE(None, c_int, c_char_p, c_char_p, c_int, c_int, c_int, c_int)


except:
    print("载入DLL失败,请检测DLL文件")
    exit(1)


# 这个类 是动态加载DLL时 设置返回值为指针
class LibSunny:
    def __getattr__(self, name):
        func = getattr(lib, name)
        func.restype = ctypes.POINTER(ctypes.c_int)
        return func


DLLSunny = LibSunny()


# 指针到字节数组 ptr=指针 skip=偏移数 num=取出几个字节
def PtrToByte(ptr, skip, num):
    result_as_int = ctypes.cast(ptr, ctypes.c_void_p).value
    if result_as_int == None:
        return bytearray()
    result_as_int += skip
    new_result_ptr = ctypes.cast(result_as_int, ctypes.POINTER(ctypes.c_int))
    buffer = ctypes.create_string_buffer(num)
    ctypes.memmove(buffer, new_result_ptr, num)
    return buffer.raw


# 指针到整数
def PtrToInt(ptr):
    return ctypes.cast(ptr, ctypes.c_void_p).value


def OtherCommands(cmd, cmd1=0, cmd2=0, cmd3=0, cmd4=0, cmd5=0, cmd6=0, cmd7=0):
    """
    预留命令,后续版本如果有可能新增函数，可以直接使用这个命令新增命令,而不用每次更新DLL导出表
    """
    r = DLLSunny.OtherCommands(cmd, cmd1, cmd2, cmd3, cmd4, cmd5, cmd6, cmd7)
    return r


# 指针到字符串
def PointerToText(ptr):
    if ptr == 0:
        return ""
    buff = b''
    i = 0
    while True:
        bs = PtrToByte(ptr, i, 1)
        i += 1
        if len(bs) == 0:
            break
        if bs[0] == 0:
            break
        buff = buff + bs

    DLLSunny.Free(ptr)  # 释放Sunny的指针,只要是Sunny返回的bytes 或 string 都需要释放指针
    try:
        # return buff.decode('latin1')
        return buff.decode('utf-8')
    except:
        return buff.decode('gbk')


# 指针到字节数组 (DLL协商的前8个字节是长度)
def PointerToBytes(ptr):
    if ptr == 0:
        return bytearray()
    lp = PtrToByte(ptr, 0, 8)
    if len(lp) != 8:
        return lp
    Lxp = PtrToInt(DLLSunny.BytesToInt(create_string_buffer(lp), 8))
    m = PtrToByte(ptr, 8, Lxp)
    DLLSunny.Free(ptr)  # 释放Sunny的指针,只要是Sunny返回的bytes 或 string 都需要释放指针
    return m


# http 请求操作类
class SunnyRequest:
    def __init__(self, _MessageId):
        self.MessageId = _MessageId

    def 删除压缩标记(self):
        """ 请求协议头中去除Gzip 若不删除压缩标记，返回数据可能是压缩后的 """
        DLLSunny.DelRequestHeader(self.MessageId, create_string_buffer("Accept-Encoding".encode("utf-8")))

    def 置代理(self, 代理):
        """
         对这个请求使用指定代理请求请求
         仅支持Socket5和http 例如 socket5://admin:123456@127.0.0.1:8888 或 http://admin:123456@127.0.0.1:8888
        """
        if not isinstance(代理, str):
            return
        return bool(DLLSunny.SetRequestProxy(self.MessageId, create_string_buffer(代理.encode("utf-8"))))

    def 置请求超时(self, 超时时间):
        """
        仅限在发起请求时候使用,单位【毫秒】
        """
        if not isinstance(超时时间, int):
            return
        DLLSunny.SetRequestOutTime(self.MessageId, 超时时间)

    def 修改Url(self, 欲转向地址):
        """
        可以转向  1->2   网址A->网址B
        """
        if not isinstance(欲转向地址, str):
            return
        DLLSunny.SetRequestUrl(self.MessageId, create_string_buffer(欲转向地址.encode("utf-8")))

    def 修改Body_字节数组(self, 欲修改为的Body):
        """
        成功返回 True
        """
        if not isinstance(欲修改为的Body, bytes):
            return False
        return PtrToInt(
            DLLSunny.SetRequestData(self.MessageId, create_string_buffer(欲修改为的Body),
                                    len(欲修改为的Body))) == 1

    def 修改Body_字符串(self, 欲修改为的Body):
        """
        成功返回 True
        """
        if not isinstance(欲修改为的Body, str):
            return False
        try:
            return self.修改Body_字节数组(欲修改为的Body.encode("gbk"))
        except:
            return self.修改Body_字节数组(欲修改为的Body.encode("utf-8"))

    def 修改或新增协议头(self, 欲修改协议头):
        """
        若本身无指定的协议头，即为新增，若有则为修改
        可多条 一行一个 例如 Accept: image/gif
        """
        if not isinstance(欲修改协议头, str):
            return
        my_list = 欲修改协议头.split("\r\n")
        for item in my_list:
            my_list2 = item.split(":")
            if len(my_list2) >= 1:
                name = my_list2[0]
                value = item.replace(name + ":").strip()
                DLLSunny.SetRequestHeader(self.MessageId, create_string_buffer(name.encode("utf-8")),
                                          create_string_buffer(value.encode("utf-8")))

    def 终止发送(self):
        """
        使用本命令后,这个请求将不会被发送出去
        """
        DLLSunny.SetResponseHeader(self.MessageId, create_string_buffer("Connection".encode("utf-8")),
                                   create_string_buffer("Close".encode("utf-8")))

    def 修改或新增协议头_单条(self, key, value):
        """
        若本身无指定的协议头，即为新增，若有则为修改
        """
        if not isinstance(key, str):
            return
        if not isinstance(value, str):
            return
        DLLSunny.SetRequestHeader(self.MessageId, create_string_buffer(key.encode("utf-8")),
                                  create_string_buffer(value.encode("utf-8")))

    def 取全部协议头(self):
        return PointerToText(DLLSunny.GetRequestAllHeader(self.MessageId))

    def 取协议头_单条(self, key):
        if not isinstance(key, str):
            return ""
        return PointerToText(
            DLLSunny.GetRequestHeader(self.MessageId, create_string_buffer(key.encode("utf-8"))))

    def 删协议头_单条(self, key):
        if not isinstance(key, str):
            return
        DLLSunny.DelRequestHeader(self.MessageId, create_string_buffer(key.encode("utf-8")))

    def 删除全部协议头(self):
        h = self.取全部协议头()
        a = h.split("\r\n")
        for item in a:
            my_list2 = item.split(":")
            if len(my_list2) >= 1:
                name = my_list2[0]
                DLLSunny.DelRequestHeader(self.MessageId, create_string_buffer(name.encode("utf-8")))

    def 修改全部Cookie(self, value):
        """ 设置请求全部Cookies 例如 a=1;b=2;c=3 """
        if not isinstance(value, str):
            return
        DLLSunny.SetRequestAllCookie(self.MessageId, create_string_buffer(value.encode("utf-8")))

    def 修改Cookie_单条(self, key, value):
        """
        若本身无指定的协议头，即为新增，若有则为修改
        """
        if not isinstance(key, str):
            return
        if not isinstance(value, str):
            return
        DLLSunny.SetRequestCookie(self.MessageId, create_string_buffer(key.encode("utf-8")),
                                  create_string_buffer(value.encode("utf-8")))

    def 取全部cookie(self):
        return PointerToText(DLLSunny.GetRequestALLCookie(self.MessageId))

    def 取cookie_单条(self, key):
        if not isinstance(key, str):
            return ""
        ptr = DLLSunny.GetRequestCookie(self.MessageId, create_string_buffer(key.encode("utf-8")))
        m = PointerToText(ptr)
        return m

    def 取cookie_单条_不包含键(self, key):
        if not isinstance(key, str):
            return ""
        ptr = DLLSunny.GetRequestCookie(self.MessageId, create_string_buffer(key.encode("utf-8")))
        a = PointerToText(ptr)
        return a.replace(key + "=", "").replace(";", "").strip()

    def 取Body_长度(self):
        return PtrToInt(DLLSunny.GetRequestBodyLen(self.MessageId))

    def 取POST数据_字符串(self):
        try:
            return self.取POST数据_字节数组().decode("gbk")
        except:
            return self.取POST数据_字节数组().decode("utf-8")

    def 取POST数据_字节数组(self):
        ptr = DLLSunny.GetRequestBody(self.MessageId)
        m = PtrToByte(ptr, 0, self.取Body_长度())
        DLLSunny.Free(ptr)  # 释放Sunny的指针,只要是Sunny返回的bytes 或 string 都需要释放指针
        return m


# http 响应操作类
class SunnyResponse:
    def __init__(self, _MessageId):
        self.MessageId = _MessageId

    def 取响应文本(self):
        return PointerToText(DLLSunny.GetResponseBody(self.MessageId))

    def 取协议头(self, 协议头_键):
        if not isinstance(协议头_键, str):
            return ""
        m = create_string_buffer(协议头_键.encode("utf-8"))
        return PointerToText(DLLSunny.GetResponseHeader(self.MessageId, m))

    def 取全部协议头(self):
        return PointerToText(DLLSunny.GetResponseAllHeader(self.MessageId))

    def 删除全部协议头(self):
        h = self.取全部协议头()
        a = h.split("\r\n")
        for inm in a:
            ar = inm.split(":")
            if len(ar) >= 1:
                self.删除协议头_单条(ar[0])

    def 删除协议头_单条(self, 协议头_键):
        if not isinstance(协议头_键, str):
            return
        DLLSunny.DelResponseHeader(self.MessageId, create_string_buffer(协议头_键.encode("utf-8")))

    def 修改或新增协议头_单条(self, key, value):
        if not isinstance(key, str):
            return
        if not isinstance(value, str):
            return
        DLLSunny.SetResponseHeader(self.MessageId, create_string_buffer(key.encode("utf-8")),
                                   create_string_buffer(value.encode("utf-8")))

    def 修改或新增协议头(self, 修改或新增协议头):
        if not isinstance(修改或新增协议头, str):
            return
        DLLSunny.SetResponseAllHeader(self.MessageId, create_string_buffer(修改或新增协议头.encode("utf-8")))

    def 修改状态码(self, Status):
        if not isinstance(Status, int):
            return
        if Status <= 0:
            DLLSunny.SetResponseStatus(self.MessageId, 200)
            return
        DLLSunny.SetResponseStatus(self.MessageId, Status)

    def 取状态码(self):
        return PtrToInt(DLLSunny.GetResponseStatusCode(self.MessageId))

    def 取状态码对应状态文本(self):
        res = PointerToText(DLLSunny.GetResponseStatus(self.MessageId))
        a = res.split(" ")
        print(res)
        if len(a) > 1:
            del a[0]
            return " ".join(a).strip()
        return ""

    def 取正文长度(self):
        ptr = DLLSunny.GetResponseBodyLen(self.MessageId)
        m = PtrToInt(ptr)
        return m

    def 取响应Body(self):
        ptr = DLLSunny.GetResponseBody(self.MessageId)
        m = PtrToByte(ptr, 0, self.取正文长度())
        DLLSunny.Free(ptr)  # 释放Sunny的指针,只要是Sunny返回的bytes 或 string 都需要释放指针
        return m

    def 修改响应内容_字节数组(self, 预修改为的内容):
        if not isinstance(预修改为的内容, bytes):
            return
        DLLSunny.SetResponseData(self.MessageId, 预修改为的内容, len(预修改为的内容))

    def 修改响应内容_字符串(self, 预修改为的内容):
        if not isinstance(预修改为的内容, str):
            return
        try:
            self.修改响应内容_字节数组(预修改为的内容.encode("utf-8"))
        except:
            self.修改响应内容_字节数组(预修改为的内容.encode("gbk"))


# http 操作类
class Sunny:
    请求 = None
    """ HTTP/HTTPS 请求操作对象 """
    响应 = None
    """ HTTP/HTTPS 响应操作对象 """
    请求来源IP = ""
    """ HTTP/HTTPS 发起请求的客户端IP """

    def __init__(self, MessageId):
        self.请求 = SunnyRequest(MessageId)
        self.响应 = SunnyResponse(MessageId)
        self.请求来源IP = PointerToText(DLLSunny.GetRequestClientIp(MessageId))
