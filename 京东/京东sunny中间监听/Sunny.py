import ctypes
import time
from ctypes import *
import SunnyDLL


def Base64ToHexDump(B):
    """ 传入字节数组 或 字符串 """
    v = B
    if isinstance(B, bytes):
        pass
    else:
        if isinstance(B, str):
            v = B.encode('utf-8')
        else:
            print("您传入的参数不是 字节数组 或 字符串")
            exit(1)
    return SunnyDLL.PointerToText(SunnyDLL.DLLSunny.HexDump(v, len(v)))


def GetSunnyVersion():
    """ 获取SunnyNet DLL版本 """
    return SunnyDLL.PointerToText(SunnyDLL.DLLSunny.GetSunnyVersion())


def Tcp_修改消息(MessageId, 消息类型, 欲修改的Body):
    """
    消息类型   【1=发送  2=接受  1=发送的消息  2=接收的消息 根据回调函数中的参数填写】
    """
    if not isinstance(MessageId, int):
        return
    if not isinstance(消息类型, int):
        return
    if not isinstance(欲修改的Body, bytes):
        return
    SunnyDLL.DLLSunny.SetTcpBody(MessageId, 消息类型, create_string_buffer(欲修改的Body), len(欲修改的Body))


def Tcp_设置代理(MessageId, 代理):
    """
    给TCP请求设置S5代理。仅在TCP 即将连接时有效
    代理   【仅支持S5代理 例如 socket5://admin:123456@127.0.0.1:8888】
    """
    if not isinstance(MessageId, int):
        return
    if not isinstance(代理, str):
        return
    SunnyDLL.DLLSunny.SetTcpAgent(MessageId, create_string_buffer(代理))


def Tcp_连接重定向(MessageId, 新地址):
    """
    仅在TCP 即将连接时有效
    新地址   【例如“127.0.0.1:80”带上端口号】
    """
    if not isinstance(MessageId, int):
        return
    if not isinstance(新地址, str):
        return
    SunnyDLL.DLLSunny.SetTcpConnectionIP(MessageId, create_string_buffer(新地址))


def Tcp_主动发送消息(唯一id, 发送方向, msg):
    """
    指定的TCP连接 向[服务器\客户端]主动发送数据
    发送方向      [0=向 服务器 主动发送数据 其他值 向 户端 主动发送数据 ]
    msg         [字节数组]
    返回发送成功的字节数
    """
    if not isinstance(唯一id, int):
        return 0
    if not isinstance(发送方向, int):
        return 0
    if not isinstance(msg, bytes):
        return 0
    if 发送方向 == 0:
        return SunnyDLL.PtrToInt(SunnyDLL.DLLSunny.TcpSendMsg(唯一id, create_string_buffer(msg), len(msg)))
    return SunnyDLL.PtrToInt(SunnyDLL.DLLSunny.TcpSendMsgClient(唯一id, create_string_buffer(msg), len(msg)))


def Tcp_断开指定连接(唯一ID):
    """
    断开指定连接
    """
    if not isinstance(唯一ID, int):
        return False
    Ptr = SunnyDLL.DLLSunny.TcpCloseClient(唯一ID)
    return bool(Ptr)


def Tcp_取数据(数据指针, 数据长度):
    """
    数据指针    [回调中的 参数]
    数据长度    [回调中的 参数]
    """
    if not isinstance(数据指针, int):
        return bytearray()
    if not isinstance(数据长度, int):
        return bytearray()
    return SunnyDLL.PtrToByte(数据指针, 0, 数据长度)


def UDP_取Body(MessageId):
    """ UDP 取 接收/发送 的消息 返回字节数组 """
    if not isinstance(MessageId, int):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.GetUdpData(MessageId)
    return SunnyDLL.PointerToBytes(Ptr)


def UDP_修改Body(MessageId, 欲修改的Body):
    """ UDP 修改 接收/发送 的消息 """
    if not isinstance(MessageId, int):
        return False
    if not isinstance(欲修改的Body, bytes):
        return False
    Ptr = SunnyDLL.DLLSunny.SetUdpData(MessageId, create_string_buffer(欲修改的Body), len(欲修改的Body))
    return bool(Ptr)


