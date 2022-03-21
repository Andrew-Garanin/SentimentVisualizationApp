# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
        MainWindow.resize(826, 668)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        self.menuOpen = QAction(MainWindow)
        self.menuOpen.setObjectName(u"menuOpen")
        self.menuSave = QAction(MainWindow)
        self.menuSave.setObjectName(u"menuSave")
        self.menuSaveAs = QAction(MainWindow)
        self.menuSaveAs.setObjectName(u"menuSaveAs")
        self.menuCopy = QAction(MainWindow)
        self.menuCopy.setObjectName(u"menuCopy")
        self.menuPaste = QAction(MainWindow)
        self.menuPaste.setObjectName(u"menuPaste")
        self.menuUndo = QAction(MainWindow)
        self.menuUndo.setObjectName(u"menuUndo")
        self.menuAddNewWord = QAction(MainWindow)
        self.menuAddNewWord.setObjectName(u"menuAddNewWord")
        self.menuChangeWordSentiment = QAction(MainWindow)
        self.menuChangeWordSentiment.setObjectName(u"menuChangeWordSentiment")
        self.menuSingleSentence = QAction(MainWindow)
        self.menuSingleSentence.setObjectName(u"menuSingleSentence")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.frame.setToolTipDuration(4)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 501, 591))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textField = QTextEdit(self.frame_2)
        self.textField.setObjectName(u"textField")
        self.textField.setMouseTracking(True)
        self.textField.setContextMenuPolicy(Qt.CustomContextMenu)
        self.textField.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textField, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(530, 210, 201, 121))
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buttonMarkup = QPushButton(self.frame_3)
        self.buttonMarkup.setObjectName(u"buttonMarkup")
        self.buttonMarkup.setMinimumSize(QSize(100, 100))

        self.gridLayout_3.addWidget(self.buttonMarkup, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 826, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.menuOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.menuSave)
        self.menu.addAction(self.menuSaveAs)
        self.menu_2.addAction(self.menuCopy)
        self.menu_2.addAction(self.menuPaste)
        self.menu_2.addAction(self.menuUndo)
        self.menu_3.addAction(self.menuAddNewWord)
        self.menu_3.addAction(self.menuChangeWordSentiment)
        self.menu_4.addAction(self.menuSingleSentence)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sentiment Text Markup", None))
        self.menuOpen.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c...", None))
        self.menuSave.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.menuSaveAs.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None))
        self.menuCopy.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.menuPaste.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c", None))
        self.menuUndo.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.menuAddNewWord.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e...", None))
        self.menuChangeWordSentiment.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0441\u043b\u043e\u0432\u0430...", None))
        self.menuSingleSentence.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0434\u043d\u043e \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.textField.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.buttonMarkup.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u0441\u043b\u043e\u0432\u0430!", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0432\u0430\u0440\u044c", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0440\u0435\u0432\u043e \u0442\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438", None))
    # retranslateUi

