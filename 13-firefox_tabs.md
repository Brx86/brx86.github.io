# Firefox使用类似Edge的侧栏标签页


>一直以来都觉得普通的1920x1080屏幕的左右空间很大，而上下空间很吃紧。在浏览器访问网页时，如果算上系统的dock/panel、系统标题栏、标签顶栏、地址栏、收藏夹栏，整个网页的上下可视区域就更小了。之前就听说可以通过修改css把火狐的顶栏去掉，今日在reddit看到一个帖子终于去试一试，效果极佳！

原帖地址：[Reddit](https://www.reddit.com/r/FirefoxCSS/comments/obw2wm/edgestyle_vertical_tabs_for_firefox_with_tab/)  
相关CSS：[Github](https://github.com/ranmaru22/firefox-vertical-tabs/)

---

## 全部操作：

### 1. 创建自定义css：

浏览器地址栏打开 `about:config` ，将以下选项设置为true，以启用自定义css

    toolkit.legacyUserProfileCustomizations.stylesheets

浏览器地址栏打开 `about:support` ，选择打开配置文件夹，路径一般为：

    cd /home/<your_user>/.mozilla/firefox/<some_hash>.default-release

在此目录新建文件夹 `chrome` ，并写入 `userChrome.css`

    wget https://raw.ay1.us/ranmaru22/firefox-vertical-tabs/main/userChrome.css -P chrome

### 2. 安装Tab Center Reborn拓展：

点击安装拓展：[Tab Center Reborn](https://addons.mozilla.org/zh-CN/firefox/addon/tabcenter-reborn/)

打开这个地址，全选复制自定义css：[tabCenterReborn.css](https://raw.ay1.us/ranmaru22/firefox-vertical-tabs/main/tabCenterReborn.css)

右键拓展图标，管理拓展，将复制的 **tabCenterReborn.css** 粘贴到自定义样式表

点击最下面的 `保存CSS` 按钮

![图 1](/pic/13.1.png)   
![图 2](/pic/13.2.png)  

### 3. 重启Firefox，享受无标签顶栏、有动态标签侧栏的火狐吧！

## 效果演示：

<video id="video" controls="" preload="none" poster="Firefox">
      <source id="mp4" src="/pic/reddit_firefox.mp4" type="video/mp4">
</videos>