def UDP_向服务器发送消息(唯一id, 欲修改的Body):
    """ 指定的UDP连接 模拟客户端向服务器端主动发送数据 """
    if not isinstance(唯一id, int):
        return False
    if not isinstance(欲修改的Body, bytes):
        return False
    Ptr = SunnyDLL.DLLSunny.UdpSendToServer(唯一id, create_string_buffer(欲修改的Body), len(欲修改的Body))
    return bool(Ptr)


def UDP_向客户端发送消息(唯一id, 欲修改的Body):
    """ 指定的UDP连接 模拟客户端向服务器端主动发送数据 """
    if not isinstance(唯一id, int):
        return False
    if not isinstance(欲修改的Body, bytes):
        return False
    Ptr = SunnyDLL.DLLSunny.UdpSendToClient(唯一id, create_string_buffer(欲修改的Body), len(欲修改的Body))
    return bool(Ptr)


def ws_取Body长度(MessageId):
    """ ws、wss 取 接收/发送 的消息长度 """
    if not isinstance(MessageId, int):
        return 0
    return SunnyDLL.PtrToInt(SunnyDLL.DLLSunny.GetWebsocketBodyLen(MessageId))


def ws_取Body(MessageId):
    """ ws、wss 取 接收/发送 的消息 返回字节数组 """
    if not isinstance(MessageId, int):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.GetWebsocketBody(MessageId)
    M = SunnyDLL.PtrToByte(Ptr, 0, ws_取Body长度(MessageId))
    SunnyDLL.DLLSunny.Free(Ptr)  # 释放Sunny的指针,只要是Sunny返回的bytes 或 string 都需要释放指针
    return M


def ws_修改Body(MessageId, 欲修改的Body):
    """ ws、wss 修改 接收/发送 的消息 """
    if not isinstance(MessageId, int):
        return False
    if not isinstance(欲修改的Body, bytes):
        return False
    Ptr = SunnyDLL.DLLSunny.SetWebsocketBody(MessageId, create_string_buffer(欲修改的Body), len(欲修改的Body))
    return bool(Ptr)


def ws_发送Body(唯一ID, 发送方向, 消息类型, 欲发送的Body):
    """
    ws、wss主动发送消息
    发送方向    [   0=向服务器发送 其他值向客户端发送 ]
    消息类型    [   ws/wss 发送或接收的消息类型 请使用[ Sunny_WsMessage_ ] ]
    """
    if not isinstance(唯一ID, int):
        return False
    if not isinstance(发送方向, int):
        return False
    if not isinstance(消息类型, int):
        return False
    if not isinstance(欲发送的Body, bytes):
        return False
    if 发送方向 == 0:
        return bool(
            SunnyDLL.DLLSunny.SendWebsocketBody(唯一ID, 消息类型, create_string_buffer(欲发送的Body),
                                                len(欲发送的Body)))
    return bool(
        SunnyDLL.DLLSunny.SendWebsocketClientBody(唯一ID, 消息类型, create_string_buffer(欲发送的Body),
                                                  len(欲发送的Body)))


def ws_断开指定连接(唯一ID):
    """
    断开指定连接
    """
    if not isinstance(唯一ID, int):
        return False
    Ptr = SunnyDLL.DLLSunny.CloseWebsocket(唯一ID)
    return bool(Ptr)


def 添加证书使用规则(Host, 证书, 使用规则):
    """
    添加证书，双向认证时使用
    Host            [如果之前设置过相同Host将会覆盖]
    使用规则          [1=发送请求时使用 2=发送及解析时使用 3=解析时使用]
    """
    if not isinstance(Host, str):
        return
    if not isinstance(证书, Sunny证书管理器):
        return
    if not isinstance(使用规则, int):
        return
    SunnyDLL.DLLSunny.AddHttpCertificate(create_string_buffer(bytes(Host, 'utf-8')), 证书.获取证书Context(), 使用规则)


def 删除证书使用规则(Host):
    if not isinstance(Host, str):
        return False
    Ptr = SunnyDLL.DLLSunny.DelHttpCertificate(create_string_buffer(Host))
    return bool(Ptr)


def Br压缩(bin):
    """ brotli Br压缩 """
    if not isinstance(bin, bytes):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.BrCompress(create_string_buffer(bin), len(bin))
    return SunnyDLL.PointerToBytes(Ptr)


def Br解压缩(bin):
    """ brotli 解压缩 """
    if not isinstance(bin, bytes):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.BrUnCompress(create_string_buffer(bin), len(bin))
    return SunnyDLL.PointerToBytes(Ptr)


