# Arch系安装并配置fcitx5输入法

> ​		之前linux下的输入法我一直用的搜狗，但随着fcitx和qt的更新，基于fcitx-qt4的搜狗越来越不好使了（甚至被踢出了仓库）。今天终于决定尝试下fcitx5，结果当然是好用到爆，我立刻抛弃了搜狗转投了fcitx5的原生输入法。真香！

废话不多说，以下就是安装fcitx5所需的
## 全部操作：

### 1. 安装fcitx5及其组件：

```shell
sudo pacman -S fcitx5-im fcitx5-chinese-addons fcitx5-pinyin-moegirl fcitx5-pinyin-zhwiki
```

### 2. 新建或修改 `~/.xprofile` ，添加以下几行：

```shell
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
export INPUT_METHOD=fcitx
export SDL_IM_MODULE=fcitx
export GLFW_IM_MODULE=ibus
```

### 3. 保存，注销重新登录，然后在托盘图标右键详细配置即可愉快使用！

注意fcitx5的配置界面应如图所示，请确保添加“键盘”与“拼音”两个选项

![图 1](/pic/2.1.webp)  


## Tips：

### 安装前请卸载全部fcitx4组件：

```shell
sudo pacman -Rsc fcitx
```

### 中文输入时 `【 】` 的问题 
中文输入法下，键盘上按方括号键的时候，预期是输出“【】”，但实际上左方括号键输出的是“·”，而右方括号键则依次输出“「」”这种方括号 

    解决方法：
    修改 /usr/share/fcitx5/punctuation/punc.mb.zh_CN
    将第17、18行分别改为“[ 【”与“] 】”，然后重启fcitx5即可


### 包名解释：

    fcitx5-im：包组，包含四个包 fcitx5 fcitx5-gtk fcitx5-qt fcitx5-configtool

    fcitx5：fcitx5引擎本体

    fcitx5-qt fcitx5-gtk：对各种图形界面的支持模块

    fcitx5-configtool：fcitx5的图形化配置工具

    fcitx5-chinese-addons：fcitx5的中文输入支持插件

    fcitx5-material-color：一个很好看的主题，详细说明：https://github.com/hosxy/Fcitx5-Material-Color

    fcitx5-nord：另一个很好看的主题，详细说明：https://github.com/tonyfettes/fcitx5-nord

    fcitx5-pinyin-moegirl：outloudvi根据萌娘百科创建的词库（涵盖了许多有意思的名词）

    fcitx5-pinyin-zhwiki：felixonmars根据中文维基百科创建的词库（肥猫百万大词库nb！）

    fcitx5-pinyin-custom-pinyin-dictionary: 另一个百万级中文词库，比zhwiki更新更全，推荐使用

### 部分好用的设置（云拼音，候选词数量等）还可以通过修改配置文件启用：

配置文件位置：`~/.config/fcitx5/conf/pinyin.conf `

![图 2](/pic/2.2.webp)

### 可以安装fcitx5-nord、fcitx5-material-color等第三方皮肤：

安装后在配置-附加组件-经典用户界面启用

![图 3](/pic/2.3.webp)

横排，在程序中显示预编辑文本，fcitx5-material-color蓝色皮肤

![图 4](/pic/2.4.webp)

竖排，不显示预编辑文本，fcitx5-nord暗色皮肤

![图 5](/pic/2.5.webp)  