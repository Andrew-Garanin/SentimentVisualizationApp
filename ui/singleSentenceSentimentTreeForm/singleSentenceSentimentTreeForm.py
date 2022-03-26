# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'singleSentenceSentimentTreeForm.ui'
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
        MainWindow.resize(1124, 849)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelFirstTree = QLabel(self.centralwidget)
        self.labelFirstTree.setObjectName(u"labelFirstTree")
        self.labelFirstTree.setGeometry(QRect(10, 190, 201, 21))
        font = QFont()
        font.setPointSize(10)
        self.labelFirstTree.setFont(font)
        self.labelFirstTree.setFrameShape(QFrame.NoFrame)
        self.graphicsViewFirstTree = QGraphicsView(self.centralwidget)
        self.graphicsViewFirstTree.setObjectName(u"graphicsViewFirstTree")
        self.graphicsViewFirstTree.setGeometry(QRect(10, 220, 541, 581))
        self.graphicsViewFirstTree.setDragMode(QGraphicsView.ScrollHandDrag)
        self.textEditSentense = QTextEdit(self.centralwidget)
        self.textEditSentense.setObjectName(u"textEditSentense")
        self.textEditSentense.setGeometry(QRect(10, 60, 1101, 111))
        self.graphicsViewSecondTree = QGraphicsView(self.centralwidget)
        self.graphicsViewSecondTree.setObjectName(u"graphicsViewSecondTree")
        self.graphicsViewSecondTree.setGeometry(QRect(570, 220, 541, 581))
        self.graphicsViewSecondTree.setDragMode(QGraphicsView.ScrollHandDrag)
        self.labelSecondTree = QLabel(self.centralwidget)
        self.labelSecondTree.setObjectName(u"labelSecondTree")
        self.labelSecondTree.setGeometry(QRect(570, 190, 211, 21))
        self.labelSecondTree.setFont(font)
        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(980, 10, 131, 41))
        self.generateTreeButton = QPushButton(self.centralwidget)
        self.generateTreeButton.setObjectName(u"generateTreeButton")
        self.generateTreeButton.setGeometry(QRect(840, 10, 131, 41))
        self.labelEnterSentence = QLabel(self.centralwidget)
        self.labelEnterSentence.setObjectName(u"labelEnterSentence")
        self.labelEnterSentence.setGeometry(QRect(10, 30, 121, 21))
        font1 = QFont()
        font1.setPointSize(8)
        self.labelEnterSentence.setFont(font1)
        self.labelFinalSentiment = QLabel(self.centralwidget)
        self.labelFinalSentiment.setObjectName(u"labelFinalSentiment")
        self.labelFinalSentiment.setGeometry(QRect(370, 10, 381, 31))
        self.labelFinalSentiment.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1124, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelFirstTree.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043f\u043e \u0441\u043b\u043e\u0432\u0430\u0440\u044e", None))
        self.labelSecondTree.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043f\u043e \u043f\u0440\u0430\u0432\u0438\u043b\u0430\u043c", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.generateTreeButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0434\u0435\u0440\u0435\u0432\u043e", None))
        self.labelEnterSentence.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435:</span></p></body></html>", None))
        self.labelFinalSentiment.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c:", None))
    # retranslateUi

