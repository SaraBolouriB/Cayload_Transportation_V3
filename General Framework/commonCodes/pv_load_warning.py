from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pv_warning_dialog(QtWidgets.QDialog):
    def __init__(self, landing_page):
        self.landing_page = landing_page
        super().__init__()
        pv_warning_dialog = self
        self.setupUi(pv_warning_dialog)

    def setupUi(self, pv_warning_dialog):
        pv_warning_dialog.setObjectName("pv_warning_dialog")
        pv_warning_dialog.resize(385, 560)
        self.gridLayout = QtWidgets.QGridLayout(pv_warning_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(pv_warning_dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.warning_label = QtWidgets.QLabel(self.frame)
        self.warning_label.setText("")
        self.warning_label.setPixmap(QtGui.QPixmap("images/warning.png"))
        self.warning_label.setScaledContents(True)
        self.warning_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_label.setObjectName("warning_label")
        self.verticalLayout.addWidget(self.warning_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.warning_message_label = QtWidgets.QLabel(self.frame)
        self.warning_message_label.setMinimumSize(QtCore.QSize(2, 0))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.warning_message_label.setFont(font)
        self.warning_message_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.warning_message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_message_label.setWordWrap(True)
        self.warning_message_label.setObjectName("warning_message_label")
        self.verticalLayout.addWidget(self.warning_message_label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.load_pushButton = QtWidgets.QPushButton(self.frame)
        self.load_pushButton.setObjectName("load_pushButton")
        self.verticalLayout.addWidget(self.load_pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)

        self.retranslateUi(pv_warning_dialog)
        self.load_pushButton.clicked.connect(lambda: self.load_privkey_window(self.landing_page))
        QtCore.QMetaObject.connectSlotsByName(pv_warning_dialog)

        pv_warning_dialog.show()

    def retranslateUi(self, pv_warning_dialog):
        _translate = QtCore.QCoreApplication.translate
        pv_warning_dialog.setWindowTitle(_translate("pv_warning_dialog", "warning"))
        self.warning_message_label.setText(_translate("pv_warning_dialog", "Dear user , Please load your private key backup for access your contracts detail.!"))
        self.load_pushButton.setText(_translate("pv_warning_dialog", "load private key"))

    def load_privkey_window(self, landing_page):
        self.close()
        landing_page.upload_private_key()