import os
import shutil

def read_file_str(path):
    sfile = ""
    with open(path, "r", encoding="utf-8") as fs:
        sfile = fs.read()
    return sfile


def write_file_str(path, ctx):
    with open(path, "w", encoding="utf-8") as fs:
        fs.write(ctx)


def copy_file(src, dst):
    if os.path.exists(src):
        shutil.copy(src, dst)