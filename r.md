## **Aya反代服务**

**aya1.top是我在 *Cloudflare Worker* 上搭建的反代服务**,

主要用于下载用途，也可以代理git clone,

[源码](https://gitlab.com/NickCao/experiments/-/blob/master/workers/r.js)可以在这里获取到。

## 使用方法：

在链接前加上aya1.top，如

```bash
git clone https://aya1.top/https://github.com/ventoy/vtoyboot

wget https://aya1.top/https://github.com/Clansty/Icalingua/releases/download/v2.2.0/Icalingua-2.2.0.AppImage
```