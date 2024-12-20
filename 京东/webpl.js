const CryptoJS = require('crypto-js');

has={
    x64Fmix: function(a) {
            a = this.x64Xor(a, [0, a[0] >>> 1]);
            a = this.x64Multiply(a, [4283543511, 3981806797]);
            a = this.x64Xor(a, [0, a[0] >>> 1]);
            a = this.x64Multiply(a, [3301882366, 444984403]);
            return a = this.x64Xor(a, [0, a[0] >>> 1])
        },
    x64LeftShift: function(a, b) {
        b %= 64;
        return 0 === b ? a : 32 > b ? [a[0] << b | a[1] >>> 32 - b, a[1] << b] : [a[1] << b - 32, 0]
    },
    x64Add: function(a, b) {
        a = [a[0] >>> 16, a[0] & 65535, a[1] >>> 16, a[1] & 65535];
        b = [b[0] >>> 16, b[0] & 65535, b[1] >>> 16, b[1] & 65535];
        var c = [0, 0, 0, 0];
        c[3] += a[3] + b[3];
        c[2] += c[3] >>> 16;
        c[3] &= 65535;
        c[2] += a[2] + b[2];
        c[1] += c[2] >>> 16;
        c[2] &= 65535;
        c[1] += a[1] + b[1];
        c[0] += c[1] >>> 16;
        c[1] &= 65535;
        c[0] += a[0] + b[0];
        c[0] &= 65535;
        return [c[0] << 16 | c[1], c[2] << 16 | c[3]]
    },
    x64Xor: function(a, b) {
        return [a[0] ^ b[0], a[1] ^ b[1]]
    },
    x64Rotl: function(a, b) {
        b %= 64;
        if (32 === b) return [a[1], a[0]];
        if (32 > b) return [a[0] << b | a[1] >>> 32 - b, a[1] << b | a[0] >>> 32 - b];
        b -= 32;
        return [a[1] << b | a[0] >>> 32 - b, a[0] << b | a[1] >>> 32 - b]
    },
    x64Multiply: function(a, b) {
        a = [a[0] >>> 16, a[0] & 65535, a[1] >>> 16, a[1] & 65535];
        b = [b[0] >>> 16, b[0] & 65535, b[1] >>> 16, b[1] & 65535];
        var c = [0, 0, 0, 0];
        c[3] += a[3] * b[3];
        c[2] += c[3] >>> 16;
        c[3] &= 65535;
        c[2] += a[2] * b[3];
        c[1] += c[2] >>> 16;
        c[2] &= 65535;
        c[2] += a[3] * b[2];
        c[1] += c[2] >>> 16;
        c[2] &= 65535;
        c[1] += a[1] * b[3];
        c[0] += c[1] >>> 16;
        c[1] &= 65535;
        c[1] += a[2] * b[2];
        c[0] += c[1] >>> 16;
        c[1] &= 65535;
        c[1] += a[3] * b[1];
        c[0] += c[1] >>> 16;
        c[1] &= 65535;
        c[0] += a[0] * b[3] + a[1] * b[2] + a[2] * b[1] + a[3] * b[0];
        c[0] &= 65535;
        return [c[0] << 16 | c[1], c[2] << 16 | c[3]]
    },
    x64hash128:function(a, b) {
        a = a || "";
        b = b || 0;
        var c = a.length % 16,
            l = a.length - c,
            h = [0, b];
        b = [0, b];
        for (var q, z, C = [2277735313, 289559509], D = [1291169091, 658871167], B = 0; B < l; B += 16) q = [a.charCodeAt(B + 4) & 255 | (a.charCodeAt(B + 5) & 255) << 8 | (a.charCodeAt(B + 6) & 255) << 16 | (a.charCodeAt(B + 7) & 255) << 24, a.charCodeAt(B) & 255 | (a.charCodeAt(B + 1) & 255) << 8 | (a.charCodeAt(B + 2) & 255) << 16 | (a.charCodeAt(B + 3) & 255) << 24], z = [a.charCodeAt(B + 12) & 255 | (a.charCodeAt(B + 13) & 255) << 8 | (a.charCodeAt(B + 14) & 255) << 16 | (a.charCodeAt(B + 15) & 255) << 24, a.charCodeAt(B + 8) & 255 | (a.charCodeAt(B + 9) & 255) << 8 | (a.charCodeAt(B + 10) & 255) << 16 | (a.charCodeAt(B + 11) & 255) << 24], q = this.x64Multiply(q, C), q = this.x64Rotl(q, 31), q = this.x64Multiply(q, D), h = this.x64Xor(h, q), h = this.x64Rotl(h, 27), h = this.x64Add(h, b), h = this.x64Add(this.x64Multiply(h, [0, 5]), [0, 1390208809]), z = this.x64Multiply(z, D), z = this.x64Rotl(z, 33), z = this.x64Multiply(z, C), b = this.x64Xor(b, z), b = this.x64Rotl(b, 31), b = this.x64Add(b, h), b = this.x64Add(this.x64Multiply(b, [0, 5]), [0, 944331445]);
        q = [0, 0];
        z = [0, 0];
        switch (c) {
            case 15:
                z = this.x64Xor(z, this.x64LeftShift([0, a.charCodeAt(B + 14)], 48));
            case 14:
                z = this.x64Xor(z, this.x64LeftShift([0, a.charCodeAt(B + 13)], 40));
            case 13:
                z = this.x64Xor(z, this.x64LeftShift([0, a.charCodeAt(B + 12)], 32));
            case 12:
                z = this.x64Xor(z, this.x64LeftShift([0, a.charCodeAt(B + 11)], 24));
            case 11:
                z = this.x64Xor(z, this.x64LeftShift([0, a.charCodeAt(B + 10)], 16));
            case 10:
                z = this.x64Xor(z, this.x64LeftShift([0, a.charCodeAt(B + 9)], 8));
            case 9:
                z = this.x64Xor(z, [0, a.charCodeAt(B + 8)]), z = this.x64Multiply(z, D), z = this.x64Rotl(z, 33), z = this.x64Multiply(z, C), b = this.x64Xor(b, z);
            case 8:
                q = this.x64Xor(q, this.x64LeftShift([0, a.charCodeAt(B + 7)], 56));
            case 7:
                q = this.x64Xor(q, this.x64LeftShift([0, a.charCodeAt(B + 6)], 48));
            case 6:
                q = this.x64Xor(q, this.x64LeftShift([0, a.charCodeAt(B + 5)], 40));
            case 5:
                q = this.x64Xor(q, this.x64LeftShift([0, a.charCodeAt(B + 4)], 32));
            case 4:
                q = this.x64Xor(q, this.x64LeftShift([0, a.charCodeAt(B + 3)], 24));
            case 3:
                q = this.x64Xor(q, this.x64LeftShift([0, a.charCodeAt(B + 2)], 16));
            case 2:
                q = this.x64Xor(q, this.x64LeftShift([0, a.charCodeAt(B + 1)], 8));
            case 1:
                q = this.x64Xor(q, [0, a.charCodeAt(B)]), q = this.x64Multiply(q, C), q = this.x64Rotl(q, 31), q = this.x64Multiply(q, D), h = this.x64Xor(h, q)
        }
        h = this.x64Xor(h, [0, a.length]);
        b = this.x64Xor(b, [0, a.length]);
        h = this.x64Add(h, b);
        b = this.x64Add(b, h);
        h = this.x64Fmix(h);
        b = this.x64Fmix(b);
        h = this.x64Add(h, b);
        b = this.x64Add(b, h);
        return ("00000000" + (h[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (h[1] >>> 0).toString(16)).slice(-8) + ("00000000" + (b[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (b[1] >>> 0).toString(16)).slice(-8)
    }
}
// hash128 方法



// 示例数组
const r = [
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0",
    "zh-CN",
    "applewebkit_chrome",
    "537.36",
    "linux",
    "NA",
    24,
    "946x110",
    -480,
    "sessionStorageKey",
    "localStorageKey",
    "indexedDbKey",
    "NA",
    "Win32",
    12,
    "NA",
    "",
    "data:image/png;base64,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",
    "data:image/png;base64,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�extensions:ANGLE_instanced_arrays;EXT_blend_minmax;EXT_clip_control;EXT_color_buffer_half_float;EXT_depth_clamp;EXT_disjoint_timer_query;EXT_float_blend;EXT_frag_depth;EXT_polygon_offset_clamp;EXT_shader_texture_lod;EXT_texture_compression_bptc;EXT_texture_compression_rgtc;EXT_texture_filter_anisotropic;EXT_texture_mirror_clamp_to_edge;EXT_sRGB;KHR_parallel_shader_compile;OES_element_index_uint;OES_fbo_render_mipmap;OES_standard_derivatives;OES_texture_float;OES_texture_float_linear;OES_texture_half_float;OES_texture_half_float_linear;OES_vertex_array_object;WEBGL_blend_func_extended;WEBGL_color_buffer_float;WEBGL_compressed_texture_s3tc;WEBGL_compressed_texture_s3tc_srgb;WEBGL_debug_renderer_info;WEBGL_debug_shaders;WEBGL_depth_texture;WEBGL_draw_buffers;WEBGL_lose_context;WEBGL_multi_draw;WEBGL_polygon_mode�extensions:ANGLE_instanced_arrays;EXT_blend_minmax;EXT_clip_control;EXT_color_buffer_half_float;EXT_depth_clamp;EXT_disjoint_timer_query;EXT_float_blend;EXT_frag_depth;EXT_polygon_offset_clamp;EXT_shader_texture_lod;EXT_texture_compression_bptc;EXT_texture_compression_rgtc;EXT_texture_filter_anisotropic;EXT_texture_mirror_clamp_to_edge;EXT_sRGB;KHR_parallel_shader_compile;OES_element_index_uint;OES_fbo_render_mipmap;OES_standard_derivatives;OES_texture_float;OES_texture_float_linear;OES_texture_half_float;OES_texture_half_float_linear;OES_vertex_array_object;WEBGL_blend_func_extended;WEBGL_color_buffer_float;WEBGL_compressed_texture_s3tc;WEBGL_compressed_texture_s3tc_srgb;WEBGL_debug_renderer_info;WEBGL_debug_shaders;WEBGL_depth_texture;WEBGL_draw_buffers;WEBGL_lose_context;WEBGL_multi_draw;WEBGL_polygon_mode�w1[1, 1]�w2[1, 1024]�w38�w4yes�w58�w624�w78�w816�w932�w1016384�w111024�w1216384�w1316�w1416384�w1530�w1616�w1716�w184095�w19[32767, 32767]�w208�w21WebKit WebGL�w22WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)�w230�w24WebKit�w25WebGL 1.0 (OpenGL ES 2.0 Chromium)�wuv:Google Inc. (NVIDIA)�wur:ANGLE (NVIDIA, NVIDIA GeForce GTX 1050 Ti (0x00001C8C) Direct3D11 vs_5_0 ps_5_0, D3D11)"
];

// 拼接字符串
const joinedString = r.join("~~~"); // 用 '~~~' 拼接数组元素
console.log(joinedString)

// 获取加密结果
const p = has.x64hash128(joinedString, 31);

console.log(p);
