# yay进阶教程

> yay是一个AUR Helper，他可以执行pacman的几乎所有操作，并在此基础上添加了很多额外用法。
>
> 我没有在网络上查找到关于yay的、除了pacman基础用法和安装AUR包以外的中文教程，英文的也几乎没有看到，这也是我写这篇文章的原因所在。
>
> 本文参考了yay的英文使用手册，如果你的arch安装了yay，那么即可通过`man yay`命令随时查阅它。
>
> 阅读提示:  本文中出现的foo一般是指包名，标注*的表示很少用到的操作（我自己没实操过、没法非常准确的理解的那种）

# 基本用法

yay的基本用法是`yay <operation> [options] [targets]`、`yay foo`和`yay`，`yay <operation> [options] [targets]`的用法可以讨论的点比较多，我会在后文中一一道来。

## `yay`

当我们仅执行`yay`，后面不跟任何参数时，yay会执行操作`yay -Syu`，他会先调用pacman更新源的数据库、更新所有从源内安装的软件包，并检查你的AUR包有没有更新。

## `yay *foo*`

通过yay后面直接跟包名的命令会让yay直接在源和AUR内搜索带有`foo`关键词的包（包名和简介中只要出现foo都会被一网打尽），以下是我执行`yay dingtalk`的输出

```
5 aur/com.dingtalk.deepin 5.0.15deepin7-1 (+0 0.00) 
    Deepin Wine dingtalk
4 aur/deepin.com.dingtalk.com 5.1.28.12-2 (+1 0.12) 
    DingTalk Client on Deepin Wine
3 aur/dingtalk 2.1.3-1 (+3 0.00) 
    钉钉桌面版，基于electron和钉钉网页版开发，支持Windows、Linux和macOS
2 aur/dingtalk-linux 3.5.5-1 (+6 0.12) 
    May be the official Linux experimental version
1 aur/dingtalk-electron 2.1.9-1 (+9 0.15) 
    钉钉Linux版本
==> Packages to install (eg: 1 2 3, 1-3 or ^4)
==
```

输入每一项对应的序号即可进入相应的安装过程。

## `yay \<operation> [options] [targets]`

在这里，\<operation>每次只能有一个，[options]和[targets]可以有多个，且多个[options]可以合起来写在一起。比如`yay -P -s -f`可以直接写成`yay -Psf`，顺序也可以颠倒，`-Psf`和`-sPf`没区别。

### `-Y (--yay)`

-Y行为其实是yay的默认行为，当你没有加其他的行为参数时，yay就会执行-Y参数，以下是-Y行为的操作选项

#### `* --gendb`

生成AUR数据库。**仅当从另一个AUR Helper迁移到yay时，才应使用此选项。**~~（根据我的个人理解，是根据你Arch内安装的源内找不到的包的包名去AUR里寻找对应的PKGBUILD，并且把能找到的PKGBUILD给clone到`~/.cache/yay/`目录下）~~

千玄子大佬说：“简单说来就是把在 AUR 的 PKGBUILD 下下来然后比对是否要更新。”

#### `-c（--clean）`

清除不再需要的、没有被依赖的包。（相当于apt中的autoremove）

### `-P(--show)`

执行特定的Print操作。

#### `-c(--complete)`

Print所有源内和AUR软件包的列表。这是给命令行操作提供的，并不打算由用户直接使用。（意思是启用了这个选项以后你的终端会出现一大串长常的列表来告诉你你的Arch到底从哪里安装了哪些包，并不是直接给你用的，是作为数据留给别的命令来玩耍的）

#### `-f(--fish)`

在输出结果到终端时，会专门为fish用户做微调。（但是根据SamLukeYes大佬说他用fish体验下来并没有感知到加不加有什么区别，应该是属于感知不强的选项）

#### `-d(--defaultconfig)`

Print默认的yay配置。

#### `-g(--currentconfig)`

Print当前的yay配置。

#### `-n(--numberupgrades)`

数一数你现在还有多少AUR包待更新。yay作者不推荐你使用呢，他推荐你用`yay -Qu`或者`wc -l`来代替它。

#### `-s(--stats)`

