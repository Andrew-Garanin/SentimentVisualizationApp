# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addNewWordForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(411, 315)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelError = QLabel(self.centralwidget)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setGeometry(QRect(100, 40, 251, 16))
        font = QFont()
        font.setPointSize(7)
        self.labelError.setFont(font)
        self.labelError.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.newWordEdit = QLineEdit(self.centralwidget)
        self.newWordEdit.setObjectName(u"newWordEdit")
        self.newWordEdit.setGeometry(QRect(100, 10, 251, 31))
        self.newWordEdit.setStyleSheet(u"")
        self.chooseSentimentGroupBox = QGroupBox(self.centralwidget)
        self.chooseSentimentGroupBox.setObjectName(u"chooseSentimentGroupBox")
        self.chooseSentimentGroupBox.setGeometry(QRect(100, 60, 191, 161))
        self.radioButtonPSTV = QRadioButton(self.chooseSentimentGroupBox)
        self.radioButtonPSTV.setObjectName(u"radioButtonPSTV")
        self.radioButtonPSTV.setGeometry(QRect(30, 30, 131, 17))
        self.radioButtonPSTV.setChecked(True)
        self.radioButtonNGTV = QRadioButton(self.chooseSentimentGroupBox)
        self.radioButtonNGTV.setObjectName(u"radioButtonNGTV")
        self.radioButtonNGTV.setGeometry(QRect(30, 70, 131, 16))
        self.radioButtonNEUT = QRadioButton(self.chooseSentimentGroupBox)
        self.radioButtonNEUT.setObjectName(u"radioButtonNEUT")
        self.radioButtonNEUT.setGeometry(QRect(30, 110, 121, 20))
        self.buttonAdd = QPushButton(self.centralwidget)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setGeometry(QRect(110, 240, 75, 23))
        self.labelNewWord = QLabel(self.centralwidget)
        self.labelNewWord.setObjectName(u"labelNewWord")
        self.labelNewWord.setGeometry(QRect(10, 20, 91, 16))
        self.buttonCancel = QPushButton(self.centralwidget)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setGeometry(QRect(210, 240, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 411, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelError.setText("")
        self.newWordEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.chooseSentimentGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.radioButtonPSTV.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.radioButtonNGTV.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.radioButtonNEUT.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0439\u0442\u0440\u0430\u043b\u044c\u043d\u0430\u044f", None))
        self.buttonAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.labelNewWord.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e:", None))
        self.buttonCancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

