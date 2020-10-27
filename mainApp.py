from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import helper

class mainApp(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(682, 636)
        # self.onlyInt = QtGui.QIntValidator()
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label.setObjectName("label")
        
        #Input Text Edit
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 241, 231))
        self.textEdit.setObjectName("textEdit")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 71, 16))
        self.label_2.setObjectName("label_2")

        #Output Text Edit
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(270, 50, 241, 231))
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 340, 55, 16))
        self.label_3.setObjectName("label_3")

        #Logs Text Edit
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 370, 491, 251))
        self.textEdit_3.setObjectName("textEdit_3")

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(520, 70, 151, 121))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 131, 82))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.withRSA = True
        self.withElgamal = False

        #Use RSA radio button
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(530, 20, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True) 
        self.radioButton.toggled.connect(self.toggleRSA)

        #Use Elgamal radio button
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(530, 40, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.toggleElgamal)

        #RSA p value
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit.setValidator(self.onlyInt)

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)

        #RSA q value
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        # self.lineEdit_2.setValidator(self.onlyInt)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)

        #RSA e value
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        # self.lineEdit_3.setValidator(self.onlyInt)

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 200, 151, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 131, 111))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)

        #Elgamal p value
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        # self.lineEdit_4.setValidator(self.onlyInt)
        self.lineEdit_4.setReadOnly(True)

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)

        #Elgamal g value
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        # self.lineEdit_5.setValidator(self.onlyInt)
        self.lineEdit_5.setReadOnly(True)

        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)

        #Elgamal x value
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        # self.lineEdit_6.setValidator(self.onlyInt)
        self.lineEdit_6.setReadOnly(True)

        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)

        #Elgamal k value
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        # self.lineEdit_7.setValidator(self.onlyInt)
        self.lineEdit_7.setReadOnly(True)

        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(520, 360, 151, 151))
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

        #Diffie-Helman n value
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_8.setObjectName("lineEdit_8")
        # self.lineEdit_8.setValidator(self.onlyInt)

        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)

        #Diffie-Helman g value
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_9.setObjectName("lineEdit_9")
        # self.lineEdit_9.setValidator(self.onlyInt)

        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)

        #Diffie-Helman x value
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_10.setObjectName("lineEdit_10")
        # self.lineEdit_10.setValidator(self.onlyInt)

        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)

        #Diffie-Helman y value
        self.lineEdit_11 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_11.setObjectName("lineEdit_11")
        # self.lineEdit_11.setValidator(self.onlyInt)

        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)

        #Encrypt Button
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 550, 151, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.encrypt)

        #Decrypt Button
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 590, 151, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        #Upload File Button
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 290, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Input Text"))
        self.label_2.setText(_translate("Dialog", "Result Text"))
        self.label_3.setText(_translate("Dialog", "Logs"))
        self.groupBox.setTitle(_translate("Dialog", "RSA"))
        self.label_4.setText(_translate("Dialog", "p"))
        self.label_5.setText(_translate("Dialog", "q"))
        self.label_6.setText(_translate("Dialog", "e"))
        self.groupBox_2.setTitle(_translate("Dialog", "Elgamal"))
        self.label_7.setText(_translate("Dialog", "p"))
        self.label_8.setText(_translate("Dialog", "g"))
        self.label_9.setText(_translate("Dialog", "x"))
        self.label_10.setText(_translate("Dialog", "k"))
        self.groupBox_3.setTitle(_translate("Dialog", "Diffie-Helman"))
        self.label_11.setText(_translate("Dialog", "n"))
        self.label_12.setText(_translate("Dialog", "g"))
        self.label_13.setText(_translate("Dialog", "x"))
        self.label_14.setText(_translate("Dialog", "y"))
        self.radioButton.setText(_translate("Dialog", "Use RSA"))
        self.radioButton_2.setText(_translate("Dialog", "Use Elgamal"))
        self.pushButton.setText(_translate("Dialog", "Encrypt"))
        self.pushButton_2.setText(_translate("Dialog", "Decrypt"))
        self.pushButton_3.setText(_translate("Dialog", "Upload File"))

    def toggleRSA(self, value):
        self.withRSA = value
        self.lineEdit_4.setReadOnly(value)
        self.lineEdit_5.setReadOnly(value)
        self.lineEdit_6.setReadOnly(value)
        self.lineEdit_7.setReadOnly(value)
    
    def toggleElgamal(self, value):
        self.withElgamal = value
        self.lineEdit.setReadOnly(value)
        self.lineEdit_2.setReadOnly(value)
        self.lineEdit_3.setReadOnly(value)

    def RSA(self, p, q, e):
        n = p*q
        toitent = (p-1)*(q-1)
        d = 0.1
        k = 0
        while not d.is_integer():
            k += 1
            d = (1 + k*toitent) / e
        d = int(d)
        helper.writeToFile(f"({e},{n})", 0)
        helper.writeToFile(f"({d},{toitent})", 1)

    def encrypt(self):
        mode = 0
        if (self.withElgamal):
            mode = 1
        
        # try:
        dh_n = int(self.lineEdit_8.text())
        dh_g = int(self.lineEdit_9.text())
        dh_x = int(self.lineEdit_10.text())
        dh_y = int(self.lineEdit_11.text())

        #Get Diffie-Helman Session Key

        if (mode == 0): #RSA
            p = int(self.lineEdit.text())
            q = int(self.lineEdit_2.text())
            e = int(self.lineEdit_3.text())
            self.RSA(p, q, e)
        else: #Elgamal
            p = int(self.lineEdit_4.text())
            g = int(self.lineEdit_5.text())
            x = int(self.lineEdit_6.text())
            k = int(self.lineEdit_7.text())

        inputText = self.textEdit.toPlainText()
        # except ValueError:
        #     self.textEdit_3.append(">ERROR: Could not convert input to int")
        # except:
        #     self.textEdit_3.append(">ERROR: Unhandled error case occured")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = mainApp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())