# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem, QLineEdit, QTableView
from PyQt5.QtCore import pyqtSignal
from DBmanage import *
import pandas as pd
import pymysql
import sys

class dbm(QDialog, Ui_DBmanage):

    dbSignal = pyqtSignal(str, int, str, str, str, str)
    db_connection = 0
    
    def __init__(self):
        super(dbm, self).__init__()
        self.setupUi(self)
        # 槽函数
        self.connButton.clicked.connect(self.mysqlconnect)
        self.outButton.clicked.connect(self.mysqldisconnect)
        #self.addButton.clicked.connect(self.add_data)
        #self.delButton.clicked.connect(self.del_data)
        # 初始化
        self.outButton.setEnabled(False)
        #self.addButton.setEnabled(False)
        #self.delButton.setEnabled(False)
        #self.tableWidget.setHorizontalHeaderLabels(['用户id', '商品id', '商品类目id', '用户行为类型', '时间戳'])


    # 数据库连接函数
    def mysqlconnect(self):
        try:
            dbhost = self.lineEdit_host.text()
            dbport = int(self.lineEdit_port.text())
            dbuser = self.lineEdit_usr.text()
            dbpsw = self.lineEdit_psw.text()
            dbname = self.lineEdit_db.text()
            self.conn = pymysql.connect(host=dbhost,
                                        port=dbport,
                                        user=dbuser,
                                        passwd=dbpsw,
                                        db=dbname,
                                        charset="utf8")
            txt_name = self.lineEdit_table.text()
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '警告', '数据库信息未完全输入，或输入的信息有误，请重新输入')
        else:
            self.connButton.setEnabled(False)
            self.outButton.setEnabled(True)
            self.dbSignal.emit(dbhost, dbport, dbuser, dbpsw, dbname, txt_name)


    # 断开连接函数
    def mysqldisconnect(self):
        try:
            self.conn.close()
            QMessageBox.about(self, '提示', '断开成功')
            self.lineEdit_host.clear()
            self.lineEdit_port.clear()
            self.lineEdit_usr.clear()
            self.lineEdit_psw.clear()
            self.lineEdit_db.clear()
            self.lineEdit_table.clear()
            self.connButton.setEnabled(True)
            self.outButton.setEnabled(False)
            db_connection = 0
            return db_connection
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dbm = dbm()
    dbm.show()
    app.exec_()
