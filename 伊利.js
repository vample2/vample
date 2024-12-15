const CryptoJS = require('crypto-js');
// Crypto ={
//     "AES":{
//         encrypt: function(e, r, i) {
            
//             return d_encrypt.encrypt(t, e, r, i)
//         },
//         decrypt: function(e, r, i) {
//             return d_encrypt.decrypt(t, e, r, i)
//         }
//     },
//     "enc":{
//         Latin1 : {
//             stringify: function(t) {
//                 var e = t.words;
//                 t = t.sigBytes;
//                 for (var r = [], i = 0; i < t; i++)
//                     r.push(String.fromCharCode(e[i >>> 2] >>> 24 - i % 4 * 8 & 255));
//                 return r.join("")
//             },
//             parse: function(t) {
//                 for (var e = t.length, r = [], i = 0; i < e; i++)
//                     r[i >>> 2] |= (255 & t.charCodeAt(i)) << 24 - i % 4 * 8;
//                 return new o_WordArray.init(r,e)
//             }
//         }
//     },
//     "mode":{
//         "CBC":{}
        
//     },
//     "pad":{
//         "Pkcs7":{}
//     }
// }

var d_encrypt={

    encrypt: function(t, e, r, i) {

    },
    decrypt: function(t, e, r, i) {
    },
    _parse: function(t, e) {
    }
}
o_WordArray={
    init: function(t, e) {
        t = this.words = t || [],
        this.sigBytes = null != e ? e : 4 * t.length
    },
    toString: function(t) {
        return (t || a).stringify(this)
    },
    concat: function(t) {
        var e = this.words
          , r = t.words
          , i = this.sigBytes;
        if (t = t.sigBytes,
        this.clamp(),
        i % 4)
            for (var n = 0; n < t; n++)
                e[i + n >>> 2] |= (r[n >>> 2] >>> 24 - n % 4 * 8 & 255) << 24 - (i + n) % 4 * 8;
        else if (65535 < r.length)
            for (n = 0; n < t; n += 4)
                e[i + n >>> 2] = r[n >>> 2];
        else
            e.push.apply(e, r);
        return this.sigBytes += t,
        this
    },
    clamp: function() {
        var e = this.words
          , r = this.sigBytes;
        e[r >>> 2] &= 4294967295 << 32 - r % 4 * 8,
        e.length = t.ceil(r / 4)
    },
    clone: function() {
        var t = s.clone.call(this);
        return t.words = this.words.slice(0),
        t
    },
    random: function(e) {
        for (var r = [], i = 0; i < e; i += 4)
            r.push(4294967296 * t.random() | 0);
        return new o.init(r,e)
    }
}
function r(n, e) {
    var r = (65535 & n) + (65535 & e);
    return (n >> 16) + (e >> 16) + (r >> 16) << 16 | 65535 & r
}
function t(n, e, t, o, u, f) {
    return r((f = r(r(e, n), r(o, f))) << u | f >>> 32 - u, t)
}
function o(n, e, r, o, u, f, c) {
    return t(e & r | ~e & o, n, e, u, f, c)
}
function u(n, e, r, o, u, f, c) {
    return t(e & o | r & ~o, n, e, u, f, c)
}
function f(n, e, r, o, u, f, c) {
    return t(e ^ r ^ o, n, e, u, f, c)
}
function c(n, e, r, o, u, f, c) {
    return t(r ^ (e | ~o), n, e, u, f, c)
}
function a(n) {
    var e = [];
    for (e[(n.length >> 2) - 1] = void 0,
    t = 0; t < e.length; t += 1)
        e[t] = 0;
    for (var r = 8 * n.length, t = 0; t < r; t += 8)
        e[t >> 5] |= (255 & n.charCodeAt(t / 8)) << t % 32;
    // console.log(e)
    // console.log(e.length)
    return e
}
function l(n) {
    return unescape(encodeURIComponent(n))
}
function i(n, e) {
    var t, i, d, a;
    n[e >> 5] |= 128 << e % 32,
    n[14 + (e + 64 >>> 9 << 4)] = e;
    for (var h = 1732584193, l = -271733879, v = -1732584194, g = 271733878, m = 0; m < n.length; m += 16)
        h = o(t = h, i = l, d = v, a = g, n[m], 7, -680876936),
        g = o(g, h, l, v, n[m + 1], 12, -389564586),
        v = o(v, g, h, l, n[m + 2], 17, 606105819),
        l = o(l, v, g, h, n[m + 3], 22, -1044525330),
        h = o(h, l, v, g, n[m + 4], 7, -176418897),
        g = o(g, h, l, v, n[m + 5], 12, 1200080426),
        v = o(v, g, h, l, n[m + 6], 17, -1473231341),
        l = o(l, v, g, h, n[m + 7], 22, -45705983),
        h = o(h, l, v, g, n[m + 8], 7, 1770035416),
        g = o(g, h, l, v, n[m + 9], 12, -1958414417),
        v = o(v, g, h, l, n[m + 10], 17, -42063),
        l = o(l, v, g, h, n[m + 11], 22, -1990404162),
        h = o(h, l, v, g, n[m + 12], 7, 1804603682),
        g = o(g, h, l, v, n[m + 13], 12, -40341101),
        v = o(v, g, h, l, n[m + 14], 17, -1502002290),
        h = u(h, l = o(l, v, g, h, n[m + 15], 22, 1236535329), v, g, n[m + 1], 5, -165796510),
        g = u(g, h, l, v, n[m + 6], 9, -1069501632),
        v = u(v, g, h, l, n[m + 11], 14, 643717713),
        l = u(l, v, g, h, n[m], 20, -373897302),
        h = u(h, l, v, g, n[m + 5], 5, -701558691),
        g = u(g, h, l, v, n[m + 10], 9, 38016083),
        v = u(v, g, h, l, n[m + 15], 14, -660478335),
        l = u(l, v, g, h, n[m + 4], 20, -405537848),
        h = u(h, l, v, g, n[m + 9], 5, 568446438),
        g = u(g, h, l, v, n[m + 14], 9, -1019803690),
        v = u(v, g, h, l, n[m + 3], 14, -187363961),
        l = u(l, v, g, h, n[m + 8], 20, 1163531501),
        h = u(h, l, v, g, n[m + 13], 5, -1444681467),
        g = u(g, h, l, v, n[m + 2], 9, -51403784),
        v = u(v, g, h, l, n[m + 7], 14, 1735328473),
        h = f(h, l = u(l, v, g, h, n[m + 12], 20, -1926607734), v, g, n[m + 5], 4, -378558),
        g = f(g, h, l, v, n[m + 8], 11, -2022574463),
        v = f(v, g, h, l, n[m + 11], 16, 1839030562),
        l = f(l, v, g, h, n[m + 14], 23, -35309556),
        h = f(h, l, v, g, n[m + 1], 4, -1530992060),
        g = f(g, h, l, v, n[m + 4], 11, 1272893353),
        v = f(v, g, h, l, n[m + 7], 16, -155497632),
        l = f(l, v, g, h, n[m + 10], 23, -1094730640),
        h = f(h, l, v, g, n[m + 13], 4, 681279174),
        g = f(g, h, l, v, n[m], 11, -358537222),
        v = f(v, g, h, l, n[m + 3], 16, -722521979),
        l = f(l, v, g, h, n[m + 6], 23, 76029189),
        h = f(h, l, v, g, n[m + 9], 4, -640364487),
        g = f(g, h, l, v, n[m + 12], 11, -421815835),
        v = f(v, g, h, l, n[m + 15], 16, 530742520),
        h = c(h, l = f(l, v, g, h, n[m + 2], 23, -995338651), v, g, n[m], 6, -198630844),
        g = c(g, h, l, v, n[m + 7], 10, 1126891415),
        v = c(v, g, h, l, n[m + 14], 15, -1416354905),
        l = c(l, v, g, h, n[m + 5], 21, -57434055),
        h = c(h, l, v, g, n[m + 12], 6, 1700485571),
        g = c(g, h, l, v, n[m + 3], 10, -1894986606),
        v = c(v, g, h, l, n[m + 10], 15, -1051523),
        l = c(l, v, g, h, n[m + 1], 21, -2054922799),
        h = c(h, l, v, g, n[m + 8], 6, 1873313359),
        g = c(g, h, l, v, n[m + 15], 10, -30611744),
        v = c(v, g, h, l, n[m + 6], 15, -1560198380),
        l = c(l, v, g, h, n[m + 13], 21, 1309151649),
        h = c(h, l, v, g, n[m + 4], 6, -145523070),
        g = c(g, h, l, v, n[m + 11], 10, -1120210379),
        v = c(v, g, h, l, n[m + 2], 15, 718787259),
        l = c(l, v, g, h, n[m + 9], 21, -343485551),
        h = r(h, t),
        l = r(l, i),
        v = r(v, d),
        g = r(g, a);
    return [h, l, v, g]
}
function d(n) {
    for (var e = "", r = 32 * n.length, t = 0; t < r; t += 8)
        e += String.fromCharCode(n[t >> 5] >>> t % 32 & 255);
    return e
}
function v(n) {
    return d(i(a(n = l(n)), 8 * n.length))
}
function h(n) {
    for (var e, r = "0123456789abcdef", t = "", o = 0; o < n.length; o += 1)
        e = n.charCodeAt(o),
        t += r.charAt(e >>> 4 & 15) + r.charAt(15 & e);
    return t
}
function m(n, e, r) {
    console.log(n)
    return e ? r ? g(e, n) : h(g(e, n)) : r ? v(n) : h(v(n))
}

