from PyQt5 import QtCore, QtGui, QtWidgets
import requests


class Ui_admin_page(QtWidgets.QDialog):
    def __init__(self, site_id=None, login_id=None, blockchain_id=None):
        super().__init__()
        # INITIALIZATION VARIABLES ---------------------------------------------
        # ----------------------------------------------------------------------
        admin_Dialog = self
        self.site_id = site_id
        self.login_id = login_id
        self.blockchain_id = blockchain_id
        self.submit_login = True if self.login_id != None else None
        self.submit_blockchain = True if self.blockchain_id != None else None
        self._all_services = None
        self._id_service_current = None
        # ----------------------------------------------------------------------
        self.setupUi(admin_Dialog)

    def setupUi(self, landing_page):
        login_dic, blockchain_dic = self.get_all_information()
        self.get_services_information()

        landing_page.setObjectName("landing_page")
        landing_page.setEnabled(True)
        landing_page.resize(670, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(landing_page.sizePolicy().hasHeightForWidth())
        landing_page.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../../../../.designer/Desktop/logo.356db89e.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        landing_page.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(landing_page)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)
        self.Subject = QtWidgets.QHBoxLayout()
        self.Subject.setObjectName("Subject")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Subject.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.framework = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.framework.setFont(font)
        self.framework.setObjectName("framework")
        self.verticalLayout.addWidget(self.framework)
        self.adminPage = QtWidgets.QLabel(self.frame)
        self.adminPage.setAlignment(QtCore.Qt.AlignCenter)
        self.adminPage.setObjectName("adminPage")
        self.verticalLayout.addWidget(self.adminPage)
        self.Subject.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Subject.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.Subject, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.Admin_bar = QtWidgets.QTabWidget(self.centralwidget)
        self.Admin_bar.setEnabled(True)
        self.Admin_bar.setMinimumSize(QtCore.QSize(650, 410))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 209, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 179, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 99, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 202, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 209, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 179, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 99, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 202, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 209, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(103, 179, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 99, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 74, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 149, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.Admin_bar.setPalette(palette)
        self.Admin_bar.setStyleSheet("selection-color: rgb(0, 0, 0);")
        self.Admin_bar.setObjectName("Admin_bar")
        self.Login_Info = QtWidgets.QWidget()
        self.Login_Info.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Login_Info.setAccessibleName("")
        self.Login_Info.setObjectName("Login_Info")
        self.L = QtWidgets.QGridLayout(self.Login_Info)
        self.L.setObjectName("L")
        self.Login = QtWidgets.QVBoxLayout()
        self.Login.setObjectName("Login")
        self.widget = QtWidgets.QWidget(self.Login_Info)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.login_username = QtWidgets.QHBoxLayout()
        self.login_username.setObjectName("login_username")
        self.label_login_username = QtWidgets.QLabel(self.widget)
        self.label_login_username.setObjectName("label_login_username")
        self.login_username.addWidget(self.label_login_username)
        self.lineEdit_login_username = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_login_username.setObjectName("lineEdit_login_username")
        self.login_username.addWidget(self.lineEdit_login_username)
        self.verticalLayout_6.addLayout(self.login_username)
        self.login_pass = QtWidgets.QHBoxLayout()
        self.login_pass.setObjectName("login_pass")
        self.label_login_pass = QtWidgets.QLabel(self.widget)
        self.label_login_pass.setObjectName("label_login_pass")
        self.login_pass.addWidget(self.label_login_pass)
        self.lineEdit_login_pass = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_login_pass.setObjectName("lineEdit_login_pass")
        self.login_pass.addWidget(self.lineEdit_login_pass)
        self.verticalLayout_6.addLayout(self.login_pass)
        self.login_public = QtWidgets.QHBoxLayout()
        self.login_public.setObjectName("login_public")
        self.label_login_public = QtWidgets.QLabel(self.widget)
        self.label_login_public.setObjectName("label_login_public")
        self.login_public.addWidget(self.label_login_public)
        self.lineEdit_login_public = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_login_public.setObjectName("lineEdit_login_public")
        self.login_public.addWidget(self.lineEdit_login_public)
        self.verticalLayout_6.addLayout(self.login_public)
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_6.addWidget(self.line_5)
        self.login_URL = QtWidgets.QHBoxLayout()
        self.login_URL.setObjectName("login_URL")
        self.label_login_URL = QtWidgets.QLabel(self.widget)
        self.label_login_URL.setObjectName("label_login_URL")
        self.login_URL.addWidget(self.label_login_URL)
        self.lineEdit_login_URL = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_login_URL.setObjectName("lineEdit_login_URL")
        self.login_URL.addWidget(self.lineEdit_login_URL)
        self.verticalLayout_6.addLayout(self.login_URL)
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 3)
        self.login_submit = QtWidgets.QPushButton(self.widget)
        self.login_submit.setObjectName("login_submit")
        self.login_submit.clicked.connect(self.submit_login_info) # SUBMIT LOGIN INFO DATA
        self.gridLayout.addWidget(self.login_submit, 4, 1, 1, 1)
        self.login_Edit = QtWidgets.QPushButton(self.widget)
        self.login_Edit.setObjectName("login_Edit")
        self.login_Edit.clicked.connect(self.edit_login_info)
        self.gridLayout.addWidget(self.login_Edit, 4, 2, 1, 1)
        self.LOGIN_API_LABEL = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.LOGIN_API_LABEL.setFont(font)
        self.LOGIN_API_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.LOGIN_API_LABEL.setObjectName("LOGIN_API_LABEL")
        self.gridLayout.addWidget(self.LOGIN_API_LABEL, 0, 0, 1, 3)
        self.Login.addWidget(self.widget)
        self.L.addLayout(self.Login, 0, 0, 1, 1)
        self.Admin_bar.addTab(self.Login_Info, "")

        if login_dic != None:
            self.lineEdit_login_URL.setText(login_dic['url'])
            jsonData = login_dic['data'].split(',')
            self.lineEdit_login_username.setText(jsonData[0])
            self.lineEdit_login_pass.setText(jsonData[1])
            self.lineEdit_login_public.setText(jsonData[2])

        # BLOCKCHIAN API ---------------------------------------------------------
        self.Blockchain_API = QtWidgets.QWidget()
        self.Blockchain_API.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Blockchain_API.setObjectName("Blockchain_API")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Blockchain_API)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Blockchain = QtWidgets.QVBoxLayout()
        self.Blockchain.setObjectName("Blockchain")
        self.widget_2 = QtWidgets.QWidget(self.Blockchain_API)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Blockchain_API1 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Blockchain_API1.setFont(font)
        self.Blockchain_API1.setAlignment(QtCore.Qt.AlignCenter)
        self.Blockchain_API1.setObjectName("Blockchain_API1")
        self.verticalLayout_3.addWidget(self.Blockchain_API1)
        self.blockchain_URL = QtWidgets.QHBoxLayout()
        self.blockchain_URL.setObjectName("blockchain_URL")
        self.Label_blockchain_URL = QtWidgets.QLabel(self.widget_2)
        self.Label_blockchain_URL.setObjectName("Label_blockchain_URL")
        self.blockchain_URL.addWidget(self.Label_blockchain_URL)
        self.lineEdit_blockchain_URL = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_blockchain_URL.setObjectName("lineEdit_blockchain_URL")
        self.blockchain_URL.addWidget(self.lineEdit_blockchain_URL)
        self.verticalLayout_3.addLayout(self.blockchain_URL)
        self.Submit_blockchain = QtWidgets.QPushButton(self.widget_2)
        self.Submit_blockchain.setObjectName("Submit_blockchain")
        self.Submit_blockchain.clicked.connect(self.submit_blockchain_info) # SUBMIT BLOCKCHAIN DATA
        self.verticalLayout_3.addWidget(self.Submit_blockchain)
        self.Edit_blockchain = QtWidgets.QPushButton(self.widget_2)
        self.Edit_blockchain.setObjectName("Edit_blockchain")
        self.Edit_blockchain.clicked.connect(self.edit_blockchain_info) # EDIT BLOCKCHAIN DATA
        self.verticalLayout_3.addWidget(self.Edit_blockchain)

        if blockchain_dic != None:
            self.lineEdit_blockchain_URL.setText(blockchain_dic['url'])
        
        self.Blockchain.addWidget(self.widget_2)
        self.gridLayout_5.addLayout(self.Blockchain, 0, 0, 1, 1)
        self.Admin_bar.addTab(self.Blockchain_API, "")
        # -----------------------------------------------------------------------

        # ADD NEW SERVICE -------------------------------------------------------
        self.Add_Service = QtWidgets.QWidget()
        self.Add_Service.setObjectName("Add_Service")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Add_Service)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.add_service = QtWidgets.QVBoxLayout()
        self.add_service.setObjectName("add_service")
        self.widget_3 = QtWidgets.QWidget(self.Add_Service)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.add_new_service = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.add_new_service.setFont(font)
        self.add_new_service.setAlignment(QtCore.Qt.AlignCenter)
        self.add_new_service.setObjectName("add_new_service")
        self.verticalLayout_4.addWidget(self.add_new_service)
        self.service_name = QtWidgets.QHBoxLayout()
        self.service_name.setObjectName("service_name")
        self.label_service_name = QtWidgets.QLabel(self.widget_3)
        self.label_service_name.setObjectName("label_service_name")
        self.service_name.addWidget(self.label_service_name)
        self.lineEdit_service_name = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_service_name.setObjectName("lineEdit_service_name")
        self.service_name.addWidget(self.lineEdit_service_name)
        self.verticalLayout_4.addLayout(self.service_name)
        self.URL_service = QtWidgets.QHBoxLayout()
        self.URL_service.setObjectName("URL_service")
        self.label_URL_service = QtWidgets.QLabel(self.widget_3)
        self.label_URL_service.setObjectName("label_URL_service")
        self.URL_service.addWidget(self.label_URL_service)
        self.lineEdit_URL_service = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_URL_service.setObjectName("lineEdit_URL_service")
        self.URL_service.addWidget(self.lineEdit_URL_service)
        self.verticalLayout_4.addLayout(self.URL_service)
        self.ServiceJSON = QtWidgets.QTabWidget(self.widget_3)
        self.ServiceJSON.setObjectName("ServiceJSON")
        self.ContractInformation = QtWidgets.QWidget()
        self.ContractInformation.setObjectName("ContractInformation")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.ContractInformation)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 575, 24))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.creationDate = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.creationDate.setContentsMargins(0, 0, 0, 0)
        self.creationDate.setObjectName("creationDate")
        self.label_year = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_year.setObjectName("label_year")
        self.creationDate.addWidget(self.label_year)
        self.lineEdit_year = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.creationDate.addWidget(self.lineEdit_year)
        self.label_month = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_month.setObjectName("label_month")
        self.creationDate.addWidget(self.label_month)
        self.lineEdit_month = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_month.setObjectName("lineEdit_month")
        self.creationDate.addWidget(self.lineEdit_month)
        self.label_day = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_day.setObjectName("label_day")
        self.creationDate.addWidget(self.label_day)
        self.lineEdit_day = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_day.setObjectName("lineEdit_day")
        self.creationDate.addWidget(self.lineEdit_day)
        self.label_3 = QtWidgets.QLabel(self.ContractInformation)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 161, 16))
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.ContractInformation)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 571, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.contractInfo = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.contractInfo.setContentsMargins(0, 0, 0, 0)
        self.contractInfo.setObjectName("contractInfo")
        self.label_contractID = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_contractID.setObjectName("label_contractID")
        self.contractInfo.addWidget(self.label_contractID)
        self.lineEdit_contractID = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_contractID.setObjectName("lineEdit_contractID")
        self.contractInfo.addWidget(self.lineEdit_contractID)
        self.label_chainfile = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_chainfile.setObjectName("label_chainfile")
        self.contractInfo.addWidget(self.label_chainfile)
        self.lineEdit_chainfile = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_chainfile.setObjectName("lineEdit_chainfile")
        self.contractInfo.addWidget(self.lineEdit_chainfile)
        self.label_number = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_number.setObjectName("label_number")
        self.contractInfo.addWidget(self.label_number)
        self.lineEdit_number = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.contractInfo.addWidget(self.lineEdit_number)
        self.line_6 = QtWidgets.QFrame(self.ContractInformation)
        self.line_6.setGeometry(QtCore.QRect(10, 40, 571, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.ServiceJSON.addTab(self.ContractInformation, "")
        self.UserInformation = QtWidgets.QWidget()
        self.UserInformation.setObjectName("UserInformation")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.UserInformation)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 571, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.service_userID = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.service_userID.setContentsMargins(0, 0, 0, 0)
        self.service_userID.setObjectName("service_userID")
        self.label_service_userID = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_service_userID.setObjectName("label_service_userID")
        self.service_userID.addWidget(self.label_service_userID)
        self.lineEdit_service_userID = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_service_userID.setObjectName("lineEdit_service_userID")
        self.service_userID.addWidget(self.lineEdit_service_userID)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.UserInformation)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 50, 571, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.service_username = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.service_username.setContentsMargins(0, 0, 0, 0)
        self.service_username.setObjectName("service_username")
        self.label_service_username = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_service_username.setObjectName("label_service_username")
        self.service_username.addWidget(self.label_service_username)
        self.lineEdit_service_username = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_service_username.setObjectName("lineEdit_service_username")
        self.service_username.addWidget(self.lineEdit_service_username)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.UserInformation)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 90, 571, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.service_public = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.service_public.setContentsMargins(0, 0, 0, 0)
        self.service_public.setObjectName("service_public")
        self.label_service_public = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_service_public.setObjectName("label_service_public")
        self.service_public.addWidget(self.label_service_public)
        self.lineEdit_service_public = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_service_public.setObjectName("lineEdit_service_public")
        self.service_public.addWidget(self.lineEdit_service_public)
        self.ServiceJSON.addTab(self.UserInformation, "")
        self.Data = QtWidgets.QWidget()
        self.Data.setObjectName("Data")
        self.label_23 = QtWidgets.QLabel(self.Data)
        self.label_23.setGeometry(QtCore.QRect(10, 10, 231, 16))
        self.label_23.setObjectName("label_23")
        self.textEdit_data = QtWidgets.QTextEdit(self.Data)
        self.textEdit_data.setGeometry(QtCore.QRect(10, 30, 571, 111))
        self.textEdit_data.setObjectName("textEdit_data")
        self.ServiceJSON.addTab(self.Data, "")
        self.verticalLayout_4.addWidget(self.ServiceJSON)
        self.Submit_service = QtWidgets.QPushButton(self.widget_3)
        self.Submit_service.setObjectName("Submit_service")
        self.Submit_service.clicked.connect(self.submit_service_info) # SUBMIT SERVICE INFO
        self.verticalLayout_4.addWidget(self.Submit_service)
        self.add_service.addWidget(self.widget_3)
        self.gridLayout_6.addLayout(self.add_service, 0, 0, 1, 1)
        self.Admin_bar.addTab(self.Add_Service, "")
        self.Edit_Service = QtWidgets.QWidget()
        self.Edit_Service.setObjectName("Edit_Service")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.Edit_Service)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.edit_service = QtWidgets.QVBoxLayout()
        self.edit_service.setObjectName("edit_service")
        self.widget_4 = QtWidgets.QWidget(self.Edit_Service)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.edit_service_label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.edit_service_label.setFont(font)
        self.edit_service_label.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_service_label.setObjectName("edit_service_label")
        self.verticalLayout_5.addWidget(self.edit_service_label)
        self.choose_service = QtWidgets.QHBoxLayout()
        self.choose_service.setObjectName("choose_service")
        self.label_chooseService = QtWidgets.QLabel(self.widget_4)
        self.label_chooseService.setObjectName("label_chooseService")
        self.choose_service.addWidget(self.label_chooseService)
        self.comboBox_chooseService = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_chooseService.setObjectName("comboBox_chooseService")
        self.comboBox_chooseService.activated[str].connect(self.choose_service_for_edit) # CHOOSE SERVICE FOR EDITING
        self.choose_service.addWidget(self.comboBox_chooseService)
        self.verticalLayout_5.addLayout(self.choose_service)
        self.line_3 = QtWidgets.QFrame(self.widget_4)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)
        self.serviceEdit_name = QtWidgets.QHBoxLayout()
        self.serviceEdit_name.setObjectName("serviceEdit_name")
        self.label_serviceEdit_name = QtWidgets.QLabel(self.widget_4)
        self.label_serviceEdit_name.setObjectName("label_serviceEdit_name")
        self.serviceEdit_name.addWidget(self.label_serviceEdit_name)
        self.lineEdit_serviceEdit_name = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_serviceEdit_name.setObjectName("lineEdit_serviceEdit_name")
        self.serviceEdit_name.addWidget(self.lineEdit_serviceEdit_name)
        self.verticalLayout_5.addLayout(self.serviceEdit_name)
        self.serviceEdit_URL = QtWidgets.QHBoxLayout()
        self.serviceEdit_URL.setObjectName("serviceEdit_URL")
        self.label_serviceEdit_URL = QtWidgets.QLabel(self.widget_4)
        self.label_serviceEdit_URL.setObjectName("label_serviceEdit_URL")
        self.serviceEdit_URL.addWidget(self.label_serviceEdit_URL)
        self.lineEdit_serviceEdit_URL = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_serviceEdit_URL.setObjectName("lineEdit_serviceEdit_URL")
        self.serviceEdit_URL.addWidget(self.lineEdit_serviceEdit_URL)
        self.verticalLayout_5.addLayout(self.serviceEdit_URL)
        self.editServices = QtWidgets.QTabWidget(self.widget_4)
        self.editServices.setObjectName("editServices")
        self.ContractInfo = QtWidgets.QWidget()
        self.ContractInfo.setObjectName("ContractInfo")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.ContractInfo)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 571, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.serviceEdit_contractInfo = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.serviceEdit_contractInfo.setContentsMargins(0, 0, 0, 0)
        self.serviceEdit_contractInfo.setObjectName("serviceEdit_contractInfo")
        self.label_edit_contractID = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_edit_contractID.setObjectName("label_edit_contractID")
        self.serviceEdit_contractInfo.addWidget(self.label_edit_contractID)
        self.lineEdit_edit_contractID = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_edit_contractID.setObjectName("lineEdit_edit_contractID")
        self.serviceEdit_contractInfo.addWidget(self.lineEdit_edit_contractID)
        self.label_edit_chainfile = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_edit_chainfile.setObjectName("label_edit_chainfile")
        self.serviceEdit_contractInfo.addWidget(self.label_edit_chainfile)
        self.lineEdit_edit_chainfile = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_edit_chainfile.setObjectName("lineEdit_edit_chainfile")
        self.serviceEdit_contractInfo.addWidget(self.lineEdit_edit_chainfile)
        self.label_edit_num = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_edit_num.setObjectName("label_edit_num")
        self.serviceEdit_contractInfo.addWidget(self.label_edit_num)
        self.lineEdit_edit_num = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_edit_num.setObjectName("lineEdit_edit_num")
        self.serviceEdit_contractInfo.addWidget(self.lineEdit_edit_num)
        self.line_7 = QtWidgets.QFrame(self.ContractInfo)
        self.line_7.setGeometry(QtCore.QRect(10, 40, 571, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_25 = QtWidgets.QLabel(self.ContractInfo)
        self.label_25.setGeometry(QtCore.QRect(10, 60, 161, 16))
        self.label_25.setObjectName("label_25")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.ContractInfo)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 80, 571, 24))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.Edit_creationContract = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.Edit_creationContract.setContentsMargins(0, 0, 0, 0)
        self.Edit_creationContract.setObjectName("Edit_creationContract")
        self.label_edit_year = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_edit_year.setObjectName("label_edit_year")
        self.Edit_creationContract.addWidget(self.label_edit_year)
        self.lineEdit_edit_year = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_edit_year.setObjectName("lineEdit_edit_year")
        self.Edit_creationContract.addWidget(self.lineEdit_edit_year)
        self.label_edit_month = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_edit_month.setObjectName("label_edit_month")
        self.Edit_creationContract.addWidget(self.label_edit_month)
        self.lineEdit_edit_month = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_edit_month.setObjectName("lineEdit_edit_month")
        self.Edit_creationContract.addWidget(self.lineEdit_edit_month)
        self.label_edit_day = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_edit_day.setObjectName("label_edit_day")
        self.Edit_creationContract.addWidget(self.label_edit_day)
        self.lineEdit_edit_day = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_edit_day.setObjectName("lineEdit_edit_day")
        self.Edit_creationContract.addWidget(self.lineEdit_edit_day)
        self.editServices.addTab(self.ContractInfo, "")
        self.userInfo = QtWidgets.QWidget()
        self.userInfo.setObjectName("userInfo")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.userInfo)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 20, 571, 24))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.edit_userID = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.edit_userID.setContentsMargins(0, 0, 0, 0)
        self.edit_userID.setObjectName("edit_userID")
        self.label_edit_userID = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_edit_userID.setObjectName("label_edit_userID")
        self.edit_userID.addWidget(self.label_edit_userID)
        self.lineEdit_edit_userID = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.lineEdit_edit_userID.setObjectName("lineEdit_edit_userID")
        self.edit_userID.addWidget(self.lineEdit_edit_userID)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.userInfo)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 80, 571, 24))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.edit_public = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.edit_public.setContentsMargins(0, 0, 0, 0)
        self.edit_public.setObjectName("edit_public")
        self.label_edit_public = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_edit_public.setObjectName("label_edit_public")
        self.edit_public.addWidget(self.label_edit_public)
        self.lineEdit_edit_public = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_edit_public.setObjectName("lineEdit_edit_public")
        self.edit_public.addWidget(self.lineEdit_edit_public)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.userInfo)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(10, 50, 571, 24))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.edit_username = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.edit_username.setContentsMargins(0, 0, 0, 0)
        self.edit_username.setObjectName("edit_username")
        self.label_edit_username = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_edit_username.setObjectName("label_edit_username")
        self.edit_username.addWidget(self.label_edit_username)
        self.lineEdit_edit_username = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.lineEdit_edit_username.setObjectName("lineEdit_edit_username")
        self.edit_username.addWidget(self.lineEdit_edit_username)
        self.editServices.addTab(self.userInfo, "")
        self.Edit_Data = QtWidgets.QWidget()
        self.Edit_Data.setObjectName("Edit_Data")
        self.Edit_data = QtWidgets.QTextEdit(self.Edit_Data)
        self.Edit_data.setGeometry(QtCore.QRect(10, 10, 571, 91))
        self.Edit_data.setObjectName("Edit_data")
        self.editServices.addTab(self.Edit_Data, "")
        self.verticalLayout_5.addWidget(self.editServices)
        self.serviceEdit_edit = QtWidgets.QPushButton(self.widget_4)
        self.serviceEdit_edit.setObjectName("serviceEdit_edit")
        self.serviceEdit_edit.clicked.connect(self.edit_service_info)
        self.verticalLayout_5.addWidget(self.serviceEdit_edit)
        self.serviceEdit_delete = QtWidgets.QPushButton(self.widget_4)
        self.serviceEdit_delete.setObjectName("serviceEdit_delete")
        self.serviceEdit_delete.clicked.connect(self.delete_service)
        self.verticalLayout_5.addWidget(self.serviceEdit_delete)
        self.edit_service.addWidget(self.widget_4)
        self.gridLayout_8.addLayout(self.edit_service, 0, 0, 1, 1)
        self.Admin_bar.addTab(self.Edit_Service, "")
        self.verticalLayout_2.addWidget(self.Admin_bar)
        self.statusbar = QtWidgets.QStatusBar(landing_page)
        self.statusbar.setObjectName("statusbar")
        self.actionShow_PublicKey = QtWidgets.QAction(landing_page)
        self.actionShow_PublicKey.setObjectName("actionShow_PublicKey")
        self.actionExit = QtWidgets.QAction(landing_page)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(landing_page)
        self.Admin_bar.setCurrentIndex(0)
        self.ServiceJSON.setCurrentIndex(0)
        self.editServices.setCurrentIndex(0)
        self.actionShow_PublicKey.triggered.connect(landing_page.close)
        self.actionExit.triggered.connect(landing_page.close)
        QtCore.QMetaObject.connectSlotsByName(landing_page)

        self.combobox_updated()
        self.buttom_update()

    def retranslateUi(self, landing_page):
        _translate = QtCore.QCoreApplication.translate
        landing_page.setWindowTitle(_translate("landing_page", "Framework"))
        self.framework.setText(_translate("landing_page", "Framework"))
        self.adminPage.setText(_translate("landing_page", "Admin Page"))
        self.label_8.setText(_translate("landing_page", "Data format which must be sent to the sever:"))
        self.label_login_username.setText(_translate("landing_page", "Username :"))
        self.label_login_pass.setText(_translate("landing_page", "Password  :"))
        self.label_login_public.setText(_translate("landing_page", "Public Key  :"))
        self.label_login_URL.setText(_translate("landing_page", "URL: "))
        self.login_submit.setText(_translate("landing_page", "Submit"))
        self.login_Edit.setText(_translate("landing_page", "Edit"))
        self.LOGIN_API_LABEL.setText(_translate("landing_page", "Login API"))
        self.Admin_bar.setTabText(self.Admin_bar.indexOf(self.Login_Info), _translate("landing_page", "Login API Information"))
        self.Blockchain_API1.setText(_translate("landing_page", "Contract Data API"))
        self.Label_blockchain_URL.setText(_translate("landing_page", "URL :"))
        self.Submit_blockchain.setText(_translate("landing_page", "Submit"))
        self.Edit_blockchain.setText(_translate("landing_page", "Edit"))
        self.Admin_bar.setTabText(self.Admin_bar.indexOf(self.Blockchain_API), _translate("landing_page", "Blockchain API"))
        self.add_new_service.setText(_translate("landing_page", "Add New Service"))
        self.label_service_name.setText(_translate("landing_page", "Service Name :"))
        self.label_URL_service.setText(_translate("landing_page", "URL :"))
        self.label_year.setText(_translate("landing_page", "Year :"))
        self.label_month.setText(_translate("landing_page", "Month :"))
        self.label_day.setText(_translate("landing_page", "Day :"))
        self.label_3.setText(_translate("landing_page", "Creation Date of Contract"))
        self.label_contractID.setText(_translate("landing_page", "Contract ID :"))
        self.label_chainfile.setText(_translate("landing_page", "Chain File :"))
        self.label_number.setText(_translate("landing_page", "Number of users :"))
        self.ServiceJSON.setTabText(self.ServiceJSON.indexOf(self.ContractInformation), _translate("landing_page", "Contract Information"))
        self.label_service_userID.setText(_translate("landing_page", "User ID :"))
        self.label_service_username.setText(_translate("landing_page", "Usesrname :"))
        self.label_service_public.setText(_translate("landing_page", "Public Key :"))
        self.ServiceJSON.setTabText(self.ServiceJSON.indexOf(self.UserInformation), _translate("landing_page", "User Information"))
        self.label_23.setText(_translate("landing_page", "All Data Information tou need to store"))
        self.ServiceJSON.setTabText(self.ServiceJSON.indexOf(self.Data), _translate("landing_page", "Data"))
        self.Submit_service.setText(_translate("landing_page", "Submit"))
        self.Admin_bar.setTabText(self.Admin_bar.indexOf(self.Add_Service), _translate("landing_page", "Add Service"))
        self.edit_service_label.setText(_translate("landing_page", "Edit Service"))
        self.label_chooseService.setText(_translate("landing_page", "Choose Service :"))
        self.label_serviceEdit_name.setText(_translate("landing_page", "Servece Name :"))
        self.label_serviceEdit_URL.setText(_translate("landing_page", "URL :"))
        self.label_edit_contractID.setText(_translate("landing_page", "Contract ID :"))
        self.label_edit_chainfile.setText(_translate("landing_page", "Chain File :"))
        self.label_edit_num.setText(_translate("landing_page", "Number of users :"))
        self.label_25.setText(_translate("landing_page", "Creation Date of Contract"))
        self.label_edit_year.setText(_translate("landing_page", "Year : "))
        self.label_edit_month.setText(_translate("landing_page", "Month :"))
        self.label_edit_day.setText(_translate("landing_page", "Day :"))
        self.editServices.setTabText(self.editServices.indexOf(self.ContractInfo), _translate("landing_page", "Contract Information"))
        self.label_edit_userID.setText(_translate("landing_page", "User ID :"))
        self.label_edit_public.setText(_translate("landing_page", "Public Key :"))
        self.label_edit_username.setText(_translate("landing_page", "Username : "))
        self.editServices.setTabText(self.editServices.indexOf(self.userInfo), _translate("landing_page", "User Information"))
        self.editServices.setTabText(self.editServices.indexOf(self.Edit_Data), _translate("landing_page", "Data"))
        self.serviceEdit_edit.setText(_translate("landing_page", "Edit"))
        self.serviceEdit_delete.setText(_translate("landing_page", "Delete"))
        self.Admin_bar.setTabText(self.Admin_bar.indexOf(self.Edit_Service), _translate("landing_page", "Edit Service"))
        self.actionShow_PublicKey.setText(_translate("landing_page", "Show PublicKey"))
        self.actionExit.setText(_translate("landing_page", "Exit"))


    # SUBMIT INFORMATION METHODS ---------------------------------------------------------------
