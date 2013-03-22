#!/usr/bin/python

import RPi.GPIO as GPIO
import wiringpi
from lib import xbox_read
import time
wiringpi.wiringPiSetupGpio
# Initialise the GPIO output channels
GPIO.setmode(GPIO.BCM)
serial = wiringpi.Serial('/dev/ttyAMA0',9600)
TURN = 18
BRAKE = 24
MODE = 25
#Set rpi.GPIO pinModes
GPIO.setup(SPEED, GPIO.OUT)
GPIO.setup(TURN, GPIO.OUT)
GPIO.setup(BRAKE, GPIO.OUT)
GPIO.setup(MODE, GPIO.OUT)

#Set WiringPi pinModes
void pinMode(TURN,PWM_OUTPUT);


# Default calibration values 
servoMid = 425
servoWidth = 180


rt_intensity = 0
lt_intensity = 0
steer = servoMid
brakeSet = 'no'

for event in xbox_read.event_stream(deadzone=12000):
    # Triggers Brake
    if event.key=='RT' or event.key=='LT':
        if event.key=='RT':
            rt_intensity = event.value
        else:
            lt_intensity = event.value
        brakeSet = yes if rt_intensity or lt_intesity >= 10 else no
        if brakeSet=='yes':
			GPIO.output(BRAKE, GRPIO.HIGH)
    # Left thumbstick controls the steering
	if event.key=='Y1':
		speed = int(event.value/32)
		speed.puts(speed)
	if event.key=='X2':
        steer = int( servoMid + (servoWidth*-event.value)/32768 )
        pwmWrite(TURN, steer);
	if event.key=='B' and event.is_press():
		GPIO.output(MODE, GPIO.HIGH)
		
        
