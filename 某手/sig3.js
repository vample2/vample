const r = require('./manifest.d92e276e.js')


const CryptoJS = require('crypto-js');
function md5Hash(data) {
    return CryptoJS.MD5(data).toString();
}

function u(e, t=!0) {
    return "object" !== typeof e ? [] : Object.keys(e).sort(( (e, a) => e === a ? 0 : t ? e > a ? 1 : -1 : e > a ? -1 : 1))
}
const p = e => u(e).reduce(( (t, a) => t + a + "=" + encodeURI(e[a])), "");
function m(e, t, a) {
    let o = {
        ...a
    }
      , i = "";
    switch (e) {
    case "form-data":
        o = {
            ...o,
            ...t
        };
        break;
    case "json":
        i = `${JSON.stringify(t)}`;
        break;
    default:
        break
    }
    const s = p(o) + i;
    return md5Hash(s)
}



function sig3(cookie){
    var api_ph;
    const parts = cookie.split(';');
    for (let part of parts) {
        part = part.trim();  // 去除多余的空格
        if (part.startsWith('kuaishou.web.cp.api_ph=')) {
            api_ph=part.split('=')[1];  // 提取 'kuaishou.web.cp.api_ph' 的值
        }
    }
    console.log(api_ph)
    const e='json';
    const t={
        "kuaishou.web.cp.api_ph": api_ph
    };
    const a={};
    const o = m(e, t, a);
    console.log(o)
    i = r(75407)
    s = r.n(i)
    // console.log(s)
    s().call("$encode", [o, {
        suc: function(t) {
            result = t; // 成功时将数据存储
        },
        err: function(e) {
            result = e; // 错误时将错误存储
        }
    }]);

    return result; // 返回结果（可能是数据或错误）
}

cookie='kuaishou.web.cp.api_ph=2af5a2f5c8befbd40d1d934d0f6'
console.log(sig3(cookie))


// function sig3() {
//     return new Promise((resolve, reject) => {
//         const e = 'json';
//         const t = {
//             "kuaishou.web.cp.api_ph": "2af5a2f5c8175dbe296befbd40d1d934d0f6"
//         };
//         const a = {};
        
//         const o = m(e, t, a);
//         console.log(o); // 可选的日志输出

//         const i = r(75407);
//         const s = r.n(i);

//         s().call("$encode", [o, {
//             suc: function(t) {
//                 resolve(t); // 成功时返回数据
//             },
//             err: function(e) {
//                 reject(e); // 发生错误时返回错误信息
//             }
//         }]);
//     });
// }

// // 调用 sig3 并处理结果，确保通过标准输出返回结果
// sig3().then(result => {
//     process.stdout.write(JSON.stringify({ result: result }) + '\n'); // 输出结果
// }).catch(error => {
//     process.stdout.write(JSON.stringify({ error: error }) + '\n'); // 输出错误信息
// });
