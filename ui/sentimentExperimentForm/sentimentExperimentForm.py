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
        sentimentExperimentForm.resize(491, 242)
        sentimentExperimentForm.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(sentimentExperimentForm)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(491, 201))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filePathLabel = QLabel(self.frame)
        self.filePathLabel.setObjectName(u"filePathLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.filePathLabel.sizePolicy().hasHeightForWidth())
        self.filePathLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        self.filePathLabel.setFont(font)

        self.horizontalLayout.addWidget(self.filePathLabel)

        self.filePathLineEdit = QLineEdit(self.frame)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        font1 = QFont()
        font1.setPointSize(8)
        self.filePathLineEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.filePathLineEdit)

        self.filePathSelectButton = QToolButton(self.frame)
        self.filePathSelectButton.setObjectName(u"filePathSelectButton")

        self.horizontalLayout.addWidget(self.filePathSelectButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.makeExperimentButton = QPushButton(self.frame)
        self.makeExperimentButton.setObjectName(u"makeExperimentButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.makeExperimentButton.sizePolicy().hasHeightForWidth())
        self.makeExperimentButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.makeExperimentButton, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        sentimentExperimentForm.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(sentimentExperimentForm)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 491, 21))
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
        self.makeExperimentButton.setText(QCoreApplication.translate("sentimentExperimentForm", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
    # retranslateUi

