# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changeWordSentimentForm.ui'
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
        MainWindow.resize(409, 315)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelError = QLabel(self.centralwidget)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setGeometry(QRect(90, 40, 261, 16))
        font = QFont()
        font.setPointSize(7)
        self.labelError.setFont(font)
        self.labelError.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.labelWord = QLabel(self.centralwidget)
        self.labelWord.setObjectName(u"labelWord")
        self.labelWord.setGeometry(QRect(30, 20, 47, 13))
        self.chooseSentimentGroupBox = QGroupBox(self.centralwidget)
        self.chooseSentimentGroupBox.setObjectName(u"chooseSentimentGroupBox")
        self.chooseSentimentGroupBox.setGeometry(QRect(110, 60, 191, 161))
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
        self.buttonCancel = QPushButton(self.centralwidget)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setGeometry(QRect(220, 240, 75, 23))
        self.wordEdit = QLineEdit(self.centralwidget)
        self.wordEdit.setObjectName(u"wordEdit")
        self.wordEdit.setGeometry(QRect(90, 10, 261, 31))
        self.buttonChange = QPushButton(self.centralwidget)
        self.buttonChange.setObjectName(u"buttonChange")
        self.buttonChange.setGeometry(QRect(120, 240, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 409, 21))
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
        self.labelWord.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0432\u043e:", None))
        self.chooseSentimentGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.radioButtonPSTV.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.radioButtonNGTV.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.radioButtonNEUT.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0439\u0442\u0440\u0430\u043b\u044c\u043d\u0430\u044f", None))
        self.buttonCancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.wordEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.buttonChange.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

