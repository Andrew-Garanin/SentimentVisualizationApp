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


class Ui_singleSentenceSentimentTreeForm(object):
    def setupUi(self, singleSentenceSentimentTreeForm):
        if not singleSentenceSentimentTreeForm.objectName():
            singleSentenceSentimentTreeForm.setObjectName(u"singleSentenceSentimentTreeForm")
        singleSentenceSentimentTreeForm.resize(1332, 874)
        self.centralwidget = QWidget(singleSentenceSentimentTreeForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 35))
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 4, 0, 1, 1)

        self.generateTreeButton = QPushButton(self.frame_2)
        self.generateTreeButton.setObjectName(u"generateTreeButton")
        self.generateTreeButton.setMinimumSize(QSize(0, 35))

        self.gridLayout_8.addWidget(self.generateTreeButton, 0, 0, 1, 1)

        self.clearButton = QPushButton(self.frame_2)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMinimumSize(QSize(0, 35))

        self.gridLayout_8.addWidget(self.clearButton, 1, 0, 1, 1)

        self.unknownWordsButton = QPushButton(self.frame_2)
        self.unknownWordsButton.setObjectName(u"unknownWordsButton")
        self.unknownWordsButton.setMinimumSize(QSize(0, 35))

        self.gridLayout_8.addWidget(self.unknownWordsButton, 2, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_2, 1, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter = QSplitter(self.frame_4)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelEnterSentence = QLabel(self.layoutWidget)
        self.labelEnterSentence.setObjectName(u"labelEnterSentence")
        font = QFont()
        font.setPointSize(8)
        self.labelEnterSentence.setFont(font)

        self.gridLayout_2.addWidget(self.labelEnterSentence, 0, 0, 1, 1)

        self.textEditSentense = QTextEdit(self.layoutWidget)
        self.textEditSentense.setObjectName(u"textEditSentense")

        self.gridLayout_2.addWidget(self.textEditSentense, 1, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(451, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.gridLayout_5 = QGridLayout(self.layoutWidget1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(268, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.labelEnterSentence_2 = QLabel(self.layoutWidget1)
        self.labelEnterSentence_2.setObjectName(u"labelEnterSentence_2")
        self.labelEnterSentence_2.setFont(font)

        self.gridLayout_5.addWidget(self.labelEnterSentence_2, 0, 0, 1, 1)

        self.foundRulesListWidget = QListWidget(self.layoutWidget1)
        self.foundRulesListWidget.setObjectName(u"foundRulesListWidget")

        self.gridLayout_5.addWidget(self.foundRulesListWidget, 1, 0, 1, 2)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_7.addWidget(self.splitter)

        self.splitter_2 = QSplitter(self.frame_4)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(5)
        sizePolicy2.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy2)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.layoutWidget2 = QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.gridLayout_3 = QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelFirstTree = QLabel(self.layoutWidget2)
        self.labelFirstTree.setObjectName(u"labelFirstTree")
        font1 = QFont()
        font1.setPointSize(10)
        self.labelFirstTree.setFont(font1)
        self.labelFirstTree.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.labelFirstTree, 0, 0, 1, 1)

        self.graphicsViewFirstTree = QGraphicsView(self.layoutWidget2)
        self.graphicsViewFirstTree.setObjectName(u"graphicsViewFirstTree")
        self.graphicsViewFirstTree.setDragMode(QGraphicsView.ScrollHandDrag)

        self.gridLayout_3.addWidget(self.graphicsViewFirstTree, 1, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(348, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.splitter_2.addWidget(self.layoutWidget2)
        self.layoutWidget3 = QWidget(self.splitter_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.gridLayout_4 = QGridLayout(self.layoutWidget3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelSecondTree = QLabel(self.layoutWidget3)
        self.labelSecondTree.setObjectName(u"labelSecondTree")
        self.labelSecondTree.setFont(font1)

        self.gridLayout_4.addWidget(self.labelSecondTree, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(268, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.graphicsViewSecondTree = QGraphicsView(self.layoutWidget3)
        self.graphicsViewSecondTree.setObjectName(u"graphicsViewSecondTree")
        self.graphicsViewSecondTree.setDragMode(QGraphicsView.ScrollHandDrag)

        self.gridLayout_4.addWidget(self.graphicsViewSecondTree, 1, 0, 1, 2)

        self.splitter_2.addWidget(self.layoutWidget3)

        self.verticalLayout_7.addWidget(self.splitter_2)


        self.gridLayout_9.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.labelFinalSentiment = QLabel(self.frame_4)
        self.labelFinalSentiment.setObjectName(u"labelFinalSentiment")
        self.labelFinalSentiment.setMaximumSize(QSize(16777215, 16))
        self.labelFinalSentiment.setFont(font1)

        self.gridLayout_9.addWidget(self.labelFinalSentiment, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_4)


        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        singleSentenceSentimentTreeForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(singleSentenceSentimentTreeForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1332, 21))
        singleSentenceSentimentTreeForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(singleSentenceSentimentTreeForm)
        self.statusbar.setObjectName(u"statusbar")
        singleSentenceSentimentTreeForm.setStatusBar(self.statusbar)

        self.retranslateUi(singleSentenceSentimentTreeForm)

        QMetaObject.connectSlotsByName(singleSentenceSentimentTreeForm)
    # setupUi

    def retranslateUi(self, singleSentenceSentimentTreeForm):
        singleSentenceSentimentTreeForm.setWindowTitle(QCoreApplication.translate("singleSentenceSentimentTreeForm", u"\u0414\u0435\u0440\u0435\u0432\u043e \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u043e\u0434\u0438\u043d\u043e\u0447\u043d\u043e\u0433\u043e \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.generateTreeButton.setText(QCoreApplication.translate("singleSentenceSentimentTreeForm", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0434\u0435\u0440\u0435\u0432\u043e", None))
        self.clearButton.setText(QCoreApplication.translate("singleSentenceSentimentTreeForm", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.unknownWordsButton.setText(QCoreApplication.translate("singleSentenceSentimentTreeForm", u"\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u0435 \u0441\u043b\u043e\u0432\u0430", None))
        self.labelEnterSentence.setText(QCoreApplication.translate("singleSentenceSentimentTreeForm", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435:</span></p></body></html>", None))
        self.labelEnterSentence_2.setText(QCoreApplication.translate("singleSentenceSentimentTreeForm", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u041d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u0430 \u0432\u044b\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438:</span></p></body></html>", None))
        self.labelFirstTree.setText(QCoreApplication.translate("singleSentenceSentimentTreeForm", u"\u0422\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0441\u043b\u043e\u0432 \u043f\u043e \u0441\u043b\u043e\u0432\u0430\u0440\u044e", None))
        self.labelSecondTree.setText(QCoreApplication.translate("singleSentenceSentimentTreeForm", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0432\u044b\u0432\u043e\u0434\u0430 \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u043f\u043e \u043f\u0440\u0430\u0432\u0438\u043b\u0430\u043c", None))
        self.labelFinalSentiment.setText(QCoreApplication.translate("singleSentenceSentimentTreeForm", u"\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c:", None))
    # retranslateUi

