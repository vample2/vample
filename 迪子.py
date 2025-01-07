def get_sign():
    # n = "2YAhmad694MnzqmcPQ5X6TJ6EoSx6sYx"
    r = "Bu0Zsh4B0SnKBRfds0XWCSn51WJfn5yN"
    a = str(int(time.time() * 1000))  # 当前时间戳，单位为毫秒
    u = 'v1'
    c = {
        "timestamp": a,
        "path": "/cotti-capi/universal/coupon/receiveLaunchRewardH5",
        "version": u
    }

    s = []
    for t in sorted(c.keys()):
        e = c[t]
        if e:
            s.append(f"{t}{e}")

    s.append(r)
    result = "".join(s)
    md5_hash = hashlib.md5(result.encode()).hexdigest().upper()
    _sign = {
        'sign': md5_hash,
        'time': a,
    }
    return _sign
