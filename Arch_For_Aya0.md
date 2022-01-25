# Aya的丢人笔记

#### **关闭reflector，编辑镜像站**

```
systemctl stop reflector
sed -i 's|#Parallel|Parallel|g' /etc/pacman.conf
sed -i 's|SigLevel|SigLevel = Never\n#SigLevel|g' /etc/pacman.conf
echo 'Server = https://mirrors.sjtug.sjtu.edu.cn/archlinux/$repo/os/$arch' >/etc/pacman.d/mirrorlist
```

#### **分区：cfdisk /dev/sda**

> /dev/sda
>
> └ sda1	10M	EFI System
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

mkdir /mnt/efi

mount /dev/sda1 /mnt/efi
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
timedatectl set-timezone Asia/Shanghai
timedatectl set-ntp true
hwclock --systohc --utc
```


#### **新建用户**并设置为管理员

```
useradd -m -G wheel aya
sed -i 's|# %wheel ALL=(ALL) ALL|%wheel ALL=(ALL) ALL|g' /etc/sudoers
```

设置密码

```
passwd aya
```

#### 桌面环境装一个就行

##### 1.安装cinnamon与网络/音频相关包

```
sed -i 's|#Parallel|Parallel|g' /etc/pacman.conf
pacman -S xorg-server xorg-xrandr cinnamon xfce4-terminal lightdm-gtk-greeter-settings
pacman -S pipewire-pulse pipewire-alsa pipewire-jack pavucontrol networkmanager
systemctl enable lightdm
systemctl enable NetworkManager
```

##### 2.安装xfce与网络/音频相关包

```bash
pacman -S xorg-server xorg-xrandr xfce4 xfce4-goodies lightdm-gtk-greeter-settings 
pacman -S pipewire-pulse pipewire-alsa pipewire-jack pavucontrol network-manager-applet
systemctl enable lightdm
systemctl enable NetworkManager
```

#### 安装与配置grub引导

```
pacman -S grub efibootmgr os-prober dosfstools intel-ucode
grub-install --efi-directory=/efi
sed -i 's|#GRUB_DISABLE_OS_PROBER=false|GRUB_DISABLE_OS_PROBER=false|g' /etc/default/grub
grub-mkconfig -o /boot/grub/grub.cfg
```

#### 重启
```
exit
reboot
```
