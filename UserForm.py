# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserForm(object):
    def setupUi(self, UserForm):
        UserForm.setObjectName("UserForm")
        UserForm.resize(850, 502)
        UserForm.setMinimumSize(QtCore.QSize(800, 502))
        UserForm.setMaximumSize(QtCore.QSize(900, 600))
        UserForm.setBaseSize(QtCore.QSize(800, 502))
        palette = QtGui.QPalette()
        UserForm.setPalette(palette)
        UserForm.setStyleSheet("")
        self.groupBox = QtWidgets.QGroupBox(UserForm)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 161, 81))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_csv = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_csv.setGeometry(QtCore.QRect(10, 20, 141, 31))
        palette = QtGui.QPalette()
        self.pushButton_csv.setPalette(palette)
        self.pushButton_csv.setObjectName("pushButton_csv")
        self.pushButton_db = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_db.setGeometry(QtCore.QRect(10, 50, 141, 31))
        self.pushButton_db.setObjectName("pushButton_db")
        self.label = QtWidgets.QLabel(UserForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 51, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(UserForm)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 121, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_back = QtWidgets.QPushButton(UserForm)
        self.pushButton_back.setGeometry(QtCore.QRect(20, 430, 181, 32))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_quit = QtWidgets.QPushButton(UserForm)
        self.pushButton_quit.setGeometry(QtCore.QRect(20, 460, 181, 31))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.groupBox_2 = QtWidgets.QGroupBox(UserForm)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 250, 161, 61))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_make = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_make.setGeometry(QtCore.QRect(10, 0, 141, 31))
        self.pushButton_make.setObjectName("pushButton_make")
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_save.setGeometry(QtCore.QRect(10, 30, 141, 32))
        self.pushButton_save.setObjectName("pushButton_save")
        self.qwebengine = QtWebEngineWidgets.QWebEngineView(UserForm)
        self.qwebengine.setGeometry(QtCore.QRect(199, 19, 631, 461))
        self.qwebengine.setObjectName("qwebengine")
        self.layoutWidget = QtWidgets.QWidget(UserForm)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 160, 171, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_choose = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_choose.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.comboBox_choose.setPalette(palette)
        self.comboBox_choose.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.comboBox_choose.setObjectName("comboBox_choose")
        self.comboBox_choose.addItem("")
        self.comboBox_choose.addItem("")
        self.comboBox_choose.addItem("")
        self.comboBox_choose.addItem("")
        self.gridLayout.addWidget(self.comboBox_choose, 0, 0, 1, 1)
        self.comboBox_type = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_type.setEnabled(True)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.gridLayout.addWidget(self.comboBox_type, 1, 0, 1, 1)

        self.retranslateUi(UserForm)
        self.pushButton_back.clicked.connect(UserForm.close)
        self.pushButton_csv.clicked.connect(UserForm.open_csv)
        self.pushButton_db.clicked.connect(UserForm.open_db)
        #self.pushButton_quit.clicked.connect(UserForm.close_event)
        QtCore.QMetaObject.connectSlotsByName(UserForm)
        UserForm.setTabOrder(self.lineEdit, self.pushButton_csv)
        UserForm.setTabOrder(self.pushButton_csv, self.pushButton_db)
        UserForm.setTabOrder(self.pushButton_db, self.comboBox_choose)
        UserForm.setTabOrder(self.comboBox_choose, self.comboBox_type)
        UserForm.setTabOrder(self.comboBox_type, self.pushButton_make)
        UserForm.setTabOrder(self.pushButton_make, self.pushButton_save)
        UserForm.setTabOrder(self.pushButton_save, self.pushButton_back)
        UserForm.setTabOrder(self.pushButton_back, self.pushButton_quit)

    def retranslateUi(self, UserForm):
        _translate = QtCore.QCoreApplication.translate
        UserForm.setWindowTitle(_translate("UserForm", "关键用户指标分析"))
        self.groupBox.setTitle(_translate("UserForm", "选择一种数据源"))
        self.pushButton_csv.setText(_translate("UserForm", "导入csv文件"))
        self.pushButton_db.setText(_translate("UserForm", "导入数据库"))
        self.label.setText(_translate("UserForm", "图表名："))
        self.pushButton_back.setText(_translate("UserForm", "返回主界面"))
        self.pushButton_quit.setText(_translate("UserForm", "退出系统"))
        self.pushButton_make.setText(_translate("UserForm", "生成图表"))
        self.pushButton_save.setText(_translate("UserForm", "保存图表"))
        self.comboBox_choose.setItemText(0, _translate("UserForm", "具体分析内容选择"))
        self.comboBox_choose.setItemText(1, _translate("UserForm", "日均用户指标"))
        self.comboBox_choose.setItemText(2, _translate("UserForm", "日均用户比例指标"))
        self.comboBox_choose.setItemText(3, _translate("UserForm", "用户活跃天数分布"))
        self.comboBox_type.setItemText(0, _translate("UserForm", "图表保存格式"))
        self.comboBox_type.setItemText(1, _translate("UserForm", "png"))
        self.comboBox_type.setItemText(2, _translate("UserForm", "jpeg"))
        self.comboBox_type.setItemText(3, _translate("UserForm", "pdf"))
        self.comboBox_type.setItemText(4, _translate("UserForm", "svg"))
from PyQt5 import QtWebEngineWidgets
