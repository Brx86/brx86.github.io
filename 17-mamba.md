# 使用Mamba作为Conda替代品

> **Conda or Mamba for production?**
>
> https://labs.epi2me.io/conda-or-mamba-for-production/

前几年第一次用 micromamba 的时候还有一些问题，没想到现在已经这么好用了。单文件无依赖便于安装，运行和安装速度完全吊打 conda ，这些足以完美替代 conda 了。

## 1. 对于Arch 系发行版，可以直接从 AUR 安装

```bash
# 使用 paru 从 aur 安装，也可使用其他方法
paru -S micromamba-bin
```

## 2. 配置 shellrc

```bash
# 初始化，--shell 后填自己使用的 shell ，--prefix 后填虚拟环境的保存路径，默认为 ~/micromamba
micromamba shell init -s zsh -p ~/.local/share/micromamba
# 习惯 conda 命令 ，alias 一下
echo 'alias conda=micromamba' >> ~/.zshrc
# 重新加载当前 shell（ bash，fish 等同理）
exec zsh
```

## 3. 配置 ~/.condarc

mambaforge 开发者建议不要使用 anaconda 的仓库，直接用 conda-forge 的

```yaml
channels:
  - conda-forge
show_channel_urls: true
custom_channels:
  conda-forge: https://mirrors.bfsu.edu.cn/anaconda/cloud
  pytorch: https://mirrors.bfsu.edu.cn/anaconda/cloud
```

## 4. 创建新环境测试（如果在aur装的，已经测试过了，可以跳过此步）

```bash
conda create -n py311 python=3.11
conda activate py311
python -V
```

## 在其他系统使用 micromamba

手动安装
```bash
cd /tmp
wget https://micro.mamba.pm/api/micromamba/linux-64/latest -O-|tar jxvf - bin/micromamba
sudo install -m755 bin/micromamba /usr/local/bin
```

官方安装脚本 （推荐）
https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html
```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```

接下来同上 2 3 4 步。
