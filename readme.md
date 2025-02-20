## 打包说明

#### 打包环境目录结构
需要说建立的 data.7z 压缩包将打包所有依赖环境，压缩包的目录结构如下，所有路径都用以 data　相对路径出发，如可执行文件 bin/exe ，说明文件 config/readme.md ，必须将所有依赖的文件都放入到 data 目录下才能完整打包
```
data
├── bin
├── config
├── lib
├── plugins
├── share
└── translations
```

#### 简易配置
需要完成 install.json 和 env.json 配置文件，将资源如压缩包、图标、免责说明 license.txt 文件等资源也一并复制到 ./pack/xxx 路径下

```
配置值说明

env.json :
    QMakePath : 指定 qmake 文件程序路径，可通过 which qmake 命令获取
    ExecPath : 打包的可执行程序的绝对路径，用于复制并生成打包依赖
    CopyConfig : 复制可执行文件依赖的配置资源文件夹，文件夹会被复制 ./pack/xxx/ 目录下

install.json :
    该文件的所有配置均来自 Qt IFW 打包框架，可查看文档或者参考 ./pack/calcbin 目录下的打包例子
    文档网址 : https://doc.qt.io/qtinstallerframework/
```

#### 打包脚本
打包脚本需要在指定的目录下执行，如切换到路径 ./pack/xxx/ 路径下，完成简易配置之后，执行 make_one_click.py 一键打包程序，会在 ./pack/xxx/tmp 路径下生成 .run 安装文件

```
make_project.py     --在pack目录下创建一个准备打包的副本目录
make_env.py         --生成打包依赖脚本，顺序1
make_ifw.py         --根据 顺序1 生成 ifw 框架所需目录结构，可以设置翻译语言，默认跟随系统，顺序2
make_pack.py        --根据 顺序2 生成 .run 安装文件，顺序3
make_one_click.py   --直接生成 .run 安装文件，自动依次执行上述脚本
```
脚本使用例子：

```
# 一键打包
cd ./pack/calcbin
python3 ../../bash/make_one_click.py

# 设置语言为英语
python3 ../../bash/make_ifw.py English
```

#### 配置文件字段说明
```
# env.json
# 功能是为Qt项目的二进制可执行程序打包运行环境-并将环境打包生成为data.zip文件-非Qt程序不使用


QMakePath   : 指定qmake程序位置-非路径而是文件
ExecPath    : 指定需要使用Qt依赖打包的二进制程序位置-非路径而是文件
CopyConfig  : 指定需要复制到安装目录下的文件夹-文件夹路径
```

```
# install.json
# 功能是为打包程序添加各类参数-程序图标、项目名称、桌面图标等参数


Name                        : 安装时显示的安装项目项目名称-文本显示
Title                       : 安装时显示的标题名称-文本显示-建议同上
DesktopName                 : 安装桌面快捷方式的名称-建议同上
TargetDir                   : 安装目录名称-默认安装在Home目录下-建议同上
ReleaseDate                 : 发布软件包日期-文本提示
Publisher                   : 发布者名称-文本提示
Version                     : 发布软件包版本号-文本提示
Logo                        : 安装包安装时出现的图标-icon文件-默认不填
InstallerWindowIcon         : 安装时窗口栏出现的图标-icon/png文件-带后缀
InstallerApplicationIcon    : 安装包在文件夹中显示的图标-icon/png文件-带后缀
Exec                        : 桌面图标的可执行程序-安装目录下的相对路径
ExecRunPath                 : 桌面图标的可执行程序启动时路径-安装目录下的相对路径
DesktopIcon                 : 桌面图标的显示图标文件路径-安装目录下的相对路径-带后缀
```



