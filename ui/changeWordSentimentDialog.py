# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changeWordSentimentDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_changeWordSentimentDialog(object):
    def setupUi(self, changeWordSentimentDialog):
        if not changeWordSentimentDialog.objectName():
            changeWordSentimentDialog.setObjectName(u"changeWordSentimentDialog")
        changeWordSentimentDialog.resize(410, 315)
        self.wordEdit = QLineEdit(changeWordSentimentDialog)
        self.wordEdit.setObjectName(u"wordEdit")
        self.wordEdit.setGeometry(QRect(90, 30, 261, 31))
        self.labelWord = QLabel(changeWordSentimentDialog)
        self.labelWord.setObjectName(u"labelWord")
        self.labelWord.setGeometry(QRect(30, 40, 47, 13))
        self.chooseSentimentGroupBox = QGroupBox(changeWordSentimentDialog)
        self.chooseSentimentGroupBox.setObjectName(u"chooseSentimentGroupBox")
        self.chooseSentimentGroupBox.setGeometry(QRect(110, 80, 191, 161))
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
        self.buttonCancel = QPushButton(changeWordSentimentDialog)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setGeometry(QRect(220, 260, 75, 23))
        self.buttonChange = QPushButton(changeWordSentimentDialog)
        self.buttonChange.setObjectName(u"buttonChange")
        self.buttonChange.setGeometry(QRect(120, 260, 75, 23))

        self.retranslateUi(changeWordSentimentDialog)

        QMetaObject.connectSlotsByName(changeWordSentimentDialog)
    # setupUi

    def retranslateUi(self, changeWordSentimentDialog):
        changeWordSentimentDialog.setWindowTitle(QCoreApplication.translate("changeWordSentimentDialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0441\u043b\u043e\u0432\u0430", None))
        self.wordEdit.setPlaceholderText(QCoreApplication.translate("changeWordSentimentDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.labelWord.setText(QCoreApplication.translate("changeWordSentimentDialog", u"\u0421\u043b\u043e\u0432\u043e:", None))
        self.chooseSentimentGroupBox.setTitle(QCoreApplication.translate("changeWordSentimentDialog", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.radioButtonPSTV.setText(QCoreApplication.translate("changeWordSentimentDialog", u"\u041f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.radioButtonNGTV.setText(QCoreApplication.translate("changeWordSentimentDialog", u"\u041e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.radioButtonNEUT.setText(QCoreApplication.translate("changeWordSentimentDialog", u"\u041d\u0435\u0439\u0442\u0440\u0430\u043b\u044c\u043d\u0430\u044f", None))
        self.buttonCancel.setText(QCoreApplication.translate("changeWordSentimentDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.buttonChange.setText(QCoreApplication.translate("changeWordSentimentDialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