# ------------------------------------------------------------------------------------------
    def submit_login_info(self):
        login_data_collection = self.get_login_info()
        login_url = 'http://127.0.0.1:8000/login/'
        result = requests.post(
            url=login_url,
            json=login_data_collection
        )
        if result.status_code == 200:
            self.submit_login = True
            self.buttom_update()
        print(result.json())

    def submit_blockchain_info(self):
        blockchain_data_collection = self.get_blockchain_info()
        blockchain_url = "http://127.0.0.1:8000/blockchain/"

        result = requests.post(
            url=blockchain_url,
            json=blockchain_data_collection
        )
        if result.status_code == 200:
            self.submit_blockchain = True
            self.buttom_update()
        print(result.json())
        
    def submit_service_info(self):
        # name = str(self.lineEdit_service_name.text())
        # url = str(self.lineEdit_URL_service.text())

        # # Contract Info
        # contract_id = self.lineEdit_contractID.text()
        # file_chain = self.lineEdit_chainfile.text()
        # num_of_user = self.lineEdit_number.text()
        # contract_info = contract_id + ',' + file_chain + ',' + num_of_user

        # # Creation Date
        # year = self.lineEdit_year.text()
        # month = self.lineEdit_month.text()
        # day = self.lineEdit_day.text()
        # creation_date = year + ',' + month + ',' + day

        # # User Info
        # user_id = self.lineEdit_service_userID.text()
        # username = self.lineEdit_service_username.text()
        # public_key = self.lineEdit_service_public.text()
        # user_info = user_id + ',' + username + ',' + public_key

        # # Whole Data
        # data = str(self.textEdit_data.toPlainText())


        # service_data_collection = {
        #     "name" : name,
        #     "url" : url,
        #     "data" : data,
        #     "contract_info" : contract_info,
        #     "user_info" : user_info,
        #     "created_on" : creation_date,
        #     "site_id" : self.site_id
        # }
        # print(service_data_collection)
        service_data_collection = self.get_service_info_for_submit()
        service_url = "http://127.0.0.1:8000/service/"
        result = requests.post(
            url=service_url,
            json=service_data_collection
        )
        if result.status_code == 200:
            self.get_services_information()
            self.combobox_updated()
            self.text_updated_service()

        print(result.json())

