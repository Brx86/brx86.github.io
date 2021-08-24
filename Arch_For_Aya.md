#### **编辑镜像站**

```
nano /etc/pacman.d/mirrorlist
```

第一行改成

```
Server = https://mirrors.163.com/archlinux/$repo/os/$arch
```

#### **分区-cfdisk**

> /dev/sda
>
> └ sda1	30M	EFI System
>
> └ sda2	50G	Linux Filesystem

#### **格式化分区**

```
mkfs.vfat /dev/sda1

mkfs.xfs /dev/sda2
```

#### **挂载分区**

```
mount /dev/sda2 /mnt

mkdir -p /mnt/boot/efi

mount /dev/sda1 /mnt/boot/efi
```

#### **安装基本系统**

```
pacstrap /mnt base base-devel linux linux-firmware nano
```

#### **生成fstab**

```
genfstab -U /mnt > /mnt/etc/fstab
```

#### **arch-chroot进入新系统**

```
arch-chroot /mnt
```

#### **设置语言**

```
nano /etc/locale.gen
```

反注释en_US与zh_CN

> en_US.UTF-8 UTF-8
>
> zh_CN.UTF-8 UTF-8

生成语言

```
locale-gen
```

修改locale.conf

```
echo LANG=en_US.UTF-8 > /etc/locale.conf
```

#### 设置时区与utc时间

```
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc --utc
```


#### **新建用户**并设置为管理员

```
useradd -m -G wheel aya
echo '%wheel ALL=(ALL) ALL' >> /etc/sudoers
```

设置密码

```
passwd aya
```

#### 安装intel核显与触摸板驱动

```
pacman -S xf86-video-intel xf86-input-synaptics
```
#### 桌面环境装一个就行

##### 1.安装cinnamon与网络/音频相关包

```
pacman -S xorg cinnamon xfce4-terminal lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings
pacman -S pulseaudio pulseaudio-alsa pavucontrol dhcpcd networkmanager
systemctl enable lightdm
systemctl enable NetworkManager
```

##### 2.安装xfce与网络/音频相关包

```bash
pacman -S xorg xfce4 xfce4-goodies lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings 
pacman -S pulseaudio pulseaudio-alsa pavucontrol dhcpcd network-manager-applet
systemctl enable lightdm
systemctl enable NetworkManager
```

#### 安装与配置grub引导

```
pacman -S grub efibootmgr os-prober dosfstools intel-ucode
grub-install --efi-directory=/boot/efi
grub-mkconfig -o /boot/grub/grub.cfg
```

#### 重启
```
exit
reboot
```
