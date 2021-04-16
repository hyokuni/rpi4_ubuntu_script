#! /usr/bin/python3
import RPi.GPIO as GPIO
import time
import subprocess

def subprocess_open(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdoutdata, stderrdata) = popen.communicate()
    return stdoutdata, stderrdata


def adaptiveFanCtrl(enable,period,temp):
    
    
    if enable:
        if temp > 80:
            pwm_led.ChangeDutyCycle(90)
            print('duty:90')
        elif temp > 70:
            pwm_led.ChangeDutyCycle(70)
            print('duty:70')
        elif temp > 60:
            pwm_led.ChangeDutyCycle(50)
            print('duty:50')
        elif temp > 40:
            pwm_led.ChangeDutyCycle(30)
            print('duty:30')
        else:
            pwm_led.ChangeDutyCycle(0)
            print('duty:0')
        
    else:
        pwm_led.ChangeDutyCycle(0)
        
    time.sleep(period)

GETTEMP = 'cat /sys/devices/virtual/thermal/thermal_zone0/temp'
PWM_PERIOD = 1000
CTRL_PERIOD = 1
TURN_ON = True
TURN_OFF = False

led_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, PWM_PERIOD)

#start value zero
pwm_led.start(0)
#pwm_led.start(100)
time.sleep(1)

tempNow = ''
err = ''
getdata = ''

try:
	while True:
            #get temp
            tempNow,err = subprocess_open(GETTEMP)
            tempNow = int(tempNow[:-1]) / 1000
        
            print('cpu temp is ',str(tempNow))
        
            #test
            #getdata = input()
            #adaptiveFanCtrl(TURN_ON,PERIOD,int(getdata))
        
            adaptiveFanCtrl(TURN_ON,CTRL_PERIOD,tempNow)
        

finally:
    pwm_led.stop()
    GPIO.cleanup()

