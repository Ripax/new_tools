from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(200, 150)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_welcome = QPushButton(Form)
        self.pushButton_welcome.setObjectName(u"pushButton_welcome")

        self.verticalLayout.addWidget(self.pushButton_welcome)

        self.pushButton_date = QPushButton(Form)
        self.pushButton_date.setObjectName(u"pushButton_date")

        self.verticalLayout.addWidget(self.pushButton_date)

        self.pushButton_root = QPushButton(Form)
        self.pushButton_root.setObjectName(u"pushButton_root")

        self.verticalLayout.addWidget(self.pushButton_root)

        self.pushButton_nk_version = QPushButton(Form)
        self.pushButton_nk_version.setObjectName(u"pushButton_nk_version")

        self.verticalLayout.addWidget(self.pushButton_nk_version)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Nuke_info", None))
        self.pushButton_welcome.setText(QCoreApplication.translate("Form", u"Welcome", None))
        self.pushButton_date.setText(QCoreApplication.translate("Form", u"Date", None))
        self.pushButton_root.setText(QCoreApplication.translate("Form", u"Root", None))
        self.pushButton_nk_version.setText(QCoreApplication.translate("Form", u"Nuke version", None))
    # retranslateUi

