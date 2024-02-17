# Aya反代与短网址服务

`aya1.eu.org`与`r.aya1.eu.org`是我在*Cloudflare Worker*上搭建的反代服务

主要用于下载用途，也可以代理git clone

~~[源码](https://gitlab.com/NickCao/experiments/-/blob/master/workers/r.js)可以在这里获取到~~ `aya1.eu.org`使用的源码作者删库了，这是我的[备份](https://fars.ee/ypXF/js)

`r.aya1.eu.org`/`aya1.eu.org`的源码可以在这里找到 [netptop/siteproxy](https://github.com/netptop/siteproxy)

由于恶意请求过多，免费额度经常被用完，因此对来自中国以外ip的请求加了cf盾，境外的机子应该也不需要这反代吧

## 反向代理使用方法：

在链接前加上`https://aya1.eu.org/`，如

```bash
❯ git clone https://aya1.eu.org/https://github.com/ventoy/vtoyboot

❯ wget https://aya1.eu.org/https://github.com/alist-org/alist/releases/download/v3.7.2/alist-linux-amd64.tar.gz
```

在链接前加上`https://r.aya1.eu.org/`或`https://aya1.eu.org/`，并去除后面的`:/`，如

```bash
❯ git clone https://aya1.eu.org/https/github.com/netptop/siteproxy

❯ wget http://r.aya1.eu.org/https/github.com/alist-org/alist/releases/download/v3.7.2/alist-linux-amd64.tar.gz
```

`r.aya1.eu.org` 同时还可以正常代理大部分网页，详见 [Readme](https://github.com/netptop/siteproxy/blob/master/README.md)

**注意：** siteproxy使用强制替换字符串的方式代理请求，网页或文本内容中任何匹配的网址都会被套上反代，建议只用于访问简单网页或代理git，用于下载文件时可能出现内容被修改的情况。

## 短网址使用方法：
1. 直接访问[网页端](https://s.aya1.eu.org/)
2. 使用api，调用方式：HTTP POST，请求格式: JSON

请求参数:

| 参数名 | 类型   | 是否必须 | 说明         |
| ------ | ------ | -------- | ------------ |
| url    | string | 必须     | 待缩短的网址 |

示例：

```bash
# 使用curl请求
❯ curl https://s.aya1.eu.org -d '{"url": "https://note.aya1.eu.org/#/Arch_For_Aya"}'
# 返回值：
{"status":200,"key":"/bPjk7C"}
# 然后访问 https://aya1.eu.org/bPjk7C 即可
```

## 或许可能的捐赠（随缘啦）
![图 2](/pic/qc.jpg)
