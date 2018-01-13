#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  queryTableDHT.py
#  
#  Developed by Marcelo Rovai, MJRoBot.org @ 9Jan18
#  
# Query dada on table "DHT_data" 

import sqlite3

conn=sqlite3.connect('sensorsData.db')

curs=conn.cursor()

maxTemp = 27.6

print ("\nEntire database contents:\n")
for row in curs.execute("SELECT * FROM DHT_data"):
    print (row)

print ("\nDatabase entries for a specific humidity value:\n")
for row in curs.execute("SELECT * FROM DHT_data WHERE hum='29'"):
    print (row)
    
print ("\nDatabase entries where the temperature is above 30oC:\n")
for row in curs.execute("SELECT * FROM DHT_data WHERE temp>30.0"):
    print (row)
    
print ("\nDatabase entries where the temperature is above x:\n")
for row in curs.execute("SELECT * FROM DHT_data WHERE temp>(?)", (maxTemp,)):
    print (row)

conn.close()
