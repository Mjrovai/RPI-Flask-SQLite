#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lastLogDataTableDHT.py
#  
# Query dada from last input on table "DHT_data" 

import sqlite3

conn=sqlite3.connect('sensorsData.db')

curs=conn.cursor()

print ("\nLast raw Data logged on database:\n")
for row in curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT 1"):
    print (str(row[0])+" ==> Temp = "+str(row[1])+"	Hum ="+str(row[2]))



