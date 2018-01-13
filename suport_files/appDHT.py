#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  appDHT.py
#  

import time
import sqlite3
import Adafruit_DHT

dbname='sensorsData.db'
sampleFreq = 2 # time in seconds


# get data from DHT sensor
def getDHTdata():	
	
	DHT22Sensor = Adafruit_DHT.DHT22
	DHTpin = 16
	hum, temp = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)
	
	if hum is not None and temp is not None:
		hum = round(hum)
		temp = round(temp, 1)
		logData (temp, hum)

# log sensor data on database
def logData (temp, hum):
	
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	
	curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, hum))
	conn.commit()
	conn.close()

# display database data
def displayData():
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	print ("\nEntire database contents:\n")
	for row in curs.execute("SELECT * FROM DHT_data"):
		print (row)
	conn.close()

# main function
def main():
	for i in range (0,3):
		getDHTdata()
		time.sleep(sampleFreq)
	displayData()

# Execute program 
main()

