// pre
// : 
// "2uMMaWqGxqNSD7HR"
// prod
// : 
// "kEyOA02sa7d8dUYr"
// test03
// : 
// "17PbwMBpDfNrHD4N"
// test04
// : 
// "gpeiHLyY1bm2zuGQ"
Crypto ={}
!function() {
    var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
      , n = Crypto
      , r = n.util = {
        rotl: function(t, n) {
            return t << n | t >>> 32 - n
        },
        rotr: function(t, n) {
            return t << 32 - n | t >>> n
        },
        endian: function(t) {
            if (t.constructor == Number)
                return 16711935 & r.rotl(t, 8) | 4278255360 & r.rotl(t, 24);
            for (var n = 0; n < t.length; n++)
                t[n] = r.endian(t[n]);
            return t
        },
        randomBytes: function(t) {
            for (var n = []; t > 0; t--)
                n.push(Math.floor(256 * Math.random()));
            return n
        },
        bytesToWords: function(t) {
            for (var n = [], r = 0, o = 0; r < t.length; r++,
            o += 8)
                n[o >>> 5] |= (255 & t[r]) << 24 - o % 32;
            return n
        },
        wordsToBytes: function(t) {
            for (var n = [], r = 0; r < 32 * t.length; r += 8)
                n.push(t[r >>> 5] >>> 24 - r % 32 & 255);
            return n
        },
        bytesToHex: function(t) {
            for (var n = [], r = 0; r < t.length; r++)
                n.push((t[r] >>> 4).toString(16)),
                n.push((15 & t[r]).toString(16));
            return n.join("")
        },
        hexToBytes: function(t) {
            for (var n = [], r = 0; r < t.length; r += 2)
                n.push(parseInt(t.substr(r, 2), 16));
            return n
        },
        bytesToBase64: function(n) {
            if ("function" == typeof btoa)
                return btoa(e.bytesToString(n));
            for (var r = [], o = 0; o < n.length; o += 3)
                for (var u = n[o] << 16 | n[o + 1] << 8 | n[o + 2], i = 0; i < 4; i++)
                    8 * o + 6 * i <= 8 * n.length ? r.push(t.charAt(u >>> 6 * (3 - i) & 63)) : r.push("=");
            return r.join("")
        },
        base64ToBytes: function(n) {
            if ("function" == typeof atob)
                return e.stringToBytes(atob(n));
            n = n.replace(/[^A-Z0-9+\/]/gi, "");
            for (var r = [], o = 0, u = 0; o < n.length; u = ++o % 4)
                0 != u && r.push((t.indexOf(n.charAt(o - 1)) & Math.pow(2, -2 * u + 8) - 1) << 2 * u | t.indexOf(n.charAt(o)) >>> 6 - 2 * u);
            return r
        }
    }
      , o = n.charenc = {}
      , e = (o.UTF8 = {
        stringToBytes: function(t) {
            return e.stringToBytes(unescape(encodeURIComponent(t)))
        },
        bytesToString: function(t) {
            return decodeURIComponent(escape(e.bytesToString(t)))
        }
    },
    o.Binary = {
        stringToBytes: function(t) {
            for (var n = [], r = 0; r < t.length; r++)
                n.push(255 & t.charCodeAt(r));
            return n
        },
        bytesToString: function(t) {
            for (var n = [], r = 0; r < t.length; r++)
                n.push(String.fromCharCode(t[r]));
            return n.join("")
        }
    })
}();
!function() {
    var n = "undefined" == typeof window ? Crypto : window.Crypto
      , o = n.pad = {};
    function t(n, o) {
        var t = 4 * n._blocksize;
        return t - o.length % t
    }
    var r = function(n) {
        for (var o = n.pop(), t = 1; t < o; t++)
            n.pop()
    };
    o.NoPadding = {
        pad: function(n, o) {},
        unpad: function(n) {}
    },
    o.ZeroPadding = {
        pad: function(n, o) {
            var t = 4 * n._blocksize
              , r = o.length % t;
            if (0 != r)
                for (r = t - r; r > 0; r--)
                    o.push(0)
        },
        unpad: function(n) {}
    },
    o.iso7816 = {
        pad: function(n, o) {
            var r = t(n, o);
            for (o.push(128); r > 1; r--)
                o.push(0)
        },
        unpad: function(n) {
            for (; 128 != n.pop(); )
                ;
        }
    },
    o.ansix923 = {
        pad: function(n, o) {
            for (var r = t(n, o), p = 1; p < r; p++)
                o.push(0);
            o.push(r)
        },
        unpad: r
    },
    o.iso10126 = {
        pad: function(n, o) {
            for (var r = t(n, o), p = 1; p < r; p++)
                o.push(Math.floor(256 * Math.random()));
            o.push(r)
        },
        unpad: r
    },
    o.pkcs7 = {
        pad: function(n, o) {
            for (var r = t(n, o), p = 0; p < r; p++)
                o.push(r)
        },
        unpad: r
    };
    var p = n.mode = {}
      , i = p.Mode = function(n) {
        n && (this._padding = n)
    }
    ;
    i.prototype = {
        encrypt: function(n, o, t) {
            this._padding.pad(n, o),
            this._doEncrypt(n, o, t)
        },
        decrypt: function(n, o, t) {
            this._doDecrypt(n, o, t),
            this._padding.unpad(o)
        },
        _padding: o.iso7816
    };
    var c = (p.ECB = function() {
        i.apply(this, arguments)
    }
    ).prototype = new i;
    c._doEncrypt = function(n, o, t) {
        for (var r = 4 * n._blocksize, p = 0; p < o.length; p += r)
            n._encryptblock(o, p)
    }
    ,
    c._doDecrypt = function(n, o, t) {
        for (var r = 4 * n._blocksize, p = 0; p < o.length; p += r)
            n._decryptblock(o, p)
    }
    ,
    c.fixOptions = function(n) {
        n.iv = []
    }
    ;
    var a = (p.CBC = function() {
        i.apply(this, arguments)
    }
    ).prototype = new i;
    a._doEncrypt = function(n, o, t) {
        for (var r = 4 * n._blocksize, p = 0; p < o.length; p += r) {
            if (0 == p)
                for (var i = 0; i < r; i++)
                    o[i] ^= t[i];
            else
                for (i = 0; i < r; i++)
                    o[p + i] ^= o[p + i - r];
            n._encryptblock(o, p)
        }
    }
    ,
    a._doDecrypt = function(n, o, t) {
        for (var r = 4 * n._blocksize, p = t, i = 0; i < o.length; i += r) {
            var c = o.slice(i, i + r);
            n._decryptblock(o, i);
            for (var a = 0; a < r; a++)
                o[i + a] ^= p[a];
            p = c
        }
    }
    ;
    var e = (p.CFB = function() {
        i.apply(this, arguments)
    }
    ).prototype = new i;
    e._padding = o.NoPadding,
    e._doEncrypt = function(n, o, t) {
        for (var r = 4 * n._blocksize, p = t.slice(0), i = 0; i < o.length; i++) {
            var c = i % r;
            0 == c && n._encryptblock(p, 0),
            o[i] ^= p[c],
            p[c] = o[i]
        }
    }
    ,
    e._doDecrypt = function(n, o, t) {
        for (var r = 4 * n._blocksize, p = t.slice(0), i = 0; i < o.length; i++) {
            var c = i % r;
            0 == c && n._encryptblock(p, 0);
            var a = o[i];
            o[i] ^= p[c],
            p[c] = a
        }
    }
    ;
    var d = (p.OFB = function() {
        i.apply(this, arguments)
    }
    ).prototype = new i;
    d._padding = o.NoPadding,
    d._doEncrypt = function(n, o, t) {
        for (var r = 4 * n._blocksize, p = t.slice(0), i = 0; i < o.length; i++)
            i % r == 0 && n._encryptblock(p, 0),
            o[i] ^= p[i % r]
    }
    ,
    d._doDecrypt = d._doEncrypt;
    var f = (p.CTR = function() {
        i.apply(this, arguments)
    }
    ).prototype = new i;
    f._padding = o.NoPadding,
    f._doEncrypt = function(n, o, t) {
        for (var r = 4 * n._blocksize, p = t.slice(0), i = 0; i < o.length; ) {
            var c = p.slice(0);
            n._encryptblock(c, 0);
            for (var a = 0; i < o.length && a < r; a++,
            i++)
                o[i] ^= c[a];
            256 == ++p[r - 1] && (p[r - 1] = 0,
            256 == ++p[r - 2] && (p[r - 2] = 0,
            256 == ++p[r - 3] && (p[r - 3] = 0,
            ++p[r - 4])))
        }
    }
    ,
    f._doDecrypt = f._doEncrypt
}();
!function() {
    for (var r = "undefined" == typeof window ? Crypto : window.Crypto, o = r.util, t = r.charenc.UTF8, f = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22], s = [], i = 0; i < 256; i++)
        s[f[i]] = i;
    var n = []
      , e = []
      , c = []
      , p = []
      , u = []
      , h = [];
    function a(r, o) {
        for (var t = 0, f = 0; f < 8; f++) {
            1 & o && (t ^= r);
            var s = 128 & r;
            r = r << 1 & 255,
            s && (r ^= 27),
            o >>>= 1
        }
        return t
    }
    for (i = 0; i < 256; i++)
        n[i] = a(i, 2),
        e[i] = a(i, 3),
        c[i] = a(i, 9),
        p[i] = a(i, 11),
        u[i] = a(i, 13),
        h[i] = a(i, 14);
    var v, y, _, b = [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54], l = [[], [], [], []], d = r.AES = {
        encrypt: function(f, s, i) {
            var n = (i = i || {}).mode || new r.mode.ECB;
            n.fixOptions && n.fixOptions(i);
            var e = f.constructor == String ? t.stringToBytes(f) : f
              , c = i.iv || o.randomBytes(4 * d._blocksize)
              , p = s.constructor == String ? r.PBKDF2(s, c, 32, {
                asBytes: !0
            }) : s;
            return d._init(p),
            n.encrypt(d, e, c),
            e = i.iv ? e : c.concat(e),
            i && i.asBytes ? e : o.bytesToBase64(e)
        },
        decrypt: function(f, s, i) {
            var n = (i = i || {}).mode || new r.mode.OFB;
            n.fixOptions && n.fixOptions(i);
            var e = f.constructor == String ? o.base64ToBytes(f) : f
              , c = i.iv || e.splice(0, 4 * d._blocksize)
              , p = s.constructor == String ? r.PBKDF2(s, c, 32, {
                asBytes: !0
            }) : s;
            return d._init(p),
            n.decrypt(d, e, c),
            i && i.asBytes ? e : t.bytesToString(e)
        },
        _blocksize: 4,
        _encryptblock: function(r, o) {
            for (var t = 0; t < d._blocksize; t++)
                for (var s = 0; s < 4; s++)
                    l[t][s] = r[o + 4 * s + t];
            for (t = 0; t < 4; t++)
                for (s = 0; s < 4; s++)
                    l[t][s] ^= _[s][t];
            for (var i = 1; i < y; i++) {
                for (t = 0; t < 4; t++)
                    for (s = 0; s < 4; s++)
                        l[t][s] = f[l[t][s]];
                l[1].push(l[1].shift()),
                l[2].push(l[2].shift()),
                l[2].push(l[2].shift()),
                l[3].unshift(l[3].pop());
                for (s = 0; s < 4; s++) {
                    var c = l[0][s]
                      , p = l[1][s]
                      , u = l[2][s]
                      , h = l[3][s];
                    l[0][s] = n[c] ^ e[p] ^ u ^ h,
                    l[1][s] = c ^ n[p] ^ e[u] ^ h,
                    l[2][s] = c ^ p ^ n[u] ^ e[h],
                    l[3][s] = e[c] ^ p ^ u ^ n[h]
                }
                for (t = 0; t < 4; t++)
                    for (s = 0; s < 4; s++)
                        l[t][s] ^= _[4 * i + s][t]
            }
            for (t = 0; t < 4; t++)
                for (s = 0; s < 4; s++)
                    l[t][s] = f[l[t][s]];
            l[1].push(l[1].shift()),
            l[2].push(l[2].shift()),
            l[2].push(l[2].shift()),
            l[3].unshift(l[3].pop());
            for (t = 0; t < 4; t++)
                for (s = 0; s < 4; s++)
                    l[t][s] ^= _[4 * y + s][t];
            for (t = 0; t < d._blocksize; t++)
                for (s = 0; s < 4; s++)
                    r[o + 4 * s + t] = l[t][s]
        },
        _decryptblock: function(r, o) {
            for (var t = 0; t < d._blocksize; t++)
                for (var f = 0; f < 4; f++)
                    l[t][f] = r[o + 4 * f + t];
            for (t = 0; t < 4; t++)
                for (f = 0; f < 4; f++)
                    l[t][f] ^= _[4 * y + f][t];
            for (var i = 1; i < y; i++) {
                l[1].unshift(l[1].pop()),
                l[2].push(l[2].shift()),
                l[2].push(l[2].shift()),
                l[3].push(l[3].shift());
                for (t = 0; t < 4; t++)
                    for (f = 0; f < 4; f++)
                        l[t][f] = s[l[t][f]];
                for (t = 0; t < 4; t++)
                    for (f = 0; f < 4; f++)
                        l[t][f] ^= _[4 * (y - i) + f][t];
                for (f = 0; f < 4; f++) {
                    var n = l[0][f]
                      , e = l[1][f]
                      , a = l[2][f]
                      , v = l[3][f];
                    l[0][f] = h[n] ^ p[e] ^ u[a] ^ c[v],
                    l[1][f] = c[n] ^ h[e] ^ p[a] ^ u[v],
                    l[2][f] = u[n] ^ c[e] ^ h[a] ^ p[v],
                    l[3][f] = p[n] ^ u[e] ^ c[a] ^ h[v]
                }
            }
            l[1].unshift(l[1].pop()),
            l[2].push(l[2].shift()),
            l[2].push(l[2].shift()),
            l[3].push(l[3].shift());
            for (t = 0; t < 4; t++)
                for (f = 0; f < 4; f++)
                    l[t][f] = s[l[t][f]];
            for (t = 0; t < 4; t++)
                for (f = 0; f < 4; f++)
                    l[t][f] ^= _[f][t];
            for (t = 0; t < d._blocksize; t++)
                for (f = 0; f < 4; f++)
                    r[o + 4 * f + t] = l[t][f]
        },
        _init: function(r) {
            v = r.length / 4,
            y = v + 6,
            d._keyexpansion(r)
        },
        _keyexpansion: function(r) {
            _ = [];
            for (var o = 0; o < v; o++)
                _[o] = [r[4 * o], r[4 * o + 1], r[4 * o + 2], r[4 * o + 3]];
            for (o = v; o < d._blocksize * (y + 1); o++) {
                var t = [_[o - 1][0], _[o - 1][1], _[o - 1][2], _[o - 1][3]];
                o % v == 0 ? (t.push(t.shift()),
                t[0] = f[t[0]],
                t[1] = f[t[1]],
                t[2] = f[t[2]],
                t[3] = f[t[3]],
                t[0] ^= b[o / v]) : v > 6 && o % v == 4 && (t[0] = f[t[0]],
                t[1] = f[t[1]],
                t[2] = f[t[2]],
                t[3] = f[t[3]]),
                _[o] = [_[o - v][0] ^ t[0], _[o - v][1] ^ t[1], _[o - v][2] ^ t[2], _[o - v][3] ^ t[3]]
            }
        }
    }
}();
e = 128
t = function(r) {
        for (var t = function(r) {
            for (var e, t, n = [], a = 0; a < r.length; a++) {
                e = r.charCodeAt(a),
                t = [];
                do {
                    t.push(255 & e),
                    e >>= 8
                } while (e);
                n = n.concat(t.reverse())
            }
            return n
        }(r), n = new Array, a = e / 8, s = 0; s < a; s++)
            t.length > s ? n.push(t[s]) : n.push(0);
        return n
    }
