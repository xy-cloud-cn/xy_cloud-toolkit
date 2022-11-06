# -*- coding: utf-8 -*-
'''
@Author   : xy_cloud
@IDE      : PyCharm
@Project  : Python Project
@File     : main.py
@Time     : 2022/11/6 11:54
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import main_window

if __name__ == '__main__':
    # 只有直接运行这个脚本，才会往下执行
    # 别的脚本文件执行，不会调用这个条件句

    # 实例化，传参
    app = QApplication(sys.argv)

    # 创建对象
    mainWindow = QMainWindow()

    # 创建ui，引用main_window文件中的Ui_MainWindow类
    ui = main_window.Ui_MainWindow()
    # 调用Ui_MainWindow类的setupUi，创建初始组件
    ui.setupUi(mainWindow)
    # 创建窗口
    mainWindow.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec_())
