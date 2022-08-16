# Aya反代与短网址服务

**ay1.us**是我在*Cloudflare Worker*上搭建的反代服务

主要用于下载用途，也可以代理git clone

[源码](https://gitlab.com/NickCao/experiments/-/blob/master/workers/r.js)可以在这里获取到

## 反向代理使用方法：

在链接前加上`https://ay1.us/`，如

```bash
❯ git clone https://ay1.us/https://github.com/ventoy/vtoyboot

❯ wget https://ay1.us/https://github.com/Icalingua/Icalingua/releases/download/v2.4.3/Icalingua-2.4.3.AppImage
```

## 短网址使用方法：
1. 直接访问[网页端](https://s.ay1.us/)
2. 使用api，调用方式：HTTP POST，请求格式: JSON

请求参数:

| 参数名 | 类型   | 是否必须 | 说明         |
| ------ | ------ | -------- | ------------ |
| url    | string | 必须     | 待缩短的网址 |

示例：

```bash
# 使用curl请求
❯ curl https://s.ay1.us -d '{"url": "https://note.ay1.us/#/Arch_For_Aya"}'
# 返回值：
{"status":200,"key":"/bPjk7C"}
# 然后访问 https://ay1.us/bPjk7C 即可
```

## Aya个人常用短网址：

vps2aya脚本：
https://ay1.us/vps2aya

zinit备份：
https://ay1.us/zinitbk