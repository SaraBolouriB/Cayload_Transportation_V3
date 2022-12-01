from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class verficatoin_code_dialog(QtWidgets.QDialog):

    def __init__(self, email, landing_page, site_id, username, company_name, login_result):
        self.landing_page = landing_page
        self.site_id = site_id
        self.username = username
        self.company_name = company_name
        self.login_result = login_result
        self.ge_code = self.gen_code(email)

        super().__init__()
        verficatoin_code_dialog = self
        self.setupUi(verficatoin_code_dialog)

    def setupUi(self, login_failed_message_dialog):
        login_failed_message_dialog.setObjectName("login_failed_message_dialog")
        login_failed_message_dialog.resize(400, 147)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Cayload_Blockchain_Both_Side/Cayload-Client/UI Files/images/logo.356db89e.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_failed_message_dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(login_failed_message_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(login_failed_message_dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 4, 1, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 2, 1, 1, 2)
        self.login_failed_message_Button = QtWidgets.QPushButton(self.frame)
        self.login_failed_message_Button.setObjectName("login_failed_message_Button")
        self.gridLayout_2.addWidget(self.login_failed_message_Button, 3, 1, 1, 2)
        self.verticalLayout.addWidget(self.frame)

        self.login_failed_message_Button.clicked.connect(self.check_code)
        self.retranslateUi(login_failed_message_dialog)
        QtCore.QMetaObject.connectSlotsByName(login_failed_message_dialog)


    def retranslateUi(self, login_failed_message_dialog):
        _translate = QtCore.QCoreApplication.translate
        login_failed_message_dialog.setWindowTitle(_translate("login_failed_message_dialog", "log in failed"))
        self.label.setText(_translate("login_failed_message_dialog", "Enter the code virification:"))
        self.login_failed_message_Button.setText(_translate("login_failed_message_dialog", "ok"))

    def gen_code(self, email):
        url = 'http://127.0.0.1:8000/send_email/'
        json_data = {
            "email" : email
        }
        req = requests.post(url=url, json=json_data)
        return req.json()

    def check_code(self):
        code = str(self.lineEdit.text())

        if code == self.ge_code:
            self.close()
            self.landing_page.show_client_page(
                site_id=self.site_id, 
                username=self.username,
                company_name=self.company_name, 
                login_result=self.login_result
            )
        else:
            print("Wrong code")

