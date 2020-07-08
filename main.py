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
        self.translate_Button = QtWidgets.QPushButton(self)
        self.translate_Button.setGeometry(QtCore.QRect(260, 1860, 543, 183))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.translate_Button.setFont(font)
        self.translate_Button.setObjectName("translate_Button")
        self.translate_Button.setText("Translate")
        self.translate_Button.clicked.connect(self.pressed)
        
        self.top_label = QtWidgets.QLabel(self)
        self.top_label.setGeometry(QtCore.QRect(300, 10, 483, 183))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(26)
        self.top_label.setFont(font)
        self.top_label.setObjectName("top_label")
        self.top_label.setText("Word Definition")
        
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(30, 200, 1000, 93))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setPlaceholderText("Enter Word")
        

        self.translation_field = QtWidgets.QGroupBox(self)
        self.translation_field.setGeometry(QtCore.QRect(30, 350, 1000, 150))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(18)
        self.translation_field.setFont(font)
        self.translation_field.setObjectName("translation_field")
        self.translation_field.setTitle("Translation:")
        
        self.translation_label = QtWidgets.QLabel(self)
        self.translation_label.setGeometry(QtCore.QRect(50, 430, 950, 50))
        self.translation_label.setObjectName("translation_label")
        self.translation_label.setText("")
        self.translation_label.setAlignment(QtCore.Qt.AlignCenter)
        

        self.noun_field = QtWidgets.QGroupBox(self)
        self.noun_field.setGeometry(QtCore.QRect(30, 550, 1000, 400))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(18)
        self.noun_field.setFont(font)
        self.noun_field.setObjectName("noun_field")
        self.noun_field.setTitle("Noun:")
        
        self.noun_label = QtWidgets.QLabel(self)
        self.noun_label.setGeometry(QtCore.QRect(50, 600, 900, 300))
        self.noun_label.setObjectName("noun_label")
        self.noun_label.setText("")
        self.noun_label.setAlignment(QtCore.Qt.AlignCenter)
        
        
        self.verb_field = QtWidgets.QGroupBox(self)
        self.verb_field.setGeometry(QtCore.QRect(30, 1000, 1000, 400))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(18)
        self.verb_field.setFont(font)
        self.verb_field.setObjectName("verb_field")
        self.verb_field.setTitle("Verb:")
        
        self.verb_label = QtWidgets.QLabel(self)
        self.verb_label.setGeometry(QtCore.QRect(50, 1000, 900, 300))
        self.verb_label.setObjectName("verb_label")
        self.verb_label.setText("")
        self.verb_label.setAlignment(QtCore.Qt.AlignCenter)


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
        
        self.translation_label.setText(translated_word)
        self.noun_label.setText(textwrap.fill(translated_noun, 40))
        self.verb_label.setText(textwrap.fill(translated_verb, 40))


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