会展示一大堆信息，如下

```
[zhullyb@Archlinux ~]$ yay -Ps
==> Yay version v10.2.0							    #yay版本
===========================================
==> Total installed packages: 1240				    #总共安装了多少包
==> Total foreign installed packages: 24		    #多少包不是从源里安装的
==> Explicitly installed packages: 271			    #有多少包是你自己主动安装的(而不是作为依赖安装的)
==> Total Size occupied by packages: 14.3 GiB	    #安装的所有包合在一起一共占了你多少空间
===========================================
==> Ten biggest packages:						    #十个体积最大的包
wps-office-cn: 990.9 MiB
ttf-sarasa-gothic: 855.5 MiB
linux-firmware: 652.3 MiB
baidunetdisk-bin: 494.7 MiB
com.antutu.benchmark: 412.0 MiB
wine: 402.2 MiB
linux-xanmod-cacule-uksm-cjktty: 324.4 MiB
microsoft-edge-dev-bin: 316.4 MiB
wine-mono: 316.2 MiB
deepin-wine5-i386: 259.5 MiB
===========================================
:: Querying AUR...
 -> Missing AUR Packages:  zhullyb-archlinux-git    #AUR里找不到的包
 -> Flagged Out Of Date AUR Packages:  xml2		    #AUR中被人标注过期的包
```

#### `-u(--upgrades)`

展示你所有待更新的包。

#### `-w(--news)`

展示来自archlinux.org的新闻。需要注意的是，这里的新闻是具有时效性的，只有在你的Arch最后一次更新以后发出来的新闻才会被显示出来。如果你不想要yay判断新闻时效性，你可以通过`yay -Pww`（即两个`w`）来获取所有能获得的新闻。

#### `-q(--quiet)`

在输出新闻的时候，仅输出新闻的标题。该功能需要与`-w`连用，即`yay -Pwq`。

### `-G(--getpkgbuild)`

后跟包名。需要注意的是，如果指定的包不存在于官方源，则无法输出。如果希望仅获取来自AUR（即排除第三方源的干扰）的PKGBUILD，后需跟`-a`参数。

#### `-f(--force)`

强制下载AUR中的PKGBUILD，如果它在yay缓存目录已经存在了，那就覆盖它！

#### `-p(--print)`

Print指定包的PKGBUILD。

## pacman 拓展用法

yay虽然可以使用pacman的所有\<operation>，但是它远不仅于此。在这一段，我将向你介绍yay中包含的那些pacman不包括的pacman \<operation>

### `-S`

#### `-S, -Si, -Sl, -Ss, -Su, -Sc, -Qu`

这些操作pacman都支持，而与pacman不同的是，yay的这些操作可以涵盖到**官方源/第三方源和AUR**中的所有包。

### `-Sc`

yay将会清除AUR包构建时的缓存和没有被track的文件。没有被track的文件在这里指AUR包构建时下载的sources或者构建完成的pkg包，但是vcs sources会被保留（比如.`git`文件夹）

### 全局的[options]

#### `--repo`

假定你给出的包名只存在源里（忽视AUR的存在）

#### `-a(--aur)`

假定你给出的包名只存在AUR中（忽视源的存在）

# 配置设置

原版的man手册排的比较混乱，我这里自己分了几个类型，或许不是特别专业，但我希望能够帮助你们理解。

#### `--requestsplitn <number>`

设置在每次向AUR的请求的最大数值。数值越高，请求时间越短，但是单次请求的数值过大会导致error。当这个数值＞500时你应当特别注意这一点。

#### `--completioninterval <days>`

刷新完成高速缓存的时间（以天为单位）。 将此值设置为0将导致每次刷新缓存，而将其设置为-1将导致永远不刷新缓存。

## 自定义调用命令型

#### `--editor <command>`

设置编辑时调用的编辑器。

#### `--makepkg <command>`

设置makepkg时需要调用makepkg命令（一般情况下用不到）

#### `--pacman <command>`

设置运行pacman时需要调用pacman命令（一般情况下用不到）

#### `--tar <command>`

设置makepkg解压tar资源时调用的tar命令（一般情况下用不到）

