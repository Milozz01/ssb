# ssb
smart spray booth

main purpose of the code is to spray objects between 5cm and 50cm efficently and automatically

IDE used: pycharm
program language used: python 3.8

the raspberry pi communicates with 2 TB6600 microstep drivers to control 2 stepper motors:
- 1 linear controlled stepper
- 1 stepper for circular plate to rotate element

GUI is created by QtDesigner from PyQt5, converted to a python file and imported into the main code and adjusted.
