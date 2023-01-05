# Github反向代理：手把手教你免费搭建github镜像站

> Cloudflare是一家国外的知名CDN加速服务商，提供免费与付费的加速和网站保护服务。这里我们使用其推出的边缘计算服务CloudFlare Workers（以下简称Workers）搭建反向代理，以实现加速访问github。

Demo地址：https://git.ay1.us/

万能反代: https://ay1.us/

***

## 注册Cloudflare

**注册地址：**https://dash.cloudflare.com/sign-up

没什么好说的，有手就行

![图 1](/pic/8.1.png)  

## 创建Workers

注册完会让你添加网站，这步可以跳过，直接点左上角进入主站，点击右侧Workers

![图 2](/pic/8.2.png)  

设置你的个人子域名，选择免费计划，每天10w次调用上限对于个人绝对够用了

![图 3](/pic/8.3.png)  

查收你的邮件

![图 4](/pic/8.4.png)  

点击邮件里的链接，验证成功，进入Workers面板，点击“创建Workers”开始你的第一个Workers

![图 5](/pic/8.5.png)  

## 部署Workers

![图 6](/pic/8.6.png)  

全选复制粘贴[github.js](https://cdn.jsdelivr.net/gh/Brx86/cf-workers-js@main/github.js)代码到左侧脚本栏，点击左上角自定义Workers名，然后“保存并部署”

![图 7](/pic/8.7.png)  

稍等片刻，点击左上角箭头后退到上一层页面，可以看到网站已经部署好了，点击链接即可访问

![图 8](/pic/8.8.png)  

![图 9](/pic/8.9.png)  

同理，另一个项目 [netptop/siteproxy](https://github.com/netptop/siteproxy) 的部署方法也是一样的，详见项目主页