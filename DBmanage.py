# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DBmanage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DBmanage(object):
    def setupUi(self, DBmanage):
        DBmanage.setObjectName("DBmanage")
        DBmanage.resize(474, 146)
        DBmanage.setMaximumSize(QtCore.QSize(580, 550))
        self.groupBox = QtWidgets.QGroupBox(DBmanage)
        self.groupBox.setGeometry(QtCore.QRect(380, 20, 81, 81))
        self.groupBox.setObjectName("groupBox")
        self.connButton = QtWidgets.QPushButton(self.groupBox)
        self.connButton.setGeometry(QtCore.QRect(0, 20, 81, 32))
        self.connButton.setObjectName("connButton")
        self.outButton = QtWidgets.QPushButton(self.groupBox)
        self.outButton.setGeometry(QtCore.QRect(0, 50, 81, 32))
        self.outButton.setObjectName("outButton")
        self.buttonBox = QtWidgets.QDialogButtonBox(DBmanage)
        self.buttonBox.setGeometry(QtCore.QRect(290, 110, 164, 31))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_db = QtWidgets.QLineEdit(DBmanage)
        self.lineEdit_db.setGeometry(QtCore.QRect(100, 80, 71, 21))
        self.lineEdit_db.setObjectName("lineEdit_db")
        self.lineEdit_psw = QtWidgets.QLineEdit(DBmanage)
        self.lineEdit_psw.setGeometry(QtCore.QRect(280, 50, 81, 21))
        self.lineEdit_psw.setObjectName("lineEdit_psw")
        self.lineEdit_table = QtWidgets.QLineEdit(DBmanage)
        self.lineEdit_table.setGeometry(QtCore.QRect(280, 80, 81, 21))
        self.lineEdit_table.setObjectName("lineEdit_table")
        self.label_2 = QtWidgets.QLabel(DBmanage)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 52, 19))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(DBmanage)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 65, 19))
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(DBmanage)
        self.label_11.setGeometry(QtCore.QRect(200, 80, 65, 19))
        self.label_11.setObjectName("label_11")
        self.lineEdit_usr = QtWidgets.QLineEdit(DBmanage)
        self.lineEdit_usr.setGeometry(QtCore.QRect(100, 50, 71, 21))
        self.lineEdit_usr.setObjectName("lineEdit_usr")
        self.label_4 = QtWidgets.QLabel(DBmanage)
        self.label_4.setGeometry(QtCore.QRect(220, 50, 39, 19))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(DBmanage)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 52, 19))
        self.label_3.setObjectName("label_3")
        self.lineEdit_host = QtWidgets.QLineEdit(DBmanage)
        self.lineEdit_host.setGeometry(QtCore.QRect(100, 20, 71, 21))
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.label = QtWidgets.QLabel(DBmanage)
        self.label.setGeometry(QtCore.QRect(30, 21, 52, 19))
        self.label.setObjectName("label")
        self.lineEdit_port = QtWidgets.QLineEdit(DBmanage)
        self.lineEdit_port.setGeometry(QtCore.QRect(280, 20, 81, 21))
        self.lineEdit_port.setObjectName("lineEdit_port")

        self.retranslateUi(DBmanage)
        self.buttonBox.accepted.connect(DBmanage.accept)
        self.buttonBox.rejected.connect(DBmanage.reject)
        QtCore.QMetaObject.connectSlotsByName(DBmanage)
        DBmanage.setTabOrder(self.lineEdit_host, self.lineEdit_port)
        DBmanage.setTabOrder(self.lineEdit_port, self.lineEdit_usr)
        DBmanage.setTabOrder(self.lineEdit_usr, self.lineEdit_psw)
        DBmanage.setTabOrder(self.lineEdit_psw, self.lineEdit_db)
        DBmanage.setTabOrder(self.lineEdit_db, self.lineEdit_table)
        DBmanage.setTabOrder(self.lineEdit_table, self.connButton)
        DBmanage.setTabOrder(self.connButton, self.outButton)

    def retranslateUi(self, DBmanage):
        _translate = QtCore.QCoreApplication.translate
        DBmanage.setWindowTitle(_translate("DBmanage", "导入并管理数据库"))
        self.groupBox.setTitle(_translate("DBmanage", "数据库连接"))
        self.connButton.setText(_translate("DBmanage", "连接"))
        self.outButton.setText(_translate("DBmanage", "断开"))
        self.label_2.setText(_translate("DBmanage", "端口号："))
        self.label_5.setText(_translate("DBmanage", "数据库名："))
        self.label_11.setText(_translate("DBmanage", "数据表名："))
        self.label_4.setText(_translate("DBmanage", "密码："))
        self.label_3.setText(_translate("DBmanage", "用户名："))
        self.label.setText(_translate("DBmanage", "主机名："))
