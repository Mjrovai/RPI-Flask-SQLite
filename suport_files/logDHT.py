#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  logDHT.py
#
#  Developed by Marcelo Rovai, MJRoBot.org @ 10Jan18
#  
#  Capture data from a DHT22 sensor and save it on a database

import time
import sqlite3
import Adafruit_DHT

dbname='sensorsData.db'
sampleFreq = 60 # time in seconds

# get data from DHT sensor
def getDHTdata():	
	
	DHT22Sensor = Adafruit_DHT.DHT22
	DHTpin = 16
	hum, temp = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)
	
	if hum is not None and temp is not None:
		hum = round(hum)
		temp = round(temp, 1)
	return temp, hum

# log sensor data on database
def logData (temp, hum):
	
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	
	curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, hum))
	conn.commit()
	conn.close()

# main function
def main():
	while True:
		temp, hum = getDHTdata()
		logData (temp, hum)
		time.sleep(sampleFreq)

# ------------ Execute program 
main()

