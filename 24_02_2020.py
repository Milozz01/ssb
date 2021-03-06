# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0
from multiprocessing import Process
import time
import sys
import RPi.GPIO as GPIO
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QVariant, QSize

stepcount = 0
DirLin = 24
StepLin = 26
EnableLin = 22
DirDreh = 38
StepDreh = 36
EnableDreh = 40
# noch richtig einsetzen
GPIO.setmode(GPIO.BOARD)
gpiostopper = GPIO.setup(7, GPIO.IN)


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
        self.comboBox.addItem("", QVariant(20 * 1600))
        self.comboBox.addItem("", QVariant(30 * 1600))
        self.comboBox.addItem("", QVariant(40 * 1600))
        self.comboBox.addItem("", QVariant(50 * 1600))
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

        self.retranslateui(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.comboBox.activated.connect(self.handleactivated)
        # current buttons ################################################
        self.pushButton.clicked.connect(lambda: self.runmultimotorsetupv2(index=self.comboBox.currentIndex()))
        self.pushButton_2.clicked.connect(lambda: self.stop())
        self.pushButton_3.clicked.connect(lambda: self.nullpunkt())

    def retranslateui(self, mainWindow):
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
        print("Programm wurde beendet, STOP gedrückt")
        sys.exit()

    def nullpunkt(self):
        # needs to be configured!
        bla = False
        GPIO.setmode(GPIO.BOARD)
        
        GPIO.setup(7, GPIO.IN)
        
        GPIO.setup(DirLin, GPIO.OUT)
        GPIO.setup(StepLin, GPIO.OUT)
        GPIO.setup(EnableLin, GPIO.OUT)
        GPIO.output(EnableLin, GPIO.HIGH)
        print("Linearantrieb wird auf NULL gesetzt")
        fast_speed_lin = 0.00001
        while(bla == False):
            print("Move Down", 50*3600, "steps")
            
            for i in range(50*3600):
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(7, GPIO.IN)
                if GPIO.input(7) == GPIO.HIGH:
                    bla == True
                    return
                    #sys.exit("Kontakt mit Nullstelle erkannt")
                    
                    
                 
                    QtCore.QCoreApplication.processEvents()
                    GPIO.cleanup()
                # self.progressBar.setValue(0)
                # counterx = counterx + 1
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(DirLin, GPIO.OUT)
                GPIO.setup(StepLin, GPIO.OUT)
                GPIO.setup(EnableLin, GPIO.OUT)
                GPIO.output(EnableLin, GPIO.HIGH)
                GPIO.output(DirLin, 0)
                GPIO.output(StepLin, 1)

                time.sleep(fast_speed_lin)
                GPIO.output(StepLin, 0)

                time.sleep(fast_speed_lin)

    def gpiostop(self):
        if GPIO.input(5) == GPIO.HIGH:
            print("SIGNAL EINGEKOMMEN")
            GPIO.cleanup()
            sys.exit(app.exec_())

    def runmultimotorsetup(self, index):
        countermulti = 0
        while True and countermulti < 4:
            p3 = Process(target=self.stepperactiondreh(index))
            p3.start()
            p4 = Process(target=self.stepperactionlinear(index))
            p4.start()
            p3.join()
            p4.join()
            countermulti += 1

    def runmultimotorsetupv2(self, index):
        # muss noch überarbeitet werden
        time.sleep(0.5)
        thread2 = threading.Thread(target=self.stepperactionlinear(index))
        thread2.start()
        thread2.join()
        thread3 = threading.Thread(target=self.stepperactiondreh(index))
        thread3.start()
        thread3.join()

    def stepperactionlinear(self, index):
        GPIO.setmode(GPIO.BOARD)  # read the pin as board instead of BCM pin
        global stepcount
        stepcount = self.comboBox.itemData(index)
        self.progressBar.setMaximum(stepcount)
        print(stepcount, "this is given step")

        GPIO.setwarnings(False)
        GPIO.setup(DirLin, GPIO.OUT)
        GPIO.setup(StepLin, GPIO.OUT)
        GPIO.setup(EnableLin, GPIO.OUT)
        GPIO.output(EnableLin, GPIO.HIGH)

        fast_speed_lin = 0.00001  # old = 0.001 Change this depends on your stepper motor
        counter = 0
        counterx = 0
        countery = 0
        counterz = 1
        if counterz == 1:
            while True and counter < 2:
                self.progressBar.setValue(0)
                print("LINEAR: Move Up", stepcount, "steps")
                for i in range(stepcount):
                    QtCore.QCoreApplication.processEvents()
                    # countery = countery + 1
                    GPIO.output(DirLin, 1)
                    GPIO.output(StepLin, 1)

                    time.sleep(fast_speed_lin)
                    GPIO.output(StepLin, 0)

                    time.sleep(fast_speed_lin)
                    # self.progressBar.setValue(countery)
                    # print("Moving")
                time.sleep(1)

                print("LINEAR: Move Down", stepcount, "steps")
                for i in range(stepcount):
                    QtCore.QCoreApplication.processEvents()
                    # self.progressBar.setValue(0)
                    # counterx = counterx + 1
                    GPIO.output(DirLin, 0)
                    GPIO.output(StepLin, 1)

                    time.sleep(fast_speed_lin)
                    GPIO.output(StepLin, 0)

                    time.sleep(fast_speed_lin)
                    # self.progressBar.setValue(counterx)
                time.sleep(1)
                counter += 1
                print("success")
                GPIO.output(EnableLin, GPIO.LOW)
        else:
            print("sensorik erkannte kontakt!!!!!!!")
            sys.exit(app.exec_())

    def stepperactiondreh(self, index):
        GPIO.setmode(GPIO.BOARD)  # read the pin as board instead of BCM pin
        global stepcount
        testcount = 400
        stepcount = self.comboBox.itemData(index)
        self.progressBar.setMaximum(stepcount)
        print(stepcount, "this is given step")
        # return stepcount

        GPIO.setwarnings(False)
        GPIO.setup(DirDreh, GPIO.OUT)
        GPIO.setup(StepDreh, GPIO.OUT)
        GPIO.setup(EnableDreh, GPIO.OUT)
        GPIO.output(EnableDreh, GPIO.HIGH)

        fast_speed = 0.001  # old = 0.001 Change this depends on your stepper motor
        counter = 0
        counterx = 0
        countery = 0
        while True and counter < 1:
            self.progressBar.setValue(0)
            print("DREH: Move Up", stepcount, "steps")
            for i in range(400):
                # countery = countery + 1

                GPIO.output(DirDreh, 1)
                GPIO.output(StepDreh, 1)
                time.sleep(fast_speed)

                GPIO.output(StepDreh, 0)
                time.sleep(fast_speed)
                # self.progressBar.setValue(countery)
            # print ("Moving")
            time.sleep(0.5)

            counter += 1
            print("success")

        GPIO.output(EnableDreh, GPIO.LOW)


def pwmdefault():
    GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
    GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)
    pwm = GPIO.PWM(12, 5000)  # Initialize PWM on pwmPin 100Hz frequency
    dc = 50  # set dc variable to 0 for 0%
    pwm.start(dc)  # Start PWM with 0% duty cycle
    print("pwm default process started")


def preparemotoren():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    EnableLin = 22
    EnableDreh = 40
    GPIO.setup(EnableLin, GPIO.OUT)
    GPIO.setup(EnableDreh, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)
    GPIO.output(EnableLin, GPIO.LOW)
    GPIO.output(EnableDreh, GPIO.LOW)
    GPIO.output(35, GPIO.HIGH)
    print("Motoren wurden entsperrt")


if __name__ == "__main__":
    preparemotoren()
    pwmdefault()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    mainWindow.update()
    sys.exit(app.exec_())

