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


class Ui_addNewWordForm(object):
    def setupUi(self, addNewWordForm):
        if not addNewWordForm.objectName():
            addNewWordForm.setObjectName(u"addNewWordForm")
        addNewWordForm.resize(467, 347)
        self.centralwidget = QWidget(addNewWordForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(13, 55, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelError = QLabel(self.frame)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setMinimumSize(QSize(251, 16))
        self.labelError.setMaximumSize(QSize(251, 16))
        font = QFont()
        font.setPointSize(7)
        self.labelError.setFont(font)
        self.labelError.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_2.addWidget(self.labelError, 2, 1, 1, 1)

        self.newWordEdit = QLineEdit(self.frame)
        self.newWordEdit.setObjectName(u"newWordEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.newWordEdit.sizePolicy().hasHeightForWidth())
        self.newWordEdit.setSizePolicy(sizePolicy1)
        self.newWordEdit.setMinimumSize(QSize(261, 31))
        self.newWordEdit.setStyleSheet(u"")
        self.newWordEdit.setFrame(True)

        self.gridLayout_2.addWidget(self.newWordEdit, 0, 1, 1, 1)

        self.labelNewWord = QLabel(self.frame)
        self.labelNewWord.setObjectName(u"labelNewWord")
        self.labelNewWord.setMinimumSize(QSize(91, 21))

        self.gridLayout_2.addWidget(self.labelNewWord, 0, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalSpacer_6 = QSpacerItem(13, 55, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.chooseSentimentGroupBox = QGroupBox(self.frame)
        self.chooseSentimentGroupBox.setObjectName(u"chooseSentimentGroupBox")
        self.chooseSentimentGroupBox.setMinimumSize(QSize(191, 161))
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

        self.horizontalLayout_3.addWidget(self.chooseSentimentGroupBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonAdd = QPushButton(self.frame)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setMinimumSize(QSize(91, 31))

        self.horizontalLayout.addWidget(self.buttonAdd)

        self.buttonCancel = QPushButton(self.frame)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setMinimumSize(QSize(91, 31))

        self.horizontalLayout.addWidget(self.buttonCancel)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        addNewWordForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(addNewWordForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 467, 21))
        addNewWordForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(addNewWordForm)
        self.statusbar.setObjectName(u"statusbar")
        addNewWordForm.setStatusBar(self.statusbar)

        self.retranslateUi(addNewWordForm)

        QMetaObject.connectSlotsByName(addNewWordForm)
    # setupUi

    def retranslateUi(self, addNewWordForm):
        addNewWordForm.setWindowTitle(QCoreApplication.translate("addNewWordForm", u"\u041d\u043e\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.labelError.setText(QCoreApplication.translate("addNewWordForm", u"\u044b\u0444\u0432\u0444\u044b", None))
        self.newWordEdit.setPlaceholderText(QCoreApplication.translate("addNewWordForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.labelNewWord.setText(QCoreApplication.translate("addNewWordForm", u"\u041d\u043e\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e:", None))
        self.chooseSentimentGroupBox.setTitle(QCoreApplication.translate("addNewWordForm", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.radioButtonPSTV.setText(QCoreApplication.translate("addNewWordForm", u"\u041f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.radioButtonNGTV.setText(QCoreApplication.translate("addNewWordForm", u"\u041e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.radioButtonNEUT.setText(QCoreApplication.translate("addNewWordForm", u"\u041d\u0435\u0439\u0442\u0440\u0430\u043b\u044c\u043d\u0430\u044f", None))
        self.buttonAdd.setText(QCoreApplication.translate("addNewWordForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.buttonCancel.setText(QCoreApplication.translate("addNewWordForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

