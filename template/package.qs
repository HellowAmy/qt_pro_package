function Component() {
    var widget = gui.pageById(QInstaller.LicenseCheck);
    widget.entered.connect(function () {
        widget.AcceptLicenseLabel.setText("同意 [ 必须接受协议才能进行下一步 ]");
        widget.AcceptLicenseCheckBox.setChecked(true);
    });
}

Component.prototype.createOperations = function () {
    component.createOperations();

    if (systemInfo.kernelType === "linux") {
        var desktopPath = "@HomeDir@/.local/share/applications/"
        var desktopIconPath = desktopPath + "[##DesktopName##].desktop"
        component.addOperation("Delete", desktopIconPath);
        component.addOperation("CreateDesktopEntry",
            desktopIconPath,
            "\
            Type=Application\n\
            Terminal=false\n\
            Path=@TargetDir@/[##ExecRunPath##]\n\
            Exec=@TargetDir@/[##Exec##]\n\
            Name=[##DesktopName##]\n\
            Icon=@TargetDir@/[##DesktopIcon##]\n\
            ");

        console.error("[添加桌面图标]" + desktopIconPath)
    }
}