# EDIT INFORMATION METHODS -----------------------------------------------------------------
# ------------------------------------------------------------------------------------------
    def edit_login_info(self):
        edited_login_info = self.get_login_info()
        edit_url = "http://127.0.0.1:8000/login/" + str(self.login_id)

        result = requests.patch(
            url=edit_url,
            json=edited_login_info
        )
        print(result.json())

    def edit_blockchain_info(self):
        edited_blockchain_info = self.get_blockchain_info()
        edit_url = "http://127.0.0.1:8000/blockchain/" + str(self.blockchain_id)

        result = requests.patch(
            url=edit_url,
            json=edited_blockchain_info
        )
        print(result.json())

    def edit_service_info(self):
        edited_service_info = self.get_service_info_for_edit()
        edit_url = "http://127.0.0.1:8000/service/" + str(self._id_service_current)

        result = requests.patch(
            url=edit_url,
            json=edited_service_info
        )
        if result.status_code == 200:
            self.get_services_information()
            self.combobox_updated()
        print(result.json())

# DELETE INFORMATION METHODS ---------------------------------------------------------------
# ------------------------------------------------------------------------------------------
    def delete_service(self):
        url = "http://127.0.0.1:8000/service/" + str(self._id_service_current)
        result = requests.delete(
            url=url
        )
        if result.status_code == 200:
            self.get_services_information()
            self.combobox_updated()
            self.text_updated_edit_service()
            # self.lineEdit_6.setText("")
            # self.lineEdit_7.setText("")
            # self.lineEdit_8.setText("")
        print(result.json())

