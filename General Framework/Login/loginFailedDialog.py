from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_failed_message_dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        login_failed_dialog = self
        self.setupUi(login_failed_dialog)

    def setupUi(self, login_failed_message_dialog):
        login_failed_message_dialog.setObjectName("login_failed_message_dialog")
        login_failed_message_dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.356db89e.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_failed_message_dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(login_failed_message_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(login_failed_message_dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.login_failed_message = QtWidgets.QLabel(self.frame)
        self.login_failed_message.setObjectName("login_failed_message")
        self.gridLayout_2.addWidget(self.login_failed_message, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 61, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 4, 1, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 3, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 0, 1, 1)
        self.login_failed_message_Button = QtWidgets.QPushButton(self.frame)
        self.login_failed_message_Button.setObjectName("login_failed_message_Button")
        self.gridLayout_2.addWidget(self.login_failed_message_Button, 3, 1, 1, 2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(login_failed_message_dialog)
        QtCore.QMetaObject.connectSlotsByName(login_failed_message_dialog)

        self.login_failed_message_Button.clicked.connect(login_failed_message_dialog.close)

        login_failed_message_dialog.show()

    def exec_login_failed_Page(self):
        pass

    def retranslateUi(self, login_failed_message_dialog):
        _translate = QtCore.QCoreApplication.translate
        login_failed_message_dialog.setWindowTitle(_translate("login_failed_message_dialog", "log in failed"))
        self.login_failed_message.setText(_translate("login_failed_message_dialog", "UserName Or Password is Incorrect !"))
        self.login_failed_message_Button.setText(_translate("login_failed_message_dialog", "ok"))

