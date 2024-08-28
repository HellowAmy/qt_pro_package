import os
import shutil
import make_env
import make_ifw
import make_pack



def main():
    _path_cwd = os.getcwd()

    if os.path.exists("tmp/"):
        shutil.rmtree("tmp/")

    os.chdir(_path_cwd)
    make_env.main()

    os.chdir(_path_cwd)
    make_ifw.main()

    os.chdir(_path_cwd)
    make_pack.main()

    print("== end ==")


if __name__ == "__main__":
    main()
    




