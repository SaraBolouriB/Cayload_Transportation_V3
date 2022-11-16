from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import requests
from PyQt5.QtCore import QThread, QObject, pyqtSignal, QRect
from PyQt5.QtWidgets import QMessageBox

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

from cryptography.fernet import Fernet
import time
import json
import os
import base64

from commonCodes.progress_bar import SaneDefaultsImageLabel

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PDFJS = QtCore.QUrl.fromLocalFile(
    os.path.join(CURRENT_DIR, "pdfjs/web/viewer.html")
).toString()


class PdfReport(QtWebEngineWidgets.QWebEngineView):

    def __init__(self, parent=None):
        super(PdfReport, self).__init__(parent)

    def loadPdf(self, file_name):

        url = QtCore.QUrl.fromLocalFile(CURRENT_DIR + '/' +file_name).toString()
        self.load(QtCore.QUrl.fromUserInput("%s?file=%s" % (PDFJS, url)))
    def sizeHint(self):
        return QtCore.QSize(640, 480)

class ContractSignatureWorker(QObject):
    finished = pyqtSignal(str, bool)

    def __init__(self, data, keywords, site_id):
        super(ContractSignatureWorker, self).__init__()
        self.data = data
        self.keywords = keywords
        self.site_id = site_id
        self.token = self.read_token()
        self.user = self.read_user()
        self.id = self.read_id()

    def read_token(self):
        with open('token.bin', 'rb') as token_file:
            token = token_file.read()
        token_file.close()
        return token

    def read_user(self):
        with open('user.bin', 'rb') as user_file:
            user = user_file.read()
        user_file.close()
        return user

    def read_id(self):
        with open('id.bin', 'r') as id_file:
            id = id_file.read()
        id_file.close()
        return id
    
    # --- RUN --------------------------------------------------------------  
    def run(self):
        is_contract_sign = 'False'
        check_signature = self.check_signature(index=self.data['index'])
        if check_signature == True:
            is_contract_sign = 'True'

        self.create_contract_pdf('none')

        self.finished.emit(is_contract_sign, False)

    def check_signature(self, index):
        key = 'CONTRACT' + str(index)
        btc_url = self.get_blockchain_url(self.site_id)
        time.sleep(0.01)
        url = btc_url + 'data/query/' + key
        data = {
            "username" : self.user
        }
        result = requests.get(url=url, data=data)
        return True if 'response' in result.json().keys() else False

    def create_contract_pdf(self, data):
        if data == 'none':
            id = self.data['id']
            data = self.data['data']
            date = self.data['date_created']
            index = self.data['index']
            if os.path.isdir('Service/contracts_pdf') == False:
                os.makedirs('Service/contracts_pdf')

            fileName = 'Service/contracts_pdf/contract_' + str(index) + '.pdf'
            pdf = canvas.Canvas(fileName)
            pdf.translate(cm, cm)
            pdf.setPageSize((3482, 2450))
            pdf.drawInlineImage('images/contract.png', -30, -25)
            pdf.setFont('Helvetica-Bold', 50)
            pdf.setFillColor('black')
            length = 200
            width = 1650
            pdf.drawString(length, width, "Contract ID: " + str(id))
            pdf.drawString(2500, 2150, str(date['year'])+'-'+str(date['month'])+'-'+str(date['day']))
            for item in data:
                width-=100
                pdf.drawString(length, width, str(item)+ ": " + str(data[item]))

            pdf.save()
    # ----------------------------------------------------------------------

    # --- IMPLMENT ---------------------------------------------------------
    def implement(self):
        # Sign contract information by user's private_key 
        blockchain_data = self.sign_contract_data()

        #Send data to Hyperledger Fabric
        try:
            btc_url = self.get_blockchain_url(self.site_id)
            self.send_data_to_blockchain(blockchain_data, btc_url) 

            self.finished.emit('', True)
        except BaseException as error:
            print(error)

    def sign_contract_data(self):
        username = self.read_user().decode('UTF-8')
        raw_contract_data = self.data['data']
        index = str(self.data['index'])

        blockchain_data = {
            "key": str(index),
            "data": raw_contract_data,
            "username": str(username)
        }
        return blockchain_data
        
    def get_blockchain_url(self, site_id):
        url = 'http://localhost:8000/blockchainn/' + str(site_id)
        result = requests.get(url).json()
        if result['url'][-1] != "/":
            result['url'] += "/"
        return result['url']


    def send_data_to_blockchain(self, contract_data, btc_url):
        url = btc_url + 'data/add'
        headers = {
            "Content-Type": "application/json", 
        }
        time.sleep(0.01) 
        result = requests.post(url, json=contract_data)
        return result    
    # ----------------------------------------------------------------------

