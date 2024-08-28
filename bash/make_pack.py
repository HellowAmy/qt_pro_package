import os
import subprocess
import json


def main():
    with open("install.json", "r", encoding="utf-8") as fjson:
        sjson = json.load(fjson)
        if os.path.exists("tmp/ifw/"):
            os.chdir("tmp/ifw/")
            cmd = "binarycreator -c config/config.xml -p packages ../{}.run".format(
                sjson["Name"]
            )
            print("pwd: ", os.getcwd())
            print("cmd: ", cmd)
            subprocess.run(cmd, shell=True)
    print("== end ==")


if __name__ == "__main__":
    main()
