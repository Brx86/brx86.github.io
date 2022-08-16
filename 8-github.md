# Github反向代理：手把手教你免费搭建github镜像站

> Cloudflare是一家国外的知名CDN加速服务商，提供免费与付费的加速和网站保护服务。这里我们使用其推出的边缘计算服务CloudFlare Workers（以下简称Workers）搭建反向代理，以实现加速访问github。

Demo地址：https://git.ay1.us/

万能反代: https://ay1.us/

***

## 注册Cloudflare

**注册地址：**https://dash.cloudflare.com/sign-up

没什么好说的，有手就行

![图 1](https://ayatale.coding.net/p/picbed/d/file/git/raw/master/ce56752eabc396a0960bbf8e275cf018362716543fcb83f1618235fe6b65f9f8.png)  

## 创建Workers

注册完会让你添加网站，这步可以跳过，直接点左上角进入主站，点击右侧Workers

![图 2](https://ayatale.coding.net/p/picbed/d/file/git/raw/master/8d033520be5a2def681f0ec2b3a0791b96b1cd928aca6debeaa421c23aad2714.png)  

设置你的个人子域名，选择免费计划，每天10w次调用上限对于个人绝对够用了

![图 3](https://ayatale.coding.net/p/picbed/d/file/git/raw/master/5f574ee5002d0765b80867249c126382396f107a6c3de026a81aecda7bab7943.png)  

查收你的邮件

![图 4](https://ayatale.coding.net/p/picbed/d/file/git/raw/master/1f0d84caa02318936dc9f00779d0675b445092add49fecf47dc2f1f464234875.png)  

点击邮件里的链接，验证成功，进入Workers面板，点击“创建Workers”开始你的第一个Workers

![图 5](https://ayatale.coding.net/p/picbed/d/file/git/raw/master/a107be44082632343ceaaa4ae70518db166e77733d31620d29b8f0057016ff26.png)  

## 部署Workers

![图 6](https://ayatale.coding.net/p/picbed/d/file/git/raw/master/e6989cc14f4e92ae7cc0e3d629e8866b49817759d2c97308da55ae0f2dd67e8c.png)  

全选复制粘贴[github.js](https://cdn.jsdelivr.net/gh/Brx86/cf-workers-js@main/github.js)代码到左侧脚本栏，点击左上角自定义Workers名，然后“保存并部署”

![图 7](https://ayatale.coding.net/p/picbed/d/file/git/raw/master/083fec9121d029c8be6190f26b1e3779a7262f2edd37a69e4d0e6b3cb8809fbc.png)  

稍等片刻，点击左上角箭头后退到上一层页面，可以看到网站已经部署好了，点击链接即可访问

![图 8](https://ayatale.coding.net/p/picbed/d/file/git/raw/master/9323fd89c61407b84b5c61ece9621a9af4d96e1805cc9e0aa32e25201af3488c.png)  

![图 9](https://ayatale.coding.net/p/picbed/d/file/git/raw/master/7daf16c847fb5b2e614ac2941e3a77a1c2bb533d868ae021b69f9ed0f38c4a22.png)  

