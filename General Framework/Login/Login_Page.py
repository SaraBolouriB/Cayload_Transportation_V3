from .loginFailedDialog import Ui_login_failed_message_dialog
from Signup.Signup_Page import Ui_signup_dialog
from .Code_Verification import verficatoin_code_dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests
import time

global closeEvent
closeEvent = 'login'

class Ui_login_dialog(QtWidgets.QDialog):
    def __init__(self, landing_page):
        self.landingPage = landing_page
        super().__init__()
        login_dialog = self
        self.setupUi(login_dialog)

    def setupUi(self, login_dialog):
        login_dialog.setObjectName("login_dialog")
        login_dialog.resize(527, 649)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_dialog.sizePolicy().hasHeightForWidth())
        login_dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../Desktop/logo.356db89e.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_dialog.setWindowIcon(icon)
        login_dialog.setSizeGripEnabled(False)
        login_dialog.setModal(False)
        self.frame = QtWidgets.QFrame(login_dialog)
        self.frame.setGeometry(QtCore.QRect(0, 10, 527, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.logo_image = QtWidgets.QLabel(self.frame)
        self.logo_image.setText("")
        self.logo_image.setPixmap(QtGui.QPixmap(".\\../Desktop/logo.356db89e.png"))
        self.logo_image.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_image.setObjectName("logo_image")
        self.verticalLayout.addWidget(self.logo_image)
        self.Cayload_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.Cayload_label.setFont(font)
        self.Cayload_label.setObjectName("Cayload_label")
        self.verticalLayout.addWidget(self.Cayload_label)
        self.logisticService_lable = QtWidgets.QLabel(self.frame)
        self.logisticService_lable.setObjectName("logisticService_lable")
        self.verticalLayout.addWidget(self.logisticService_lable)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.username_label = QtWidgets.QLabel(self.frame)
        self.username_label.setObjectName("username_label")
        self.horizontalLayout_3.addWidget(self.username_label)
        self.username_box = QtWidgets.QLineEdit(self.frame)
        self.username_box.setObjectName("username_box")
        self.horizontalLayout_3.addWidget(self.username_box)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.password_label = QtWidgets.QLabel(self.frame)
        self.password_label.setObjectName("password_label")
        self.horizontalLayout_4.addWidget(self.password_label)
        self.password_box = QtWidgets.QLineEdit(self.frame)
        self.password_box.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_box.setObjectName("password_box")
        self.horizontalLayout_4.addWidget(self.password_box)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.login_button = QtWidgets.QPushButton(login_dialog)
        self.login_button.setGeometry(QtCore.QRect(10, 570, 503, 28))
        self.login_button.setObjectName("login_button")
        self.horizontalLayoutWidget = QtWidgets.QWidget(login_dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 540, 501, 24))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.is_admin = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.is_admin.setObjectName("is_admin")
        self.horizontalLayout_6.addWidget(self.is_admin)
        self.company = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.company.setObjectName("company")

        all_site_names = self.get_all_company_name()
        self.company.addItem('')
        for name in all_site_names:
            self.company.addItem(name)
        self.horizontalLayout_6.addWidget(self.company)

        self.signup = QtWidgets.QCommandLinkButton(login_dialog, clicked=lambda:self.signup_page_show())
        self.signup.setGeometry(QtCore.QRect(280, 600, 101, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signup.sizePolicy().hasHeightForWidth())
        self.signup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.signup.setFont(font)
        self.signup.setCheckable(False)
        self.signup.setChecked(False)
        self.signup.setObjectName("signup")
        self.account = QtWidgets.QLabel(login_dialog)
        self.account.setGeometry(QtCore.QRect(110, 610, 171, 21))
        self.account.setObjectName("account")

        self.retranslateUi(login_dialog)
        self.login_button.clicked.connect(self.login)
        QtCore.QMetaObject.connectSlotsByName(login_dialog)

        login_dialog.show()

    def retranslateUi(self, login_dialog):
        _translate = QtCore.QCoreApplication.translate
        login_dialog.setWindowTitle(_translate("login_dialog", "Blockchain Framework"))
        self.Cayload_label.setText(_translate("login_dialog", "<html><head/><body><p align=\"center\">Blockchain Framework</p></body></html>"))
        self.logisticService_lable.setText(_translate("login_dialog", "<html><head/><body><p align=\"center\">Login Page</p></body></html>"))
        self.username_label.setText(_translate("login_dialog", "username :"))
        self.password_label.setText(_translate("login_dialog", "password :"))
        self.login_button.setText(_translate("login_dialog", "login"))
        self.is_admin.setText(_translate("login_dialog", "Are you admin?"))
        self.company.setItemText(0, _translate("login_dialog", ""))
        self.signup.setText(_translate("login_dialog", "sign up"))
        self.account.setText(_translate("login_dialog", "Don\'t have an admin account?"))

    def login(self):
        username = str(self.username_box.text()).strip().replace("\n", "")
        password = str(self.password_box.text())
        site_name = str(self.company.currentText())

        # username = "saraboloori@yahoo.com"
        # password = "s@CPass1376"
        # site_name = "cayload-customer"
        if self.is_admin.isChecked():
            self.user_type = 'admin'
            url = 'http://127.0.0.1:8000/admin_login/'
            json_data = {
                "siteName" : site_name,
                "adminUsername" : username,
                "adminPassword" : password
            }
            req = self.check_connection(url=url, json=json_data, timeout=20, method="get")
            if req.status_code == 200:
                if req.json()['exist'] == True:
                    result = req.json()
                    site_id = result['site_id']
                    login_id = result['login_id']
                    blockchain_id = result['blockchain_id']
                    self.close()
                    self.landingPage.show_admin_page(site_id, login_id, blockchain_id)
            else:
                self.exec_login_failed_message_dialog()

        else:
            # self.landingPage.show_client_page(site_id=1, username='sara' ,company_name='university')
            self.user_type = 'user'
            url = 'http://127.0.0.1:8000/user_login/'
            json_data = {
                "siteName" : site_name
            }
            req = self.check_connection(url=url, json=json_data, timeout=5, method="get")
            if req.status_code == 200:
                result = req.json()
                login_url = result['url']
                login_json = result['data'].split(',')
                data = {
                    login_json[0].split('[')[1].split(']')[0] : username,
                    login_json[1].split('[')[1].split(']')[0] : password
                }

                req = self.check_connection(url=login_url,json=data, timeout=5, method='post')
                site_result = req.json()
                if req.status_code == 200:
                    # ---------------- PREPROCESS FOR FINDING USER ID ----------------- #
                    _user_id = self.process(data=site_result, keyword=login_json[2])
                    # ----------------------------------------------------------------- #
                    self.landingPage.user_token = site_result['token']
                    self.save_token(site_result['token'])
                    self.save_user(username)
                    self.save_id(_user_id)
                    self.close()
                    self.vcode = verficatoin_code_dialog(
                        email= username, 
                        landing_page = self.landingPage, 
                        site_id=result['site_id'], 
                        username=username,
                        company_name=site_name, 
                        login_result=site_result
                    )
                    self.vcode.show()
                    # self.landingPage.show_client_page(site_id=result['site_id'], username=username ,company_name=site_name, login_result=site_result)
                else:
                    print(site_result)
            else:
                print("wrong")
                self.exec_login_failed_message_dialog()
                self.close()

    def process(self, data, keyword):
        keywords = keyword.split('][')
        keywords[0] = keywords[0].split('[')[1]
        keywords[-1] = keywords[-1].split(']')[0]
        output = data.copy()  
        for key in keywords:
            output = output[key]
        return output

    def signup_page_show(self):
        global closeEvent
        closeEvent = "signup"
        self.close()
        self.signup_dialog = Ui_signup_dialog(self)
        self.signup_dialog.show()

    def check_connection(self, url, json, timeout, method):  
        try:
            if method == "get":
                time.sleep(0.02) 
                req = requests.get(
                    url, 
                    json=json
                )
            else: 
                time.sleep(0.02) 
                req = requests.post(
                    url, 
                    json=json,
                    timeout=timeout
                )
            return req
        except requests.exceptions.ConnectionError as err_code:
            QtWidgets.QMessageBox.information(self, 'OK', 'The Internet is not available')
            QtCore.QCoreApplication.quit()
            sys.exit()

    def get_all_company_name(self):
        url = 'http://127.0.0.1:8000/site/'
        all_names = requests.get(
            url,
            timeout=5
        )
        return all_names.json()

    def run(self):
        self.company.clear()
        all_site_names = self.get_all_company_name()
        self.company.addItem('')
        for name in all_site_names:
            self.company.addItem(name)
        self.horizontalLayout_6.addWidget(self.company)
        self.show()

    def save_user(self, username):
        with open('user.bin', 'wb') as user_file:
            user_file.write(username.encode())

    def save_type(self, type):
        with open('type.bin', 'w') as file:
            file.write(type)
        file.close()

    def save_id(self, id):
        with open('id.bin', 'w') as file:
            file.write(str(id))
        file.close()

    def save_company(self, name):
        with open('company.bin', 'w') as file:
            file.write(str(name))
        file.close()

    def save_token(self, token):
        with open('token.bin', 'w') as file:
            file.write(str(token))
        file.close

    # def is_eligible(self, )

    def exec_login_failed_message_dialog(self):
        self.login_failed_dialog = Ui_login_failed_message_dialog()
        self.login_failed_dialog.exec_()

    # def closeEvent(self, evef closeEvent(self, event):
    #     global closeEvent
    #     if closeEvent == 'login':
    #         if self.landingPage.user_token == None:
    #             self.landingPage.close()
    #         else:
    #             username = str(self.username_box.text()).strip().replace("\n", "").upper()
    #             self.landingPage.store_keys(username)
    #             self.landingPage.lets_upload(self.landingPage)
    #     else:
    #         closent):
    #     global closeEvent
    #     if closeEvent == 'login':
    #         if self.landingPage.user_token == None:
    #             self.landingPage.close()
    #         else:
    #             username = str(self.username_box.text()).strip().replace("\n", "").upper()
    #             self.landingPage.store_keys(username)
    #             self.landingPage.lets_upload(self.landingPage)
    #     else:
    #         closeEvent = 'login'

