# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0
from multiprocessing import process, Process
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
        self.comboBox.addItem("", QVariant(10 * 1600))
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
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMinimum(0)
        # self.progressBar.setMaximum()
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
        self.pushButton.clicked.connect(lambda: self.runmultimotorsetup(index=self.comboBox.currentIndex()))
        self.pushButton_2.clicked.connect(lambda: self.stop())
        self.pushButton_3.clicked.connect(lambda: self.nullpunkt())

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

        self.menuSmart_Spray_Booth_Configuration.setTitle(
            _translate("mainWindow", "Smart Spray Booth - Configuration"))

        if self.comboBox.currentTextChanged:
            print(self.comboBox.currentData(), "from if")

    def handleactivated(self, index):
        print(self.comboBox.itemText(index), "handle")
        print(self.comboBox.itemData(index), "handle")
        self.label_3.setText(self.comboBox.itemText(index))

    def stop(self):
        print("programm wird beendet")
        sys.exit()

    def nullpunkt(self):
        # needs to be configured!
        print("wird auf null gesetzt")

    def runmultimotorsetup(self, index):
        p3 = Process(target=self.stepperactiondreh(index))
        p3.start()
        p4 = Process(target=self.stepperactionlinear(index))
        p4.start()
        p3.join()
        p4.join()

    def stepperactionlinear(self, index):
        # GPIO.setmode(GPIO.BOARD)  # read the pin as board instead of BCM pin
        global stepcount
        stepcount = self.comboBox.itemData(index)
        self.progressBar.setMaximum(stepcount)
        print(stepcount, "this is given step")
        # return stepcount
        FastSpeed = 0.0001  # old = 0.001 Change this depends on your stepper motor
        LowSpeed = 0.0001  # old = 0.001 Change this depends on your stepper motor
        counter = 0
        countery = 0
        while True and counter < 1:
            print("linear starting")
            print("Move Up", stepcount, "steps")
            for i in range(stepcount):
                countery = countery + 1
                print(countery)
                time.sleep(LowSpeed)
                print(countery)
                time.sleep(LowSpeed)
                self.progressBar.setValue(countery)
            time.sleep(1)
            print("Move Down", stepcount, "steps")
            for i in range(stepcount):
                countery = countery + 1
                print(countery)
                time.sleep(FastSpeed)
                print(countery)
                time.sleep(FastSpeed)
            time.sleep(1)
            counter += 1
            print("success")
            self.progressBar.reset()
            mainWindow.update()

    def stepperactiondreh(self, index):
        # GPIO.setmode(GPIO.BOARD)  # read the pin as board instead of BCM pin
        global stepcount
        stepcount = self.comboBox.itemData(index)
        self.progressBar.setMaximum(stepcount)
        print(stepcount, "this is given step")
        # return stepcount
        FastSpeed = 0.0001  # old = 0.001 Change this depends on your stepper motor
        LowSpeed = 0.0001  # old = 0.001 Change this depends on your stepper motor
        counter = 0
        countery = 0
        while True and counter < 1:
            print("dreh starting")
            print("Move Up", stepcount, "steps")
            for i in range(stepcount):
                countery = countery + 1
                print(countery)
                time.sleep(LowSpeed)
                print(countery)
                time.sleep(LowSpeed)
                self.progressBar.setValue(countery)
            time.sleep(1)
            print("Move Down", stepcount, "steps")
            for i in range(stepcount):
                countery = countery + 1
                print(countery)
                time.sleep(FastSpeed)
                print(countery)
                time.sleep(FastSpeed)
            time.sleep(1)
            counter += 1
            print("success")
            self.progressBar.reset()
            mainWindow.update()


def pwmdefault():
    #GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.

    #GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
    #GPIO.setup(40, GPIO.OUT)
    #pwm = GPIO.PWM(12, 5000)  # Initialize PWM on pwmPin 100Hz frequency
    #GPIO.output(40, GPIO.HIGH)

    # main loop of program
    #print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
    #dc = 50  # set dc variable to 0 for 0%
    #pwm.start(dc)  # Start PWM with 0% duty cycle
    print("pwm default process starting")


def test():
    print("hi")


if __name__ == "__main__":
    import sys
    p1 = Process(target=test())
    p1.start()
    p2 = Process(target=pwmdefault())
    p2.start()
    p1.join()
    p2.join()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

