# Aya反代与短网址服务

`ay1.us`与`r.ay1.us`是我在*Cloudflare Worker*上搭建的反代服务

主要用于下载用途，也可以代理git clone

~~[源码](https://gitlab.com/NickCao/experiments/-/blob/master/workers/r.js)可以在这里获取到~~ `ay1.us`使用的源码作者删库了，这是我的[备份](https://fars.ee/YMpg/js)

`r.ay1.us`/`aya1.eu.org`的源码可以在这里找到 [netptop/siteproxy](https://github.com/netptop/siteproxy)

## 反向代理使用方法：

在链接前加上`https://ay1.us/`，如

```bash
❯ git clone https://ay1.us/https://github.com/ventoy/vtoyboot

❯ wget https://ay1.us/https://github.com/alist-org/alist/releases/download/v3.7.2/alist-linux-amd64.tar.gz
```

在链接前加上`https://r.ay1.us/`或`https://aya1.eu.org/`，并去除后面的`:/`，如

```bash
❯ git clone https://aya1.eu.org/https/github.com/netptop/siteproxy

❯ wget http://r.ay1.us/https/github.com/alist-org/alist/releases/download/v3.7.2/alist-linux-amd64.tar.gz
```

`r.ay1.us`/`aya1.eu.org` 同时还可以正常代理大部分网页，详见 [Readme](https://github.com/netptop/siteproxy/blob/master/README.md)

**注意：** siteproxy使用强制替换字符串的方式代理请求，网页或文本内容中任何匹配的网址都会被套上反代，建议只用于访问简单网页或代理git，用于下载文件时可能出现内容被修改的情况。

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


## 或许可能的捐赠（随缘啦）
![图 2](/pic/qc.jpg)