#### `--git <command>`

设置makepkg clone git资源时调用的git命令（比如你可以安装AUR中的fgit-go，使用`--git fgit`参数来让fastgit代理clone的过程）

#### `--gpg <command>`

设置gpg验证资源时调用的gpg命令

#### `--sudo <command>`

设置调用sudo获取su权限安装pkg时所调用的sudo命令。

## 自定义配置文件型

#### `--config <file>`

设置读取的pacman配置文件。

#### `--makepkgconf <file>`

设置读取的makepkg配置文件。

#### `--nomakepkgconf`

不读取系统中的makepkg.conf，仅使用Arch默认状态下的配置文件。

## 自定义路径类型

#### `--builddir \<dir>`

设置build路径，默认路径为`~/.cache/yay/`

#### `--absdir \<dir>`

 设置abs路径，默认路径为`~/.cache/yay/abs/`

## 参数传递型

#### `--editorflags <flags>`

后跟需要跟随传递给编辑器的参数。如果需要传递多个参数，可以使用引号。

#### `--mflags <flags>`

后跟需要跟随传递给makepkg的参数。如果需要传递多个参数，可以使用引号。

#### `--gpgflags <flags>`

后跟需要跟随传递给pgp的参数。如果需要传递多个参数，可以使用引号。

#### `--sudoflags <flags>`

后跟需要跟随传递给sudo的参数。如果需要传递多个参数，可以使用引号。

## 菜单配置型

### clean菜单

#### `--cleanmenu`

启用清除询问菜单，该功能默认启用。（询问你是否需要清除已存在的文件）

#### `--nocleanmenu`

禁用清除询问菜单。（不询问你是否需要清除已存在的文件）

#### `--answerclean`

 自动回答cleanmenu，后跟`<All|None|Installed|NotInstalled>`参数。

#### `--noanswerclean`

不设置自动回答，该功能默认启用。

### diff菜单

#### `--diffmenu`

启用对比询问菜单，该功能默认启用。（询问你是否需要对比本地文件和AUR文件）

#### `--nodiffmenu`

禁用对比询问菜单。（不询问你是否需要对比本地文件和AUR文件）

#### `--answerdiff`

自动回答cleanmenu，后跟`<All|None|Installed|NotInstalled>`参数。

#### `--noanswerdiff`

不设置自动回答，该功能默认启用。

### edit菜单

#### `--editmenu`

启用修改询问菜单。（询问你是否需要修改PKGBUILD以及相关文件）

#### `--noeditmenu`

禁用修改询问菜单该功能默认启用。（不询问你是否需要修改PKGBUILD以及相关文件）

#### `--answeredit`

自动回答editmenu，后跟`<All|None|Installed|NotInstalled>`参数。

#### `--noansweredit`

不设置自动回答，该功能默认启用。

### upgrade菜单

#### `--upgrademenu`

启用更新询问菜单，该功能默认启用。（询问你是否需要更新AUR包）

#### `--noupgrademenu`

禁用更新询问菜单。（不询问你是否需要更新AUR包）

#### `--answerupgrade`

自动回答upgrademenu，后跟`<All|None|Installed|NotInstalled`参数。

#### `--noanswerupgrade`

不设置自动回答，该功能默认启用。

### removemake菜单

#### `--askremovemake`

在编译结束后，询问是否删除make depend，该项默认启用

#### `--removemake`

在编译结束后，删除make depend。

#### `--noremovemake`

在编译结束后，不删除make depend。

### provides菜单

#### `--provides`

搜索AUR包时，一同寻找其在AUR上的依赖程序。 当找到多个提供该依赖的包时，将出现一个菜单，提示您选择一个。尽管这不会引起注意，但这会增加依赖项解决时间。

#### `--noprovides`

搜索AUR包时，不在AUR上寻找其依赖程序。尽管yay不会再次弹出依赖菜单供你选择，yay调用pacman时依然会出现pacman的选择菜单让你选择。

### pgpfetch菜单

#### `--pgpfetch`

询问你是否从每个PKGBUILD的validpgpkeys字段导入未知的PGP密钥，该项默认开启。