def Deflate压缩(bin):
    """ (可能等同于zlib压缩) """
    if not isinstance(bin, bytes):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.DeflateCompress(create_string_buffer(bin), len(bin))
    return SunnyDLL.PointerToBytes(Ptr)


def Deflate解压缩(bin):
    """ (可能等同于zlib解压缩) """
    if not isinstance(bin, bytes):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.DeflateUnCompress(create_string_buffer(bin), len(bin))
    return SunnyDLL.PointerToBytes(Ptr)


def ZSTD压缩(bin):
    """ (可能等同于zlib压缩) """
    if not isinstance(bin, bytes):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.ZSTDCompress(create_string_buffer(bin), len(bin))
    return SunnyDLL.PointerToBytes(Ptr)


def ZSTD解压缩(bin):
    """ (可能等同于zlib解压缩) """
    if not isinstance(bin, bytes):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.ZSTDDecompress(create_string_buffer(bin), len(bin))
    return SunnyDLL.PointerToBytes(Ptr)


def Gzip压缩(bin):
    if not isinstance(bin, bytes):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.GzipCompress(create_string_buffer(bin), len(bin))
    return SunnyDLL.PointerToBytes(Ptr)


def Gzip解压缩(bin):
    if not isinstance(bin, bytes):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.GzipUnCompress(create_string_buffer(bin), len(bin))
    return SunnyDLL.PointerToBytes(Ptr)


def Zlib压缩(bin):
    if not isinstance(bin, bytes):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.ZlibCompress(create_string_buffer(bin), len(bin))
    return SunnyDLL.PointerToBytes(Ptr)


def Zlib解压缩(bin):
    if not isinstance(bin, bytes):
        return bytearray()
    Ptr = SunnyDLL.DLLSunny.ZlibUnCompress(create_string_buffer(bin), len(bin))
    return SunnyDLL.PointerToBytes(Ptr)


def PB转PbJSON(PB字节数组数据):
    if not isinstance(PB字节数组数据, bytes):
        return ""
    return SunnyDLL.DLLSunny.PbToJson(create_string_buffer(PB字节数组数据), len(PB字节数组数据))


def PbJson转Pb(PBjson字符串):
    if not isinstance(PBjson字符串, str):
        return bytearray()
    try:
        d = PBjson字符串.encode("gbk")
    except:
        d = PBjson字符串.encode("utf-8")
    return SunnyDLL.PointerToBytes(SunnyDLL.DLLSunny.JsonToPB(create_string_buffer(d), len(d)))


class Queue:
    """ Sunny 队列 """

    def __init__(self, 唯一标识=""):
        self._id = ""
        if isinstance(唯一标识, str):
            self.创建队列(唯一标识)

    def 是否为空(self):
        if self._id == "":
            return True
        return bool(SunnyDLL.DLLSunny.QueueIsEmpty(create_string_buffer(self._id.encode("utf-8"))))

    def 销毁(self):
        if self._id == "":
            return
        SunnyDLL.DLLSunny.QueueRelease(create_string_buffer(self._id.encode("utf-8")))

    def 创建队列(self, 唯一标识):
        if not isinstance(唯一标识, str):
            return
        self._id = 唯一标识
        SunnyDLL.DLLSunny.CreateQueue(create_string_buffer(self._id.encode("utf-8")))

    def 置唯一标识(self, 唯一标识):
        if not isinstance(唯一标识, str):
            return
        self._id = 唯一标识

    def 清空(self):
        if self._id == "":
            return
        self.销毁()
        self.创建队列(self._id)

    def 取队列长度(self):
        if self._id == "":
            return
        return SunnyDLL.PtrToInt(SunnyDLL.DLLSunny.QueueLength(create_string_buffer(self._id.encode("utf-8"))))

    def 压入(self, Data):
        """ Data 可以是字节数组 也可以字符串 """
        if self._id == "":
            return
        if isinstance(Data, bytes):
            SunnyDLL.DLLSunny.QueuePush(create_string_buffer(self._id.encode("utf-8")), create_string_buffer(Data),
                                        len(Data))
            return
        if isinstance(Data, str):
            d = Data.encode("utf-8")
            SunnyDLL.DLLSunny.QueuePush(create_string_buffer(self._id.encode("utf-8")), create_string_buffer(d), len(d))
            return

    def 弹出_字节数组(self):
        if self._id == "":
            return bytearray()
        p = SunnyDLL.DLLSunny.QueuePull(create_string_buffer(self._id.encode("utf-8")))
        return SunnyDLL.PointerToBytes(p)

    def 弹出_字符串(self):
        sb = self.弹出_字节数组()
        try:
            return sb.decode("utf-8")
        except:
            return sb.decode("gbk")


