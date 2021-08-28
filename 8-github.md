# Github反向代理：手把手教你免费搭建github镜像站

> Cloudflare是一家国外的知名CDN加速服务商，提供免费与付费的加速和网站保护服务。这里我们使用其推出的边缘计算服务CloudFlare Workers（以下简称Workers）搭建反向代理，以实现加速访问github。

Demo地址：https://git.aya1.xyz/

***

## 注册Cloudflare

**注册地址：**https://dash.cloudflare.com/sign-up

没什么好说的，有手就行

![](https://gitee.com/brx86/picpool/raw/master/2021/03/25/a9024f1f11fdb11931cb6293e58eedfc.png)

## 创建Workers

注册完会让你添加网站，这步可以跳过，直接点左上角进入主站，点击右侧Workers

![](https://gitee.com/brx86/picpool/raw/master/2021/03/25/03c2ca54f6e8b6492dec3be8dd61aedc.png)

设置你的个人子域名，选择免费计划，每天10w次调用上限对于个人绝对够用了

![](https://gitee.com/brx86/picpool/raw/master/2021/03/25/bcf1f35349a7aba30c6ffb271f2d851c.png)

查收你的邮件

![](https://gitee.com/brx86/picpool/raw/master/2021/03/25/3c56a2b7de697a74b7634d8aead31265.png)

点击邮件里的链接，验证成功，进入Workers面板，点击“创建Workers”开始你的第一个Workers

![](https://gitee.com/brx86/picpool/raw/master/2021/03/25/8e10cbb4959672c683ea8a6f09a41a43.png)

## 部署Workers

![](https://gitee.com/brx86/picpool/raw/master/2021/03/25/319a633a18d38763116b54e2dfe5ad9b.png)

全选复制粘贴[github.js](https://cdn.jsdelivr.net/gh/Brx86/cf-workers-js@main/github.js)代码到左侧脚本栏，点击左上角自定义Workers名，然后“保存并部署”

![](https://gitee.com/brx86/picpool/raw/master/2021/03/25/47e762f89f5734958d49c92aeefcbb62.png)

稍等片刻，点击左上角箭头后退到上一层页面，可以看到网站已经部署好了，点击链接即可访问

![](https://gitee.com/brx86/picpool/raw/master/2021/03/25/f95380145e4c468976eeca0c9ce57cbe.png)

![](https://gitee.com/brx86/picpool/raw/master/2021/03/25/1cdbe24c50ccd6f134b1335fca9744d1.png)

