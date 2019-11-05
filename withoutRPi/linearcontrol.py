# coding=utf-8
import tkinter as tk


master = tk.Tk()

#FastSpeed = 0.001  # default Speed

var = tk.StringVar(master)
var2 = tk.IntVar(master)
fSpeed = tk.StringVar(master)

labelZero = tk.Label(master, text="Smart Spray Booth - Configuration", anchor='center')
labelZero.grid(row=1)
labelPreset = tk.Label(master, text="Presets:")
labelPreset.grid(row=3, column=1)


options = {"10cm": 10*1600, "20cm": 20*1600, "30cm": 30*1600, "40cm": 40*1600, "50cm": 50*1600}
option = tk.OptionMenu(master, var, *options.keys())
option.grid(row=3, column=2)
x = options.values()

def getBauteil():
    print("value is", options[var.get()])
    motorSpeed()
    # master.quit()
    label4 = tk.Label(master, text=options[var.get()])
    label4.grid(row=5, column=2)
    print(stepperaction())

def motorSpeed():
    if var != 0:
        FastSpeed = options[var.get()]
        global fSpeed
        fSpeed = FastSpeed / 2
        print(FastSpeed)
        print(fSpeed)
        master.update_idletasks()
        return FastSpeed
        return fSpeed
    label3 = tk.Label(master, text=options[var.get()])
    label3.grid(row=5, column=3)

button = tk.Button(master, text="OK", command=getBauteil)
button.grid(row=3, column=3)

label1 = tk.Label(master, textvariable=var)
label1.grid(row=5, column=1)

labela = tk.Label(master, text="bla")
labela.grid(row=5, column=1)

master.title("Smart Spray Booth - Configuration")
master.configure(bg="grey80")
master.geometry("400x300")


def stepperaction():
    #import RPi.GPIO as GPIO
    import time
    GPIO = None
    #GPIO.setmode(GPIO.BOARD)  # read the pin as board instead of BCM pin

    stepcount = options[var.get()]
    print(stepcount, "Steps")
    return stepcount

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

    while True:
        print("Move Up")
        for i in range(stepcount):
            GPIO.output(Dir, 1)
            GPIO.output(Step, 1)
            time.sleep(LowSpeed)
            GPIO.output(Step, 0)
            time.sleep(LowSpeed)
        # print ("Moving")
        time.sleep(5)
        print("Move Down")
        for i in range(stepcount):
            GPIO.output(Dir, 0)
            GPIO.output(Step, 1)
            time.sleep(FastSpeed)
            GPIO.output(Step, 0)
            time.sleep(FastSpeed)
        time.sleep(5)

    #GPIO.output(Enable, GPIO.LOW)

tk.mainloop()
