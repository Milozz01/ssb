import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #read the pin as board instead of BCM pin


Dir = 35
Step = 37
Enable = 33


GPIO.setwarnings(False)
GPIO.setup(Dir, GPIO.OUT)
GPIO.setup(Step, GPIO.OUT)
GPIO.setup(Enable, GPIO.OUT)

FastSpeed = 0.0001 #old = 0.001 Change this depends on your stepper motor
LowSpeed = 0.0001
#Speed = FastSpeed

GPIO.output(Enable, GPIO.HIGH)

while True:
	print ("Move Up")
	for i in range (40*1600):
		GPIO.output(Dir, 1)
		GPIO.output(Step, 1)
		time.sleep(LowSpeed)
		GPIO.output(Step, 0)
		time.sleep(LowSpeed)
		#print ("Moving")
	time.sleep(5)
	print ("Move Down")
	for i in range (40*1600):
		GPIO.output(Dir, 0)
		GPIO.output(Step, 1)
		time.sleep(FastSpeed)
		GPIO.output(Step, 0)
		time.sleep(FastSpeed)
	time.sleep(5)

GPIO.output(Enable, GPIO.LOW)
