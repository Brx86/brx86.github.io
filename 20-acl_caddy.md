# ACL 权限与 Caddy

arch 下安装的 caddy，如果用 `caddy.service`​ 启动，只能访问 `/var/lib/caddy /var/log/caddy /run/caddy`​ 这几个目录，

而用 `sudo caddy start`​ 又不太安全。

那么有什么办法可以让 caddy 访问用户 aya 的部分文件呢？

这时就需要 ACL 权限了。

> ACL 的全称是 Access Control List (**访问控制列表**) ，一个针对文件/目录的访问控制列表。它在 UGO 权限管理的基础上为**文件系统**提供一个额外的、更灵活的权限管理机制。它被设计为 UNIX 文件权限管理的一个补充。ACL 允许你给任何的用户或用户组设置任何文件/目录的访问权限。

需求：

让 caddy 的 `file_server`​​ ​可以处理 aya 家目录下的 `Downloads`​​​ 文件夹，
即 `/home/aya/Downloads`​​​

## 实际操作

* 文件权限相关

  ```bash
  # 修改 /home/aya 的权限
  sudo setfacl -m u:caddy:rx /home/aya
  # 递归修改 /home/aya/Downloads 及子目录与文件的权限，以后在其中创建的文件也有同样的属性
  sudo setfacl -Rm u:caddy:rx /home/aya/Downloads

  # 查看权限，测试修改是否有效
  getfacl /home/aya/Downloads
  sudo -u caddy ls -lh /home/aya/Downloads
  ```

  可以看到 caddy 用户已经可以读取这个目录内的文件了（有个小坑，忘记给目录加 x 权限会导致无法进入目录）

* systemd 安全性限制

  查看 `/usr/lib/systemd/system/caddy.service`​ 可以发现这个服务是以用户 caddy 运行的，且开启了很多安全选项。

  使用 `sudo systemctl edit caddy --full`​ 修改 `caddy.service`​

  ```ini
  # 其中，修改这两行
  # 关闭对家目录访问的限制
  ProtectHome=false
  # 在行末添加需要允许访问的目录 (/home/aya)
  ReadWritePaths=/var/lib/caddy /var/log/caddy /run/caddy /home/aya
  ```
* Caddyfile 的配置

  这里我的 caddy 配置位于 `/etc/caddy/conf.d/aya_file`​

  作用为在 `/home/aya/Downloads/` ​目录下启用 caddy `file_server`​

  ```ini
  https://api.aya1.de:22002 {
          encode zstd gzip
          tls /var/lib/caddy/key/aya1.de_ecc/fullchain.cer /var/lib/caddy/key/aya1.de_ecc/aya1.de.key
          root * /home/aya/Downloads/
          file_server browse
  }
  ```

到此为止需求解决。

## 一点小问题

发现启用 ACL 权限时，如果给家目录写权限，会导致不能通过密钥登录 ssh

命令：`sudo setfacl -m u:caddy:rwx /home/aya/`​

原因：这条命令会使得 caddy 用户可以更改 `/home/aya/.ssh`​ 目录，被认为不安全

解决方法（暂定）：如果有写入需求，只给需要的特定目录写权限，示例如下：

```bash
sudo setfacl -m u:caddy:rx /home/aya
sudo setfacl -Rm u:caddy:rwx /home/aya/Downloads
```
