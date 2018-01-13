#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  DHT22_test.py
#  
import Adafruit_DHT
DHT22Sensor = Adafruit_DHT.DHT22

DHTpin = 16

humidity, temperature = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
