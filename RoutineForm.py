# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RoutineForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RoutineForm(object):
    def setupUi(self, RoutineForm):
        RoutineForm.setObjectName("RoutineForm")
        RoutineForm.resize(850, 502)
        RoutineForm.setMinimumSize(QtCore.QSize(800, 502))
        RoutineForm.setMaximumSize(QtCore.QSize(900, 600))
        self.pushButton_back = QtWidgets.QPushButton(RoutineForm)
        self.pushButton_back.setGeometry(QtCore.QRect(20, 430, 181, 32))
        self.pushButton_back.setObjectName("pushButton_back")
        self.label = QtWidgets.QLabel(RoutineForm)
        self.label.setGeometry(QtCore.QRect(20, 50, 51, 21))
        self.label.setObjectName("label")
        self.qwebengine = QtWebEngineWidgets.QWebEngineView(RoutineForm)
        self.qwebengine.setGeometry(QtCore.QRect(199, 19, 631, 461))
        self.qwebengine.setObjectName("qwebengine")
        self.groupBox_2 = QtWidgets.QGroupBox(RoutineForm)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 220, 161, 61))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_make = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_make.setGeometry(QtCore.QRect(10, 0, 141, 31))
        self.pushButton_make.setObjectName("pushButton_make")
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_save.setGeometry(QtCore.QRect(10, 30, 141, 32))
        self.pushButton_save.setObjectName("pushButton_save")
        self.lineEdit = QtWidgets.QLineEdit(RoutineForm)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 121, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_quit = QtWidgets.QPushButton(RoutineForm)
        self.pushButton_quit.setGeometry(QtCore.QRect(20, 460, 181, 31))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.groupBox = QtWidgets.QGroupBox(RoutineForm)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 161, 81))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_csv = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_csv.setGeometry(QtCore.QRect(10, 20, 141, 31))
        palette = QtGui.QPalette()
        self.pushButton_csv.setPalette(palette)
        self.pushButton_csv.setObjectName("pushButton_csv")
        self.pushButton_db = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_db.setGeometry(QtCore.QRect(10, 50, 141, 31))
        self.pushButton_db.setObjectName("pushButton_db")
        self.label_2 = QtWidgets.QLabel(RoutineForm)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 181, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox_type = QtWidgets.QComboBox(RoutineForm)
        self.comboBox_type.setEnabled(True)
        self.comboBox_type.setGeometry(QtCore.QRect(20, 180, 171, 32))
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")

        self.retranslateUi(RoutineForm)
        self.pushButton_back.clicked.connect(RoutineForm.close)
        #self.pushButton_quit.clicked.connect(RoutineForm.close)
        QtCore.QMetaObject.connectSlotsByName(RoutineForm)
        RoutineForm.setTabOrder(self.lineEdit, self.pushButton_csv)
        RoutineForm.setTabOrder(self.pushButton_csv, self.pushButton_db)
        RoutineForm.setTabOrder(self.pushButton_db, self.comboBox_type)
        RoutineForm.setTabOrder(self.comboBox_type, self.pushButton_make)
        RoutineForm.setTabOrder(self.pushButton_make, self.pushButton_save)
        RoutineForm.setTabOrder(self.pushButton_save, self.pushButton_back)
        RoutineForm.setTabOrder(self.pushButton_back, self.pushButton_quit)

    def retranslateUi(self, RoutineForm):
        _translate = QtCore.QCoreApplication.translate
        RoutineForm.setWindowTitle(_translate("RoutineForm", "用户行为路径分析"))
        self.pushButton_back.setText(_translate("RoutineForm", "返回主界面"))
        self.label.setText(_translate("RoutineForm", "图表名："))
        self.pushButton_make.setText(_translate("RoutineForm", "生成图表"))
        self.pushButton_save.setText(_translate("RoutineForm", "保存图表"))
        self.pushButton_quit.setText(_translate("RoutineForm", "退出系统"))
        self.groupBox.setTitle(_translate("RoutineForm", "选择一种数据源"))
        self.pushButton_csv.setText(_translate("RoutineForm", "导入csv文件"))
        self.pushButton_db.setText(_translate("RoutineForm", "导入数据库"))
        self.label_2.setText(_translate("RoutineForm", "以转化漏斗模型分析路径转化率"))
        self.comboBox_type.setItemText(0, _translate("RoutineForm", "图表保存格式"))
        self.comboBox_type.setItemText(1, _translate("RoutineForm", "png"))
        self.comboBox_type.setItemText(2, _translate("RoutineForm", "jpeg"))
        self.comboBox_type.setItemText(3, _translate("RoutineForm", "pdf"))
        self.comboBox_type.setItemText(4, _translate("RoutineForm", "svg"))
from PyQt5 import QtWebEngineWidgets