class Sunny证书管理器:
    SSL_ClientAuth_NoClientCert = 0
    """ 表示在握手过程中不应该请求客户端证书，并且如果发送了任何证书，它们将不会被验证。 """
    SSL_ClientAuth_RequestClientCert = 1
    """     表示应该在握手过程中请求客户端证书，但不要求客户端发送任何证书。     """
    SSL_ClientAuth_RequireAnyClientCert = 2
    """     表示在握手过程中应该请求客户端证书，并且客户端至少需要发送一个证书，但该证书不需要有效。 """
    SSL_ClientAuth_VerifyClientCertIfGiven = 3
    """     表示应该在握手过程中请求客户端证书，但不要求客户端发送证书。如果客户端发送了一个证书，它就需要是有效的。 """
    SSL_ClientAuth_RequireAndVerifyClientCert = 4
    """     表示握手时需要请求客户端证书，客户端至少需要发送一个有效的证书。 """

    def __init__(self):
        self.CertificateContext = SunnyDLL.DLLSunny.CreateCertificate()
        self.跳过主机验证(True)

    def __del__(self):
        SunnyDLL.DLLSunny.RemoveCertificate(self.CertificateContext)

    def 跳过主机验证(self, Skip):
        """ 请先载入证书 默认真 """
        SunnyDLL.DLLSunny.SetInsecureSkipVerify(self.CertificateContext, Skip)

    def 重新创建(self):
        if self.CertificateContext > 0:
            SunnyDLL.DLLSunny.RemoveCertificate(self.CertificateContext)
        self.CertificateContext = SunnyDLL.DLLSunny.CreateCertificate()
        self.跳过主机验证(True)

    def 载入P12Certificate(self, P12证书路径, P12证书密码):
        """ 默认 跳过主机验证 """
        SunnyDLL.DLLSunny.LoadP12Certificate(self.CertificateContext, create_string_buffer(P12证书路径.encode("utf-8")),
                                             create_string_buffer(P12证书密码.encode("utf-8")))

    def _载入X509KeyPair(self, cert文件路径, key文件路径):
        """ 从一对文件读取和解析一个公钥/私钥对。文件必须包含PEM编码的数据。证书文件可以在叶证书之后包含中间证书，形成证书链。 默认 跳过主机验证 """
        SunnyDLL.DLLSunny.LoadX509KeyPair(self.CertificateContext, create_string_buffer(cert文件路径.encode("utf-8")),
                                          create_string_buffer(key文件路径.encode("utf-8")))

    def _载入X509Certificate(self, Host, cer文件内容, key文件内容):
        """ 默认 跳过主机验证 """
        SunnyDLL.DLLSunny.LoadX509Certificate(self.CertificateContext, create_string_buffer(Host.encode("utf-8")),
                                              create_string_buffer(cer文件内容.encode("utf-8")),
                                              create_string_buffer(key文件内容.encode("utf-8")))

    def 设置ServerName(self, Name):
        """ 请先载入证书 设置的证书上的主机名 """
        SunnyDLL.DLLSunny.SetServerName(self.CertificateContext, create_string_buffer(Name.encode("utf-8")))

    def 获取ServerName(self):
        """ 请先载入证书 返回的证书上的主机名 """
        return SunnyDLL.PointerToText(SunnyDLL.DLLSunny.GetServerName(self.CertificateContext))

    def 获取证书Context(self):
        return self.CertificateContext

    def 添加客户端信任证书_文件(self, 文件路径):
        SunnyDLL.DLLSunny.AddCertPoolPath(self.CertificateContext, create_string_buffer(文件路径.encode("utf-8")))

    def 添加客户端信任证书_文本(self, 信任的证书文件内容):
        SunnyDLL.DLLSunny.AddCertPoolText(self.CertificateContext,
                                          create_string_buffer(信任的证书文件内容.encode("utf-8")))

    def 设置客户端身份验证模式(self, 模式=0):
        """  0-4 使用  SSL_ClientAuth_ """
        SunnyDLL.DLLSunny.AddClientAuth(self.CertificateContext, 模式)

    def 创建证书(self, 证书域名, 证书所属的国家="CN", 证书存放的公司名称="Sunny", 证书所属的部门名称="Sunny",
                 证书签发机构所在省="BeiJing",
                 证书签发机构所在市="BeiJing", 到期时间=3650):
        """
        证书所属的国家              默认      CN
        证书存放的公司名称           默认      Sunny
        证书所属的部门名称           默认      Sunny
        证书签发机构所在省           默认      BeiJing
        证书签发机构所在市           默认      BeiJing
        到期时间                   默认      3650天
        """
        r = SunnyDLL.DLLSunny.CreateCA(self.CertificateContext,
                                       create_string_buffer(证书所属的国家.encode("utf-8")),
                                       create_string_buffer(证书存放的公司名称.encode("utf-8")),
                                       create_string_buffer(证书所属的部门名称.encode("utf-8")),
                                       create_string_buffer(证书签发机构所在省.encode("utf-8")),
                                       create_string_buffer(证书域名.encode("utf-8")),
                                       create_string_buffer(证书签发机构所在市.encode("utf-8")), 2048, 到期时间)
        return bool(r)

    def _Replace(self, str):
        return str.replace("\r", "").replace("\n", "\r\n")

    def 导出公钥(self):
        return self._Replace(SunnyDLL.PointerToText(SunnyDLL.DLLSunny.ExportPub(self.CertificateContext)))

    def 导出私钥(self):
        return self._Replace(SunnyDLL.PointerToText(SunnyDLL.DLLSunny.ExportKEY(self.CertificateContext)))

    def 导出CA证书(self):
        return self._Replace(SunnyDLL.PointerToText(SunnyDLL.DLLSunny.ExportCA(self.CertificateContext)))

    def 获取CommonName(self):
        return self._Replace(SunnyDLL.PointerToText(SunnyDLL.DLLSunny.GetCommonName(self.CertificateContext)))

    def 导出P12文件(self, 保存路径, P12密码):
        r = SunnyDLL.DLLSunny.ExportP12(self.CertificateContext, create_string_buffer(
            保存路径.encode("utf-8")), create_string_buffer(P12密码.encode("utf-8")))
        return bool(r)


