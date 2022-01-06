# 把PulseAudio替换成Pipewire


>Pipewire 是 Red Hat 的 Wim Taymans 领导开发的，他也是 GStreamer 项目的联合创始人。当初由于 Linux 声音系统 PulseAudio 在许多方面不如人意，因此其决定从头实现一个全新的媒体系统 ，计划最终取代 PulseAudio，成为新的 Linux 多媒体基础设施。 
>就个人体验而言，使用btrfs反复对比后感觉音质提升挺明显的（戴上原道，已触发悔恨之泪buff）

---
<h2 p style="color:#FF0000";>注意：</h2>
<h3 p style="color:#FF0000";>操作前请做好准备，如有可能最好创建快照。</h3>
<h3 p style="color:#FF0000";>请勿随意使用pacman -Rc以免卸载掉桌面必备组件</h3>

## 全部操作：

#### 1.安装Pipewire及其组件：
提示与pulseaudio冲突是正常现象，选y确认替换
```shell# 安装Pipewire本体
# 提示选择pipewire-media-session和wireplumber时二选一即可，建议后者
sudo pacman -S pipewire-pulse pipewire-alsa pipewire-jack
# 如果需要32位支持，可以再安装lib32-pipewire lib32-pipewire-jack
sudo pacman -S lib32-pipewire lib32-pipewire-jack
# 如果需要均衡器，安装easyeffects
sudo pacman -S easyeffects
```

#### 2.启用Pipewire相关服务：

```shell
systemctl enable pipewire --user
systemctl enable pipewire-pulse --user
```

#### 3.如果是新装的Arch，还未配置蓝牙，可以顺便装上（已经配置好的可以忽略这一步）

```shell
sudo pacman -S blueman
systemctl enable bluetooth
```


#### 4.安装完成，重启体验Pipewire的音质吧！

>Pipewire是红帽造的新一代音视频轮子，主要是用来取代PulseAudio、jack还有gstreams什么的。
>据说延迟补偿还不错，据说能统一音视频框架还兼容PulseAudio和Jack，据说是朝着专业级音效去的。据说支持Wayland和平板，据说支持Flatpak之类的容器内使用，据说有类似PolKit的权限管理，不需要像PulseAudio那样新建音频用户组和添加用户……

>以上摘选自 https://zhangjk98.xyz/pipewire/