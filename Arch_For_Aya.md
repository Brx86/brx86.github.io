# Arch安装笔记

#### **编辑镜像站**

```
nano /etc/pacman.d/mirrorlist
```

第一行改成

```
Server = https://mirrors.bfsu.edu.cn/archlinux/$repo/os/$arch
```

#### **分区-cfdisk**

> /dev/sda
>
> └ sda1	300M	EFI
>
> └ sda2	30G	Linux Filesystem
>
> └ sda3	100G	Linux Filesystem

#### **格式化分区**

```
mkfs.vfat /dev/sda1

mkfs.xfs /dev/sda2

mkfs.xfs /dev/sda3
```

#### **挂载分区**

```
mount /dev/sda2 /mnt
mkdir -p /mnt/boot/efi
mkdir /mnt/home
mount /dev/sda1 /mnt/boot/efi
mount /dev/sda3 /mnt/home
```

#### **安装基本系统**

```
pacstrap -i /mnt base base-devel linux linux-firmware nano
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

#### **安装与配置grub引导**

```
pacman -S grub efibootmgr dosfstools intel-ucode
grub-install --target=x86_64-efi --efi-directory=/boot/efi
grub-mkconfig -o /boot/grub/grub.cfg
```

#### **新建用户**

```
useradd -m -G wheel aya
```

设置密码

```
passwd aya
```

**安装intel核显与触摸板驱动**

```
pacman -S xf86-video-intel xf86-input-synaptics
```

安装X窗口与桌面环境

```
pacman -S xorg xfce4 xfce4-goodies
echo "exec startxfce4" > /etc/X11/xinit/xinitrc
exec startplasma-x11
```

