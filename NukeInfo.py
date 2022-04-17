# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainxIDfwe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(446, 394)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"color: rgb(79, 143, 0);")
        self.label.setFrameShape(QFrame.StyledPanel)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(1)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_root = QPushButton(self.groupBox)
        self.pushButton_root.setObjectName(u"pushButton_root")

        self.gridLayout_2.addWidget(self.pushButton_root, 3, 0, 1, 1)

        self.pushButton_date = QPushButton(self.groupBox)
        self.pushButton_date.setObjectName(u"pushButton_date")

        self.gridLayout_2.addWidget(self.pushButton_date, 2, 0, 1, 1)

        self.pushButton_nk_version = QPushButton(self.groupBox)
        self.pushButton_nk_version.setObjectName(u"pushButton_nk_version")

        self.gridLayout_2.addWidget(self.pushButton_nk_version, 4, 0, 1, 1)

        self.pushButton_welcome = QPushButton(self.groupBox)
        self.pushButton_welcome.setObjectName(u"pushButton_welcome")

        self.gridLayout_2.addWidget(self.pushButton_welcome, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Nuke_info", None))
        self.label.setText(QCoreApplication.translate("Form", u"Test Text", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"all Buttons", None))
        self.pushButton_root.setText(QCoreApplication.translate("Form", u"Root", None))
        self.pushButton_date.setText(QCoreApplication.translate("Form", u"Date", None))
        self.pushButton_nk_version.setText(QCoreApplication.translate("Form", u"Nuke version", None))
        self.pushButton_welcome.setText(QCoreApplication.translate("Form", u"Welcome", None))
    # retranslateUi

