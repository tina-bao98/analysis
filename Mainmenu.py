# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(950, 600)
        MainWindow.setMinimumSize(QtCore.QSize(950, 595))
        MainWindow.setMaximumSize(QtCore.QSize(950, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 232, 68, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 232, 68, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 232, 68, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 232, 68, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 232, 68, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 232, 68, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 232, 68, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 232, 68, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 232, 68, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 9, 9, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("\n"
"background-image: url(:/新前缀/6-bg-4.jpg);\n"
"background-color: rgba(255, 232, 68, 216);\n"
"color: rgb(8, 9, 9);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(320, 210, 281, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("\n"
"font: 75 28pt \"Helvetica\";\n"
"\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 130, 371, 61))
        self.label_2.setStyleSheet("\n"
"font: 75 28pt \"Helvetica\";\n"
"\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.userButton = QtWidgets.QRadioButton(self.centralwidget)
        self.userButton.setGeometry(QtCore.QRect(280, 330, 131, 21))
        self.userButton.setObjectName("userButton")
        self.routineButton = QtWidgets.QRadioButton(self.centralwidget)
        self.routineButton.setGeometry(QtCore.QRect(510, 330, 131, 21))
        self.routineButton.setObjectName("routineButton")
        self.itemButton = QtWidgets.QRadioButton(self.centralwidget)
        self.itemButton.setGeometry(QtCore.QRect(510, 390, 131, 20))
        self.itemButton.setObjectName("itemButton")
        self.timeButton = QtWidgets.QRadioButton(self.centralwidget)
        self.timeButton.setGeometry(QtCore.QRect(280, 390, 131, 21))
        self.timeButton.setObjectName("timeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 22))
        self.menubar.setTabletTracking(True)
        self.menubar.setDefaultUp(True)
        self.menubar.setObjectName("menubar")
        self.Filemenu = QtWidgets.QMenu(self.menubar)
        self.Filemenu.setObjectName("Filemenu")
        self.menu_Open = QtWidgets.QMenu(self.Filemenu)
        self.menu_Open.setObjectName("menu_Open")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Input_csv = QtWidgets.QAction(MainWindow)
        self.action_Input_csv.setObjectName("action_Input_csv")
        self.action_Input_DataBase_3 = QtWidgets.QAction(MainWindow)
        self.action_Input_DataBase_3.setObjectName("action_Input_DataBase_3")
        self.action_Save = QtWidgets.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_png = QtWidgets.QAction(MainWindow)
        self.action_png.setObjectName("action_png")
        self.action_jpeg = QtWidgets.QAction(MainWindow)
        self.action_jpeg.setObjectName("action_jpeg")
        self.action_pdf = QtWidgets.QAction(MainWindow)
        self.action_pdf.setObjectName("action_pdf")
        self.action_svg = QtWidgets.QAction(MainWindow)
        self.action_svg.setObjectName("action_svg")
        self.menu_Open.addAction(self.action_Input_csv)
        self.menu_Open.addAction(self.action_Input_DataBase_3)
        self.Filemenu.addAction(self.menu_Open.menuAction())
        self.Filemenu.addSeparator()
        self.Filemenu.addAction(self.action_Quit)
        self.menubar.addAction(self.Filemenu.menuAction())

        self.retranslateUi(MainWindow)
        self.action_Quit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "请选择所要分析的内容"))
        self.label_2.setText(_translate("MainWindow", " 欢迎使用本用户行为分析系统"))
        self.userButton.setText(_translate("MainWindow", "关键用户指标分析"))
        self.routineButton.setText(_translate("MainWindow", "用户行为路径分析"))
        self.itemButton.setText(_translate("MainWindow", "用户行为商品分析"))
        self.timeButton.setText(_translate("MainWindow", "用户行为时间分析"))
        self.Filemenu.setTitle(_translate("MainWindow", "文件"))
        self.menu_Open.setTitle(_translate("MainWindow", "打开..."))
        self.action_Input_csv.setText(_translate("MainWindow", "导入csv文件"))
        self.action_Input_DataBase_3.setText(_translate("MainWindow", "导入数据库"))
        self.action_Save.setText(_translate("MainWindow", "保存"))
        self.action_Quit.setText(_translate("MainWindow", "退出"))
        self.action_png.setText(_translate("MainWindow", "png"))
        self.action_jpeg.setText(_translate("MainWindow", "jpeg"))
        self.action_pdf.setText(_translate("MainWindow", "pdf"))
        self.action_svg.setText(_translate("MainWindow", "svg"))
import 背景图2
import 背景图