var i_Crypto ={
    encrypt: function(t, e, i) {
        
        return CryptoJS.AES.encrypt(t, CryptoJS.enc.Latin1.parse(e), {
            iv: CryptoJS.enc.Latin1.parse(i),
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }).toString()
    },
    decrypt: function(t, e, i) {
        return r.AES.decrypt(t, r.enc.Latin1.parse(e), {
            iv: r.enc.Latin1.parse(i),
            padding: r.pad.Pkcs7
        }).toString(r.enc.Utf8)
    }
};
var a_encrypt ={
    saltedHash1 : function(e) {
        return m(e)
    },
    aesEncrypt : function(e) {
        console.log(e)
        var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "asdvbnqwer!=564av8952116lkouytb+"
          , r = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : "Y9uR16ByteIvH8q9"
          , n = i_Crypto.encrypt(e, t, r);
        return n
    },
    encryptText : function(e) {
        return s.encrypt(e)
    }

};



var r_EncryptText ={
    getEncryptText: function(f, d, s) {
        var F = f + {
            1: "465QQ4546546541W545192!jkaasQeqw`erzR2`xcvdasfasdfzxEcadfafzafwaaadaweoi897as8dfw8af7r8t78g4za78qqfd878000df8/er78a",
            2: "465454654654154`251A92!jkaaseqw891r8zasd8f9Ewaa451AQa4qfRds5aR4q45adaw11eoi897as8dfw8af7r8t78g4za78qqfd878000df8/erASDF",
            3: "4654!qwe5549543asdf`qw1236s12w2w3f2b6y6s2v6e14qw63d346546541211545192!jkaaseqw891r8zasd8f9waa45a4qfddf8/erQp",
            4: "4654!qwe78ASFQ8WQR7Z87Q8VFCZXVSDFGasdfqw1236sw2w3fSADF5465411545192!jkaaseqw891r8zasd8f9waa45a4qfddf8/PLJHGYHGHJASDF",
            5: "9659!qwe78ASFQASDF7Z87Q8121DFGasdfqw1212F54654115ASDFjka1212ASDF1r8zasd8f9waaASDFqfdASDFf8/PLJHGYHGHJASDF",
            6: "0619!qSA1we178ASFQASDF7Z87Q8ASDF1121212FGasdfqw1212546541AEWRQDf5ASDFjka121ASDF1r8zasd8f9ASDFDFqfdASDFf8/PLJHGYHG1212",
            7: "@0866!qSA1wASDFe178AWE121SFQA2SDF7Z8@1237Q8ASDF5469891514512FGasdfqw1212546784541665241AEWRQDf5ASDFjka121FDFqfdASDFf8/",
            8: "1262!qSA5468@e178AWE121SFQA2SDF7Z81237Q8A898912169891514512FGasdSDASDFCGHAWQ1212546784541665241AEWRQDf5ASDFjka121FDF&",
            9: "0866!qSA1wASDFe178AWE121SFQA2SDF7Z81237Q8ASDF1129854@91514512FGasdfqw1212546784541665241AEWRQDf5ASDFjka121FDFqfdASDFf!",
            10: "@465#QQ89898546546541W545192!jkaasASDFqw`erzR2`xcvdasfaEARcadfafzafwaaadaweoi897as8dfw8af7r8t78g4za78!!!@#000df8/er78a"
        }[s]
          , e = (0,
            a_encrypt.saltedHash1)(F).toUpperCase();
        return 1 == d ? (0,
            a_encrypt.encryptText)(e) : 2 == d ? (0,
                a_encrypt.encryptText)((0,
                    a_encrypt.saltedHash1)(e).toUpperCase()) : 3 == d ? (0,
                        a_encrypt.saltedHash1)(e).toUpperCase() : 4 == d ? (0,
                            a_encrypt.encryptText)(F) : e
    },
    getLoginEncryptText: function(f, d, s) {
        var F = f + {
            1: "963QQ45465465xcvdasfasdfzxEcadfafzafoi897as8dfw8g4za78qqfd878000df8/er78a",
            2: "363QQ45465465xcvdas89!safzafwa36paweoi897as8dfw8g4za78qqfd878000df8/er89b",
            3: "763Qi45895465xcv89as89!sa2616wa36paweoi897as8dfw8g4za78qqfd878000df8/eqr23b",
            4: "7531Qi45891546115xcv89as819!sa26161wa36pa81g4z1a78qqfd87810001df18/eqr213b",
            5: "3f53f1Qia4f5f91546fa115axcvfff89asf819!saff26161fwa36fpa81g4z1fa7/eqr21f3b",
            6: "egf513gf1Qifag4f5f9f154g6fa115afxgcvffgf89gasgf8g19!saffg2g6161gfg6fpa@g1g",
            7: "2e@gf513g2f1Qif@ag4!f5f92f215!4g6fa115afxgcvffgf89gasgf82g19!2gfwa3g62fpa2",
            8: "6e@!gf514g2fb1Qif@!bag41f89gasbgf8b2g19!2gfwa3gb62fbpa@g1g32b9999!",
            9: "6a@!gf514g2fb1Qif@!bag41f89gasbgf8b2g19!2gfwa3gb62fbpa@g1g32b9869!++3",
            10: "2e@gf513g2f1Qif@ag4!sdfzxEcadfafzafoi897as8dfw8g4za78qqfd8780df8==/er78a"
        }[s]
          , e = (0,
            a_encrypt.saltedHash1)(F).toUpperCase();
        return 1 == d ? (0,
            a_encrypt.aesEncrypt)(e) : 2 == d ? (0,
                a_encrypt.saltedHash1)(e).toUpperCase() : 3 == d ? (0,
                    a_encrypt.saltedHash1)((0,
                        a_encrypt.aesEncrypt)(F)).toUpperCase() : 4 == d ? (0,
                            a_encrypt.aesEncrypt)((0,
                                a_encrypt.aesEncrypt)(F)) : e
    }
}


// var t_n = Date.now(), 
// o_d = Date.now() + "&" + String(Math.floor(1e5 + 9e5 * Math.random()))
// , c_c = "timeStamp:".concat(t_n, "&uniqueCode:").concat(o_d)
// , type = 4
// , type2 = 10
// console.log(c_c)
// s = (0,
//     r_EncryptText.getLoginEncryptText)(c_c, type, type2);
// console.log(s)
//type1,type2请求获得，openid
function generateSignature(timestamp,type1,type2) {
    var t_n = timestamp, 
    o_d = timestamp + "&" + String(Math.floor(1e5 + 9e5 * Math.random()))
    , c_c = "timeStamp:".concat(t_n, "&uniqueCode:").concat(o_d)
    , type = type1
    , type2 = type2
    console.log(c_c)
    s = (0,
        r_EncryptText.getLoginEncryptText)(c_c, type, type2);

    return {signature:s,uniqueCode:o_d};
}