# GET INFORMATION METHODS FROM UI ----------------------------------------------------------
# ------------------------------------------------------------------------------------------
    def get_login_info(self):
        url = str(self.lineEdit_login_URL.text())
        usernameFormat = str(self.lineEdit_login_username.text())
        passFormat = str(self.lineEdit_login_pass.text())
        publicKeyFormat = str(self.lineEdit_login_public.text())

        login_data_collection = {
            "url" : url,
            "data" : usernameFormat + ',' + passFormat + ',' + publicKeyFormat,
            "site_id" : self.site_id
        }
        return login_data_collection

    def get_blockchain_info(self):
        url = str(self.lineEdit_blockchain_URL.text())

        blockchain_data_collection = {
            "url" : url,
            "site_id" : self.site_id
        }
        return blockchain_data_collection

    def get_service_info_for_submit(self):
        name = self.lineEdit_service_name.text()
        url = self.lineEdit_URL_service.text()
        
        # Contract Info
        contract_id = self.lineEdit_contractID.text()
        chain_file = self.lineEdit_chainfile.text()
        num_of_user = self.lineEdit_number.text()
        contract_info = contract_id + ',' + chain_file + ',' + num_of_user

        # Creation Date of contract
        year = self.lineEdit_year.text()
        month = self.lineEdit_month.text()
        day = self.lineEdit_day.text()
        creation_date = year + ',' + month + ',' + day

        # User info
        user_id = self.lineEdit_service_userID.text()
        username = self.lineEdit_service_username.text()
        public_key = self.lineEdit_service_public.text()
        user_info = user_id + ',' + username + ',' + public_key

        # Whole data
        data = self.textEdit_data.toPlainText()

        edited_service_info = {
            "name" : name,
            "url" : url,
            "data" : data,
            "created_on" : creation_date,
            "user_info" : user_info,
            "contract_info" : contract_info,
            "site_id" : self.site_id
        }
        return edited_service_info

    def get_service_info_for_edit(self):
        name = self.lineEdit_serviceEdit_name.text()
        url = self.lineEdit_serviceEdit_URL.text()
        
        # Contract Info
        contract_id = self.lineEdit_edit_contractID.text()
        chain_file = self.lineEdit_edit_chainfile.text()
        num_of_user = self.lineEdit_edit_num.text()
        contract_info = contract_id + ',' + chain_file + ',' + num_of_user

        # Creation Date of contract
        year = self.lineEdit_edit_year.text()
        month = self.lineEdit_edit_month.text()
        day = self.lineEdit_edit_day.text()
        creation_date = year + ',' + month + ',' + day

        # User info
        user_id = self.lineEdit_edit_userID.text()
        username = self.lineEdit_edit_username.text()
        public_key = self.lineEdit_edit_public.text()
        user_info = user_id + ',' + username + ',' + public_key

        # Whole data
        data = self.Edit_data.toPlainText()

        edited_service_info = {
            "name" : name,
            "url" : url,
            "data" : data,
            "created_on" : creation_date,
            "user_info" : user_info,
            "contract_info" : contract_info,
            "site_id" : self.site_id
        }
        return edited_service_info

