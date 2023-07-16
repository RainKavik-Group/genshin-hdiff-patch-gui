import json
import os
import shutil
import stat
import subprocess
import sys
import traceback

from PySide6 import QtCore
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import (QApplication, QFileDialog, QLineEdit, QMainWindow, QMessageBox)

from mainWindow import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        if self.checkBox.isChecked():
            self.checkAudio()
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
        self.plainTextEdit.moveCursor(QTextCursor.MoveOperation.End)  # (self.plainTextEdit.textCursor().End) in PyQt5
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
        # 之前写的太乱了，重构一下

        # 检查hpatchz.exe是否存在
        if not os.path.exists("hpatchz.exe"):
            QMessageBox.critical(self, "Error", "hpatchz.exe 文件不存在于当前路径下！\n\n请重新下载完整程序！")
            return

        # 格式化路径
        path50 = self.path50_textbox.text().replace("/", "\\")
        path51 = self.path51_textbox.text().replace("/", "\\")
        pathAudio = self.pathAudio_textbox.text().replace("/", "\\")
        if (path50 == "" or path51 == "") or (self.checkBox.isChecked() and pathAudio == ""):
            QMessageBox.critical(self, "Error", "路径不能为空！")
            return

        # 检查修补列表是否存在 / 游戏本体
        for file_name in ("deletefiles.txt", "hdifffiles.txt"):
            if not os.path.exists(os.path.join(path51, file_name)):
                QMessageBox.critical(self, "Error", "{} 文件不存在于游戏差分包路径下！\n\n请确保你下载的是正确的差分包文件！"
                                                    .format(file_name))
                return

        # 检查修补列表是否存在 / 语音
        if self.checkBox.isChecked():
            file_name = "hdifffiles.txt"
            if not os.path.exists(os.path.join(pathAudio, file_name)):
                QMessageBox.critical(self, "Error", "{} 文件不存在于语音差分包路径下！\n\n请确保你下载的是正确的差分包文件！"
                                                    .format(file_name))
                return

        # 路径列表，用于显示确认框用
        paths_str = "完整客户端路径：\n      " + str(path50) + "\n\n游戏差分包路径：\n      " + str(path51)
        if self.checkBox.isChecked():
            paths_str += "\n\n语音差分包路径：\n      " + str(pathAudio)

        def showConfirmDialog() -> bool:  # 显示两次确认框
            if QMessageBox.Yes == QMessageBox.information(self, "Warning",
                                          "请确认你所填的路径是否正确：\n\n\n" +
                                          paths_str +
                                          "\n\n\n填写不正确的路径会导致合并失败！",
                                          QMessageBox.Yes | QMessageBox.No):
                if QMessageBox.Yes == QMessageBox.warning(self, "Warning!!!",
                                          "你真的确定填的是正确路径吗？\n\n\n" +
                                          paths_str +
                                          "\n\n\n这是最后一次警告，确认后将直接开始合并操作！",
                                          QMessageBox.Yes | QMessageBox.No):
                    return True
                else:
                    return False
            else:
                return False

        if showConfirmDialog():  # 用户确认合并

            # 禁用控件，防止误操作
            self.plainTextEdit.setPlainText("")
            self.commandLinkButton.setEnabled(False)
            self.checkBox.setEnabled(False)

            try:
                def str_strip(content: str) -> str:  # 格式化字符串
                    return content.replace("\n", "").replace("/", "\\")

                def mkdir(path) -> bool:  # 新建文件夹
                    path = path.strip()
                    path = path.rstrip("\\")
                    isExists = os.path.exists(path)
                    if not isExists:
                        os.makedirs(path)
                        return True
                    else:
                        return False

                def movefile(oripath, tardir):  # 移动文件
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

                def do_some_copy(root_src_dir, root_dst_dir):  # 复用
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

                def remove_read_only(path: str):  # 移除只读权限
                    for root, dirs, files in os.walk(path):
                        for dir in dirs:
                            for file in files:
                                file_path = os.path.join(root, file)
                                os.chmod(str_strip(file_path), stat.S_IWRITE)
                                self.consoleWrite("{} done".format(file))
                                # QApplication.processEvents()  # 保证文本框实时显示内容

                # 目录定义
                rootPath_50 = path50 + "\\"
                rootPath_51 = path51 + "\\"
                rootPath_Audio = pathAudio + "\\"
                if self.checkBox.isChecked():
                    dirlist = [rootPath_50, rootPath_51, rootPath_Audio]
                else:
                    dirlist = [rootPath_50, rootPath_51]
                hpatchzPath = str_strip(os.path.join(os.getcwd(), "hpatchz.exe"))

                # 读修补列表
                with open(os.path.join(rootPath_51, "deletefiles.txt")) as file1:
                    deletefiles = file1.readlines()
                with open(os.path.join(rootPath_51, "hdifffiles.txt")) as file2:
                    hdifffiles = file2.readlines()
                if self.checkBox.isChecked():
                    with open(os.path.join(rootPath_Audio, "hdifffiles.txt")) as file3:
                        hdifffiles_audio = file3.readlines()

                # 修补前移除所有文件的只读权限
                # So miHoYo, Fuck You
                for eachDir in dirlist:
                    self.consoleWrite("————————————————————")
                    self.consoleWrite("0.Removing Read-Only in {} ...".format(eachDir))
                    remove_read_only(eachDir)

                # 移除Path50中需要删除的文件
                for eachFile1 in deletefiles:
                    self.consoleWrite("————————————————————")
                    self.consoleWrite("1.Removing " + eachFile1)
                    try:
                        os.remove(str_strip(os.path.join(rootPath_50, eachFile1)))
                    except FileNotFoundError:
                        self.consoleWrite("WARN: {} not found!".format(eachFile1))
                        continue

                # 新建temp文件夹，放修补后的文件
                tempPath = os.path.join(rootPath_50, "temp")
                mkdir(tempPath)

                # 修补游戏本体差分包，临时放在temp目录
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
                    os.remove(str_strip(os.path.join(rootPath_51, remoteName + ".hdiff")))

                # 修补语音差分包，临时放在temp目录
                if (self.checkBox.isChecked()):
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
                        os.remove(str_strip(os.path.join(rootPath_Audio, remoteName + ".hdiff")))

                # 复制修补后的游戏本体到游戏目录
                self.consoleWrite("————————————————————")
                self.consoleWrite("3.GAME Copying...")
                do_some_copy(rootPath_51, rootPath_50)

                # 复制修补后的音频到游戏目录
                if (self.checkBox.isChecked()):
                    self.consoleWrite("————————————————————")
                    self.consoleWrite("3.AUDIO Copying...")
                    do_some_copy(rootPath_Audio, rootPath_50)

                # 撒花
                self.consoleWrite("————————————————————")
                self.consoleWrite("Done!")
                QMessageBox.information(self, "Information", "合并操作成功完成！\n\n现在你可以退出程序了！")

            except Exception as e:
                self.consoleWrite(traceback.format_exc())
                self.commandLinkButton.setEnabled(True)
                QMessageBox.critical(self, "Error", "合并过程中抛出异常！\n\n请检查输出框来定位问题！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
