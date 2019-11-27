import RPi.GPIO as GPIO   # Import the GPIO library.
from time import sleep              # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.


GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(40, GPIO.OUT)
pwm = GPIO.PWM(12, 5000)   # Initialize PWM on pwmPin 100Hz frequency
GPIO.output(40, GPIO.HIGH)

# main loop of program
print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
dc=50# set dc variable to 0 for 0%
pwm.start(dc)                      # Start PWM with 0% duty cyclel