var L = "kEyOA02sa7d8dUYr";
var data = "Kl2_X6P85gZp7jT9A1seUPqhGIV8StkyonEH0KUikYlxbIzokUVoI57unNaNtDoPkKks0xoHtorAw3SfjLeOve9dQT9oOtVGMdowXSYtQ-9l5s69bwkE8AiOSuawhVBhEbyxVqFIW7zPCP4qXuRlXP1VDvWM4dGXRdNBDO-v1tpPwNum6TgQ8ABlOuweo6d-VpG-oSI9QzLaaK2zfNOL1UcdG3DeYEFqj4_B5aPXG6pc3Et8JZ0nTSuJPVsIHqtfxrZchae7V8fTbHgXYqWTgbL17SEI8RSIobY1r6Wu3PbsPknWyis-T79-NP6j_LqbQr0SpPMj5LR1umIUIOgiPUU_kTsH7au5EnVcUyv2LLXKxCBa3q_P6A23OD3GGToHAnDpZNnerMjcKDLcU04pvSWIh-kUGDJKvSr52-2AoLSyZEpJNrtrE2NRQG3PpcglRWQUg0M1cdrJIZP37UFoX9k4IYLmxc241JjvBR3BnzoIJ6Zwai2_gOHct10LiQY8xVdxuQUrC3Mq41t8pFjngv86-peEA6gD8OSMwRXRF8Ikmzd9H9ln_R_tCInzlOyxMHOY5KG15BF7o1ka0hvcD2t1xff__tOfobVUW-Z5WLkAwx9QZvfsRaBEtxRTKoGLzldEh36C2p-8xFWwRnX1neskpJvDoCfS5iBVqO0c1K9LqTrZOLF699e2cXpBCsdHcm0h1kx9qdoqJGkA4tP9s9dXEl9oVnNzvXiaFF5_xCyEWIkXx5KY9fmQuiyknipcGD4qPptcxt6dTvQNRHPYhGUcVYlT5Xmzu1KjW11HjQaxcd--8GiekBVwxG78Vns-JDqoDEolUM12ejNyuAak_JOMKhoiJpgEVqM_zv3x70wktQ2_q5NteMHQ_XfWcqvZ0utZoV95RtT1efUrHNh4f66KYfIHeNkMDE-C-n-8-gxxgoqN0J9yAW2_QzhIWWDcHh7GCFNP3jHGSsoAiLyr5loCtzCcm0gQk1sjIujJkWFZf-Z-JSu0lFOqmfKR77XleRVK_r67_DcmjVAFZtas56EeLj6ZP87qB4UHxf-PimK5n7RqGiAlinhSES5wMf5GY4qO35ewzey2j1Daa6FHj_deEmj97u9HjkrhkeXOHc9D6cIntpmjL5JqXo59gsMSJ1LEWzxAgPomZWYuCw84yp6xRV_-Zmd48rhwlw0_lOw9itf9U7p-i-byE7jtU5sZxaS9HUsWtM_DNXa5igQiTHeFMFpXwYwE7Qy0R8Re9p52Z2E8OMaazxOAU65KlkCi3WNREfUdRHo-VXdxCFJ9QEZmQGztU7Qg9dgPmYe2MsqVo8gh7ylIHnjYwfam4nhomoMoqV1dV7ItiRc5QYpa37JRctjiPrFjpDctOd3X_GjCquUphaosb61igWYayLSXWUG-ndsyYtca59rGSQOSnCtrxdjah2nyRjsFVlflcujDIzaguUBICc_fZYJqFPoOGUN3z9Nlajlbyupv_k5r4A==";
function de(e, n, a) {
    a && (e = e.replace(/-/g, "+").replace(/_/g, "/"));
    var s = new Crypto.mode.ECB(Crypto.pad.pkcs7)
      , o = Crypto.util.base64ToBytes(e);
      Crypto.charenc.UTF8.stringToBytes(n);
    return Crypto.AES.decrypt(o, t(n), {
        asBpytes: !0,
        mode: s,
        iv: ""
    })
}
console.log(de(data,L,true))
