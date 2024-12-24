window=global;
document={};
const deasync = require('deasync');
const Module =require("./jcap_2020_04_27.min.js")
// 等待 Module['getEncryptData'] 加载
function waitForEncryptDataSync() {
    const start = Date.now();
    while (typeof Module['getEncryptData'] === 'undefined') {
        if (Date.now() - start > 10000) { // 设置超时时间 10 秒
            throw new Error("Timeout waiting for Module['getEncryptData'] to load.");
        }
        deasync.sleep(100); // 每 100 毫秒检查一次
    }
}

var o = function(t, e) {
    var n = i[t -= 0];
    if (void 0 === o.OcTlit) {
        o.cmwhiL = function(t) {
            for (var e = function(t) {
                for (var e, n, r = String(t).replace(/=+$/, ""), i = "", o = 0, a = 0; n = r.charAt(a++); ~n && (e = o % 4 ? 64 * e + n : n,
                o++ % 4) ? i += String.fromCharCode(255 & e >> (-2 * o & 6)) : 0)
                    n = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=".indexOf(n);
                return i
            }(t), n = [], r = 0, i = e.length; r < i; r++)
                n += "%" + ("00" + e.charCodeAt(r).toString(16)).slice(-2);
            console.log(n)
            return decodeURIComponent(n)
        }
        ,
        o.IidJoH = {},
        o.OcTlit = !0
    }
    var r = o.IidJoH[t];
    return void 0 === r ? (n = o.cmwhiL(n),
    o.IidJoH[t] = n) : n = r,
    n
}
var o = function(t, e) {
    var n = i[t -= 0];
    if (void 0 === o.OcTlit) {
        o.cmwhiL = function(t) {
            for (var e = function(t) {
                for (var e, n, r = String(t).replace(/=+$/, ""), i = "", o = 0, a = 0; n = r.charAt(a++); ~n && (e = o % 4 ? 64 * e + n : n,
                o++ % 4) ? i += String.fromCharCode(255 & e >> (-2 * o & 6)) : 0)
                    n = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=".indexOf(n);
                return i
            }(t), n = [], r = 0, i = e.length; r < i; r++)
                n += "%" + ("00" + e.charCodeAt(r).toString(16)).slice(-2);
            return decodeURIComponent(n)
        }
        ,
        o.IidJoH = {},
        o.OcTlit = !0
    }
    var r = o.IidJoH[t];
    return void 0 === r ? (n = o.cmwhiL(n),
    o.IidJoH[t] = n) : n = r,
    n
}
o.OcTlit=true;
o.IidJoH={
    "0": "seq",
    "1": "Mar",
    "2": "ine",
    "3": "ilW",
    "4": "-99",
    "5": "22|",
    "7": "var",
    "9": "26|",
    "10": "ame",
    "11": "ra ",
    "12": "czj",
    "13": "cap",
    "14": "ext",
    "15": "bcd",
    "17": "Cor",
    "18": "unk",
    "20": " ve",
    "21": "Luc",
    "22": "GLR",
    "23": "Buf",
    "24": "U-E",
    "25": "Ena",
    "26": "02,",
    "27": "bui",
    "28": "efg",
    "29": "cTH",
    "30": "2.0",
    "31": "ion",
    "32": "FaW",
    "33": "Sho",
    "35": "rAc",
    "36": "sty",
    "37": "ida",
    "38": "Ver",
    "39": "leG",
    "40": "lSt",
    "41": "plu",
    "42": " Yi",
    "43": "het",
    "44": " Se",
    "45": "TVg",
    "46": "QPI",
    "47": "pri",
    "48": "rra",
    "49": "VEN",
    "50": "Far",
    "51": "und",
    "52": "rce",
    "53": "XtZ",
    "54": "KeB",
    "55": "(25",
    "56": "Con",
    "57": "c2 ",
    "59": "Vvg",
    "61": "app",
    "62": "ont",
    "63": "8|1",
    "65": "med",
    "66": "oor",
    "67": "rAt",
    "68": "glo",
    "70": "ble",
    "71": "0,1",
    "72": "hlj",
    "73": "now",
    "74": "g v",
    "76": "rit",
    "77": "nti",
    "78": "rgb",
    "79": "HBe",
    "80": "ARR",
    "81": "Got",
    "82": "REN",
    "83": "Zoq",
    "84": "234",
    "85": "GUw",
    "86": "YSw",
    "87": "IJJ",
    "88": "rep",
    "89": "ome",
    "90": "_WE",
    "91": "orm",
    "92": "ify",
    "94": "bri",
    "95": "|3|",
    "96": "chr",
    "97": "dBu",
    "98": "-we",
    "100": "KaC",
    "101": "deA",
    "102": "ave",
    "104": "Tho",
    "105": "has",
    "106": "2|1",
    "107": "r N",
    "108": "Cou",
    "109": "Gab",
    "110": "|14",
    "111": "gua",
    "112": "ens",
    "113": "clo",
    "114": "EvR",
    "115": "0, ",
    "116": "Riq",
    "117": "18p",
    "118": "inP",
    "119": "Uni",
    "120": "ikl",
    "121": "Pro",
    "122": "yrU",
    "123": "DER",
    "124": "|35",
    "125": "TLJ",
    "126": "ssy",
    "127": "cTP",
    "128": "oma",
    "129": "te;",
    "130": "Tre",
    "131": "Ayj",
    "132": "ati",
    "133": "er_",
    "135": "lnb",
    "136": "mal",
    "139": "eid",
    "140": "Pri",
    "141": "ldI",
    "142": "ing",
    "143": "|13",
    "144": "NvT",
    "145": "pin",
    "146": "Pos",
    "147": "mem",
    "148": "sha",
    "149": "str",
    "150": "ica",
    "151": "end",
    "152": "ug_",
    "153": "AcP",
    "154": ");}",
    "155": "mDj",
    "156": "cho",
    "157": "FdX",
    "158": "div",
    "159": "for",
    "160": "tfo",
    "161": "FCn",
    "162": " Sa",
    "163": "Ele",
    "164": "som",
    "165": "GHI",
    "166": "lan",
    "167": "men",
    "168": "duB",
    "169": "mUj",
    "170": "use",
    "171": "sBb",
    "172": "max",
    "173": "iDq",
    "174": "qNP",
    "175": "isA",
    "176": "num",
    "180": "89-",
    "181": "|9|",
    "182": "9|9",
    "183": "Sou",
    "184": "mCh",
    "185": "cke",
    "186": "1.0",
    "187": " Ya",
    "188": "oth",
    "189": "vwJ",
    "190": "nat",
    "191": "oft",
    "192": "gTV",
    "193": "|2|",
    "194": "pft",
    "196": "l_P",
    "198": "Reu",
    "199": "STR",
    "200": "DEF",
    "201": "sdf",
    "202": "kie",
    "203": "orD",
    "204": "iLk",
    "205": "ade",
    "206": "23|",
    "207": "27|",
    "208": "Poi",
    "209": "Dro",
    "210": "tur",
    "211": "New",
    "212": "ter",
    "213": "GL_",
    "214": "der",
    "215": "age",
    "216": "joi",
    "218": "mp ",
    "219": "dev",
    "220": "rip",
    "221": "Arr",
    "222": "pti",
    "223": "dan",
    "224": "set",
    "225": "wid",
    "228": "ary",
    "229": "lac",
    "230": "tal",
    "231": "att",
    "232": "edi",
    "233": "ngC",
    "234": "rem",
    "236": "eiI",
    "237": "pus",
    "238": "bod",
    "239": "bol",
    "240": "vas",
    "243": "lef",
    "244": "inl",
    "245": "iBL",
    "246": "|32",
    "247": "VWX",
    "248": "Fre",
    "249": "izZ",
    "250": "pYI",
    "251": "|19",
    "252": "s> ",
    "253": "AlR",
    "255": "pla",
    "256": "anT",
    "257": "dpF",
    "260": "hPK",
    "262": "arC",
    "263": "kPQ",
    "264": "Wid",
    "265": "toS",
    "266": ",25",
    "267": "agC",
    "268": "Dam",
    "269": "pTv",
    "270": "3|3",
    "272": "QmX",
    "273": "fCQ",
    "274": "cod",
    "275": "fil",
    "276": "Ite",
    "277": "dwa",
    "278": " va",
    "280": " ma",
    "281": "mXD",
    "282": "vAl",
    "283": "cti",
    "284": "yyV",
    "285": "VER",
    "286": "qPp",
    "287": "xVu",
    "288": "ath",
    "289": "vil",
    "290": "hhX",
    "291": "CHM",
    "292": "idt",
    "293": "Cyj",
    "295": "rte",
    "296": "tex",
    "297": " Sc",
    "298": "6|1",
    "299": "|5|",
    "300": "p F",
    "302": "MrN",
    "303": "cha",
    "304": "ngs",
    "305": "JgN",
    "306": "nbu",
    "307": "ubZ",
    "308": "s M",
    "309": "qrs",
    "310": "GME",
    "311": "ITC",
    "312": "fro",
    "313": "rCo",
    "314": "Hei",
    "315": "eri",
    "316": "5,0",
    "317": "lLa",
    "318": "ADE",
    "319": "fse",
    "320": "Att",
    "322": "inf",
    "323": "nTV",
    "324": "ght",
    "325": "seP",
    "326": "arc",
    "327": "Bas",
    "328": "mLo",
    "329": "24|",
    "330": "|11",
    "331": "IAD",
    "332": "Scr",
    "334": "Wrc",
    "335": "JmM",
    "337": "igh",
    "338": "Typ",
    "339": "|15",
    "340": "oTh",
    "341": "yle",
    "342": "tio",
    "343": "9|1",
    "344": "len",
    "345": "ory",
    "346": "Enc",
    "348": "n O",
    "349": "typ",
    "350": "mbo",
    "351": "syw",
    "352": "eSh",
    "353": "XET",
    "354": "dis",
    "355": "drW",
    "356": "cur",
    "357": "dvn",
    "358": "tri",
    "360": "Dez",
    "361": "Ope",
    "362": "dri",
    "364": "Tou",
    "365": "Seg",
    "366": "DEy",
    "367": "efi",
    "368": "web",
    "369": "TSs",
    "370": "ach",
    "371": "Boo",
    "372": "iti",
    "373": "fEx",
    "374": "-sy",
    "375": "pre",
    "376": "AXE",
    "377": "ual",
    "378": "siv",
    "379": "15|",
    "382": "wxy",
    "383": "MLP",
    "384": "gin",
    "385": "oty",
    "386": "trV",
    "387": "ate",
    "388": "7|6",
    "389": "yeb",
    "390": "ren",
    "392": "laS",
    "393": "tim",
    "394": "tiv",
    "395": "gth",
    "396": "ite",
    "397": "Chi",
    "398": "get",
    "399": "toD",
    "400": "ept",
    "401": "Pix",
    "402": "siz",
    "403": "TzA",
    "404": "rib",
    "405": "HCK",
    "406": "deb",
    "407": "Ejv",
    "408": "Xfb",
    "409": "spl",
    "410": "ace",
    "411": "Tim",
    "412": "oe ",
    "413": "Fea",
    "414": "mil",
    "415": " Mo",
    "416": "000",
    "417": "hic",
    "418": "cre",
    "419": "lmj",
    "420": "WEB",
    "421": "ec4",
    "422": "Tex",
    "423": "GGG",
    "424": "UNM",
    "425": "mSi",
    "426": "6|0",
    "427": "ngu",
    "428": "e e",
    "429": "EkJ",
    "430": "|10",
    "431": "AY_",
    "432": "lcu",
    "433": "KLD"
}
function p(t, e) {
    var n = function(t, e) {
        return o(t - "0x323", e)
    }
      , r = function(t, e) {
        return o(t - "0x323", e)
    }
      , i = {
        mDjJH: function(t, e) {
            return t << e
        },
        ZdUuO: function(t, e) {
            return t < e
        },
        cFWgd: function(t, e) {
            return t - e
        },
        ANEuq: function(t, e) {
            return t > e
        }
    };
    i[n("0x3b3") + "GQ"] = function(t, e) {
        return t < e
    }
    ,
    i[n("0x4bb") + "gU"] = function(t, e) {
        return t & e
    }
    ,
    i.pdIJp = function(t, e) {
        return t >>> e
    }
    ;
    var a = i
      , c = t["len" + r("0x4ae")]
      , s = a[r("0x3be") + "JH"](c, 2);
    if (e) {
        var u = t[c - 1];
        if (s -= 4,
        a.ZdUuO(u, a.cFWgd(s, 3)) || a.ANEuq(u, s))
            return null;
        s = u
    }
    for (var f = 0; a.NvTGQ(f, c); f++)
        t[f] = String["fro" + n("0x3db") + "arCode"](a[r("0x4bb") + "gU"](t[f], 255), 255 & a.pdIJp(t[f], 8), t[f] >>> 16 & 255, t[f] >>> 24 & 255);
    var l = t.join("");
    return e ? l.substring(0, s) : l
}
function v(t, e, n) {
    var r = function(t, e) {
        return o(t - "0x79", e)
    }
      , i = {};
    i[function(t, e) {
        return o(t - "0x79", e)
    }("0x121") + "GJ"] = function(t) {
        return t()
    }
    ,
    i.gTVbn = function(t, e) {
        return t & e
    }
    ,
    i.cTHvA = function(t, e, n, r, i, o, a, c) {
        return t(e, n, r, i, o, a, c)
    }
    ,
    i.YAzCo = function(t, e, n, r, i, o, a, c) {
        return t(e, n, r, i, o, a, c)
    }
    ;
    var a, c, s, u, f, l, d = i, h = t[r("0x1d1") + r("0x204")], p = h - 1;
    for (c = t[p],
    s = 0,
    l = 0 | Math.floor(6 + 52 / h); l > 0; --l) {
        for (s = g(s + d.duBGJ(x)),
        u = d[r("0x139") + "bn"](s >>> 2, 3),
        f = 0; f < p; ++f)
            a = t[f + 1],
            c = t[f] = g(t[f] + d[r("0x96") + "vA"](m, s, a, c, f, u, e, n));
        a = t[0],
        c = t[p] = g(t[p] + d.YAzCo(m, s, a, c, p, u, e, n))
    }
    return t
}
function w(t, e) {
    var n = function(t, e) {
        return o(t - -194, e)
    }
      , r = {
        lCviv: function(t, e) {
            return t >> e
        }
    };
    r[n("0x71") + "Km"] = function(t, e) {
        return t << e
    }
    ;
    var i, a = r, c = t.length, s = a.lCviv(c, 2);
    0 != (3 & c) && ++s,
    e ? (i = new Array(s + 1))[s] = c : i = new Array(s);
    for (var u = 0; u < c; ++u)
        i[u >> 2] |= a.ubZKm(t.charCodeAt(u), a[n("0x71") + "Km"](3 & u, 3));
    return i
}
function _(t) {
    var e = function(t, e) {
        return o(t - "0x211", e)
    };
    return t.length < 4 && (t[e("0x369") + e("0x39c")] = 4),
    t
}
function g(t) {
    return 4294967295 & t
}
function x() {
    var t = {};
    return t.QsOVK = "MTU0Mjk2N" + function(t, e) {
        return o(t - "0x248", e)
    }("0x3b6") + "OQ",
    1111471640 + parseInt(y(t.QsOVK))
}
function y(t) {
    var e = function(t, e) {
        return o(t - "0x2c", e)
    }
      , n = function(t, e) {
        return o(t - "0x2c", e)
    }
      , r = {};
    r[e("0x133") + "Xi"] = function(t, e) {
        return t - e
    }
    ,
    r[n("0x130") + "sH"] = function(t, e) {
        return t + e
    }
    ,
    r.XgTDg = function(t, e) {
        return t >> e
    }
    ,
    r.drWLi = function(t, e) {
        return t < e
    }
    ,
    r.pTvwW = function(t, e) {
        return t & e
    }
    ,
    r.kRnVo = function(t, e) {
        return t >> e
    }
    ,
    r[n("0x1a4") + "Ol"] = function(t, e) {
        return t & e
    }
    ;
    var i, a, c, s, u, f, l, d, h, p, v = r, g = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1];
    if (l = t[n("0x184") + "gth"],
    t = (t += Array(5 - l % 4)[e("0x104") + "n"]("=")).replace(/\-/g, "+")[n("0x84") + e("0x111") + "e"](/\_/g, "/"),
    /[^ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\+\/\=]/.test(t))
        return "";
    for (h = l,
    (d = "=" == t["cha" + e("0x6f")](l - 2) ? 1 : "=" == t[n("0x15b") + "rAt"](v.kPQXi(l, 1)) ? 2 : 0) > 0 && (h -= 4),
    h = v[e("0x130") + "sH"](3 * v.XgTDg(h, 2), d),
    p = new Array(h),
    u = f = 0; v[e("0x18f") + "Li"](u, l) && -1 != (i = g[t.charCodeAt(u++)]) && -1 != (a = g[t["charCo" + n("0x91") + "t"](u++)]) && (p[f++] = String.fromCharCode(i << 2 | (48 & a) >> 4),
    -1 != (c = g[t.charCodeAt(u++)])) && (p[f++] = String.fromCharCode(v[n("0x139") + "wW"](a, 15) << 4 | v.kRnVo(60 & c, 2)),
    -1 != (s = g[t[e("0x15b") + "rCodeAt"](u++)])); )
        p[f++] = String[n("0x164") + "mCh" + n("0x132") + "ode"](v.AXEOl(c, 3) << 6 | s);
    return p.join("")
}
function m(t, e, n, r, i, a, c) {
    var s = function(t, e) {
        return o(t - "0xd8", e)
    }
      , u = {
        qNPpO: function(t, e) {
            return t - e
        }
    };
    u[s("0x1e8") + "nj"] = function(t, e) {
        return t >>> e
    }
    ,
    u.FKQrE = function(t, e) {
        return t & e
    }
    ,
    u.PGTAt = function(t, e) {
        return t & e
    }
    ,
    u.lcuPp = function(t, e) {
        return t ^ e
    }
    ,
    u.vUugl = function(t, e) {
        return t >>> e
    }
    ,
    u.dtMtv = function(t, e) {
        return t + e
    }
    ;
    var f = u
      , l = f[s("0x186") + "pO"](c, 25700);
    if (1 == f.QmXnj(l, 16)) {
        var d = 7 & f.QmXnj(l, 12)
          , h = f.FKQrE(l >>> 8, 7)
          , p = l >>> 4 & 7
          , v = f.PGTAt(l, 7);
        return f.lcuPp(b(t, e, n, r, i, a), (f.vUugl(e, d) ^ n << h) + f[s("0x288") + "Pp"](t >>> p & 63, f.dtMtv(n, e) >>> (f.qNPpO(7, v) >>> 1) & 63))
    }
    return b(t, e, n, r, i, a)
}
function b(t, e, n, r, i, o) {
    var a = {
        aa: function(t, e) {
            return t ^ e
        },
        bb: function(t, e) {
            return t + e
        },
        cc: function(t, e) {
            return t << e
        },
        dd: function(t, e) {
            return t >>> e
        }
    };
    return a.aa(a.bb(a.aa(n >>> 5, a.cc(e, 2)), a.aa(a.dd(e, 3), a.cc(n, 4))), (t ^ e) + (o[a.aa(3 & r, i)] ^ n))
}
function l(t) {
                var e = function(t, e) {
                    return o(t - "0x26d", e)
                }
                  , n = function(t, e) {
                    return o(t - "0x26d", e)
                }
                  , r = {};
                r[e("0x38f") + "MD"] = function(t, e) {
                    return t << e
                }
                ,
                r.HDFem = function(t, e) {
                    return t + e
                }
                ,
                r.xMlmP = function(t, e) {
                    return t >> e
                }
                ,
                r.BCXAB = function(t, e) {
                    return t & e
                }
                ,
                r[e("0x28d") + "AT"] = function(t, e) {
                    return t | e
                }
                ,
                r[n("0x2a3") + "fP"] = function(t, e) {
                    return t / e
                }
                ,
                r[e("0x3ce") + "hb"] = function(t, e) {
                    return t % e
                }
                ;
                for (var i = r, a = ("0|1|4|8|6|9|5|10|7" + e("0x2cc") + "2|11").split("|"), c = 0; ; ) {
                    switch (a[c++]) {
                    case "0":
                        var s = ("ABC" + e("0x335") + n("0x312") + "JKLMNOPQRSTU" + n("0x364") + "YZa" + n("0x27c") + e("0x289") + "hijklmnop" + e("0x3a2") + "tuv" + n("0x3eb") + "z01" + n("0x2c1") + "567" + e("0x321") + "_")[n("0x406") + "it"]("");
                        continue;
                    case "1":
                        var u, f, l, d, h, p, v;
                        continue;
                    case "2":
                        1 == h ? (v = t[e("0x39c") + "rCodeAt"](f++),
                        u[l++] = s[v >> 2] + s[i[e("0x38f") + "MD"](3 & v, 4)]) : 2 == h && (v = t["cha" + e("0x3a6") + "deAt"](f++) << 8 | t["cha" + e("0x3a6") + "deAt"](f++),
                        u[l++] = i.HDFem(s[i.xMlmP(v, 10)], s[v >> 4 & 63]) + s[i.BCXAB(v, 15) << 2]);
                        continue;
                    case "3":
                        for (; f < d; )
                            v = i[n("0x28d") + "AT"](t.charCodeAt(f++) << 16 | t["cha" + n("0x3a6") + "deAt"](f++) << 8, t[n("0x39c") + e("0x3a6") + "deAt"](f++)),
                            u[l++] = i.HDFem(i.HDFem(s[v >> 18], s[i.BCXAB(v >> 12, 63)]) + s[v >> 6 & 63], s[63 & v]);
                        continue;
                    case "4":
                        f = l = 0;
                        continue;
                    case "5":
                        p = i[e("0x2a3") + "fP"](d, 3) << 2;
                        continue;
                    case "6":
                        h = i.XEThb(d, 3);
                        continue;
                    case "7":
                        u = new Array(p);
                        continue;
                    case "8":
                        d = t[n("0x3c5") + "gth"];
                        continue;
                    case "9":
                        d -= h;
                        continue;
                    case "10":
                        h > 0 && (p += 4);
                        continue;
                    case "11":
                        return u.join("")
                    }
                    break
                }
            }
