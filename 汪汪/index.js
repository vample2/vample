
window ={
    
};
const fetch = require('node-fetch');

let pa = async (t) => {
    
    let T;
    const R = new Array(128).fill(void 0);
    function o(e) {
        return R[e]
    }
    R.push(void 0, null, !0, !1);
    let W = R.length;
    function f(e) {
        W === R.length && R.push(R.length + 1);
        const t = W;
        return W = R[t],
        R[t] = e,
        t
    }
    function ct(e) {
        const t = o(e);
        return function(a) {
            a < 132 || (R[a] = W,
            W = a)
        }(e),
        t
    }
    const gt = typeof TextDecoder < "u" ? new TextDecoder("utf-8",{
        ignoreBOM: !0,
        fatal: !0
    }) : {
        decode: () => {
            throw Error("TextDecoder not available")
        }
    };
    typeof TextDecoder < "u" && gt.decode();
    let L = null;
    function _() {
        return L !== null && L.byteLength !== 0 || (L = new Uint8Array(T.memory.buffer)),
        L
    }
    function $(e, t) {
        return e >>>= 0,
        gt.decode(_().subarray(e, e + t))
    }
    function H(e) {
        return e == null
    }
    let K = null
      , q = null;
    function C() {
        return q !== null && q.byteLength !== 0 || (q = new Int32Array(T.memory.buffer)),
        q
    }
    let O = 0;
    const ee = typeof TextEncoder < "u" ? new TextEncoder("utf-8") : {
        encode: () => {
            throw Error("TextEncoder not available")
        }
    }
      , Gt = typeof ee.encodeInto == "function" ? function(e, t) {
        return ee.encodeInto(e, t)
    }
    : function(e, t) {
        const a = ee.encode(e);
        return t.set(a),
        {
            read: e.length,
            written: a.length
        }
    }
    ;
    function oe(e, t, a) {
        if (a === void 0) {
            const n = ee.encode(e)
              , g = t(n.length, 1) >>> 0;
            return _().subarray(g, g + n.length).set(n),
            O = n.length,
            g
        }
        let i = e.length
          , s = t(i, 1) >>> 0;
        const A = _();
        let r = 0;
        for (; r < i; r++) {
            const n = e.charCodeAt(r);
            if (n > 127)
                break;
            A[s + r] = n
        }
        if (r !== i) {
            r !== 0 && (e = e.slice(r)),
            s = a(s, i, i = r + 3 * e.length, 1) >>> 0;
            const n = _().subarray(s + r, s + i);
            r += Gt(e, n).written
        }
        return O = r,
        s
    }
    let te = 128;
    function pt(e) {
        let t, a;
        try {
            const c = T.__wbindgen_add_to_stack_pointer(-16);
            T.get_timestamp(c, function(u) {
                if (te == 1)
                    throw new Error("out of js stack");
                return R[--te] = u,
                te
            }(e));
            var i = C()[c / 4 + 0]
              , s = C()[c / 4 + 1]
              , A = C()[c / 4 + 2]
              , r = C()[c / 4 + 3]
              , n = i
              , g = s;
            if (r)
                throw n = 0,
                g = 0,
                ct(A);
            return t = n,
            a = g,
            $(n, g)
        } finally {
            T.__wbindgen_add_to_stack_pointer(16),
            R[te++] = void 0,
            T.__wbindgen_free(t, a, 1)
        }
    }
    function ge(e, t) {
        try {
            return e.apply(this, t)
        } catch (a) {
            T.__wbindgen_exn_store(f(a))
        }
    }
    
    
    function Et() {
        const e = {
            wbg: {}
        };
        return e.wbg.__wbg_new_3830e8137e71ec75 = function() {
            return f(new Date)
        }
        ,
        e.wbg.__wbg_getTime_2246299160f4a9b5 = function(t) {
            return o(t).getTime()
        }
        ,
        e.wbg.__wbindgen_is_null = function(t) {
            return o(t) === null
        }
        ,
        e.wbg.__wbindgen_object_clone_ref = function(t) {
            return f(o(t))
        }
        ,
        e.wbg.__wbindgen_object_drop_ref = function(t) {
            ct(t)
        }
        ,
        e.wbg.__wbindgen_string_new = function(t, a) {
            return f($(t, a))
        }
        ,
        e.wbg.__wbindgen_boolean_get = function(t) {
            const a = o(t);
            return typeof a == "boolean" ? a ? 1 : 0 : 2
        }
        ,
        e.wbg.__wbindgen_is_bigint = function(t) {
            return typeof o(t) == "bigint"
        }
        ,
        e.wbg.__wbindgen_number_get = function(t, a) {
            const i = o(a)
              , s = typeof i == "number" ? i : void 0;
            (K !== null && K.byteLength !== 0 || (K = new Float64Array(T.memory.buffer)),
            K)[t / 8 + 1] = H(s) ? 0 : s,
            C()[t / 4 + 0] = !H(s)
        }
        ,
        e.wbg.__wbindgen_bigint_from_i64 = function(t) {
            return f(t)
        }
        ,
        e.wbg.__wbindgen_jsval_eq = function(t, a) {
            return o(t) === o(a)
        }
        ,
        e.wbg.__wbindgen_string_get = function(t, a) {
            const i = o(a)
              , s = typeof i == "string" ? i : void 0;
            var A = H(s) ? 0 : oe(s, T.__wbindgen_malloc, T.__wbindgen_realloc)
              , r = O;
            C()[t / 4 + 1] = r,
            C()[t / 4 + 0] = A
        }
        ,
        e.wbg.__wbindgen_is_object = function(t) {
            const a = o(t);
            return typeof a == "object" && a !== null
        }
        ,
        e.wbg.__wbindgen_in = function(t, a) {
            return o(t)in o(a)
        }
        ,
        e.wbg.__wbindgen_bigint_from_u64 = function(t) {
            return f(BigInt.asUintN(64, t))
        }
        ,
        e.wbg.__wbindgen_error_new = function(t, a) {
            return f(new Error($(t, a)))
        }
        ,
        e.wbg.__wbindgen_jsval_loose_eq = function(t, a) {
            return o(t) == o(a)
        }
        ,
        e.wbg.__wbg_String_b9412f8799faab3e = function(t, a) {
            const i = oe(String(o(a)), T.__wbindgen_malloc, T.__wbindgen_realloc)
              , s = O;
            C()[t / 4 + 1] = s,
            C()[t / 4 + 0] = i
        }
        ,
        e.wbg.__wbg_get_44be0491f933a435 = function(t, a) {
            return f(o(t)[a >>> 0])
        }
        ,
        e.wbg.__wbg_length_fff51ee6522a1a18 = function(t) {
            return o(t).length
        }
        ,
        e.wbg.__wbindgen_is_function = function(t) {
            return typeof o(t) == "function"
        }
        ,
        e.wbg.__wbg_next_526fc47e980da008 = function(t) {
            return f(o(t).next)
        }
        ,
        e.wbg.__wbg_next_ddb3312ca1c4e32a = function() {
            return ge(function(t) {
                return f(o(t).next())
            }, arguments)
        }
        ,
        e.wbg.__wbg_done_5c1f01fb660d73b5 = function(t) {
            return o(t).done
        }
        ,
        e.wbg.__wbg_value_1695675138684bd5 = function(t) {
            return f(o(t).value)
        }
        ,
        e.wbg.__wbg_iterator_97f0c81209c6c35a = function() {
            return f(Symbol.iterator)
        }
        ,
        e.wbg.__wbg_get_97b561fb56f034b5 = function() {
            return ge(function(t, a) {
                return f(Reflect.get(o(t), o(a)))
            }, arguments)
        }
        ,
        e.wbg.__wbg_call_cb65541d95d71282 = function() {
            return ge(function(t, a) {
                return f(o(t).call(o(a)))
            }, arguments)
        }
        ,
        e.wbg.__wbg_isArray_4c24b343cb13cfb1 = function(t) {
            return Array.isArray(o(t))
        }
        ,
        e.wbg.__wbg_instanceof_ArrayBuffer_39ac22089b74fddb = function(t) {
            let a;
            try {
                a = o(t)instanceof ArrayBuffer
            } catch (i) {
                a = !1
            }
            return a
        }
        ,
        e.wbg.__wbg_instanceof_Map_41f4584cbc3ce79f = function(t) {
            let a;
            try {
                a = o(t)instanceof Map
            } catch (i) {
                a = !1
            }
            return a
        }
        ,
        e.wbg.__wbg_isSafeInteger_bb8e18dd21c97288 = function(t) {
            return Number.isSafeInteger(o(t))
        }
        ,
        e.wbg.__wbg_entries_e51f29c7bba0c054 = function(t) {
            return f(Object.entries(o(t)))
        }
        ,
        e.wbg.__wbg_buffer_085ec1f694018c4f = function(t) {
            return f(o(t).buffer)
        }
        ,
        e.wbg.__wbg_new_8125e318e6245eed = function(t) {
            return f(new Uint8Array(o(t)))
        }
        ,
        e.wbg.__wbg_set_5cf90238115182c3 = function(t, a, i) {
            o(t).set(o(a), i >>> 0)
        }
        ,
        e.wbg.__wbg_length_72e2208bbc0efc61 = function(t) {
            return o(t).length
        }
        ,
        e.wbg.__wbg_instanceof_Uint8Array_d8d9cb2b8e8ac1d4 = function(t) {
            let a;
            try {
                a = o(t)instanceof Uint8Array
            } catch (i) {
                a = !1
            }
            return a
        }
        ,
        e.wbg.__wbindgen_bigint_get_as_i64 = function(t, a) {
            const i = o(a)
              , s = typeof i == "bigint" ? i : void 0;
            (J !== null && J.byteLength !== 0 || (J = new BigInt64Array(T.memory.buffer)),
            J)[t / 8 + 1] = H(s) ? BigInt(0) : s,
            C()[t / 4 + 0] = !H(s)
        }
        ,
        e.wbg.__wbindgen_debug_string = function(t, a) {
            const i = oe(ce(o(a)), T.__wbindgen_malloc, T.__wbindgen_realloc)
              , s = O;
            C()[t / 4 + 1] = s,
            C()[t / 4 + 0] = i
        }
        ,
        e.wbg.__wbindgen_throw = function(t, a) {
            throw new Error($(t, a))
        }
        ,
        e.wbg.__wbindgen_memory = function() {
            return f(T.memory)
        }
        ,
        e
    }
    async function lt(e) {
        if (T !== void 0)
            return T;
        e === void 0 && (e = new URL("https://static-cpn.hotkidclub.com/cpn/2025year/assets/campaign_bg-9d108286.wasm",self.location));
        const t = Et();
        (typeof e == "string" || typeof Request == "function" && e instanceof Request || typeof URL == "function" && e instanceof URL) && (e = fetch(e));
        const {instance: a, module: i} = await async function(s, A) {
            if (typeof Response == "function" && s instanceof Response) {
                if (typeof WebAssembly.instantiateStreaming == "function")
                    try {
                        return await WebAssembly.instantiateStreaming(s, A)
                    } catch (n) {
                        if (s.headers.get("Content-Type") == "application/wasm")
                            throw n;
                        console.warn("`WebAssembly.instantiateStreaming` failed because your server does not serve wasm with `application/wasm` MIME type. Falling back to `WebAssembly.instantiate` which is slower. Original error:\n", n)
                    }
                const r = await s.arrayBuffer();
                return await WebAssembly.instantiate(r, A)
            }
            {
                const r = await WebAssembly.instantiate(s, A);
                return r instanceof WebAssembly.Instance ? {
                    instance: r,
                    module: s
                } : r
            }
        }(await e, t);
        return function(s, A) {
            return T = s.exports,
            lt.__wbindgen_wasm_module = A,
            J = null,
            K = null,
            q = null,
            L = null,
            T
        }(a, i)
    }
    const Mt = await fetch("https://static-cpn.hotkidclub.com/cpn/2025year/assets/campaign_bg-9d108286.wasm").then(e => e.arrayBuffer());
    await lt(Mt);
    const s = pt(t);
    // console.log(s)
    return s

}

const args = process.argv.slice(2);

// 解析传入的 JSON 字符串
const jsonData = JSON.parse(args[0]);

// 打印接收到的 JSON 数据
// console.log("接收到的 JSON 数据:", jsonData);

pa(jsonData).then((result) => {
    console.log(result);
    // 这里可以对 result 进行其他处理
    return result
});

