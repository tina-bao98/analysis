# -*- coding: utf-8 -*-
import sys
from InputCsv import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox, QProgressBar
from PyQt5.QtCore import *


class inputcsv(QDialog, Ui_Dialog):

    # 定义信号
    Signal = pyqtSignal(str)
    f = 0
    def __init__(self):
        super(inputcsv, self).__init__()
        self.setupUi(self)
        self.toolButton.clicked.connect(self.open_event)
        # 导入按钮初始不可用
        self.buttonBox.setEnabled(False)

        #self.timer = QBasicTimer()

    def open_event(self):
        try:
            filename, _ = QFileDialog.getOpenFileName(None,
                                                      '选中文件',
                                                      '/Users/baoyixuan/PycharmProjects',
                                                      'CSV Files(*.csv)')
            self.lineEdit.setText(filename)
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '错误警告', '文件打开错误，文件可能不存在')
        else:
            QMessageBox.about(self, '提示', '文件打开成功')
            self.buttonBox.setEnabled(True)
            # 传递文件路径
            self.Signal.emit(filename)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cv = inputcsv()
    cv.show()
    app.exec_()