class SunnyNet:
    def __init__(self):
        """ 创建Sunny中间件对象,可创建多个 """
        self.WsCallback = None
        self.TcpCallback = None
        self.HttpCallback = None
        self.Context = SunnyDLL.DLLSunny.CreateSunnyNet()

    def __del__(self):
        """ 释放SunnyNet """
        SunnyDLL.DLLSunny.ReleaseSunnyNet(self.Context)

    def 取SunnyNetContext(self):
        """ Sunny中间件可创建多个 由这个参数判断是哪个Sunny回调过来的 """
        return self.Context

    def 导出证书(self):
        """ 导出已经设置的证书 """
        return SunnyDLL.PointerToText(SunnyDLL.DLLSunny.ExportCert(self.Context))

    def 强制客户端走TCP(self, open):
        """ 开启后SunnyNet不再对数据进行解密直接使用TCP发送，HTTPS的数据无法解码 """
        if isinstance(open, bool):
            SunnyDLL.DLLSunny.SunnyNetMustTcp(self.Context, open)

    def 身份验证模式_开启(self, open):
        """ 开启后客户端只能使用S5代理，并且输入设置的账号密码"""
        if isinstance(open, bool):
            SunnyDLL.DLLSunny.SunnyNetVerifyUser(self.Context, open)

    def 身份验证模式_添加用户(self, m_user, m_pass):
        """ 开启 身份验证模式 后 添加用户名 """
        if isinstance(m_user, str) and isinstance(m_pass, str):
            print(bool(
                SunnyDLL.DLLSunny.SunnyNetSocket5AddUser(self.Context, create_string_buffer(m_user.encode("utf-8")),
                                                         create_string_buffer(m_pass.encode("utf-8")))))

    def 身份验证模式_删除用户(self, m_user):
        """ 开启 身份验证模式 后 删除用户名 """
        if isinstance(m_user, str):
            SunnyDLL.DLLSunny.SunnyNetSocket5DelUser(self.Context, m_user)

    def 身份验证模式_获取授权的身份(self, 请求唯一ID):
        """ 开启身份验证模式后 获取授权的S5账号,注意UDP请求无法获取到授权的s5账号 """
        if isinstance(请求唯一ID, int):
            return SunnyDLL.PointerToText(SunnyDLL.DLLSunny.SunnyNetGetSocket5User(请求唯一ID))

    def 绑定端口(self, port):
        """ 在启动之前调用 """
        if isinstance(port, int):
            SunnyDLL.DLLSunny.SunnyNetSetPort(self.Context, port)

    def 启动(self):
        """ 启动前先绑定端口 """
        return bool(SunnyDLL.DLLSunny.SunnyNetStart(self.Context))

    def 关闭IE代理(self):
        """ 取消已经设置的IE代理 """
        SunnyDLL.DLLSunny.SetIeProxy(self.Context, True)

    def 停止代理(self):
        """ 停止中间件【停止的同时将会自动关闭IE代理】 """
        self.关闭IE代理()
        SunnyDLL.DLLSunny.SunnyNetClose(self.Context)

    def 绑定回调地址(self, HTTP回调地址, TCP回调地址, ws回调地址, UDP回调地址):
        """ 开启 身份验证模式 后 删除用户名 """
        self.HttpCallback = 0
        self.TcpCallback = 0
        self.WsCallback = 0
        self.UDPCallback = 0
        if callable(HTTP回调地址):
            self.HttpCallback = SunnyDLL.HttpCallback(HTTP回调地址)
        if callable(TCP回调地址):
            self.TcpCallback = SunnyDLL.TcpCallback(TCP回调地址)
        if callable(ws回调地址):
            self.WsCallback = SunnyDLL.WsCallback(ws回调地址)
        if callable(UDP回调地址):
            self.UDPCallback = SunnyDLL.UDPCallback(UDP回调地址)
        SunnyDLL.DLLSunny.SunnyNetSetCallback(self.Context, self.HttpCallback, self.TcpCallback, self.WsCallback,
                                              self.UDPCallback)

    def 设置自定义CA证书(self, 证书管理器):
        """ 导入自己的证书 """
        if isinstance(证书管理器, Sunny证书管理器):
            r = SunnyDLL.DLLSunny.SunnyNetSetCert(self.Context, 证书管理器.获取证书Context())
            return bool(r)
        else:
            print("设置自定义CA证书 传入参数错误")
            exit(0)

    def 安装证书(self):
        """ 启动后调用,将中间件的证书安装到系统内 返回安装结果文本，若失败需要手动安装 """
        err = SunnyDLL.PointerToText(SunnyDLL.DLLSunny.SunnyNetInstallCert(self.Context))
        if "添加到存储" in err:
            return True
        if "已经在存储中" in err:
            return True
        return False

    def 取错误(self):
        """ 获取中间件启动时的错误信息 """
        return SunnyDLL.PointerToText(SunnyDLL.DLLSunny.SunnyNetError(self.Context))

    def 禁用TCP(self, 禁用):
        """
        将禁止非HTTP/S的TCP连接,某些APP,将先尝试TCP请求,如果TCP请求失败才会发送HTTP请求,这种场景下有用
        """
        if not isinstance(禁用, bool):
            return False
        param = 1 if 禁用 else 0
        return bool(SunnyDLL.OtherCommands(1001, self.Context, param))

    def TLS指纹_获取一个随机值(self):
        """
        获取后，您可以使用“TLS指纹_固定指纹”命令进行设置，
        """
        return SunnyDLL.PointerToText(SunnyDLL.OtherCommands(1004, self.Context))

    def TLS指纹_固定指纹(self, CipherSuites):
        """
        设置后您可以使用“TLS指纹_开启请求随机指纹”命令来取消设置
        您可以使用“TLS指纹_获取一个随机值”命令来生成一个随机值
        """
        return bool(SunnyDLL.OtherCommands(1003, self.Context, CipherSuites, len(CipherSuites)))

    def TLS指纹_开启请求随机指纹(self, open):
        """
        开启后,每次请求将使用随机的指纹请求
        注意关闭后,“TLS指纹_固定指纹”也会同时取消
        """
        param = 1 if open else 0
        return bool(SunnyDLL.OtherCommands(1002, self.Context, param))

    def 设置上游代理(self, 代理):
        """
        设置上游代理 仅支持S5代理 或 http代理
        仅支持Socket5和http 例如 socket5://admin:123456@127.0.0.1:8888 或 http://admin:123456@127.0.0.1:8888
        """
        if not isinstance(代理, str):
            return False
        return bool(SunnyDLL.DLLSunny.SetGlobalProxy(self.Context, create_string_buffer(代理.encode("utf-8"))))

    def 设置上游代理使用规则(self, 规则):
        """
        默认全部使用上游代理(只要设置了上游代理)
        输入Host不带端口号;在此规则内的不使用上游代理 多个用";"分号或换行分割 例如"127.0.0.1;192.168.*.*"地址不使用上游代理
        """
        if not isinstance(规则, str):
            return False
        return bool(SunnyDLL.DLLSunny.CompileProxyRegexp(self.Context, create_string_buffer(规则.encode("utf-8"))))

    def 设置强制走TCP规则(self, 规则):
        """
        设置强制走TCP规则,如果 打开了全部强制走TCP状态,本功能则无效
        输入Host不带端口号;在此规则内 多个用";"分号或换行分割 例如"127.0.0.1;192.168.*.*"强制使用TCP
        """
        if not isinstance(规则, str):
            return False
        return bool(SunnyDLL.DLLSunny.SetMustTcpRegexp(self.Context, create_string_buffer(规则.encode("utf-8"))))

    def 设置IE代理(self):
        """
        设置当前绑定的端口号为当前IE代理 设置前请先绑定端口
        """
        SunnyDLL.DLLSunny.SetIeProxy(self.Context, False)

    def 进程代理_加载驱动(self):
        """
        只允许一个中间件服务 加载驱动,使用前，请先启动Sunny中间件
        """
        return bool(SunnyDLL.DLLSunny.StartProcess(self.Context))

    def 进程代理_添加进程名(self, name):
        """
        添加指定的进程名进行捕获[需调用 启动进程代理 后生效]
        name = 进程名 例如 e.exe
		会强制断开此进程已经连接的TCP连接
        """
        if not isinstance(name, str):
            return
        SunnyDLL.DLLSunny.ProcessAddName(self.Context, create_string_buffer(name.encode("utf-8")))

    def 进程代理_删除进程名(self, name):
        """
        删除指定的进程名 停止捕获[需调用 启动进程代理 后生效]
        name = 进程名 例如 e.exe
		会强制断开此进程已经连接的TCP连接
        """
        if not isinstance(name, str):
            return
        SunnyDLL.DLLSunny.ProcessDelName(self.Context, create_string_buffer(name.encode("utf-8")))

    def 进程代理_添加Pid(self, pid):
        """
        添加指定的进程PID进行捕获[需调用 启动进程代理 后生效]
        pid = 进程PID 例如 11223
		会强制断开此进程已经连接的TCP连接
        """
        if not isinstance(pid, int):
            return
        SunnyDLL.DLLSunny.ProcessAddPid(self.Context, pid)

    def 进程代理_删除Pid(self, pid):
        """
        删除指定的进程PID 停止捕获[需调用 启动进程代理 后生效]
        pid = 进程PID 例如 11223
		会强制断开此进程已经连接的TCP连接
        """
        if not isinstance(pid, int):
            return
        SunnyDLL.DLLSunny.ProcessDelPid(self.Context, pid)

    def 进程代理_设置捕获任意进程(self, open):
        """
        开启后 所有进程将会被捕获[需调用 启动进程代理 后生效]
        无论开启还是关闭 都会将之前添加的进程名或PID清空
		会强制断开所有进程已经连接的TCP连接
        """
        if not isinstance(open, bool):
            return
        SunnyDLL.DLLSunny.ProcessALLName(self.Context, open)

    def 进程代理_删除全部(self):
        """
        删除已设置的所有PID,进程名 [需调用 启动进程代理 后生效]
		会强制断开所有进程已经连接的TCP连接
        """
        SunnyDLL.DLLSunny.ProcessCancelAll(self.Context)


def MessageIdToSunny(MessageId):
    if not isinstance(MessageId, int):
        print("MessageIdToSunny 传入参数错误")
        exit(0)
    return SunnyDLL.Sunny(MessageId)
