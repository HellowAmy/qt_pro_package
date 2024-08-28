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
make_env.py         --生成打包依赖脚本，顺序1
make_ifw.py         --根据 顺序1 生成 ifw 框架所需目录结构，顺序2
make_pack.py        --根据 顺序2 生成 .run 安装文件，顺序3
make_one_click.py   --直接生成 .run 安装文件，自动依次执行上述脚本
```
脚本使用例子：

```
cd ./pack/calcbin
python3 ../../bash/make_one_click.py
```


