from hashlib import new
import requests
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect, QObject, QThread
from PyQt5.QtWidgets import QFrame, QAbstractItemView
from PyQt5.QtCore import pyqtSignal as Signal

from commonCodes.progress_bar import SaneDefaultsImageLabel
from .service import Ui_service_dialog
from commonCodes.processLang import dataProcess, dataProcess_with_label

window_width = 800
window_height = 500
global service_url
service_url = ""

class QVLine(QFrame):
    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(QFrame.VLine)
        self.setFixedWidth(1000)
        self.setFrameShadow(QFrame.Sunken)

class GetContractListAndCheckSignedWorker(QObject):
    finished = Signal(list)
    '''
        Getting all contracts from server for user which loged in system. 
        Checking which contract has blockchain file. each contract that has blockchain file is showed to user.
        Also checking if contract signed fully or not.
    '''
    def run(self):
        user_token = self.read_token()
        global service_url, contracts
        headers = {
                    "Content-Type": "application/json",
                    "Authorization": "Token {}".format(user_token)
                }
        payload = self.check_params()
        if payload != False:
            time.sleep(0.01)        
            contracts = requests.get(
                            url=service_url, 
                            headers=headers,
                            params=payload
                        ).json()
        else:
            time.sleep(0.01)        
            contracts = requests.get(
                            url=service_url, 
                            headers=headers,

                        ).json()

        contracts = self.preprocess(data=contracts) # FOR EVALUATION AIR SUBSERVIS
        service_contracts = contracts['services']
        c_list = []

        for contract in service_contracts:
            if contract['blockchain_chain_file'] == True:
                c_list.append(contract)
                number_of_users = contract['number_of_user']
                all_users = contract['users']
                correspond_sign = self.corresponds_sign(number_of_users=number_of_users, all_users=all_users)
                if correspond_sign == 'FULL':
                    contract['signed'] = 'FULL'
                if correspond_sign == 'USER':
                    contract['signed'] = 'SIGNED'
                if correspond_sign == 'NOT':
                    contract['signed'] = 'NOT'
        self.finished.emit(c_list)

    def check_params(self):   

        if service_keywords['params'] != "":
            params = {}
            for param in service_keywords['params']:
                output, label = dataProcess_with_label(_login_result, service_keywords['params'])
                params[param] = output
            return params
        else:
            return False



    def read_user_type(self):
        with open('type.bin', 'r') as file:
            user_type = file.read()
        file.close()
        return user_type

    def read_user_id(self):
        with open('id.bin', 'r') as file:
            user_id = file.read()
        file.close()
        return user_id

    def read_token(self):
        with open('token.bin', 'r') as file:
            user_token = file.read()
        file.close()
        return user_token

    def preprocess(self, data):
        global service_keywords
        new_collection = {
            "services" : [],
            "token" : ""
        }
        services = []
        for contract in data["air_cargo_customer_data_quotations"]:
            # ___ CONTRACT INFO ____
            x = service_keywords['contract_info']
            contract_info = x.split(',')
            new_contract = {"id" : dataProcess(full_data=contract, keyword=contract_info[0])}
            exist = dataProcess(full_data=contract, keyword=contract_info[1])
    
            new_contract["blockchain_chain_file"] = True if exist else False
            new_contract["number_of_user"] = contract_info[2]

            # ___ CONTRACT DATE CREATION ___
            date = service_keywords['created_on'].split(',')
            new_contract["date_created"] = {}
            new_contract["date_created"]["year"] = dataProcess(full_data=contract, keyword=date[0])
            new_contract["date_created"]["month"] = dataProcess(full_data=contract, keyword=date[1])
            new_contract["date_created"]["day"] = dataProcess(full_data=contract, keyword=date[2])

            # ___ USER INFORMATION ___
            new_contract["users"] = self.users(contract)

            # ___ DATA ___
            new_contract['data'] = self.data_collect(full_data=contract, keys=service_keywords['data'])

            new_contract['index'] = self.get_index(cid=new_contract['id'])

            services.append(new_contract)  

        new_collection["services"] = services
        new_collection["token"] = data["token"]
        return new_collection

    def data_collect(self, full_data, keys):
        keys = keys.split(',')
        data_splited = {}
        for key in keys:
            val, label = dataProcess_with_label(full_data=full_data, keyword=key)
            data_splited[label] = val
        return data_splited
        
    def users(self, contract):
        users = {}
        user_1 = {
            "id" : contract["provider"]["id"],
            "username" : contract['provider']['email']['key'],
            "signed" : False,
            "public_key" : contract['provider']['blockchain_public_key']
        }
        user_2 = {
            "id" : contract["service"]["customer"]["id"],
            "username" : contract['service']['customer']['email']['key'],
            "signed" : False,
            "public_key" : contract['service']['customer']['blockchain_public_key']
        }
        users["user_" + str(user_1["id"])] = user_1
        users["user_" + str(user_2["id"])] = user_2
        return users

    def get_index(self, cid):
        with open('id.bin', 'r') as id_file:
            uid = id_file.read()
        return int(str(cid) + str(uid))

    def corresponds_sign(self, number_of_users, all_users):
        '''
            Checking the number of signs. 
            If both sides of the contract sign it, the contract has been signed FULLY. (=Full)
            If one side of the contract sign it who is login, the contract has been signed by the user. (=user)
            If no one signs the contract, the contract has not been signed. (=Not)
        '''
        count = 0
        user_flag = False
        user_id = self.read_user_id()
        for user in all_users:
            if all_users[user]['signed'] == True:
                count += 1
                if str(all_users[user]['id']) == str(user_id):
                    user_flag = True

        if count == number_of_users:
            return 'FULL'
        elif user_flag == True:
            return 'USER'
        else:
            return 'NOT'

