# coding=utf-8
import tkinter as tk
import RPi.GPIO as GPIO
import time

master = tk.Tk()

#FastSpeed = 0.001  # default Speed

var = tk.StringVar(master)
var2 = tk.IntVar(master)
fSpeed = tk.StringVar(master)

labelZero = tk.Label(master, text="Smart Spray Booth - Configuration")
labelZero.grid(row=1, column=1)
labelPreset = tk.Label(master, text="Presets:")
labelPreset.grid(row=2, column=1)


options = {"10cm": 10*1600, "20cm": 20*1600, "30cm": 30*1600, "40cm": 40*1600, "50cm": 50*1600}
option = tk.OptionMenu(master, var, *options.keys())
option.grid(row=3, column=2)
x = options.values()

def getBauteil():
    print("entered value is", options[var.get()])
    motorSpeed()
    # master.quit()
    label4 = tk.Label(master, text=options[var.get()])
    label4.grid(row=5, column=4)
    #print(stepperaction())
    stepperaction() #holt die function stepperaction, verhindert dann jedoch, dass label 3 angezeigt wird

def motorSpeed():
    if var != 0:
        FastSpeed = options[var.get()]
        global fSpeed
        fSpeed = FastSpeed / 2
        print(FastSpeed, "from motorspeed func")
        print(fSpeed, "from motorspeed func")
        master.update_idletasks()
        return FastSpeed
        return fSpeed
    label3 = tk.Label(master, text=options[var.get()])
    label3.grid(row=5, column=5)
      
button = tk.Button(master, text="OK", command=getBauteil)
button.grid(row=3, column=3)

label1 = tk.Label(master, textvariable=var)
label1.grid(row=5, column=3)


master.title("Smart Spray Booth - Configuration")
master.configure(bg="grey80")
master.geometry("300x300")



def stepperaction():
    #GPIO = None
    GPIO.setmode(GPIO.BOARD)  # read the pin as board instead of BCM pin

    stepcount = options[var.get()]
    print(stepcount / 6, "this is from stepperaction function")
    #return stepcount

    Dir = 35
    Step = 37
    Enable = 33

    GPIO.setwarnings(False)
    GPIO.setup(Dir, GPIO.OUT)
    GPIO.setup(Step, GPIO.OUT)
    GPIO.setup(Enable, GPIO.OUT)

    FastSpeed = 0.0001  # old = 0.001 Change this depends on your stepper motor
    LowSpeed = 0.0001
    # Speed = FastSpeed
    
    GPIO.output(Enable, GPIO.HIGH)
    counter = 0
    while True and counter < 3:
        print("Move Up", stepcount, "steps")
        for i in range(stepcount):
            GPIO.output(Dir, 1)
            GPIO.output(Step, 1)
            time.sleep(LowSpeed)
            GPIO.output(Step, 0)
            time.sleep(LowSpeed)
        # print ("Moving")
        time.sleep(1)
        print("Move Down", stepcount, "steps")
        for i in range(stepcount):
            GPIO.output(Dir, 0)
            GPIO.output(Step, 1)
            time.sleep(FastSpeed)
            GPIO.output(Step, 0)
            time.sleep(FastSpeed)
        time.sleep(1)
        counter += 1
        print("success")
    GPIO.output(Enable, GPIO.LOW)

tk.mainloop()
