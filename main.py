# -*- coding: utf-8 -*-
from Mainmenu import *
from UserForm import *
from RoutineForm import *
from TimeForm import *
from ItemForm import *
from csvToMS import inputcsv
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QDialog

import sys

class mainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

class userForm(QWidget,Ui_UserForm):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

class routineForm(QWidget,Ui_RoutineForm):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

class timeForm(QWidget,Ui_TimeForm):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

class itemForm(QWidget,Ui_ItemForm):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = mainWindow()

    user = userForm()
    main.userButton.clicked.connect(user.show)
    routine = routineForm()
    main.routineButton.clicked.connect(routine.show)
    time = timeForm()
    main.timeButton.clicked.connect(time.show)
    item = itemForm()
    main.itemButton.clicked.connect(item.show)
    csv = inputcsv()
    main.action_Input_csv.triggered.connect(csv.show)

    main.show()
    sys.exit(app.exec_())







