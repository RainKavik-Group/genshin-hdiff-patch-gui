# genshin-hdiff-patch-gui

GUI图形界面 自动完成hdiff差分包更新

## 编译：

1. 安装Python 3.8, 新建virtualvenv
2. 安装依赖包：pyqt5, pyqt5-tools, pyinstaller
3. pyinstaller -D -w -i RoundCorner.ico main.py
   编译成一个目录，包含运行库文件，路径./dist/main
   要编译成单文件用这个：pyinstaller -F -w -i RoundCorner.ico main.py
4. 把hpatchz.exe手动复制进main.exe同级目录（无论是编译成目录还是单文件都需要复制）
5. Enjoy.
