#! /usr/bin/python3
import RPi.GPIO as GPIO
import time
import subprocess

def subprocess_open(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdoutdata, stderrdata) = popen.communicate()
    return stdoutdata, stderrdata

btn_pin = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN, GPIO.PUD_UP)
#GPIO.setup(btn_pin, GPIO.IN)

try:
    #for i in range(0,300):
    while True:
        GPIO.wait_for_edge(btn_pin,GPIO.FALLING,bouncetime=100)
        time.sleep(0.1)
        print(GPIO.input(btn_pin))

        if GPIO.input(btn_pin) == 0:
            subprocess.call(['shutdown','-h','now'], shell=False)
            print('os cmd run')

        print('soft power off working')
        time.sleep(1)

finally:
    GPIO.cleanup()