# GET INFORMATION FROM SERVER TO FILL LINE-EDIT WIDGETS ------------------------------------
# ------------------------------------------------------------------------------------------
    def get_all_information(self):
        url = "http://127.0.0.1:8000/all_data/" + str(self.site_id)
        all_data = requests.get(
            url=url
        )
        return all_data.json()['login'], all_data.json()['blockchain']

    def get_services_information(self):
        url = "http://127.0.0.1:8000/services/" + str(self.site_id)
        all_services = requests.get(
            url=url,
        )
        if all_services.json() != []:
            self._all_services = all_services.json()
        else:
            self._all_services = None
   
# OTHER METHODS ----------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
    def choose_service_for_edit(self):
        value = self.comboBox_chooseService.currentText()
        for service in self._all_services:
            if service['name'] == value:
                self._id_service_current = service['id']
                self.lineEdit_serviceEdit_name.setText(service['name'])
                self.lineEdit_serviceEdit_URL.setText(service['url'])
                self.Edit_data.setText(service['data'])

                creation_date = service['created_on'].split(',')
                self.lineEdit_edit_year.setText(creation_date[0])
                self.lineEdit_edit_month.setText(creation_date[1])
                self.lineEdit_edit_day.setText(creation_date[2])

                user_info = service['user_info'].split(',')
                self.lineEdit_edit_userID.setText(user_info[0])
                self.lineEdit_edit_username.setText(user_info[1])
                self.lineEdit_edit_public.setText(user_info[2])

                contract_info = service['contract_info'].split(',')
                self.lineEdit_edit_contractID.setText(contract_info[0])
                self.lineEdit_edit_chainfile.setText(contract_info[1])
                self.lineEdit_edit_num.setText(contract_info[2])

                break

    def combobox_updated(self):
        self.comboBox_chooseService.clear()
        if self._all_services != None:
            self.comboBox_chooseService.addItem("")
            for service in self._all_services:
                self.comboBox_chooseService.addItem(service['name'])
        else:
            self.lineEdit_serviceEdit_name.setText("")
            self.lineEdit_serviceEdit_URL.setText("")
            self.Edit_data.setText("")
            
            self.lineEdit_edit_year.setText("")
            self.lineEdit_edit_month.setText("")
            self.lineEdit_edit_day.setText("")

            self.lineEdit_edit_userID.setText("")
            self.lineEdit_edit_username.setText("")
            self.lineEdit_edit_public.setText("")

            self.lineEdit_edit_contractID.setText("")
            self.lineEdit_edit_chainfile.setText("")
            self.lineEdit_edit_num.setText("")

    def text_updated_service(self):
        self.lineEdit_service_name.setText("")
        self.lineEdit_URL_service.setText("")

        # Contract Info
        self.lineEdit_contractID.setText("")
        self.lineEdit_chainfile.setText("")
        self.lineEdit_number.setText("")

        # Creation Date
        self.lineEdit_year.setText("")
        self.lineEdit_month.setText("")
        self.lineEdit_day.setText("")
        

        # User Info
        self.lineEdit_service_userID.setText("")
        self.lineEdit_service_username.setText("")
        self.lineEdit_service_public.setText("")

        # Whole Data
        self.textEdit_data.setText("")

    def text_updated_edit_service(self):
        self.lineEdit_serviceEdit_name.setText("")
        self.lineEdit_serviceEdit_URL.setText("")

        self.lineEdit_edit_contractID.setText("")
        self.lineEdit_edit_chainfile.setText("")
        self.lineEdit_edit_num.setText("")

        self.lineEdit_edit_year.setText("")
        self.lineEdit_edit_month.setText("")
        self.lineEdit_edit_day.setText("")

        self.lineEdit_edit_userID.setText("")
        self.lineEdit_edit_username.setText("")
        self.lineEdit_edit_public.setText("")

        self.Edit_data.setText("")

    def buttom_update(self):
        if self.submit_login == True:
            self.login_submit.setEnabled(False)

        if self.submit_blockchain == True:
            self.Submit_blockchain.setEnabled(False)
