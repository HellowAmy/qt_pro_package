function Controller() {
    installer.finishButtonClicked.connect(onFinishButtonClicked)
}

onFinishButtonClicked = function () {
    var widgetT = gui.pageById(QInstaller.TargetDirectory);
    var widgetF = gui.pageById(QInstaller.InstallationFinished);
    if (widgetT && widgetF) {
        if (widgetF.RunItCheckBox.checked) {
            var path = widgetT.TargetDirectoryLineEdit.text;
            installer.executeDetached(path + "/[##Exec##]", [], path + "/[##ExecRunPath##]");
            console.error("[运行程序]")
        }
    }
    console.error("[安装完成并退出]")
}

Controller.prototype.IntroductionPageCallback = function () {
    console.error("[欢迎界面]")

    var widget = gui.currentPageWidget();
    if (widget != null) {
        // widget.title = "[主题]欢迎主界面";
        // widget.MessageLabel.setText("[安装文本]Welcome to the <Name> Setup");
    }
}

Controller.prototype.TargetDirectoryPageCallback = function () {
    console.error("[目录选择界面]")

    var widget = gui.currentPageWidget();
    if (widget != null) {
        var path = widget.TargetDirectoryLineEdit.text;
        var filebib = path + "/maintenancetool";
        if (installer.fileExists(filebib)) {
            var yes = QMessageBox.question("提示", "覆盖安装", "安装目录已存在,是否覆盖安装<br>[ " + path + " ]");
            if (yes != QMessageBox.No) {
                console.error("[覆盖安装]")
                installer.execute(path + "/maintenancetool", ["pr", "-c"]);
                gui.clickButton(buttons.NextButton);
            }
            else {
                console.error("[选择其他路径安装]")
            }
        }
    }
}

Controller.prototype.FinishedPageCallback = function () {
    var widget = gui.currentPageWidget();
    if (widget != null) {
        widget.MessageLabel.setText("启动程序")
    }
}
