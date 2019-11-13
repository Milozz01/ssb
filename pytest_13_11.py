# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0

import time
import sys
# import RPi.GPIO as GPIO
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QVariant, QSize
from PyQt5.QtGui import QImage, QPalette, QBrush

stepcount = 0


class Ui_mainWindow(object):

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(557, 320)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 70, 75, 23))
        self.pushButton_4.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 40, 101, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("", QVariant(10*1600))
        self.comboBox.addItem("", QVariant(20))
        self.comboBox.addItem("", QVariant(30))
        self.comboBox.addItem("", QVariant(40))
        self.comboBox.addItem("", QVariant(50))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 250, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 40, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 252, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 252, 51, 21))
        self.label_3.setObjectName("label_3")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 21))
        self.menubar.setObjectName("menubar")
        self.menuSmart_Spray_Booth_Configuration = QtWidgets.QMenu(self.menubar)
        self.menuSmart_Spray_Booth_Configuration.setObjectName("menuSmart_Spray_Booth_Configuration")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSmart_Spray_Booth_Configuration.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.comboBox.activated.connect(self.handleactivated)
        self.pushButton.clicked.connect(lambda: self.stepperaction(index=self.comboBox.currentIndex()))
        self.pushButton_2.clicked.connect(lambda: self.stop())
        self.pushButton_3.clicked.connect(lambda: self.nullpunkt())

    def handleactivated(self, index):
        print(self.comboBox.itemText(index), "handle")
        print(self.comboBox.itemData(index), "handle")
        self.label_3.setText(self.comboBox.itemText(index))

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Smart Spray Booth - Configuration"))
        self.pushButton.setText(_translate("mainWindow", "START"))
        self.pushButton_2.setText(_translate("mainWindow", "STOP"))
        self.pushButton_3.setText(_translate("mainWindow", "Nullpunkt"))

        self.comboBox.setItemText(0, _translate("mainWindow", "5cm"))
        self.comboBox.setItemText(1, _translate("mainWindow", "10cm"))
        self.comboBox.setItemText(2, _translate("mainWindow", "15cm"))
        self.comboBox.setItemText(3, _translate("mainWindow", "20cm"))
        self.comboBox.setItemText(4, _translate("mainWindow", "25cm"))

        self.label.setText(_translate("mainWindow", "Bauteilgröße:"))
        self.label_2.setText(_translate("mainWindow", "Bauteilgröße:"))
        self.label_3.setText(_translate("mainWindow", "0 cm"))

        self.menuSmart_Spray_Booth_Configuration.setTitle(_translate("mainWindow", "Smart Spray Booth - Configuration"))

        if self.comboBox.currentTextChanged:
            print(self.comboBox.currentData(), "from if")

    def stop(self):
        print("programm wird beendet")
        sys.exit()

    def nullpunkt(self):
        # needs to be configured!
        print("wird auf null gesetzt")

    def stepperaction(self, index):
        # GPIO.setmode(GPIO.BOARD)  # read the pin as board instead of BCM pin
        global stepcount
        stepcount = self.comboBox.itemData(index)
        print(stepcount, "this is given step")
        # return stepcount
        Dir = 35
        Step = 37
        Enable = 33
        Dirb = 38
        Stepb = 36
        Enableb = 40
        GPIO.setwarnings(False)
        GPIO.setup(Dir, GPIO.OUT)
        GPIO.setup(Step, GPIO.OUT)
        GPIO.setup(Enable, GPIO.OUT)
        GPIO.setup(Dirb, GPIO.OUT)
        GPIO.setup(Stepb, GPIO.OUT)
        GPIO.setup(Enableb, GPIO.OUT)
        GPIO.output(Enable, GPIO.HIGH)
        GPIO.output(Enableb, GPIO.HIGH)
        FastSpeed = 0.0001  # old = 0.001 Change this depends on your stepper motor
        LowSpeed = 0.0001   # old = 0.001 Change this depends on your stepper motor
        counter = 0
        countery = 0
        while True and counter < 1:
            print("Move Up", stepcount, "steps")
            for i in range(stepcount):
                GPIO.output(Dir, 1)
                GPIO.output(Step, 1)
                GPIO.output(Dirb, 1)
                GPIO.output(Stepb, 1)
                time.sleep(LowSpeed)
                GPIO.output(Step, 0)
                GPIO.output(Stepb, 0)
                time.sleep(LowSpeed)
            # print ("Moving")
            time.sleep(1)
            print("Move Down", stepcount, "steps")
            for i in range(stepcount):
                GPIO.output(Dir, 0)
                GPIO.output(Step, 1)
                GPIO.output(Dirb, 0)
                GPIO.output(Stepb, 1)
                time.sleep(FastSpeed)
                GPIO.output(Step, 0)
                GPIO.output(Stepb, 0)
                time.sleep(FastSpeed)
            time.sleep(1)
            counter += 1
            print("success")
        GPIO.output(Enable, GPIO.LOW)
        GPIO.output(Enableb, GPIO.LOW)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