class ContractDetailDialog(QtWidgets.QDialog):
    def __init__(self, orig_parent=None):
        super(ContractDetailDialog, self).__init__()
        self.orig_parent = orig_parent
        self.exec_()

    def init_ui(self):
        pass

    def done(self, a0: int):
        self.orig_parent.setVisible(True)
        return super(ContractDetailDialog, self).done(a0)

class MyQWidgetItem(QtWidgets.QWidget):

    def __init__(self, parent=None, data=None, no=0):
        super(MyQWidgetItem, self).__init__()
        self.parent = parent
        self.data = data
        self.no = no
        self.init_ui()

    def init_ui(self):
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()
        items = list()
        self.no_label = QtWidgets.QLabel()
        items.append(self.no_label)
        self.name_label = QtWidgets.QLabel()
        items.append(self.name_label)
        self.date_label = QtWidgets.QLabel()
        items.append(self.date_label)
        self.urlButton = QtWidgets.QPushButton()
        items.append(self.urlButton)
        self.signButton = QtWidgets.QPushButton()
        items.append(self.signButton)
        self.declineButton = QtWidgets.QPushButton()
        items.append(self.declineButton)
        self.status_lable = QtWidgets.QLabel()
        items.append(self.status_lable)

        self.no_label.setText(str(self.no))
        self.name_label.setText(str(self.data['id']))
        self.date_label.setText(
            str(self.data['date_created']['year']) + ' / ' + 
            str(self.data['date_created']['month']) + ' / ' + 
            str(self.data['date_created']['day'])
        )
        self.urlButton.setText('Contract Detail')
        self.status_lable.setText('signed')

        # print(self.data)
        result = self.check_image(self.data)

        if result == 'SIGNED':
            self.status_lable.setPixmap(QtGui.QPixmap("images/single.png"))
        elif result == 'NOT':
            self.status_lable.setPixmap(QtGui.QPixmap("images/not.png"))
        else:
            self.status_lable.setPixmap(QtGui.QPixmap("images/contracts.png"))

        self.hbox.addWidget(self.no_label)
        self.hbox.addWidget(self.name_label)
        self.hbox.addWidget(self.date_label)
        self.hbox.addWidget(self.urlButton)
        self.hbox.addWidget(self.status_lable)
        self.vbox.addItem(self.hbox)
        for item in items:
            self.hbox.setAlignment(item, Qt.AlignCenter)
        self.urlButton.clicked.connect(self.clicked_detail)
        self.setLayout(self.vbox)

    def check_image(self, data):
        counter = 0
        flag = False
        uid = self.read_user_id()
        id = data['id']
        for user in data['users'].values():
            ch_uid = user['id']
            index = str(id) + str(ch_uid)
            if self.check_signature(index):
                if str(ch_uid) == str(uid):
                    flag = True
                counter += 1
        if str(counter) == str(data['number_of_user']):
            return "FULL"
        elif flag == False:
            return "NOT"
        else:
            return "SIGNED"

    def check_signature(self, index):
        key = 'CONTRACT' + str(index)
        btc_url = self.get_blockchain_url(site_iid)
        time.sleep(0.01)
        url = btc_url + 'data/query/' + key
        data = {
            "username" : self.read_user()
        }
        result = requests.get(url=url, data=data)
        return True if 'response' in result.json().keys() else False

    def get_blockchain_url(self, site_id):
        url = 'http://localhost:8000/blockchainn/' + str(site_id)
        result = requests.get(url)
        result = result.json()
        if result['url'][-1] != "/":
            result['url'] += "/"
        return result['url']

    def read_user_id(self):
        with open('id.bin', 'r') as file:
            user_id = file.read()
        file.close()
        return user_id

    def read_user(self):
        with open('user.bin', 'r') as file:
            user = file.read()
        file.close()
        return user

    def clicked_detail(self):
        global service_keywords
        contract_detail = Ui_service_dialog(self.data, service_keywords, site_iid)
        contract_detail.exec_()

