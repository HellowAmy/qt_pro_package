import os
import shutil
import pathlib
import subprocess
import json


def main():
    path_cwd = os.getcwd()

    # 清空并生成 data 文件夹结构
    if os.path.exists("tmp/"):
        shutil.rmtree("tmp/")
    os.makedirs("tmp/data/")
    os.makedirs("tmp/data/bin/")

    # 复制文件到路径
    path_qmake = ""
    path_exec = ""
    name_exec = ""
    sjson = None
    with open("env.json", "r", encoding="utf-8") as fjson:
        sjson = json.load(fjson)
        path_qmake = sjson["QMakePath"]
        path_exec = sjson["ExecPath"]
        name_exec = os.path.basename(path_exec)
        shutil.copy(path_exec, "tmp/data/bin/")
        for it in sjson["CopyConfig"]:
            nbase = str(pathlib.Path(it).name)
            dst = "tmp/data/{}".format(nbase)
            shutil.copytree(it, dst)

    print("== argv ==")
    print(path_qmake)
    print(path_exec)
    print(name_exec)

    # 打包环境依赖
    cmd_deploy = "linuxdeployqt {} -qmake={}".format(name_exec, path_qmake)
    print("cmd: " + cmd_deploy)
    print("pwd: " + os.getcwd())
    os.chdir("tmp/data/bin/")
    subprocess.run(cmd_deploy, shell=True, capture_output=True, text=True)

    # 将 data 目录压缩成 7z 压缩包
    os.chdir(path_cwd)
    cmd_7z = "7z a {} {}".format("tmp/data.7z", "tmp/data/")
    print("pwd: " + os.getcwd())
    print("cmd: " + cmd_7z)
    subprocess.run(cmd_7z, shell=True, capture_output=True, text=True)

    print("== end ==")


if __name__ == "__main__":
    main()
