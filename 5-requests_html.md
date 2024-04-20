# 爬虫库requests_html踩坑笔记

> Python爬虫很常用的一个库requests的作者[Kenneth Reitz](https://github.com/kennethreitz)又发布了一个新库**requests-html**。它基于现有的框架 pyquery、requests、lxml、beautifulsoup4等库进行了二次封装，使用起来更加简单便捷。

初次使用，在尝试渲染js页面时：

```python
from requests_html import HTMLSession
session = HTMLSession()
r = session.get('http://stock.finance.sina.com.cn/usstock/quotes/bidu.html').html
r.render() #解析js
r.encoding = 'UTF-8'
title = r.find('.hq_title > h1:nth-child(1)', first=True).text
price = r.find('div.hq_change_time:nth-child(2) > div:nth-child(1)', first=True).text
print(f'{title}\n盘后数据：{price}')
```

第一次使用requests_html解析js，会自动调用pyppeteer下载chromium。

***

此时出现第一个问题：

### Chromium下载速度过慢：

![图 1](/pic/5.1.webp)

#### 解决方法：

查看下载文件的真实链接，手动axel多线程下载或代理下载：

```python
import pyppeteer.chromium_downloader
print(f'默认版本是：{pyppeteer.__chromium_revision__}')
print(f'可执行文件默认路径：{pyppeteer.chromium_downloader.chromiumExecutable.get("linux")}')
print(f'linux平台下载链接为：{pyppeteer.chromium_downloader.downloadURLs.get("linux")}')
```

输出结果为：

```bash
默认版本是：588429
可执行文件默认路径：/home/lighthouse/.local/share/pyppeteer/local-chromium/588429/chrome-linux/chrome
linux平台下载链接为：https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/588429/chrome-linux.zip
```

手动下载完成后解压到对应文件夹即可。

***

随后再次尝试运行脚本，出现另一问题：

### 无法启动无头Chrome：

```bash
pyppeteer.errors.BrowserError: Browser closed unexpectedly:
```

#### 解决方法：

安装相关依赖：

```bash
sudo aptitude install ca-certificates fonts-liberation libappindicator3-0.1-cil libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release wget xdg-utils 
```

参考资料：[Chrome headless doesn't launch on UNIX](https://github.com/puppeteer/puppeteer/blob/main/docs/troubleshooting.md#chrome-headless-doesnt-launch-on-unix)

***

问题解决后，文章开始时的脚本输出为：

```bash
百度 NASDAQ:BIDU Baidu, Inc.
盘后数据：263.7 1.98(0.76%)
```

