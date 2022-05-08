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


class Ui_changeWordSentimentForm(object):
    def setupUi(self, changeWordSentimentForm):
        if not changeWordSentimentForm.objectName():
            changeWordSentimentForm.setObjectName(u"changeWordSentimentForm")
        changeWordSentimentForm.resize(528, 375)
        self.centralwidget = QWidget(changeWordSentimentForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.currentWordSentimentLabel = QLabel(self.frame)
        self.currentWordSentimentLabel.setObjectName(u"currentWordSentimentLabel")
        font = QFont()
        font.setPointSize(10)
        self.currentWordSentimentLabel.setFont(font)

        self.horizontalLayout_6.addWidget(self.currentWordSentimentLabel)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonChange = QPushButton(self.frame)
        self.buttonChange.setObjectName(u"buttonChange")
        self.buttonChange.setMinimumSize(QSize(91, 31))

        self.horizontalLayout.addWidget(self.buttonChange)

        self.buttonCancel = QPushButton(self.frame)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setMinimumSize(QSize(91, 31))

        self.horizontalLayout.addWidget(self.buttonCancel)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.chooseSentimentGroupBox = QGroupBox(self.frame)
        self.chooseSentimentGroupBox.setObjectName(u"chooseSentimentGroupBox")
        sizePolicy.setHeightForWidth(self.chooseSentimentGroupBox.sizePolicy().hasHeightForWidth())
        self.chooseSentimentGroupBox.setSizePolicy(sizePolicy)
        self.chooseSentimentGroupBox.setMinimumSize(QSize(201, 161))
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

        self.verticalLayout_2.addWidget(self.chooseSentimentGroupBox)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(77, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelError = QLabel(self.frame)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setMinimumSize(QSize(261, 16))
        self.labelError.setMaximumSize(QSize(251, 16))
        font1 = QFont()
        font1.setPointSize(7)
        self.labelError.setFont(font1)
        self.labelError.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.labelError, 1, 1, 1, 2)

        self.labelWord = QLabel(self.frame)
        self.labelWord.setObjectName(u"labelWord")
        self.labelWord.setMinimumSize(QSize(51, 21))

        self.gridLayout.addWidget(self.labelWord, 0, 0, 1, 1)

        self.wordEdit = QLineEdit(self.frame)
        self.wordEdit.setObjectName(u"wordEdit")
        self.wordEdit.setMinimumSize(QSize(261, 31))

        self.gridLayout.addWidget(self.wordEdit, 0, 2, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.horizontalSpacer_6 = QSpacerItem(37, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        changeWordSentimentForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(changeWordSentimentForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 528, 21))
        changeWordSentimentForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(changeWordSentimentForm)
        self.statusbar.setObjectName(u"statusbar")
        changeWordSentimentForm.setStatusBar(self.statusbar)

        self.retranslateUi(changeWordSentimentForm)

        QMetaObject.connectSlotsByName(changeWordSentimentForm)
    # setupUi

    def retranslateUi(self, changeWordSentimentForm):
        changeWordSentimentForm.setWindowTitle(QCoreApplication.translate("changeWordSentimentForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0441\u043b\u043e\u0432\u0430", None))
        self.currentWordSentimentLabel.setText(QCoreApplication.translate("changeWordSentimentForm", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u0441\u043b\u043e\u0432\u0430: \u043d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u043e", None))
        self.buttonChange.setText(QCoreApplication.translate("changeWordSentimentForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.buttonCancel.setText(QCoreApplication.translate("changeWordSentimentForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.chooseSentimentGroupBox.setTitle(QCoreApplication.translate("changeWordSentimentForm", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.radioButtonPSTV.setText(QCoreApplication.translate("changeWordSentimentForm", u"\u041f\u043e\u043b\u043e\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.radioButtonNGTV.setText(QCoreApplication.translate("changeWordSentimentForm", u"\u041e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.radioButtonNEUT.setText(QCoreApplication.translate("changeWordSentimentForm", u"\u041d\u0435\u0439\u0442\u0440\u0430\u043b\u044c\u043d\u0430\u044f", None))
        self.labelError.setText(QCoreApplication.translate("changeWordSentimentForm", u"asdasd", None))
        self.labelWord.setText(QCoreApplication.translate("changeWordSentimentForm", u"\u0421\u043b\u043e\u0432\u043e:", None))
        self.wordEdit.setPlaceholderText(QCoreApplication.translate("changeWordSentimentForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043b\u043e\u0432\u043e", None))
    # retranslateUi

