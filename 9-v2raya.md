# Arch系配置代理最简方法

> v2rayA 是一个支持全局透明代理的 V2Ray Linux 客户端，同时兼容SS、SSR、[Trojan](https://github.com/trojan-gfw/trojan)、[PingTunnel](https://github.com/esrrhs/pingtunnel)协议。 
> v2rayA 致力于提供最简单的操作，满足绝大部分需求。
> 得益于Web客户端的优势，你不仅可以将其用于本地计算机，还可以轻松地将它部署在路由器或NAS上。
> 项目地址：https://github.com/v2rayA/v2rayA

因为众所周知的原因，国内连接github非常不稳定，因此在使用aur的过程中经常出现下载缓慢甚至无法下载的情况。除此之外，作为linux用户也常常需要到外网查询资料，这时一个靠谱的代理软件的重要性就显现出来了。arch/manjaro群日常：求助大佬，怎么挂代理

Arch系常用的代理软件有**v2rayA**和**Qv2ray**等。相比后者，v2rayA有安装方便无需插件，支持全局透明代理，支持RoutingA自定义规则，systemd服务无痕自启，可以部署到服务器或路由器等等诸多优点，配置简单，适合新手使用。至于Qv2ray，感兴趣的自己看[wiki](https://qv2ray.net/lang/zh/)去（逃）

v2rayA实际界面如图所示：

![图 1](/pic/9.1.png)  


****

## 安装步骤：

1. ### 编辑`/etc/pacman.conf`，在文件末尾添加archlinuxcn仓库（已经添加的可以跳过此步）

   ```bash
   [archlinuxcn]
   SigLevel = Never
   Server = https://mirrors.bfsu.edu.cn/archlinuxcn/$arch
   ```

2. ### 安装v2rayA与v2ray-core

   ```bash
   sudo pacman -Sy v2ray v2raya
   ```

3. ### 启动v2rayA服务（如果从aur安装会自动执行这步）

   ```bash
   systemctl enable v2raya --now
   ```

4. ### 浏览器打开```127.0.0.1:2017```

   根据提示设置管理员用户名和密码，以后更改相关设置可能要用到

   进入界面，点击打开右上角设置，点击右上角更新GFWList（可选）

   将“全局透明代理”和“规则端口的分流模式”都设置为**GFWList**或**大陆白名单**，其他设置默认，点击保存并应用


   ![图 2](/pic/9.2.png)  

   回到主界面，点击导入订阅或节点链接

   ![图 3](/pic/9.3.png)  

## 然后就可以愉快使用节点了！

#### Tips：

- 某次更新后v2rayA在使用v2ray-core时可以负载均衡，所以连接节点后需要点击左上角的“就绪”按钮以运行
- 点击全选，PING可以测试节点的TCP延迟，点击列表上的“时延”可以对节点进行排序
- PING测试延迟未必准确，有时部分节点会失效。这时可以点击HTTP测试真延迟，显示TIMEOUT或NOT STABLE的节点不可用
- 如果无法打开外网网页，浏览器显示PR_END_OF_FILE_ERROR错误，请检查当前节点是否可用
- “全局透明代理”启用分流时对系统全局生效，浏览器与终端联网自动分流，均不用做特别设置
- 设置里点击“开启局域网共享”，点击“地址与端口”查看代理端口号，同一局域网下的设备均可通过ip与端口使用该设备的socks或http代理
- 更多详细使用方法请参考[wiki](https://github.com/v2rayA/v2rayA/wiki/Home_zh)

![图 4](/pic/9.1.png)
