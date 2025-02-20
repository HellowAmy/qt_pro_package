import os
import shutil
import pathlib
import json
import func
import locale
import sys


def main():
    path_pwd = str(pathlib.Path.cwd())
    pro_name = pathlib.Path(path_pwd).name

    # 设置翻译语言 zh_CN en_US
    sys_language, sys_encoding = locale.getdefaultlocale()
    key_language = ""
    if len(sys.argv) >= 2:
        key_language = sys.argv[1]
    else:
        if sys_language == "zh_CN":
            key_language = "Chinese"
        elif sys_language == "en_US":
            key_language = "English"

    print("< 设置语言 > [ Chinese/English ]", key_language)

    # 读取并替换模板文件
    path_config_xml = "../../template/config.xml"
    path_config_qs = "../../template/config.qs"
    path_package_xml = "../../template/package.xml"
    path_package_qs = "../../template/package.qs"

    sfile_config_xml = func.read_file_str(path_config_xml)
    sfile_config_qs = func.read_file_str(path_config_qs)
    sfile_package_xml = func.read_file_str(path_package_xml)
    sfile_package_qs = func.read_file_str(path_package_qs)

    print("== template path ==")
    print(path_config_xml)
    print(path_config_qs)
    print(path_package_xml)
    print(path_package_qs)

    install_sjson = None
    with open("install.json", "r", encoding="utf-8") as fjson:
        install_sjson = json.load(fjson)
        for key, val in install_sjson.items():
            skey = "[##{}##]".format(key)
            sfile_config_xml = sfile_config_xml.replace(skey, val)
            sfile_config_qs = sfile_config_qs.replace(skey, val)
            sfile_package_xml = sfile_package_xml.replace(skey, val)
            sfile_package_qs = sfile_package_qs.replace(skey, val)

    with open("translate.json", "r", encoding="utf-8") as fjson:
        sjson = json.load(fjson)
        for key, valjson in sjson.items():
            val = valjson[key_language]
            skey = "[##{}##]".format(key)
            sfile_config_xml = sfile_config_xml.replace(skey, val)
            sfile_config_qs = sfile_config_qs.replace(skey, val)
            sfile_package_xml = sfile_package_xml.replace(skey, val)
            sfile_package_qs = sfile_package_qs.replace(skey, val)

    # 生成 ifw 打包目录和复制模板文件到目录下
    if os.path.exists("tmp/ifw/"):
        shutil.rmtree("tmp/ifw/")

    ifw_config = "tmp/ifw/config"
    ifw_packages_main_data = "tmp/ifw/packages/{}/data".format(pro_name)
    ifw_packages_main_meta = "tmp/ifw/packages/{}/meta".format(pro_name)

    os.makedirs(ifw_config)
    os.makedirs(ifw_packages_main_data)
    os.makedirs(ifw_packages_main_meta)

    func.copy_file(install_sjson["Logo"], ifw_config + "/" + install_sjson["Logo"])
    func.copy_file(
        install_sjson["InstallerWindowIcon"],
        ifw_config + "/" + install_sjson["InstallerWindowIcon"],
    )
    func.copy_file(
        install_sjson["InstallerApplicationIcon"] + ".ico",
        ifw_config + "/" + install_sjson["InstallerApplicationIcon"] + ".ico",
    )
    func.copy_file("tmp/data.zip", ifw_packages_main_data + "/" + "data.zip")
    func.copy_file("license.txt", ifw_packages_main_meta + "/" + "license.txt")

    func.write_file_str(ifw_config + "/config.xml", sfile_config_xml)
    func.write_file_str(ifw_config + "/config.qs", sfile_config_qs)
    func.write_file_str(ifw_packages_main_meta + "/package.xml", sfile_package_xml)
    func.write_file_str(ifw_packages_main_meta + "/package.qs", sfile_package_qs)

    print("== end ==")


if __name__ == "__main__":
    main()
