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
        }
    }
}

Controller.prototype.IntroductionPageCallback = function () {
    var widget = gui.currentPageWidget();
    if (widget != null) {
    }
}

Controller.prototype.TargetDirectoryPageCallback = function () {
    var widget = gui.currentPageWidget();
    if (widget != null) {
        var path = widget.TargetDirectoryLineEdit.text;
        var filebib = "";
        var toolpath = "";
        if (systemInfo.kernelType == "linux") {
            toolpath = "/maintenancetool";
        }
        else {
            toolpath = "/maintenancetool.exe";
        }
        filebib = path + toolpath;

        if (installer.fileExists(filebib)) {
            var yes = QMessageBox.question("[##TrOverlapTips##]", "[##TrOverlapTitle##]", "[##TrOverlapContent##]<br>[ " + path + " ]");
            if (yes != QMessageBox.No) {
                installer.execute(filebib, ["pr", "-c"]);
                if (systemInfo.kernelType === "linux") {
                    gui.clickButton(buttons.NextButton);
                }
            }
        }
    }
}

Controller.prototype.FinishedPageCallback = function () {
    var widget = gui.currentPageWidget();
    if (widget != null) {
        widget.MessageLabel.setText("[##TrRunProgram##]")
    }
}
