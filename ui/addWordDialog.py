# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addWordDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_addNewWordDialog(object):
    def setupUi(self, addNewWordDialog):
        if not addNewWordDialog.objectName():
            addNewWordDialog.setObjectName(u"addNewWordDialog")
        addNewWordDialog.setWindowModality(Qt.WindowModal)
        addNewWordDialog.setEnabled(True)
        addNewWordDialog.resize(373, 290)
        self.chooseSentimentGroupBox = QGroupBox(addNewWordDialog)
        self.chooseSentimentGroupBox.setObjectName(u"chooseSentimentGroupBox")
        self.chooseSentimentGroupBox.setGeometry(QRect(100, 80, 191, 131))
        self.radioButtonPSTV = QRadioButton(self.chooseSentimentGroupBox)
        self.radioButtonPSTV.setObjectName(u"radioButtonPSTV")
        self.radioButtonPSTV.setGeometry(QRect(30, 30, 131, 17))
        self.radioButtonPSTV.setChecked(True)
        self.radioButtonNGTV = QRadioButton(self.chooseSentimentGroupBox)
        self.radioButtonNGTV.setObjectName(u"radioButtonNGTV")
        self.radioButtonNGTV.setGeometry(QRect(30, 70, 131, 16))
        self.newWordEdit = QLineEdit(addNewWordDialog)
        self.newWordEdit.setObjectName(u"newWordEdit")
        self.newWordEdit.setGeometry(QRect(100, 30, 251, 31))
        self.labelNewWord = QLabel(addNewWordDialog)
        self.labelNewWord.setObjectName(u"labelNewWord")
        self.labelNewWord.setGeometry(QRect(10, 40, 91, 16))
        self.buttonAdd = QPushButton(addNewWordDialog)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setGeometry(QRect(110, 230, 75, 23))
        self.buttonCancel = QPushButton(addNewWordDialog)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setGeometry(QRect(200, 230, 75, 23))

        self.retranslateUi(addNewWordDialog)

        QMetaObject.connectSlotsByName(addNewWordDialog)
    # setupUi

    def retranslateUi(self, addNewWordDialog):
        addNewWordDialog.setWindowTitle(QCoreApplication.translate("addNewWordDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.chooseSentimentGroupBox.setTitle(QCoreApplication.translate("addNewWordDialog", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.radioButtonPSTV.setText(QCoreApplication.translate("addNewWordDialog", u"\u041f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.radioButtonNGTV.setText(QCoreApplication.translate("addNewWordDialog", u"\u041e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.newWordEdit.setPlaceholderText(QCoreApplication.translate("addNewWordDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.labelNewWord.setText(QCoreApplication.translate("addNewWordDialog", u"\u041d\u043e\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e:", None))
        self.buttonAdd.setText(QCoreApplication.translate("addNewWordDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.buttonCancel.setText(QCoreApplication.translate("addNewWordDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

