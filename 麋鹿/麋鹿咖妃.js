Crypto ={
    "aes": {}
}
!function() {
    var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
      n = Crypto,
      r = n.util = {
        rotl: function (t, n) {
          return t << n | t >>> 32 - n
        },
        rotr: function (t, n) {
          return t << 32 - n | t >>> n
        },
        endian: function (t) {
          if (t.constructor == Number) return 16711935 & r.rotl(t, 8) | 4278255360 & r.rotl(t, 24);
          for (var n = 0; n < t.length; n++) t[n] = r.endian(t[n]);
          return t
        },
        randomBytes: function (t) {
          for (var n = []; t > 0; t--) n.push(Math.floor(256 * Math.random()));
          return n
        },
        bytesToWords: function (t) {
          for (var n = [], r = 0, o = 0; r < t.length; r++, o += 8) n[o >>> 5] |= (255 & t[r]) << 24 - o % 32;
          return n
        },
        wordsToBytes: function (t) {
          for (var n = [], r = 0; r < 32 * t.length; r += 8) n.push(t[r >>> 5] >>> 24 - r % 32 & 255);
          return n
        },
        bytesToHex: function (t) {
          for (var n = [], r = 0; r < t.length; r++) n.push((t[r] >>> 4).toString(16)), n.push((15 & t[r]).toString(16));
          return n.join("")
        },
        hexToBytes: function (t) {
          for (var n = [], r = 0; r < t.length; r += 2) n.push(parseInt(t.substr(r, 2), 16));
          return n
        },
        bytesToBase64: function (n) {
          if ("function" == typeof btoa) return btoa(e.bytesToString(n));
          for (var r = [], o = 0; o < n.length; o += 3)
            for (var u = n[o] << 16 | n[o + 1] << 8 | n[o + 2], i = 0; i < 4; i++) 8 * o + 6 * i <= 8 * n.length ? r.push(t.charAt(u >>> 6 * (3 - i) & 63)) : r.push("=");
          return r.join("")
        },
        base64ToBytes: function (n) {
          if ("function" == typeof atob) return e.stringToBytes(atob(n));
          n = n.replace(/[^A-Z0-9+\/]/gi, "");
          for (var r = [], o = 0, u = 0; o < n.length; u = ++o % 4) 0 != u && r.push((t.indexOf(n.charAt(o - 1)) & Math.pow(2, -2 * u + 8) - 1) << 2 * u | t.indexOf(n.charAt(o)) >>> 6 - 2 * u);
          return r
        }
      },
      o = n.charenc = {},
      e = (o.UTF8 = {
        stringToBytes: function (t) {
          return e.stringToBytes(unescape(encodeURIComponent(t)))
        },
        bytesToString: function (t) {
          return decodeURIComponent(escape(e.bytesToString(t)))
        }
      }, o.Binary = {
        stringToBytes: function (t) {
          for (var n = [], r = 0; r < t.length; r++) n.push(255 & t.charCodeAt(r));
          return n
        },
        bytesToString: function (t) {
          for (var n = [], r = 0; r < t.length; r++) n.push(String.fromCharCode(t[r]));
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
        for (var r = Crypto, o = r.util, t = r.charenc.UTF8, f = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22], s = [], i = 0; i < 256; i++)
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
!function() {
    var r, t, n, e, i, o;
    r = Crypto,
    t = r.util,
    n = r.charenc,
    e = n.UTF8,
    i = n.Binary,
    (o = r.MD5 = function(r, n) {
        var e = t.wordsToBytes(o._md5(r));
        return n && n.asBytes ? e : n && n.asString ? i.bytesToString(e) : t.bytesToHex(e)
    }
    )._md5 = function(r) {
        r.constructor == String && (r = e.stringToBytes(r));
        for (var n = t.bytesToWords(r), i = 8 * r.length, s = 1732584193, u = -271733879, a = -1732584194, f = 271733878, c = 0; c < n.length; c++)
            n[c] = 16711935 & (n[c] << 8 | n[c] >>> 24) | 4278255360 & (n[c] << 24 | n[c] >>> 8);
        n[i >>> 5] |= 128 << i % 32,
        n[14 + (i + 64 >>> 9 << 4)] = i;
        var g = o._ff
        , _ = o._gg
        , y = o._hh
        , d = o._ii;
        for (c = 0; c < n.length; c += 16) {
            var v = s
            , h = u
            , T = a
            , l = f;
            s = g(s, u, a, f, n[c + 0], 7, -680876936),
            f = g(f, s, u, a, n[c + 1], 12, -389564586),
            a = g(a, f, s, u, n[c + 2], 17, 606105819),
            u = g(u, a, f, s, n[c + 3], 22, -1044525330),
            s = g(s, u, a, f, n[c + 4], 7, -176418897),
            f = g(f, s, u, a, n[c + 5], 12, 1200080426),
            a = g(a, f, s, u, n[c + 6], 17, -1473231341),
            u = g(u, a, f, s, n[c + 7], 22, -45705983),
            s = g(s, u, a, f, n[c + 8], 7, 1770035416),
            f = g(f, s, u, a, n[c + 9], 12, -1958414417),
            a = g(a, f, s, u, n[c + 10], 17, -42063),
            u = g(u, a, f, s, n[c + 11], 22, -1990404162),
            s = g(s, u, a, f, n[c + 12], 7, 1804603682),
            f = g(f, s, u, a, n[c + 13], 12, -40341101),
            a = g(a, f, s, u, n[c + 14], 17, -1502002290),
            s = _(s, u = g(u, a, f, s, n[c + 15], 22, 1236535329), a, f, n[c + 1], 5, -165796510),
            f = _(f, s, u, a, n[c + 6], 9, -1069501632),
            a = _(a, f, s, u, n[c + 11], 14, 643717713),
            u = _(u, a, f, s, n[c + 0], 20, -373897302),
            s = _(s, u, a, f, n[c + 5], 5, -701558691),
            f = _(f, s, u, a, n[c + 10], 9, 38016083),
            a = _(a, f, s, u, n[c + 15], 14, -660478335),
            u = _(u, a, f, s, n[c + 4], 20, -405537848),
            s = _(s, u, a, f, n[c + 9], 5, 568446438),
            f = _(f, s, u, a, n[c + 14], 9, -1019803690),
            a = _(a, f, s, u, n[c + 3], 14, -187363961),
            u = _(u, a, f, s, n[c + 8], 20, 1163531501),
            s = _(s, u, a, f, n[c + 13], 5, -1444681467),
            f = _(f, s, u, a, n[c + 2], 9, -51403784),
            a = _(a, f, s, u, n[c + 7], 14, 1735328473),
            s = y(s, u = _(u, a, f, s, n[c + 12], 20, -1926607734), a, f, n[c + 5], 4, -378558),
            f = y(f, s, u, a, n[c + 8], 11, -2022574463),
            a = y(a, f, s, u, n[c + 11], 16, 1839030562),
            u = y(u, a, f, s, n[c + 14], 23, -35309556),
            s = y(s, u, a, f, n[c + 1], 4, -1530992060),
            f = y(f, s, u, a, n[c + 4], 11, 1272893353),
            a = y(a, f, s, u, n[c + 7], 16, -155497632),
            u = y(u, a, f, s, n[c + 10], 23, -1094730640),
            s = y(s, u, a, f, n[c + 13], 4, 681279174),
            f = y(f, s, u, a, n[c + 0], 11, -358537222),
            a = y(a, f, s, u, n[c + 3], 16, -722521979),
            u = y(u, a, f, s, n[c + 6], 23, 76029189),
            s = y(s, u, a, f, n[c + 9], 4, -640364487),
            f = y(f, s, u, a, n[c + 12], 11, -421815835),
            a = y(a, f, s, u, n[c + 15], 16, 530742520),
            s = d(s, u = y(u, a, f, s, n[c + 2], 23, -995338651), a, f, n[c + 0], 6, -198630844),
            f = d(f, s, u, a, n[c + 7], 10, 1126891415),
            a = d(a, f, s, u, n[c + 14], 15, -1416354905),
            u = d(u, a, f, s, n[c + 5], 21, -57434055),
            s = d(s, u, a, f, n[c + 12], 6, 1700485571),
            f = d(f, s, u, a, n[c + 3], 10, -1894986606),
            a = d(a, f, s, u, n[c + 10], 15, -1051523),
            u = d(u, a, f, s, n[c + 1], 21, -2054922799),
            s = d(s, u, a, f, n[c + 8], 6, 1873313359),
            f = d(f, s, u, a, n[c + 15], 10, -30611744),
            a = d(a, f, s, u, n[c + 6], 15, -1560198380),
            u = d(u, a, f, s, n[c + 13], 21, 1309151649),
            s = d(s, u, a, f, n[c + 4], 6, -145523070),
            f = d(f, s, u, a, n[c + 11], 10, -1120210379),
            a = d(a, f, s, u, n[c + 2], 15, 718787259),
            u = d(u, a, f, s, n[c + 9], 21, -343485551),
            s = s + v >>> 0,
            u = u + h >>> 0,
            a = a + T >>> 0,
            f = f + l >>> 0
        }
        return t.endian([s, u, a, f])
    }
    ,
    o._ff = function(r, t, n, e, i, o, s) {
        var u = r + (t & n | ~t & e) + (i >>> 0) + s;
        return (u << o | u >>> 32 - o) + t
    }
    ,
    o._gg = function(r, t, n, e, i, o, s) {
        var u = r + (t & e | n & ~e) + (i >>> 0) + s;
        return (u << o | u >>> 32 - o) + t
    }
    ,
    o._hh = function(r, t, n, e, i, o, s) {
        var u = r + (t ^ n ^ e) + (i >>> 0) + s;
        return (u << o | u >>> 32 - o) + t
    }
    ,
    o._ii = function(r, t, n, e, i, o, s) {
        var u = r + (n ^ (t | ~e)) + (i >>> 0) + s;
        return (u << o | u >>> 32 - o) + t
    }
    ,
    o._blocksize = 16,
    o._digestsize = 16;
}();


e = 128,
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
  , n = function(r, e) {
    return (255 & r[e]) << 24 | (255 & r[e + 1]) << 16 | (255 & r[e + 2]) << 8 | 255 & r[e + 3]
}
  , Crypto.aes = {
    en: function(e, n, a) {
        var s = new Crypto.mode.ECB(Crypto.pad.pkcs7)
          , o = Crypto.charenc.UTF8.stringToBytes(e)
          , c = (Crypto.charenc.UTF8.stringToBytes(n),
          Crypto.AES.encrypt(o, t(n), {
            iv: "",
            mode: s,
            asBpytes: !0
        }));
        return a && (c = c.replace(/\+/g, "-").replace(/\//g, "_")),
        c
    },
    de:function(e, n, a) {
        a && (e = e.replace(/-/g, "+").replace(/_/g, "/"));
        var s = new Crypto.mode.ECB(r.pad.pkcs7)
          , o = Crypto.util.base64ToBytes(e);
          Crypto.charenc.UTF8.stringToBytes(n);
        return Crypto.AES.decrypt(o, t(n), {
            asBpytes: !0,
            mode: s,
            iv: ""
        })
    },
    md5: function(e) {
        var t = Crypto.MD5(e, {
            asBytes: !0
        });
        if (16 !== t.length)
            throw new Error("MD5加密结果字节数组错误");
        var a = Math.abs(n(t, 0))
          , s = Math.abs(n(t, 4))
          , o = Math.abs(n(t, 8))
          , c = Math.abs(n(t, 12));
        return a.toString() + s.toString() + o.toString() + c.toString()
    }
};
data ={
    "spuCode": "SPU116308775836540928",
    "skuCode": "SKU116308775836540928",
    "miniversion": "5273"
};
s = "kEyOA02sa7d8dUYr";
var p = JSON.stringify(data)
console.log(p)
var d ="230101"
var g = Crypto.aes.en(p, s, c=true)
var v = ["cid=".concat(d), "dk=1", "q=".concat(g)]
, m = "d3ccf300-b8f9-496e-98f7-e4cfbef849db1733799978194";
v.push("uid=".concat(m))

// console.log(v)
// console.log(v.sort().join(";") + s)
params=({
    cid: d,
    q: g,
    dk: 1,
    sign: Crypto.aes.md5(v.sort().join(";") + s),
    uid: m
})
console.log(params)
