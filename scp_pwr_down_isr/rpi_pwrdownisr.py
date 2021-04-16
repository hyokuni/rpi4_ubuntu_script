#! /usr/bin/python3
import RPi.GPIO as GPIO
import time

#period unit : sec
ISR_PERIOD = 2
btn_pin = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.OUT)

GPIO.output(btn_pin,GPIO.HIGH)
print('pulse out')
time.sleep(ISR_PERIOD)
GPIO.output(btn_pin,GPIO.LOW)
print('pulse low')

#deinit GPIㅒ
GPIO.cleanup()

