# genshin-hdiff-patch-gui

GUI图形界面 自动完成hdiff差分包更新

## 构建：

1. 安装Python 3.8, 新建virtualvenv
2. 安装软件包：pyside6, pyinstaller  
3. pyinstaller -D -w -i RoundCorner.ico main.py  
   构建成一个目录，包含运行库文件，路径./dist/main  
   要构建成单文件用这个：pyinstaller -F -w -i RoundCorner.ico main.py
4. 把hpatchz.exe手动复制进main.exe同级目录（无论是构建成目录还是单文件都需要复制）
5. Enjoy.