class Ui_service_dialog(QtWidgets.QDialog):
    def __init__(self, data, keywords, site_id):
        super().__init__()
        service_dialog = self
        self.data = data
        self.keywords = keywords
        self.site_id = site_id
        self.is_signing = False
        self.user_id = self.read_id()
        self.setupUi(service_dialog)

    def setupUi(self, service_dialog):
        self._width = 1024
        self._height = 720
        self.prg_x_loc = self._width / 2 - 100
        self.prg_y_loc = self._height / 2 - 100
        service_dialog.setObjectName("service_dialog")
        service_dialog.resize(self._width, self._height)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.356db89e.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        service_dialog.setWindowIcon(icon)
        service_dialog.setWindowTitle('Test')
        self.gridLayout = QtWidgets.QGridLayout(service_dialog)
        self.gridLayout.setObjectName("gridLayout")

        self.frame = QtWidgets.QFrame(service_dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.pdf = PdfReport()
        
        self.vbox = QtWidgets.QVBoxLayout(self.frame)
        self.vbox.setObjectName("vbox")

        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox1.setObjectName("hbox1")

        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox2.setObjectName("hbox2")
        
        self.signature_Button = QtWidgets.QPushButton(self.frame)
        self.signature_Button.setObjectName("signature_Button")

        self.hbox1.addWidget(self.pdf)
        self.hbox2.addWidget(self.signature_Button)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.signature_Button.clicked.connect(self.implement)

        self.retranslateUi(service_dialog)
        QtCore.QMetaObject.connectSlotsByName(service_dialog)
        self.prg_bar = SaneDefaultsImageLabel()
        self.prg_bar.setGeometry(QRect(self.prg_x_loc, self.prg_y_loc, 200, 200))
        self.layout().addChildWidget(self.prg_bar)
        service_dialog.show()

    def show(self):
        super(Ui_service_dialog, self).show()
        self.is_signing = True
        self.signature_Button.setEnabled(False)
        self.thread = QThread()
        self.worker = ContractSignatureWorker(self.data, self.keywords, self.site_id)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.show_contracts_list)
        self.thread.start()

    def retranslateUi(self, service_dialog):
        _translate = QtCore.QCoreApplication.translate
        service_dialog.setWindowTitle(_translate("service_dialog", "Dialog"))
        self.signature_Button.setText(_translate("service_dialog", "Signature"))

    def show_contracts_list(self, is_contract_sign):
        num_users = self.data['number_of_user']
        id = str(self.data['id'])
        self.is_signing = False
        self.prg_bar.setVisible(False)
        if is_contract_sign != 'True':
            corresponds_public_Key = []
            all_users = self.data['users']
            for user in all_users:
                user = all_users[user]
                if user['public_key']:
                    corresponds_public_Key.append({
                            'public_key': user['public_key'],
                            'user': user['username']
                        })

            if str(len(corresponds_public_Key)) == str(num_users):
                self.signature_Button.setEnabled(True)
            else:
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setWindowTitle('signature not available')
                self.msg.setText("other participants haven't started blockchain application")
                self.msg.setStandardButtons(QMessageBox.Ok)
                self.msg.buttonClicked.connect(self.error_message_btn)
                self.msg.show()
                self.msg.exec_()
                self.signature_Button.setDisabled(True)
            self.pdf = self.pdf.loadPdf('Service/contracts_pdf/contract_' + id + self.user_id + '.pdf')
        else:
            self.signature_Button.setDisabled(True)
            self.pdf = self.pdf.loadPdf('Service/contracts_pdf/contract_' + id + self.user_id + '.pdf')

    def implement(self):
        self.prg_bar.setVisible(True)
        self.signature_Button.setEnabled(False)
        self.is_signing = True
        self.thread = QThread()
        self.worker = ContractSignatureWorker(self.data, self.keywords, self.site_id)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.implement)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.sign_finished)
        self.thread.start()

    def sign_finished(self, result, result_2):
        self.prg_bar.setVisible(False)
        self.is_signing = False
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Contract Signed')
        msg.setText("Your Contract has been signed successfully")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.message_btn)
        msg.show()
        msg.exec_()

    def read_id(self):
        with open('id.bin', 'r') as id_file:
            id = id_file.read()
        id_file.close()
        return id

    def error_message_btn(self, i):
        self.msg.close()

    def message_btn(self, i):
        self.close()

    def close(self):
        if self.is_signing:
            return None
        return super(Ui_service_dialog, self).close()

    def done(self, a0: int):
        if self.is_signing:
            return None
        return super(Ui_service_dialog, self).done(a0)

    def closeEvent(self, a0: QtGui.QCloseEvent):
        if self.is_signing:
            a0.ignore()
        super(Ui_service_dialog, self).closeEvent(a0)