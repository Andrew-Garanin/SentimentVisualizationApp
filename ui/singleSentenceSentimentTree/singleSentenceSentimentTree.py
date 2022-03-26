# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'singleSentenceSentimentTree.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_singleSentenceSentimentTree(object):
    def setupUi(self, singleSentenceSentimentTree):
        if not singleSentenceSentimentTree.objectName():
            singleSentenceSentimentTree.setObjectName(u"singleSentenceSentimentTree")
        singleSentenceSentimentTree.resize(1122, 820)
        singleSentenceSentimentTree.setModal(True)
        self.textEditSentense = QTextEdit(singleSentenceSentimentTree)
        self.textEditSentense.setObjectName(u"textEditSentense")
        self.textEditSentense.setGeometry(QRect(10, 60, 1101, 111))
        self.labelFirstTree = QLabel(singleSentenceSentimentTree)
        self.labelFirstTree.setObjectName(u"labelFirstTree")
        self.labelFirstTree.setGeometry(QRect(10, 190, 201, 21))
        font = QFont()
        font.setPointSize(10)
        self.labelFirstTree.setFont(font)
        self.labelFirstTree.setFrameShape(QFrame.NoFrame)
        self.generateTreeButton = QPushButton(singleSentenceSentimentTree)
        self.generateTreeButton.setObjectName(u"generateTreeButton")
        self.generateTreeButton.setGeometry(QRect(840, 10, 131, 41))
        self.labelFinalSentiment = QLabel(singleSentenceSentimentTree)
        self.labelFinalSentiment.setObjectName(u"labelFinalSentiment")
        self.labelFinalSentiment.setGeometry(QRect(370, 10, 381, 31))
        self.labelFinalSentiment.setFont(font)
        self.labelEnterSentence = QLabel(singleSentenceSentimentTree)
        self.labelEnterSentence.setObjectName(u"labelEnterSentence")
        self.labelEnterSentence.setGeometry(QRect(10, 30, 121, 21))
        font1 = QFont()
        font1.setPointSize(8)
        self.labelEnterSentence.setFont(font1)
        self.labelSecondTree = QLabel(singleSentenceSentimentTree)
        self.labelSecondTree.setObjectName(u"labelSecondTree")
        self.labelSecondTree.setGeometry(QRect(570, 190, 211, 21))
        self.labelSecondTree.setFont(font)
        self.clearButton = QPushButton(singleSentenceSentimentTree)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(980, 10, 131, 41))
        self.graphicsViewFirstTree = QGraphicsView(singleSentenceSentimentTree)
        self.graphicsViewFirstTree.setObjectName(u"graphicsViewFirstTree")
        self.graphicsViewFirstTree.setGeometry(QRect(10, 220, 541, 581))
        self.graphicsViewFirstTree.setDragMode(QGraphicsView.ScrollHandDrag)
        self.graphicsViewSecondTree = QGraphicsView(singleSentenceSentimentTree)
        self.graphicsViewSecondTree.setObjectName(u"graphicsViewSecondTree")
        self.graphicsViewSecondTree.setGeometry(QRect(570, 220, 541, 581))
        self.graphicsViewSecondTree.setDragMode(QGraphicsView.ScrollHandDrag)

        self.retranslateUi(singleSentenceSentimentTree)

        QMetaObject.connectSlotsByName(singleSentenceSentimentTree)
    # setupUi

    def retranslateUi(self, singleSentenceSentimentTree):
        singleSentenceSentimentTree.setWindowTitle(QCoreApplication.translate("", u"\u0414\u0435\u0440\u0435\u0432\u043e \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438. \u041e\u0434\u043d\u043e \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.labelFirstTree.setText(QCoreApplication.translate("", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043f\u043e \u0441\u043b\u043e\u0432\u0430\u0440\u044e", None))
        self.generateTreeButton.setText(QCoreApplication.translate("", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0434\u0435\u0440\u0435\u0432\u043e", None))
        self.labelFinalSentiment.setText(QCoreApplication.translate("", u"\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c:", None))
        self.labelEnterSentence.setText(QCoreApplication.translate("", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435:</span></p></body></html>", None))
        self.labelSecondTree.setText(QCoreApplication.translate("", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043f\u043e \u043f\u0440\u0430\u0432\u0438\u043b\u0430\u043c", None))
        self.clearButton.setText(QCoreApplication.translate("", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

