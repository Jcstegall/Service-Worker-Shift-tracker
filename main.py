from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import mysql.connector as con

ui, _  = loadUiType('ValetTracker.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.tabWidget.tabBar().setVisible(False) #hides the tabbar 
        self.tabWidget.setCurrentIndex(0) #sets the home page the first to pop up
        self.btn_Create_New_Entry.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1)) #sets the home page the first to pop up
        self.btn_My_Stats.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))  #naigates to the add new stat once clicked button
        self.btn_Raw_Data.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3)) #navigates to the calculated stats page 
        #self.btn_TBD.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3)) #navigates to the TBD page that will be set up later 


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

