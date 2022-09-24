import json
import shutil
import stat
import sys
import os
import traceback
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
        self.path51_button.clicked.connect(lambda: self.selectFolder(self.path51_textbox, "选择游戏差分包路径："))
        self.pathAudio_button.clicked.connect(lambda: self.selectFolder(self.pathAudio_textbox, "选择语音差分包路径："))
        self.checkBox.clicked.connect(self.checkAudio)
        self.commandLinkButton.clicked.connect(self.startPatch)

    def selectFolder(self, textbox: QLineEdit, title: str):
        dialog = QFileDialog()
        ret_path = dialog.getExistingDirectory(self, title)
        if ret_path != "":
            textbox.setText(ret_path)

    def checkAudio(self):
        self.pathAudio_textbox.setEnabled(self.checkBox.isChecked())
        self.pathAudio_button.setEnabled(self.checkBox.isChecked())

    def consoleWrite(self, content: str):
        self.plainTextEdit.appendPlainText(content)
        self.plainTextEdit.moveCursor(self.plainTextEdit.textCursor().End)
        QApplication.processEvents()  # 保证文本框实时显示内容
        return

    def execCMD(self, cmd, decode="gbk"):
        with subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                shell=True,
        ) as stream:
            stdout = stream.communicate()[0].decode(decode)
        self.consoleWrite(stdout)
        return

    def startPatch(self):
        if not os.path.exists("hpatchz.exe"):
            QMessageBox.critical(self, "Error", "hpatchz.exe 文件不存在于当前路径下！\n\n请重新下载完整版软件！")
            return
        path50 = self.path50_textbox.text().replace("/", "\\")
        path51 = self.path51_textbox.text().replace("/", "\\")
        pathAudio = self.pathAudio_textbox.text().replace("/", "\\")
        if (path50 == "" or path51 == "") or (self.checkBox.isChecked() and pathAudio == ""):
            QMessageBox.critical(self, "Error", "路径不能为空！")
            return
        '''for mypath in (path50, path51):
            if " " in mypath:
                QMessageBox.critical(self, "Error", "路径中不能含有空格！")
                return'''
        for file_name in ("deletefiles.txt", "hdifffiles.txt"):
            if (not os.path.exists(os.path.join(path51, file_name))) or (
            not os.path.exists(os.path.join(pathAudio, "hdifffiles.txt"))):
                QMessageBox.critical(self, "Error",
                                     file_name + " 文件不存在于差分包路径下！\n\n请确保你下载的是正确的差分包文件！")
                return
        paths_str = "完整客户端路径：\n      " + str(path50) + "\n\n游戏差分包路径：\n      " + str(path51)
        if self.checkBox.isChecked():
            paths_str += "\n\n语音差分包路径：\n      " + str(pathAudio)
        ret_1 = QMessageBox.information(self, "Warning",
                                        "请确认你所填的路径是否正确：\n\n\n" + paths_str + "\n\n\n填写不正确的路径会导致合并失败，一旦出错只能重新解压重来！",
                                        QMessageBox.Yes | QMessageBox.No)
        if ret_1 == QMessageBox.Yes:
            ret_2 = QMessageBox.warning(self, "Warning!!!",
                                        "你真的确定填的是正确路径吗？\n\n\n" + paths_str + "\n\n\n这是最后一次警告，确认后将直接开始合并操作！",
                                        QMessageBox.Yes | QMessageBox.No)
            if ret_2 == QMessageBox.Yes:
                self.plainTextEdit.setPlainText("")
                self.commandLinkButton.setEnabled(False)
                self.checkBox.setEnabled(False)
                try:
                    def str_strip(content: str):
                        return content.replace("\n", "").replace("/", "\\")

                    def mkdir(path):
                        path = path.strip()
                        path = path.rstrip("\\")
                        isExists = os.path.exists(path)
                        if not isExists:
                            os.makedirs(path)
                            return True
                        else:
                            return False

                    def movefile(oripath, tardir):
                        filename = os.path.basename(oripath)
                        tarpath = os.path.join(tardir, filename)
                        if not os.path.exists(oripath):
                            self.consoleWrite('the dir is not exist:%s' % oripath)
                            status = 0
                        else:
                            if os.path.exists(tardir):
                                if os.path.exists(tarpath):
                                    os.remove(tarpath)
                            else:
                                os.makedirs(tardir)
                            shutil.move(oripath, tardir)
                            status = 1
                        return status

                    # rootPath_50 = r"C:\Users\MLChinoo\Downloads\Compressed\GenshinImpact_3.0.50_beta_3" + "\\"
                    # rootPath_51 = r"C:\Users\MLChinoo\Downloads\Compressed\game_3.0.50_3.0.51_hdiff_XoHbpS403sPYEw9K_2" + "\\"
                    # hpatchzPath = r"C:\Users\MLChinoo\Downloads\Compressed\hpatchz.exe"
                    rootPath_50 = path50 + "\\"
                    rootPath_51 = path51 + "\\"
                    rootPath_Audio = pathAudio + "\\"
                    hpatchzPath = str_strip(os.path.join(os.getcwd(), "hpatchz.exe"))

                    with open(os.path.join(rootPath_51, "deletefiles.txt")) as file1:
                        deletefiles = file1.readlines()
                    with open(os.path.join(rootPath_51, "hdifffiles.txt")) as file2:
                        hdifffiles = file2.readlines()
                    with open(os.path.join(rootPath_Audio, "hdifffiles.txt")) as file3:
                        hdifffiles_audio = file3.readlines()

                    for eachFile1 in deletefiles:
                        # print(os.path.join(rootPath_50, eachFile1))
                        self.consoleWrite("————————————————————")
                        self.consoleWrite("1.Removing " + eachFile1)
                        os.remove(str_strip(os.path.join(rootPath_50, eachFile1)))

                    tempPath = os.path.join(rootPath_50, "temp")
                    mkdir(tempPath)
                    for eachLine2 in hdifffiles:
                        tempArray = json.loads(eachLine2)
                        remoteName = tempArray["remoteName"]
                        baseName = os.path.basename(remoteName)
                        self.consoleWrite("————————————————————")
                        self.consoleWrite("2.GAME Patching " + baseName)
                        self.execCMD('"' + hpatchzPath + '" "{}" "{}" "{}"'.format(
                            str_strip(os.path.join(rootPath_50, remoteName)),
                            str_strip(os.path.join(rootPath_51, remoteName + ".hdiff")),
                            str_strip(os.path.join(tempPath, baseName))))
                        movefile(str_strip(os.path.join(tempPath, baseName)),
                                 str_strip(os.path.join(rootPath_51, remoteName)))
                        # print(os.path.join(tempPath, baseName), os.path.join(rootPath_51, remoteName))
                        # print(os.path.join(rootPath_51, remoteName + ".hdiff"))
                        os.remove(str_strip(os.path.join(rootPath_51, remoteName + ".hdiff")))

                    tempPath = os.path.join(rootPath_50, "temp_audio")
                    mkdir(tempPath)
                    for eachLine2 in hdifffiles_audio:
                        tempArray = json.loads(eachLine2)
                        remoteName = tempArray["remoteName"]
                        baseName = os.path.basename(remoteName)
                        self.consoleWrite("————————————————————")
                        self.consoleWrite("2.AUDIO Patching " + baseName)
                        self.execCMD('"' + hpatchzPath + '" "{}" "{}" "{}"'.format(
                            str_strip(os.path.join(rootPath_50, remoteName)),
                            str_strip(os.path.join(rootPath_Audio, remoteName + ".hdiff")),
                            str_strip(os.path.join(tempPath, baseName))))
                        movefile(str_strip(os.path.join(tempPath, baseName)),
                                 str_strip(os.path.join(rootPath_Audio, remoteName)))
                        # print(os.path.join(tempPath, baseName), os.path.join(rootPath_51, remoteName))
                        # print(os.path.join(rootPath_51, remoteName + ".hdiff"))
                        os.remove(str_strip(os.path.join(rootPath_Audio, remoteName + ".hdiff")))

                    self.consoleWrite("————————————————————")
                    self.consoleWrite("3.GAME Copying...")
                    root_src_dir = rootPath_51
                    root_dst_dir = rootPath_50
                    for mypath in (root_dst_dir, root_src_dir):
                        try:
                            os.chmod(
                                str_strip(os.path.join(mypath, "GenshinImpact_Data", "Plugins", "crashreport.exe")),
                                stat.S_IWRITE)
                        except FileNotFoundError:
                            try:
                                os.chmod(
                                    str_strip(os.path.join(mypath, "YuanShen_Data", "Plugins", "crashreport.exe")),
                                    stat.S_IWRITE)
                            except FileNotFoundError:
                                pass
                                # self.consoleWrite("Warning: crashreport.exe not found, may cause some problems!")
                    for src_dir, dirs, files in os.walk(root_src_dir):
                        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
                        if not os.path.exists(dst_dir):
                            os.makedirs(dst_dir)
                        for file_ in files:
                            src_file = os.path.join(src_dir, file_)
                            dst_file = os.path.join(dst_dir, file_)
                            if os.path.exists(dst_file):
                                # in case of the src and dst are the same file
                                if os.path.samefile(src_file, dst_file):
                                    continue
                                os.remove(dst_file)
                            shutil.move(src_file, dst_dir)

                    self.consoleWrite("————————————————————")
                    self.consoleWrite("3.AUDIO Copying...")
                    root_src_dir = rootPath_Audio
                    root_dst_dir = rootPath_50
                    for mypath in (root_dst_dir, root_src_dir):
                        try:
                            os.chmod(
                                str_strip(os.path.join(mypath, "GenshinImpact_Data", "Plugins", "crashreport.exe")),
                                stat.S_IWRITE)
                        except FileNotFoundError:
                            try:
                                os.chmod(
                                    str_strip(os.path.join(mypath, "YuanShen_Data", "Plugins", "crashreport.exe")),
                                    stat.S_IWRITE)
                            except FileNotFoundError:
                                pass
                                # self.consoleWrite("Warning: crashreport.exe not found, may cause some problems!")
                    for src_dir, dirs, files in os.walk(root_src_dir):
                        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
                        if not os.path.exists(dst_dir):
                            os.makedirs(dst_dir)
                        for file_ in files:
                            src_file = os.path.join(src_dir, file_)
                            dst_file = os.path.join(dst_dir, file_)
                            if os.path.exists(dst_file):
                                # in case of the src and dst are the same file
                                if os.path.samefile(src_file, dst_file):
                                    continue
                                os.remove(dst_file)
                            shutil.move(src_file, dst_dir)

                    self.consoleWrite("————————————————————")
                    self.consoleWrite("Done!")

                    QMessageBox.information(self, "Information", "合并操作成功完成！\n\n现在你可以退出本软件了！")
                except Exception as e:
                    self.consoleWrite(traceback.format_exc())
                    self.commandLinkButton.setEnabled(True)
                    QMessageBox.critical(self, "Error", "合并过程中抛出异常！\n\n请检查输出框来定位问题！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
