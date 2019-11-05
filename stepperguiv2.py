# coding=utf-8
from tkinter import *
import time
import tk
import RPi.GPIO as GPIO


master = Tk()

#fSpeed = 0
FastSpeed = 0.0001  # default Speed
LowSpeed = 0.0001
#steps = 1600

steps = IntVar(master)
fSpeed = StringVar(master)
# var.set("bitte Länge setzen")  # initial value

labelZero = Label(master, text="Smart Spray Booth - Configuration")
labelZero.grid(row=1, column=1, sticky=EW)
labelPreset = Label(master, text="Presets:")
labelPreset.grid(row=2, column=1, sticky=W)
options = {"10cm": 10*1600, "20cm": 20*1600, "30cm": 30*1600, "40cm": 40*1600, "50cm": 50*1600}
option = OptionMenu(master, steps, *options.keys())
option.grid(row=3, column=2, sticky=W)


def getBauteil():
    print("value is", options[steps.get()])
    motorSpeed()
    # master.quit()
    label3 = Label(master, text=options[steps.get()])
    label3.grid(row=5, column=4)

def motorSpeed():
    if steps != 0:
        FastSpeed = options[steps.get()]
        global fSpeed
        fSpeed = FastSpeed / 2
        print(FastSpeed)
        print(fSpeed)
        master.update_idletasks()
        return FastSpeed
        return fSpeed
    label3 = Label(master, text=options[steps.get()])
    label3.grid(row=5, column=5)


button = Button(master, text="OK", command=getBauteil)
button.grid(row=3, column=3, sticky=W)

label1 = Label(master, textvariable=steps)
label1.grid(row=5, column=3, sticky=W)
label2 = Label(master, text=fSpeed)
label2.grid(row=5, column=3, sticky=W)

master.title("Smart Spray Booth - Configuration")
master.configure(bg="grey80")
master.geometry("300x300")


class MotorConfig:
    GPIO.setmode(GPIO.BOARD)  # read the pin as board instead of BCM pin
    Dir = 35
    Step = 37
    Enable = 33
    GPIO.setwarnings(False)
    GPIO.setup(Dir, GPIO.OUT)
    GPIO.setup(Step, GPIO.OUT)
    GPIO.setup(Enable, GPIO.OUT)
    GPIO.output(Enable, GPIO.HIGH)
    stepsgetter = motorSpeed(FastSpeed)
    #stepsgetter = options[steps.get()]
    convertedstep = int(stepsgetter)

    while True:
        print("Move Up")
        for i in range(convertedstep):
            GPIO.output(Dir, 1)
            GPIO.output(Step, 1)
            time.sleep(LowSpeed)
            GPIO.output(Step, 0)
            time.sleep(LowSpeed)
        # print ("Moving")
        time.sleep(5)
        print("Move Down")
        for i in range(convertedstep):
            GPIO.output(Dir, 0)
            GPIO.output(Step, 1)
            time.sleep(FastSpeed)
            GPIO.output(Step, 0)
            time.sleep(FastSpeed)
        time.sleep(5)

    GPIO.output(Enable, GPIO.LOW)


mainloop()
