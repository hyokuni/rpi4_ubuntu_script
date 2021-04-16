#! /usr/bin/python3
import RPi.GPIO as GPIO
import time
import subprocess

def subprocess_open(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdoutdata, stderrdata) = popen.communicate()
    return stdoutdata, stderrdata

#period unit : sec
ISR_PERIOD = 5
#GPIO6 default pull-up
btn_pin = 13
ORDERCMD = 'sudo halt'

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.OUT)

GPIO.output(btn_pin,GPIO.HIGH)
print('push-button pull-low')
time.sleep(ISR_PERIOD)
#GPIO.output(btn_pin,GPIO.LOW)
#print('pulse low')

subprocess_open(ORDERCMD)


#deinit GPIㅒ
#GPIO.cleanup()

