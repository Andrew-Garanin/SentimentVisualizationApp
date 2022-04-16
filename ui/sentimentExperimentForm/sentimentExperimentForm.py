# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sentimentExperimentForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_sentimentExperimentForm(object):
    def setupUi(self, sentimentExperimentForm):
        if not sentimentExperimentForm.objectName():
            sentimentExperimentForm.setObjectName(u"sentimentExperimentForm")
        sentimentExperimentForm.resize(508, 323)
        sentimentExperimentForm.setMinimumSize(QSize(508, 323))
        self.centralwidget = QWidget(sentimentExperimentForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 451, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.filePathLabel = QLabel(self.layoutWidget)
        self.filePathLabel.setObjectName(u"filePathLabel")
        font = QFont()
        font.setPointSize(11)
        self.filePathLabel.setFont(font)

        self.horizontalLayout.addWidget(self.filePathLabel)

        self.filePathLineEdit = QLineEdit(self.layoutWidget)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        font1 = QFont()
        font1.setPointSize(8)
        self.filePathLineEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.filePathLineEdit)

        self.filePathSelectButton = QToolButton(self.layoutWidget)
        self.filePathSelectButton.setObjectName(u"filePathSelectButton")

        self.horizontalLayout.addWidget(self.filePathSelectButton)

        self.makeExperimentButton = QPushButton(self.centralwidget)
        self.makeExperimentButton.setObjectName(u"makeExperimentButton")
        self.makeExperimentButton.setGeometry(QRect(190, 100, 131, 31))
        sentimentExperimentForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(sentimentExperimentForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 508, 21))
        sentimentExperimentForm.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(sentimentExperimentForm)
        self.statusbar.setObjectName(u"statusbar")
        sentimentExperimentForm.setStatusBar(self.statusbar)

        self.retranslateUi(sentimentExperimentForm)

        QMetaObject.connectSlotsByName(sentimentExperimentForm)
    # setupUi

    def retranslateUi(self, sentimentExperimentForm):
        sentimentExperimentForm.setWindowTitle(QCoreApplication.translate("sentimentExperimentForm", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442", None))
        self.filePathLabel.setText(QCoreApplication.translate("sentimentExperimentForm", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443:", None))
        self.filePathLineEdit.setPlaceholderText(QCoreApplication.translate("sentimentExperimentForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443", None))
        self.filePathSelectButton.setText(QCoreApplication.translate("sentimentExperimentForm", u"...", None))
        self.makeExperimentButton.setText(QCoreApplication.translate("sentimentExperimentForm", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442", None))
    # retranslateUi

