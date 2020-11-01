from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import helper
# import decimal
import math
import copy
import time
from Crypto.Util import number

class mainApp(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(758, 691)
        # decimal.getcontext().prec = 100
        self.inputFileData = None
        self.e = None
        self.d = None
        self.n = None
        self.y = None
        self.g = None
        self.p = None
        self.x = None
        # self.onlyInt = QtGui.QIntValidator()
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label.setObjectName("label")

        # Input Text Edit
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 245, 231))
        self.textEdit.setObjectName("textEdit")

        # Output Text Edit
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(270, 50, 245, 231))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 370, 55, 16))
        self.label_3.setObjectName("label_3")

        # Logs Text Edit
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 400, 491, 281))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setReadOnly(True)

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(520, 70, 231, 181))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 131, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.withRSA = True
        self.withElgamal = False

        # Use RSA radio button
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(530, 20, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(self.toggleRSA)

        # Use ElGamal radio button
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(530, 40, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.toggleElgamal)

        # RSA p value
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit.setValidator(self.onlyInt)

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)

        # RSA q value
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        # self.lineEdit_2.setValidator(self.onlyInt)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)

        # RSA e value
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        # self.lineEdit_3.setValidator(self.onlyInt)

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_15)

        # RSA d value
        self.lineEdit_12 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_16)

        # RSA n value
        self.lineEdit_13 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_13.setObjectName("lineEdit_13")

        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)

        # RSA generate p value
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 28, 71, 25))
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.generateRandomPrime(0))

        # RSA generate q value
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 58, 71, 25))
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.generateRandomPrime(1))

        # RSA generate e value
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 88, 71, 25))
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: self.generateCoprime(2))

        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 250, 231, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 131, 140))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)

        # ElGamal p value
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        # self.lineEdit_4.setValidator(self.onlyInt)
        self.lineEdit_4.setReadOnly(True)

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)

        # ElGamal g value
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        # self.lineEdit_5.setValidator(self.onlyInt)
        self.lineEdit_5.setReadOnly(True)

        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)

        # ElGamal x value
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        # self.lineEdit_6.setValidator(self.onlyInt)
        self.lineEdit_6.setReadOnly(True)

        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)

        # ElGamal k value
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        # self.lineEdit_7.setValidator(self.onlyInt)
        self.lineEdit_7.setReadOnly(True)

        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_17)

        # ElGamal y value
        self.lineEdit_14 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setReadOnly(True)

        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)

        # ElGamal generate p value
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 28, 71, 25))
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: self.generateRandomPrime(3))

        # ElGamal generate g value
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setGeometry(QtCore.QRect(150, 58, 71, 25))
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda: self.generateRandomNumber(4))

        # ElGamal generate x value
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 88, 71, 25))
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda: self.generateRandomNumber(5))

        # ElGamal generate k value
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setGeometry(QtCore.QRect(150, 117, 71, 25))
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(lambda: self.generateRandomNumber(6))

        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(520, 430, 231, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 131, 111))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)

        # Diffie-Helman n value
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_8.setObjectName("lineEdit_8")
        # self.lineEdit_8.setValidator(self.onlyInt)

        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)

        # Diffie-Helman g value
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_9.setObjectName("lineEdit_9")
        # self.lineEdit_9.setValidator(self.onlyInt)

        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)

        # Diffie-Helman x value
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_10.setObjectName("lineEdit_10")
        # self.lineEdit_10.setValidator(self.onlyInt)

        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)

        # Diffie-Helman y value
        self.lineEdit_11 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_11.setObjectName("lineEdit_11")
        # self.lineEdit_11.setValidator(self.onlyInt)

        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)

        # Diffie-Helman generate n value
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_13.setGeometry(QtCore.QRect(150, 28, 71, 25))
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(lambda: self.generateRandomPrime(7))

        # Diffie-Helman generate g value
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_14.setGeometry(QtCore.QRect(150, 58, 71, 25))
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(lambda: self.generateRandomPrime(8))

        # Diffie-Helman generate x value
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_15.setGeometry(QtCore.QRect(150, 88, 71, 25))
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(lambda: self.generateRandomNumber(9))

        # Diffie-Helman generate y value
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_16.setGeometry(QtCore.QRect(150, 117, 71, 25))
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(lambda: self.generateRandomNumber(10))

        # Encrypt Button
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 610, 221, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.handleSubmit(0))

        # Decrypt Button
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 650, 221, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.handleSubmit(1))

        # Upload File Button
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 290, 121, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openInputFileNameDialog)

        # Upload Public Key
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 290, 141, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.openKeyFileNameDialog(0))

        # Upload Private Key
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 290, 151, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.openKeyFileNameDialog(1))

        # Input Text is ciphertext checkbox
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(20, 330, 171, 20))
        self.checkBox.setObjectName("checkBox")

        # Result filename
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(339, 330, 141, 22))
        self.label_18.setObjectName("label_18")
        self.lineEdit_15 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_15.setGeometry(QtCore.QRect(340, 350, 171, 22))
        self.lineEdit_15.setObjectName("lineEdit_15")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Input Text"))
        self.label_2.setText(_translate("Dialog", "Result Text"))
        self.label_3.setText(_translate("Dialog", "Logs"))
        self.pushButton_3.setText(_translate("Dialog", "Upload Input File"))
        self.pushButton_4.setText(_translate("Dialog", "Upload Public Key File"))
        self.pushButton_5.setText(_translate("Dialog", "Upload Private Key File"))
        self.checkBox.setText(_translate("Dialog", "Input is ciphertext?"))
        self.label_18.setText(_translate("Dialog", "Decrypt result filename"))

        self.groupBox.setTitle(_translate("Dialog", "RSA"))
        self.label_4.setText(_translate("Dialog", "p"))
        self.label_5.setText(_translate("Dialog", "q"))
        self.label_6.setText(_translate("Dialog", "e"))
        self.label_15.setText(_translate("Dialog", "d"))
        self.label_16.setText(_translate("Dialog", "n"))
        self.pushButton_6.setText(_translate("Dialog", "Generate"))
        self.pushButton_7.setText(_translate("Dialog", "Generate"))
        self.pushButton_8.setText(_translate("Dialog", "Generate"))

        self.groupBox_2.setTitle(_translate("Dialog", "Elgamal"))
        self.label_7.setText(_translate("Dialog", "p"))
        self.label_8.setText(_translate("Dialog", "g"))
        self.label_9.setText(_translate("Dialog", "x"))
        self.label_10.setText(_translate("Dialog", "k"))
        self.label_17.setText(_translate("Dialog", "y"))
        self.pushButton_9.setText(_translate("Dialog", "Generate"))
        self.pushButton_10.setText(_translate("Dialog", "Generate"))
        self.pushButton_11.setText(_translate("Dialog", "Generate"))
        self.pushButton_12.setText(_translate("Dialog", "Generate"))

        self.groupBox_3.setTitle(_translate("Dialog", "Diffie-Helman"))
        self.label_11.setText(_translate("Dialog", "n"))
        self.label_12.setText(_translate("Dialog", "g"))
        self.label_13.setText(_translate("Dialog", "x"))
        self.label_14.setText(_translate("Dialog", "y"))
        self.pushButton_13.setText(_translate("Dialog", "Generate"))
        self.pushButton_14.setText(_translate("Dialog", "Generate"))
        self.pushButton_15.setText(_translate("Dialog", "Generate"))
        self.pushButton_16.setText(_translate("Dialog", "Generate"))

        self.radioButton.setText(_translate("Dialog", "Use RSA"))
        self.radioButton_2.setText(_translate("Dialog", "Use Elgamal"))

        self.pushButton.setText(_translate("Dialog", "Encrypt"))
        self.pushButton_2.setText(_translate("Dialog", "Decrypt"))

    def toggleRSA(self, value):
        self.withRSA = value
        self.lineEdit_4.setReadOnly(value)
        self.lineEdit_5.setReadOnly(value)
        self.lineEdit_6.setReadOnly(value)
        self.lineEdit_7.setReadOnly(value)
        self.lineEdit_14.setReadOnly(value)

    def toggleElgamal(self, value):
        self.withElgamal = value
        self.lineEdit.setReadOnly(value)
        self.lineEdit_2.setReadOnly(value)
        self.lineEdit_3.setReadOnly(value)
        self.lineEdit_12.setReadOnly(value)
        self.lineEdit_13.setReadOnly(value)

    def openInputFileNameDialog(self):
        try:
            fileName = QtWidgets.QFileDialog.getOpenFileName()[0]
            self.textEdit_3.append(f">Reading input file '{fileName}'")
            inputData, is_cipherText = helper.readFromFile(fileName)
            self.textEdit_3.append(">Reading file done.")
            self.textEdit_3.append(f">Input file size = {len(inputData)} bytes.")
            if (is_cipherText):
                if (len(inputData) < 16000):
                    self.textEdit.setText(inputData)
                else:
                    self.textEdit.setText("")
                self.checkBox.setChecked(True)
            else:
                self.checkBox.setChecked(False)
            self.inputFileData = (inputData, is_cipherText)
        except FileNotFoundError:
            pass

    def openKeyFileNameDialog(self, keyType):
        try:
            fileName = QtWidgets.QFileDialog.getOpenFileName()[0]
            if (keyType == 0):  # Public key file
                if (self.withRSA):  # Public RSA key
                    self.textEdit_3.append(f">Reading RSA public key file '{fileName}'")
                    self.e, self.n = helper.readFromFile(fileName)
                    self.lineEdit_3.setText(str(self.e))
                    self.lineEdit_13.setText(str(self.n))
                else:  # Public ElGamal key
                    self.textEdit_3.append(f">Reading ElGamal public key file '{fileName}'")
                    self.y, self.g, self.p = helper.readFromFile(fileName)
                    self.lineEdit_14.setText(str(self.y))
                    self.lineEdit_5.setText(str(self.g))
                    self.lineEdit_4.setText(str(self.p))
            else:  # Private key file
                if (self.withRSA):  # Private RSA key
                    self.textEdit_3.append(f">Reading RSA private key file '{fileName}'")
                    self.d, self.n = helper.readFromFile(fileName)
                    self.lineEdit_12.setText(str(self.d))
                    self.lineEdit_13.setText(str(self.n))
                else:  # Private ElGamal key
                    self.textEdit_3.append(f">Reading ElGamal private key file '{fileName}'")
                    self.x, self.p = helper.readFromFile(fileName)
                    self.lineEdit_6.setText(str(self.x))
                    self.lineEdit_4.setText(str(self.p))
            self.textEdit_3.append(">Reading file done.")
        except FileNotFoundError:
            pass
        except ValueError:
            self.textEdit_3.append(">ERROR: Input is not int")

    def generateRandomPrime(self, fieldID):
        prime = number.getPrime(512)
        if (fieldID == 0):  # RSA p value
            self.lineEdit.setText(str(prime))
        elif (fieldID == 1):  # RSA q value
            self.lineEdit_2.setText(str(prime))
        elif (fieldID == 3):  # ElGamal p value
            self.lineEdit_4.setText(str(prime))
        elif (fieldID == 7):  # Diffie-Helman n value
            self.lineEdit_8.setText(str(prime))
        elif (fieldID == 8):  # Diffie-Helman g value
            if (self.lineEdit_8.text()):
                n = int(self.lineEdit_8.text())
                while prime >= n:
                    prime = number.getPrime(512)
                self.lineEdit_9.setText(str(prime))
            else:
                self.textEdit_3.append(f">Diffie-Helman n must be filled before generating g value")

    def generateCoprime(self, fieldID):  # RSA e value
        try:
            p = None
            q = None
            if (self.lineEdit.text()):
                p = int(self.lineEdit.text())
            if (self.lineEdit_2.text()):
                q = int(self.lineEdit_2.text())
            if (p and q):
                toitent = (p - 1) * (q - 1)
                coprime = number.getStrongPrime(512, toitent)
                if (fieldID == 2):
                    self.lineEdit_3.setText(str(coprime))
            else:
                raise GenerateCoprimeFail
        except GenerateCoprimeFail:
            self.textEdit_3.append(">ERROR: Value of p and q is not detected.")

    def generateRandomNumber(self, fieldID):
        randNum = number.getRandomInteger(512)
        if (fieldID == 4):  # ElGamal g value
            if (self.lineEdit_4.text()):
                p = int(self.lineEdit_4.text())
                while randNum >= p:
                    randNum = number.getRandomInteger(512)
                self.lineEdit_5.setText(str(randNum))
            else:
                self.textEdit_3.append(f">ElGamal p must must be filled before generating g value")
        elif (fieldID == 5):  # ElGamal x value
            if (self.lineEdit_4.text()):
                p = int(self.lineEdit_4.text())
                while not (1 <= randNum and randNum <= (p - 2)):
                    randNum = number.getRandomInteger(512)
                self.lineEdit_6.setText(str(randNum))
            else:
                self.textEdit_3.append(f">ElGamal p must must be filled before generating g value")
        elif (fieldID == 6):  # ElGamal k value
            if (self.lineEdit_4.text()):
                p = int(self.lineEdit_4.text())
                while not (1 <= randNum and randNum <= (p - 2)):
                    randNum = number.getRandomInteger(512)
                self.lineEdit_7.setText(str(randNum))
            else:
                self.textEdit_3.append(f">ElGamal p must must be filled before generating g value")
        elif (fieldID == 9):  # Diffie-Helman x value
            self.lineEdit_10.setText(str(randNum))
        elif (fieldID == 10):  # Diffie-Helman y value
            self.lineEdit_11.setText(str(randNum))

    def RSA(self, p, q, e, d_, n_):
        self.textEdit_3.append(">Creating public key.")
        if (n_):
            n = n_
        else:
            if (p >= 503 and q >= 503):
                n = p * q
            else:
                raise RSAPrimesTooLow
        publicKey = f"{e},{n}"
        self.textEdit_3.append(f">n = {n}")
        self.textEdit_3.append(f">RSA public key = ({publicKey})")
        helper.writeToFile(publicKey, 0)

        self.textEdit_3.append(">Creating private key.")
        if (d_):
            d = d_
        else:
            toitent = (p - 1) * (q - 1)

            if (helper.is_coprime(toitent, e)):
                d = pow(e, -1, toitent)
                # d = decimal.Decimal(0.1)
                # k = 0
                # while not d == d.to_integral_value():
                #     k += 1
                #     d = (decimal.Decimal(1) + decimal.Decimal(k)*decimal.Decimal(toitent)) / decimal.Decimal(e)
                # d = d.to_integral_value()

                privateKey = f"{d},{n}"
                self.textEdit_3.append(f">d = {d}")
                self.textEdit_3.append(f">RSA private key = ({privateKey})")
                helper.writeToFile(privateKey, 1)

                return n
            else:
                raise RSAPublicKeyNotCoprime

    def elgamal(self, p, g, x, y_):
        self.textEdit_3.append(">Creating public key.")
        if (y_):
            y = y_
        else:
            y = pow(g, x, p)
        publicKey = f"{y},{g},{p}"
        self.textEdit_3.append(f">y = {y}")
        self.textEdit_3.append(f">ElGamal public key = ({publicKey})")
        helper.writeToFile(publicKey, 0)
        self.textEdit_3.append(">Creating private key.")
        privateKey = f"{x},{p}"
        self.textEdit_3.append(f">ElGamal private key = ({privateKey})")
        helper.writeToFile(privateKey, 1)
        return y

    def handleSubmit(self, sender):
        mode = 0
        if (self.withElgamal):
            mode = 1

        try:
            if (self.inputFileData):
                if (self.inputFileData[1]):  # cipherText
                    codedText = copy.copy(self.inputFileData[0])
                    if (len(codedText) < 16000):
                        self.textEdit.setText(codedText)
                else:
                    codedText = helper.codeMessage(self.inputFileData[0], 1)
                self.inputFileData = None
            else:
                inputText = self.textEdit.toPlainText()
                if (self.checkBox.isChecked()):
                    codedText = inputText
                else:
                    codedText = helper.codeMessage(inputText, 0)

            if (not self.lineEdit_8.text() or not \
                    self.lineEdit_9.text() or not \
                    self.lineEdit_10.text() or not \
                    self.lineEdit_11.text()):
                raise ParamNotFilled
            dh_n = int(self.lineEdit_8.text())
            dh_g = int(self.lineEdit_9.text())
            dh_x = int(self.lineEdit_10.text())
            dh_y = int(self.lineEdit_11.text())

            if (dh_g < dh_n):
                # Get Diffie-Helman Session Key
                self.textEdit_3.append(">Generating session key.")
                sessionKey = helper.diffie_helman(dh_n, dh_g, dh_x, dh_y)
                self.textEdit_3.append(f">Session key = {sessionKey}")

                ################################################
                ##                     RSA                    ##
                ################################################

                if (mode == 0):  # RSA
                    p = None
                    q = None
                    e = None
                    d = None
                    n = None
                    if (self.lineEdit.text()):
                        p = int(self.lineEdit.text())
                        self.textEdit_3.append(f">p = {p}")
                    if (self.lineEdit_2.text()):
                        q = int(self.lineEdit_2.text())
                        self.textEdit_3.append(f">q = {q}")
                    if (self.lineEdit_3.text()):
                        e = int(self.lineEdit_3.text())
                        self.textEdit_3.append(f">e = {e}")
                    if (self.lineEdit_12.text()):
                        d = int(self.lineEdit_12.text())
                        self.textEdit_3.append(f">d = {d}")
                    if (self.lineEdit_13.text()):
                        n = int(self.lineEdit_13.text())
                        self.textEdit_3.append(f">n = {n}")

                    if (self.d):
                        d = copy.copy(self.d)
                    self.d = None

                    if (self.n):
                        n = copy.copy(self.n)
                    self.n = None

                    if (sender == 0):  # encrypt
                        self.textEdit_3.append(">Starting RSA")
                        if (not e):
                            raise ParamNotFilled
                        if (not n):
                            if (not p or not q):
                                raise RSAPrimesNotFilled
                        if (not d):
                            if (not p or not q):
                                raise RSAPrimesNotFilled

                        n = self.RSA(p, q, e, d, n)
                        data = (codedText, e, n)
                        startTime = time.time()
                        self.encrypt(mode, data)
                        endTime = time.time()
                        elapsedTime = endTime - startTime
                        self.textEdit_3.append(f">Encryption time: {elapsedTime} sec")
                        self.textEdit_3.append("")
                    else:  # decrypt
                        if (not self.lineEdit_15.text()):
                            raise ParamNotFilled
                        if (d and n):
                            data = (codedText, d, n)
                            startTime = time.time()
                            self.decrypt(mode, data)
                            endTime = time.time()
                            elapsedTime = endTime - startTime
                            self.textEdit_3.append(f">Decryption time: {elapsedTime} sec")
                            self.textEdit_3.append("")
                        else:
                            raise ParamNotFilled

                ################################################
                ##                    ElGamal                 ##
                ################################################

                else:  # ElGamal
                    p = None
                    g = None
                    x = None
                    k = None
                    y = None
                    if (self.lineEdit_4.text()):
                        p = int(self.lineEdit_4.text())
                        self.textEdit_3.append(f">p = {p}")
                    if (self.lineEdit_5.text()):
                        g = int(self.lineEdit_5.text())
                        self.textEdit_3.append(f">g = {g}")
                    if (self.lineEdit_6.text()):
                        x = int(self.lineEdit_6.text())
                        self.textEdit_3.append(f">x = {x}")
                    if (self.lineEdit_7.text()):
                        k = int(self.lineEdit_7.text())
                        self.textEdit_3.append(f">k = {k}")
                    if (self.lineEdit_14.text()):
                        y = int(self.lineEdit_14.text())
                        self.textEdit_3.append(f">y = {y}")

                    if (self.y):
                        y = copy.copy(self.y)
                    self.y = None

                    if (self.g):
                        g = copy.copy(self.g)
                    self.g = None

                    if (self.p):
                        p = copy.copy(self.p)
                    self.p = None

                    if (self.x):
                        x = copy.copy(self.x)
                    self.x = None

                    if (sender == 0):  # encrypt
                        self.textEdit_3.append(">Starting ElGamal")
                        if (not k):
                            raise ParamNotFilled
                        if (not y):
                            if (not p or not g or not x or not k):
                                raise ParamNotFilled
                            if ((x < 1) or (x >= (p - 2))):
                                raise ElGamalInvalidX
                            if ((k < 1) or (k >= (p - 2))):
                                raise ElGamalInvalidK
                        if (g >= p):
                            raise ElGamalBiggerG
                        if (p <= 255255):
                            raise ElGamalPrimeTooLow

                        y = self.elgamal(p, g, x, y)
                        data = (codedText, p, g, k, y)
                        startTime = time.time()
                        self.encrypt(mode, data)
                        endTime = time.time()
                        elapsedTime = endTime - startTime
                        self.textEdit_3.append(f">Encryption time: {elapsedTime} sec")
                        self.textEdit_3.append("")
                    else:  # decrypt
                        if (not self.lineEdit_15.text()):
                            raise ParamNotFilled
                        if (not p or not x):
                            raise ParamNotFilled
                        if (p <= 255255):
                            raise ElGamalPrimeTooLow
                        if ((x < 1) or (x >= (p - 2))):
                            raise ElGamalInvalidX
                        data = (codedText, p, x)
                        startTime = time.time()
                        self.decrypt(mode, data)
                        endTime = time.time()
                        elapsedTime = endTime - startTime
                        self.textEdit_3.append(f">Decryption time: {elapsedTime} sec")
                        self.textEdit_3.append("")
            else:
                raise DHBiggerG

        except ParamNotFilled:
            self.textEdit_3.append(">ERROR: One or more required param is not filled.")
        except DHBiggerG:
            self.textEdit_3.append(">ERROR: Value of Diffie-Helman g must be smaller than n.")
        except ElGamalBiggerG:
            self.textEdit_3.append(">ERROR: Value of g must be smaller than p.")
        except ElGamalInvalidX:
            self.textEdit_3.append(">ERROR: Value of x must between 1 < x < p-2.")
        except ElGamalInvalidK:
            self.textEdit_3.append(">ERROR: Value of k must between 1 < k < p-2.")
        except RSAPrimesNotFilled:
            self.textEdit_3.append(">ERROR: Param p and q must be filled if n or d is not filled.")
        except RSAPrimesTooLow:
            self.textEdit_3.append(">ERROR: Value of p*q must be bigger than 255255")
        except ElGamalPrimeTooLow:
            self.textEdit_3.append(">ERROR: Value of p must be bigger than 255255")
        except RSAPublicKeyNotCoprime:
            self.textEdit_3.append(">ERROR: Value of e must be coprime of toitent.")
        except:
            self.textEdit_3.append(">ERROR: Unhandled error case occured")

    def encrypt(self, mode, data):
        ################################################
        ##                     RSA                    ##
        ################################################

        if (mode == 0):
            self.textEdit_3.append(">Starting RSA encryption")
            codedText = data[0]
            e = data[1]
            n = data[2]
            cipherText = ""
            nLength = len(str(n))
            cleanDiv = len(codedText) % nLength == 0
            amount = math.ceil(len(codedText) / 6)
            # print(f"amount: {amount}")
            for i in range(amount):
                # print(f"Encrypting: {(i+1)/amount}")
                block = codedText[i * 6:i * 6 + 6]
                code = str(pow(int(block), e, n))
                paddingLength = nLength - len(code)
                padding = '0' * paddingLength
                code = padding + code
                cipherText += code
            if (not cleanDiv):
                randomPaddingNumber = str(number.getRandomRange(100,999))
                cipherText = randomPaddingNumber + cipherText
            self.textEdit_3.append(">RSA encryption finished")
            self.textEdit_3.append(">Writing ciphertext to cipherText.ecr")
            print("Set ciphertext")
            if (len(cipherText) < 16000):
                self.textEdit_2.setText(cipherText)
            else:
                self.textEdit_2.setText("")
            print("Writing ciphertext to file")
            helper.writeToFile(cipherText, 2)
            self.textEdit_3.append(">Ciphertext saved to cipherText.ecr")
            self.textEdit_3.append("")
            self.textEdit_3.append(f">Ciphertext file size = {len(cipherText)} bytes.")

        ################################################
        ##                    ElGamal                 ##
        ################################################

        else:
            self.textEdit_3.append(">Starting ElGamal encryption")
            codedText = data[0]
            p = data[1]
            g = data[2]
            k = data[3]
            y = data[4]
            cipherText = ""
            cipherText_a = ""
            cipherText_b = ""
            pLength = len(str(p))
            cleanDiv = len(codedText) % pLength == 0
            amount = math.ceil(len(codedText) / 6)
            for i in range(amount):
                block = codedText[i * 6:i * 6 + 6]
                code = str(pow(g, k, p))
                paddingLength = pLength - len(code)
                padding = '0' * paddingLength
                code = padding + code
                cipherText_a += code
                temp_int = pow(y, k, p)
                code = str((int(block) * temp_int) % p)
                paddingLength = pLength - len(code)
                padding = '0' * paddingLength
                code = padding + code
                cipherText_b += code
                cipherText = cipherText_a + cipherText_b
            if (not cleanDiv):
                randomPaddingNumber = str(number.getRandomRange(100,999))
                cipherText = randomPaddingNumber + cipherText
            self.textEdit_3.append(">ElGamal encryption finished")
            self.textEdit_3.append(">Writing ciphertext to cipherText.ecr")
            print("Set ciphertext")
            if (len(cipherText) < 16000):
                self.textEdit_2.setText(cipherText)
            else:
                self.textEdit_2.setText("")
            print("Writing ciphertext to file")
            helper.writeToFile(cipherText, 2)
            self.textEdit_3.append(">Ciphertext saved to cipherText.ecr")
            self.textEdit_3.append("")
            self.textEdit_3.append(f">Ciphertext file size = {len(cipherText)} bytes.")

    def decrypt(self, mode, data):
        ################################################
        ##                     RSA                    ##
        ################################################

        if (mode == 0):  # RSA
            self.textEdit_3.append(">Starting decryption.")
            codedText = data[0]
            d = data[1]
            n = data[2]
            nLength = len(str(n))

            plainCode = ""
            cleanDiv = len(codedText) % nLength == 0
            if (not cleanDiv):
                codedText = codedText[3:] 
            amount = math.ceil(len(codedText) / nLength)
            for i in range(amount):
                # print(f"Decrypting phase 1: {(i+1)/amount}")
                block = codedText[i * nLength:i * nLength + nLength]
                code = str(pow(int(block), d, n))
                paddingLength = 6 - len(code)
                padding = '0' * paddingLength
                code = padding + code
                plainCode += code

            plainText = ""
            byteArray = []
            charAmount = int(len(plainCode) / 3)
            for i in range(charAmount):
                # print(f"Decrypting phase 2: {(i+1)/charAmount}")
                block = plainCode[i * 3:i * 3 + 3]
                code = int(block)
                if (not cleanDiv and i == charAmount - 2 and code == 0):
                    pass
                else:
                    byteArray.append(code)
                    char = chr(code)
                    plainText += char

            self.textEdit_3.append(">Decryption done.")
            print("Set plaintext")
            if (len(plainText) < 16000):
                self.textEdit_2.setText(plainText)
            else:
                self.textEdit_2.setText("")
            print("Writing plaintext to file")

            fileName = self.lineEdit_15.text()
            helper.writePlainText(byteArray, fileName)
            self.textEdit_3.append(f">Plaintext saved to {fileName}")
            self.textEdit_3.append("")
            self.textEdit_3.append(f">Plaintext file size = {len(plainText)} bytes.")

        ################################################
        ##                    ElGamal                 ##
        ################################################

        else:  # Elgamal
            self.textEdit_3.append(">Starting decryption.")
            codedText = data[0]
            p = data[1]
            x = data[2]
            pLength = len(str(p))

            plainCode = ""
            cleanDiv = len(codedText) % pLength == 0
            if (not cleanDiv):
                codedText = codedText[3:]
            codedLength = int(len(codedText) / 2)
            codedText_a = codedText[:codedLength]
            codedText_b = codedText[codedLength:]
            amount = math.ceil(codedLength / pLength)
            for i in range(amount):
                block_a = int(codedText_a[i * pLength:i * pLength + pLength])
                block_b = int(codedText_b[i * pLength:i * pLength + pLength])
                temp = pow(block_a, p - 1 - x, p)
                code = str((block_b * temp) % p)
                paddingLength = 6 - len(code)
                padding = '0' * paddingLength
                code = padding + code
                plainCode += code
            plainText = ""
            byteArray = []
            charAmount = int(len(plainCode) / 3)
            for i in range(charAmount):
                block = plainCode[i * 3:i * 3 + 3]    
                code = int(block)
                if (not cleanDiv and i == charAmount - 2 and code == 0):
                    pass
                else:
                    byteArray.append(code)
                    char = chr(code)
                    plainText += char

            self.textEdit_3.append(">Decryption done.")
            print("Set plaintext")
            if (len(plainText) < 16000):
                self.textEdit_2.setText(plainText)
            else:
                self.textEdit_2.setText("")
            print("Writing plaintext to file")

            fileName = self.lineEdit_15.text()
            helper.writePlainText(byteArray, fileName)
            self.textEdit_3.append(f">Plaintext saved to {fileName}")
            self.textEdit_3.append("")
            self.textEdit_3.append(f">Plaintext file size = {len(plainText)} bytes.")


class Error(Exception):
    # Base class for other exceptions
    pass


class ParamNotFilled(Error):
    # When a param is not filled
    pass


class DHBiggerG(Error):
    # When g is bigger than n
    pass


class ElGamalBiggerG(Error):
    # When g is bigger than p
    pass


class ElGamalInvalidX(Error):
    # When x is bigger than p-2 or less than 1
    pass


class ElGamalInvalidK(Error):
    # When k is bigger than p-2 or less than 1
    pass


class RSAPrimesNotFilled(Error):
    # Param p or q is not filled when n is not filled
    pass


class RSAPrimesTooLow(Error):
    # Value of p*q is less than 255255
    pass


class ElGamalPrimeTooLow(Error):
    # Value of p is less than 255255
    pass


class RSAPublicKeyNotCoprime(Error):
    # Value of e is not coprime of toitent
    pass


class GenerateCoprimeFail(Error):
    # Value of p and q not known
    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = mainApp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
