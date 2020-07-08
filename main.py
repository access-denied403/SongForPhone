import sys
import textwrap
from googletrans import Translator
from PyDictionary import PyDictionary
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable 
from PyQt5.QtCore import QThread, QThreadPool, pyqtSignal

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Word Definition")
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
        self.pushButton.clicked.connect(self.pressed)
        
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(300, 10, 483, 183))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Word Definition")
        
        
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(30, 200, 1000, 93))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setPlaceholderText("Enter Word")
        
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(30, 350, 1000, 150))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(18)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Translation:")
        
        
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 430, 950, 50))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 550, 1000, 400))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(18)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setTitle("Noun:")
        
        
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(50, 600, 900, 300))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 1000, 1000, 400))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(18)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setTitle("Verb:")
        
        
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(50, 1000, 900, 300))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)


    def pressed(self):
        word = self.lineEdit.text()
        noun, verb = self.definition(word)
        try:
            noun = str(*noun[0])
            verb = str(*verb[0])
        except:
            noun = str(noun[0])
            verb = str(verb[0])

        translated_word = self.translate_func(word).text
        translated_noun = self.translate_func(noun).text
        translated_verb = self.translate_func(verb).text
        
        self.label_2.setText(translated_word)
        self.label_3.setText(textwrap.fill(translated_noun, 40))
        self.label_4.setText(textwrap.fill(translated_verb, 40))


    def definition(self, word):
        nouns, verbs = [], []
        dictionary = PyDictionary()
        word = self.translate_func(word).text
        my_meaning = dictionary.meaning(word)
        try:
            if my_meaning['Noun']: nouns.append(my_meaning['Noun'][0])
            if my_meaning['Verb']: verbs.append(my_meaning['Verb'][0])
        except:
            nouns.append("No Data")
            verbs.append("No Data")
        return nouns, verbs


    def translate_func(self, words):
        translator = Translator(service_urls=["translate.google.com"])
        translation = translator.translate(words, dest="en")
        return translation


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