#### `--nopgpfetch`

不自动导入陌生的PGP密钥。

### useask选项

#### `--useask`

调用pacman的--ask询问用户是否删除系统中与当前包冲突的软件包。该项默认开启。

#### `--nouseask`

不调用pacman的--ask询问用户是否删除系统中与当前包冲突的软件包，遇到冲突的软件包时直接报错，由用户来手动解决。

## 其他型

#### `--save`

把你这一次执行yay后面跟的配置参数永久保存下来。

#### `--aururl`

更改aur源地址（默认为https://aur.archlinux.org），适用于中国用户，可以使用此参数将AUR的地址设置成清华的反代，具体的配置命令为

```
yay --aururl "https://aur.tuna.tsinghua.edu.cn" --save
```

#### `--sortby`

在搜索过程中，按特定条件对AUR结果进行排序，后跟`<votes|popularity|id|baseid|name|base|submitted|modified>`参数，默认为`votes`。

#### `--searchby`

通过指定查询类型来搜索AUR软件包，后跟`<name|name-desc|maintainer|depends|checkdepends|makedepends|optdepends>`参数，默认为`name-desc`。

#### `--topdown`

优先展示源内包，其次才是AUR包

#### `--bottomup`

优先展示AUR包，其次才是源内包

#### `--devel`

在系统更新期间，检查AUR的vcs包是否有更新，当前仅支持AUR的-git包。 devel查询是使用`git ls-remote`对比安装时和现在最新的commit_id完成的。

#### `--nodevel`

在系统更新期间， 不检查AUR的vcs包是否有更新，该项默认开启。

#### `--cleanafter`

在构建AUR包完成以后清除cache文件。

#### `--nocleanafter`

在构建AUR包完成以后不清除cache文件，该项默认启用。

#### `--timeupdate`

在系统更新期间，将已安装软件包的构建时间与每个软件包的AUR的最后修改时间进行比较。

#### `--notimeupdate`

在系统更新期间，不将已安装软件包的构建时间与每个软件包的AUR的最后修改时间进行比较。

#### `--redownload`

就算PKGBUILD已经存在，也要重新从AUR上获取一份新的PKGBUILD并覆盖原有PKGBUILD。

#### `--redownloadall`

就算PKGBUILD已经存在，也要重新从AUR上获取所有AUR包的PKGBUILD并覆盖原有PKGBUILD。

#### `--noredownload`

当下载PKGBUILD时，，如果发现cache中的PKGBUILD版本＞＝AUR上的版本时，直接使用本地的PKGBUILD。该项默认开启

#### `--combinedupgrade`

在系统更新期间，将源内包和AUR包的更新菜单合并到一起。

#### `--nocombinedupgrade`

在系统更新期间，先支持源内包的升级，完成后再进行AUR包的升级。

#### `--batchinstall`

在构建和安装AUR包时，对每个软件包的安装进行排序，而并非在构建之后立刻安装每个软件包时。 需要注意的是，一旦构建了所有软件包，或者需要构建队列中的软件包作为构建另一个软件包的依赖项，应当在安装队列中安装所有软件包。

#### `--nobatchinstall`

在构建AUR包成功后立即安装，该项默认启用。

#### `--rebuild`

即使在cache中有可用的二进制包的情况下，也始终要重新编译目标软件包。

#### `--rebuildall`

即使在cache中有可用的二进制包的情况下，也始终要重新编译所有的AUR包。

#### `--rebuildtree`

安装AUR包时，以递归方式重新编译并重新安装其所有AUR依赖包，即使已安装的依赖项也是如此。 该选项使您可以轻松地针对当前系统的库重新构建软件包，如果它们变得不兼容。（比如python3.8->3.9）

#### `--norebuild`

构建软件包时，如果在缓存中找到该软件包并且该软件包与想要的软件包的版本相同，则跳过软件包的编译过程并使用现有的二进制程序。该项默认启用

#### `--sudoloop`

在后台循环调用sudo，以防止sudo授权在长时间构建期间超时。

#### `--nosudoloop`

不在后台循环调用sudo，可能会导致sudo授权在长时间构建期间超时，该项默认启用。
