# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMDIForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainMDIForm(object):
    def setupUi(self, mainMDIForm):
        if not mainMDIForm.objectName():
            mainMDIForm.setObjectName(u"mainMDIForm")
        mainMDIForm.resize(1202, 738)
        self.menuSentimentTextMarkup = QAction(mainMDIForm)
        self.menuSentimentTextMarkup.setObjectName(u"menuSentimentTextMarkup")
        self.menuSingleSentence = QAction(mainMDIForm)
        self.menuSingleSentence.setObjectName(u"menuSingleSentence")
        self.menuAddNewWord = QAction(mainMDIForm)
        self.menuAddNewWord.setObjectName(u"menuAddNewWord")
        self.menuChangeWordSentiment = QAction(mainMDIForm)
        self.menuChangeWordSentiment.setObjectName(u"menuChangeWordSentiment")
        self.menuWindowsCascade = QAction(mainMDIForm)
        self.menuWindowsCascade.setObjectName(u"menuWindowsCascade")
        self.menuSentimentExperiment = QAction(mainMDIForm)
        self.menuSentimentExperiment.setObjectName(u"menuSentimentExperiment")
        self.centralwidget = QWidget(mainMDIForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mdiArea = QMdiArea(self.frame)
        self.mdiArea.setObjectName(u"mdiArea")

        self.verticalLayout.addWidget(self.mdiArea)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        mainMDIForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainMDIForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1202, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        mainMDIForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainMDIForm)
        self.statusbar.setObjectName(u"statusbar")
        mainMDIForm.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.menuSentimentTextMarkup)
        self.menu_2.addAction(self.menuSingleSentence)
        self.menu_3.addAction(self.menuAddNewWord)
        self.menu_3.addAction(self.menuChangeWordSentiment)
        self.menu_4.addAction(self.menuWindowsCascade)
        self.menu_5.addAction(self.menuSentimentExperiment)

        self.retranslateUi(mainMDIForm)

        QMetaObject.connectSlotsByName(mainMDIForm)
    # setupUi

    def retranslateUi(self, mainMDIForm):
        mainMDIForm.setWindowTitle(QCoreApplication.translate("mainMDIForm", u"\u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0441\u043b\u043e\u0432 \u0438 \u0444\u0440\u0430\u0437", None))
        self.menuSentimentTextMarkup.setText(QCoreApplication.translate("mainMDIForm", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.menuSingleSentence.setText(QCoreApplication.translate("mainMDIForm", u"\u041e\u0434\u0438\u043d\u043e\u0447\u043d\u043e\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.menuAddNewWord.setText(QCoreApplication.translate("mainMDIForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.menuChangeWordSentiment.setText(QCoreApplication.translate("mainMDIForm", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0441\u043b\u043e\u0432\u0430", None))
        self.menuWindowsCascade.setText(QCoreApplication.translate("mainMDIForm", u"\u041a\u0430\u0441\u043a\u0430\u0434\u043e\u043c", None))
        self.menuSentimentExperiment.setText(QCoreApplication.translate("mainMDIForm", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442", None))
        self.menu.setTitle(QCoreApplication.translate("mainMDIForm", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.menu_2.setTitle(QCoreApplication.translate("mainMDIForm", u"\u0414\u0435\u0440\u0435\u0432\u043e \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438", None))
        self.menu_3.setTitle(QCoreApplication.translate("mainMDIForm", u"\u0421\u043b\u043e\u0432\u0430\u0440\u044c", None))
        self.menu_4.setTitle(QCoreApplication.translate("mainMDIForm", u"\u041e\u043a\u043d\u0430", None))
        self.menu_5.setTitle(QCoreApplication.translate("mainMDIForm", u"\u042d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442", None))
    # retranslateUi

