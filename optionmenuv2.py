# coding=utf-8
import tkinter as tk

master = tk.Tk()

#fSpeed = 0
FastSpeed = 0.001  # default Speed

var = tk.StringVar(master)
var2 = tk.IntVar(master)
fSpeed = tk.StringVar(master)
# var.set("20cm")  # initial value

labelZero = tk.Label(master, text="Smart Spray Booth - Configuration")
labelZero.grid(row=1, column=1)
labelPreset = tk.Label(master, text="Presets:")
labelPreset.grid(row=2, column=1)


options = {"20cm": 200, "30cm": 300, "40cm": 400, "50cm": 500, "60cm": 600}
option = tk.OptionMenu(master, var, *options.keys())
option.grid(row=3, column=2)
x = options.values()

def getBauteil():
    print("value is", options[var.get()])
    motorSpeed()
    # master.quit()
    label3 = tk.Label(master, text=options[var.get()])
    label3.grid(row=5, column=4)

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
    label3.grid(row=5, column=5)


button = tk.Button(master, text="OK", command=getBauteil)
button.grid(row=3, column=3)

label1 = tk.Label(master, textvariable=var)
label1.grid(row=5, column=3)
label2 = tk.Label(master, text=fSpeed)
label2.grid(row=5, column=3)

master.title("Smart Spray Booth - Configuration")
master.configure(bg="grey80")
master.geometry("300x300")
tk.mainloop()