class service_list_dialog(QtWidgets.QDialog):
    def __init__(self, widget, service, site_id, login_result):
        global service_url, service_keywords, site_iid, _login_result
        _login_result = login_result
        service_url = service['url']
        site_iid = site_id
        contract_info = service['contract_info']
        user_info = service['user_info']
        created_on = service['created_on']
        data = service['data']
        service_keywords = {
            "contract_info" : contract_info,
            "user_info" : user_info,
            "created_on" : created_on,
            "data" : data,
            "params" : service['params']
        }

        super(service_list_dialog, self).__init__(widget)
        self.setMinimumSize(window_width, window_height)
        self.setWindowTitle("My Contracts")
        self.thread = QThread()
        self.worker = GetContractListAndCheckSignedWorker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.after_data_download)
        self.thread.start()
        self.init_ui()

    def after_data_download(self, data):
        for i in range(1, len(data) + 1):
            myQCustomQWidget = MyQWidgetItem(parent=self, data=data[i - 1], no=i)
            myQListWidgetItem = QtWidgets.QListWidgetItem(self.myQListWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        self.vbox_loading.setEnabled(False)
        self.zbox.takeAt(1).setGeometry(QRect(0, 0, 0, 0))
        self.zbox.removeItem(self.vbox_loading)
        self.zbox.update()
        self.update()

    def init_ui(self):
        self.zbox = QtWidgets.QGridLayout()
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox_loading = QtWidgets.QVBoxLayout()
        self.myQListWidget = QtWidgets.QListWidget(self)
        self.load_progress_bar()
        self.load_table()
        self.zbox.addItem(self.vbox, 0, 0)
        self.zbox.addItem(self.vbox_loading, 0, 0)
        self.setLayout(self.zbox)

    def load_progress_bar(self):
        self.bar = SaneDefaultsImageLabel()
        empty_label = QtWidgets.QLabel()
        hbox = QtWidgets.QHBoxLayout()
        empty_label.setText('')
        self.vbox_loading.addWidget(empty_label)
        hbox.addWidget(empty_label)
        hbox.addWidget(self.bar)
        hbox.addWidget(empty_label)
        self.vbox_loading.addItem(hbox)
        self.vbox_loading.addWidget(empty_label)

    def load_table(self):
        self.load_table_header()
        self.myQListWidget.setSelectionRectVisible(False)
        self.myQListWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.myQListWidget.verticalScrollBar().setMinimumWidth(40)

    def load_table_header(self):
        self.hbox = QtWidgets.QHBoxLayout()
        for item in ['No.', 'Contract ID', 'Date', 'Operates', 'Status']:
            label = QtWidgets.QLabel()
            label.setFixedWidth(32)
            self.hbox.addWidget(label)
            label = QtWidgets.QLabel()
            label.setText(item)
            self.hbox.addWidget(label)
            self.hbox.setAlignment(label, Qt.AlignCenter)
        self.vbox.addItem(self.hbox)
        self.vbox.addWidget(self.myQListWidget)
    # ----------------------------------------------------------------------------------------
    def show(self):
        super(service_list_dialog, self).show()
        self.update()

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.myQListWidget.setFixedWidth(a0.size().width() - 20)
        self.myQListWidget.setFixedHeight(a0.size().height())
        return super(service_list_dialog, self).resizeEvent(a0)
