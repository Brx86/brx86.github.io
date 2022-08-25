# 使用AutoKey在Vscode-QQ快速发送图片

>相关项目地址：
>Vscode-QQ：https://github.com/takayama-lily/vscode-qq
>AutoKey：https://github.com/autokey/autokey

Linux下使用QQ有很多方案，比如linuxqq(不推荐)，electron-qq，com.qq.tim.spark，deepin-wine-tim等等……

但还有一种方法：**[Vscode-QQ](https://github.com/takayama-lily/vscode-qq)**

![图 1](/pic/10.1.png)  

>  Vscode-QQ可以收发消息、查看历史消息、图片，回复、撤回、@、戳一戳、禁言、踢出，发送emoji、QQ表情与收藏表情……常用功能基本都有，但其中的一个功能用起来很麻烦：**发送图片**

****

## 正常发送图片的方法：

```bash
[CQ:image,file=替换为本地图片或网络URL路径]
```

## AutoKey发送图片的方法：

```bash
快捷键一键发送
```

那么如何快速发送呢？这里需要用到AutoKey与Flameshot

### 1. 在截图软件里进行设置

设置自动保存与保存后复制文件路径（这里使用Flameshot，其他有复制路径功能的截图软件也可以）

![图 2](/pic/10.2.png)  

### 2. 安装AutoKey并编写脚本

```bash
yay -S autokey-gtk #安装对应的版本，如使用kde等qt桌面请安装autokey-qt
```

打开AutoKey，在“My Phrases”里新建一个python脚本，内容为：

```python
picmsg = '[CQ:image,file=' + clipboard.get_clipboard() + ']'
keyboard.send_keys(picmsg)
keyboard.send_keys("<ctrl>+<enter>")
```

设置一个快捷键，我这里使用的是**Super+F1**

![图 3](/pic/10.3.png)  

### 3. 然后就可以愉快发送图片了！

快捷键截图，保存，在Vscode-QQ的聊天烂使用快捷键，就可以自动发送图片了，非常的银杏，非常的实用

***

## 注意：

发送图片时输入法应处于英文输入状态，否则可能会发出什么奇奇怪怪的东西