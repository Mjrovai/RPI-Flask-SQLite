#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  insertDataTableDHT.py
#  
#  Developed by Marcelo Rovai, MJRoBot.org @ 9Jan18
#  
#  Query dada on table "DHT_data" 

import sqlite3

conn=sqlite3.connect('sensorsData.db')

curs=conn.cursor()

def add_data (temp, hum):
    curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, hum))
    conn.commit()

add_data (20.5, 30)
add_data (25.8, 40)
add_data (30.3, 50)


print ("\nEntire database contents:\n")
for row in curs.execute("SELECT * FROM DHT_data"):
    print (row)


conn.close()
