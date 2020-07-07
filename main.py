import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                    QThreadPool, pyqtSignal)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Translator")
        self.initUI()

    def initUI(self):
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(260, 1860, 543, 183))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Translate")
        
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(350, 10, 483, 183))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Translator")
        
        
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(10, 200, 1053, 93))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 350, 1053, 150))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Translation:")
        
        
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("--")
        
        
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 550, 1053, 400))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setTitle("Verb:")
        
        
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(160, 60, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("--")
        
        
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 1000, 1053, 400))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setTitle("Verb:")
        
        
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(160, 60, 21, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("--")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())