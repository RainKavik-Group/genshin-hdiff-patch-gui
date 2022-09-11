import sys
import os
import shutil
import json
import stat
import subprocess
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLineEdit, QMessageBox
from mainWindow import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.path50_button.clicked.connect(lambda: self.selectFolder(self.path50_textbox, "选择完整客户端路径："))
        self.path51_button.clicked.connect(lambda: self.selectFolder(self.path51_textbox, "选择差分包路径："))
        self.commandLinkButton.clicked.connect(self.startPatch)

    def selectFolder(self, textbox: QLineEdit, title: str):
        dialog = QFileDialog()
        ret_path = dialog.getExistingDirectory(self, title)
        if ret_path != "":
            textbox.setText(ret_path)

    def consoleWrite(self, content: str):
        self.plainTextEdit.appendPlainText(content)

    def read_from_cmd(self, cmd, decode='utf-8'):
        try:
            with subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.DEVNULL,
                    stdin=subprocess.DEVNULL,
                    shell=True,
            ) as stream:
                stdout = stream.communicate()[0].decode(decode)
            raise PermissionError
            self.consoleWrite(stdout)
        except Exception as e:
            self.consoleWrite(repr(e))

    def startPatch(self):
        if not os.path.exists("hpatchz.exe"):
            QMessageBox.critical(self, "Error", "hpatchz.exe 文件不存在于当前路径下！\n\n请重新下载完整版软件！")
            return
        path50 = self.path50_textbox.text().replace("/", "\\")
        path51 = self.path51_textbox.text().replace("/", "\\")
        if path50 == "" or path51 == "":
            QMessageBox.critical(self, "Error", "路径不能为空！")
            return
        for file_name in ("deletefiles.txt", "hdifffiles.txt"):
            if not os.path.exists(os.path.join(path51, file_name)):
                QMessageBox.critical(self, "Error", file_name + " 文件不存在于差分包路径下！\n\n请确保你下载的是正确的差分包文件！")
                return
        paths_str = "完整客户端路径：\n      " + str(path50) + "\n\n差分包路径：\n      " + str(path51)
        ret_1 = QMessageBox.information(self, "Warning", "请确认你所填的路径是否正确：\n\n\n" + paths_str + "\n\n\n填写不正确的路径会导致合并失败，一旦出错只能重新解压重来！", QMessageBox.Yes | QMessageBox.No)
        if ret_1 == QMessageBox.Yes:
            ret_2 = QMessageBox.warning(self, "Warning!!!", "你真的确定填的是正确路径吗？\n\n\n" + paths_str + "\n\n\n这是最后一次警告，确认后将直接开始合并操作！", QMessageBox.Yes | QMessageBox.No)
            if ret_2 == QMessageBox.Yes:
                self.read_from_cmd("hpatchz.exe -v")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
