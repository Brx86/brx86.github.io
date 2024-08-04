# podman 踩坑记录

## 初次尝试一段时间的小坑

1. 尝试把 docker 换成 podman ，为了类似的命令体验，安装 `podman`​ `podman-compose`​ `podman-docker`​。
2. 注意镜像的位置 `~/.local/share/containers/storage`​ 和 `/var/lib/containers/storage`​，和 docker 不一样。
3. 使用 btrfs 驱动需要修改以下配置文件（不存在就新建），并执行重置命令

   ```toml
   # ~/.config/containers/storage.conf
   # /etc/containers/storage.conf
   [storage]
   driver = "btrfs"
   ```

   ```bash
   # 更换驱动后重置，会删除全部容器与镜像
   podman system reset
   sudo podman system reset
   ```
4. 无默认仓库，只有常用镜像的 alias，无前缀使用 dockerhub 需要修改配置

   ```toml
   # 编辑 /etc/containers/registries.conf，加入默认 dockerhub
   unqualified-search-registries = ["docker.io"]
   # 可选操作，修改 /etc/containers/registries.conf.d/01-registries.conf，可以使用镜像站（虽然现在全寄完了）
   [[registry]]
   location = "docker.io"
   ```
5. 如果需要调用 podman.sock（类似 docker.sock ），需要启动服务

   ```bash
   # rootless，对应 /run/user/$UID/podman/podman.sock
   systemctl --user enable podman.socket --now
   # 系统级，对应 /var/run/docker.sock
   sudo systemctl enable podman.socket --now
   ```
6. 运行后一段时间总是退出，需要启用 linger

   `loginctl enable-linger $USER`​

   参考：[Archwiki: Containers_terminate_on_shell_logout](https://wiki.archlinux.org/title/Podman#Containers_terminate_on_shell_logout)
7. rootless 模式挂载目录后权限是 /etc/subuid 里的高位，我的目录所有者直接变成 100999 了，自己的用户反而无法访问

   > 我们确实认识到这不符合许多人打算如何使用无根 Podman 的方式——他们希望容器内外的 UID 匹配。因此，我们提供了 --userns=keep-id 标志，它确保您的用户在容器内部被映射到它自己的 UID 和 GID。
   > https://podmancn.pages.dev/docs/tutorials/rootless_tutorial
   > https://github.com/containers/podman-compose/issues/166
   >

   但我用起来有问题，没法在 podman-compose.yaml 里设置，issue 里提到的选项也失效了。最终解决方法：设置 ACL 权限 凑合用吧。

## 使用 Quadlet 管理容器，实现开机自启和自动更新

又使用了一段时间，podman 容器自启的方法有好几种，但看起来都不是很优雅。

最终选择了 quadlet，也是官方推荐的方法，把之前写的 podman-compose.yaml 全改成 quadlet 的 .container 文件了。

##### 安装 `podlet`​

[https://github.com/containers/podlet](https://github.com/containers/podlet)

##### 使用 podlet 转换 yaml，生成基础 container 文件

​`podlet -u compose compose.yaml`​

```ini
# 用户级 rootless 容器的配置文件生成到 ~/.config/containers/systemd/alist.container
# 以管理员权限运行，则生成到 /usr/share/containers/systemd/alist.container
[Container]
ContainerName=alist
Environment=PUID=1000 PGID=1000 UMASK=022
Image=xhofe/alist:latest
PublishPort=5244:5244
Volume=./config:/opt/alist/data
Volume=./downloads:/downloads

[Service]
Restart=always
```

##### 修改文件，最终如下

```ini
[Unit]
Description=Alist Podman
# 启动顺序，在网络后启动
After=network-online.target
# 服务依赖，必须有网络才启动
Wants=network-online.target

[Container]
ContainerName=alist
Environment=PUID=1000 PGID=1000 UMASK=022
Image=xhofe/alist:latest
PublishPort=5244:5244
# 挂载路径必须是绝对路径
Volume=/home/aya/stacks/alist/config:/opt/alist/data
Volume=/home/aya/stacks/alist/downloads:/downloads

[Service]
Restart=always
# 当 Quadlet 启动时，Podman 通常会再拉取或构建一个容器映像
# Systemd 默认服务启动时间为 90 秒，需要更改以免拉取超时导致启动失败
TimeoutStartSec=900

# quadlet 生成的 service 无法 enable/disable，要开机自启需要 Install
[Install]
WantedBy=multi-user.target default.target
```

##### 生成 service ，启动容器，并开机自启

```bash
# 普通用户 rootless 容器，操作如下，如果以管理员权限运行，则除去 --user 参数
# 修改 .container 后需刷新，重新生成 service
systemctl --user daemon-reload
# 查看生成的 service 文件
systemctl --user cat alist.service
# 启动容器
systemctl --user start alist.service
```

##### 自动更新容器镜像

```bash
# 启动更新 images 的定时服务，如果以管理员权限运行，则除去 --user 参数
systemctl --user enable podman-auto-update.timer --now
```

---

##### **参考：** 

1. [Red Hat: Make systemd better for Podman with Quadlet](https://www.redhat.com/sysadmin/quadlet-podman)
2. [Redhat: 使用 Podman 将容器移植到 systemd](https://docs.redhat.com/zh_hans/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/assembly_porting-containers-to-systemd-using-podman_building-running-and-managing-containers#auto-generating-a-systemd-unit-file-using-quadlets_assembly_porting-containers-to-systemd-using-podman)
3. [Podman Docs: podman-systemd.unit.5](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
4. [Quadlets might make me finally stop using docker-compose](https://major.io/p/quadlets-replace-docker-compose/)
5. [GitHub: containers/podlet](https://github.com/containers/podlet)

