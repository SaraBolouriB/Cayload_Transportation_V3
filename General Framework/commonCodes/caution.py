from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_caution_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        caution_Dialog = self
        self.setupUi(caution_Dialog)

    def setupUi(self, caution_Dialog):
        caution_Dialog.setObjectName("caution_Dialog")
        caution_Dialog.resize(884, 649)
        self.frame = QtWidgets.QFrame(caution_Dialog)
        self.frame.setGeometry(QtCore.QRect(9, 9, 870, 634))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.caution_checkBox = QtWidgets.QCheckBox(self.frame)
        self.caution_checkBox.setObjectName("caution_checkBox")
        self.gridLayout.addWidget(self.caution_checkBox, 1, 0, 1, 1)
        self.ok_pushButton = QtWidgets.QPushButton(self.frame)
        self.ok_pushButton.setObjectName("ok_pushButton")
        self.gridLayout.addWidget(self.ok_pushButton, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/blockchain-disrupt-forex-market.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(caution_Dialog)
        self.ok_pushButton.clicked.connect(self.got_it)
        QtCore.QMetaObject.connectSlotsByName(caution_Dialog)
        self.show()

    def retranslateUi(self, caution_Dialog):
        _translate = QtCore.QCoreApplication.translate
        caution_Dialog.setWindowTitle(_translate("caution_Dialog", "Dialog"))
        self.caution_checkBox.setText(_translate("caution_Dialog", "Don\'t Show Me Again"))
        self.ok_pushButton.setText(_translate("caution_Dialog", "OK, I got it"))

    def got_it(self):
        if self.caution_checkBox.isChecked():
            with open('user.bin', 'r') as user_file:
                user = user_file.read()
            user_file.close()
            with open('caution.bin', 'w') as file:
                file.write(user)
            file.close()
        self.close()
