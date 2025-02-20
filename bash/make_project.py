import os
import shutil
import json
import sys


def main():
    if len(sys.argv) < 2:
        print("< 创建一个全新的打包项目路径 > [ 打包项目名称 ]")
        return

    pro_name = sys.argv[1]
    path_src = "../template/"
    path_dst = "../pack/" + pro_name
    shutil.copytree(path_src, path_dst)

if __name__ == "__main__":
    main()