function h(t) {
    var e = function(t, e) {
        return o(t - -778, e)
    }
      , n = function(t, e) {
        return o(t - -778, e)
    }
      , r = {
        RNcsD: function(t, e) {
            return t < e
        },
        WPEgW: function(t, e) {
            return t >> e
        },
        kcHQJ: function(t, e) {
            return t | e
        }
    };
    r[e(-405) + "ve"] = function(t, e) {
        return t & e
    }
    ,
    r[n(-375) + "aH"] = function(t, e) {
        return t <= e
    }
    ,
    r.uaVpl = function(t, e) {
        return t << e
    }
    ,
    r[e(-443) + "RH"] = function(t, e) {
        return t & e
    }
    ,
    r.izwEa = function(t, e) {
        return t & e
    }
    ,
    r[e(-496) + "aU"] = "Mal" + n(-619) + e(-713) + " string";
    var i = r;
    if (/^[\x00-\x7f]*$captcha/.test(t))
        return t;
    for (var a = [], c = t.length, s = 0, u = 0; i.RNcsD(s, c); ++s,
    ++u) {
        var f = t[n(-475) + e(-465) + "deAt"](s);
        if (f < 128)
            a[u] = t.charAt(s);
        else if (f < 2048)
            a[u] = String[e(-466) + e(-594) + "arCode"](192 | i.WPEgW(f, 6), 128 | 63 & f);
        else {
            if (!(f < 55296 || f > 57343)) {
                if (s + 1 < c) {
                    var l = t.charCodeAt(s + 1);
                    if (i.RNcsD(f, 56320) && l >= 56320 && i[n(-375) + "aH"](l, 57343)) {
                        var d = 65536 + (i.uaVpl(1023 & f, 10) | i.JmMRH(l, 1023));
                        a[u] = String.fromCharCode(240 | 63 & i[n(-477) + "gW"](d, 18), 128 | 63 & i.WPEgW(d, 12), 128 | d >> 6 & 63, 128 | i[n(-599) + "Ea"](d, 63)),
                        ++s;
                        continue
                    }
                }
                throw new Error(i.vAlaU)
            }
            a[u] = String["fro" + e(-594) + e(-516) + "ode"](i.kcHQJ(224, f >> 12), 128 | f >> 6 & 63, 128 | i.fExve(f, 63))
        }
    }
    return a.join("")
}
function d(t, e, n) {
    var r = function(t, e) {
        return o(t - -524, e)
    }
      , i = {
        Wrcde: function(t, e) {
            return t === e
        },
        gOvIv: function(t, e) {
            return t === e
        }
    };
    i[r(-101) + "Dw"] = function(t, e) {
        return h(e)
    }
    ;
    var a = i;
    return void 0 === t || a[r(-190) + "de"](t, null) || a.gOvIv(t["len" + function(t, e) {
        return o(t - -524, e)
    }(-129)], 0) ? t : (t = a[r(-101) + "Dw"](h, t),
    e = h(e),
    p(v(w(t, !0), _(w(e, !1)), n), !1))
}
function f(t, e) {
    return l(d(t, e, c=99992))
}
function pt(t, e, n) {
    var r = t
      , i = "E736B80A35290F193C2034A8021CC63B";
    e && (c = e);
    try {
        waitForEncryptDataSync(); // 确保加载完成
        return n ? JSON.stringify(Module['getEncryptData'](r, n)) : f(r, i)
    } catch (t) {
        return f(r, i)
    }

}
function vt(t) {
    for (var e = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], n = "", r = 0; r < t; r++) {
        n += e[Math.floor(35 * Math.random())]
    }
    return n
}
// var i = "YzymcgACAAAAAAPgl4IAMDkuIzA7vfs_MYdwL7h06ozMXx2gBkrmFKxrS5psa6yILONZPls1hrQBD3i_QMrL5QAAAAA"
// , _o = "B4qJXCc15Pe9mvAU"
// , _f = "23130303037303236454145424647333930364347354831453137323142373636383333363233303033333234454636454541433246344546333730344346493333373831483530334233303035313030303"

// , _l = {};
// _l.nonce = vt(16)
// _l.token = _o,
// _l.sid = i;
// var _d = _l,
// _h = {};
// _h.si = i,
// _h['version'] = 2,
// _h.se = pt(JSON.stringify(_d), null, _f),
// _h.lang = 1,
// _h.client = 'm',
// _h.type = 0;
// console.log(_l)
// console.log(_h)

function generateRequestData(sessionId, token, secretKey) {
    var requestData = {};
    requestData.nonce = vt(16);  // Assuming vt(16) generates a nonce
    requestData.token = token;
    requestData.sid = sessionId;
    
    var data = requestData;
    var params = {};
    params.si = sessionId;
    params['version'] = 2;
    params.se = pt(JSON.stringify(data), null, secretKey);  // Assuming pt is a predefined function
    params.lang = 1;
    params.client = 'm';
    params.type = 0;
    
    return params ;
}
// console.log(generateRequestData(i,_o,_f))
