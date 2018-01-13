#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  createTableDHT.py
#  
# Developed by Marcelo Rovai, MJRoBot.org @ 9Jan18
#  
# Create a table "DHT_data" to store DHT temp and hum data

import sqlite3 as lite
import sys

con = lite.connect('sensorsData.db')

with con:
    
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS DHT_data")
    cur.execute("CREATE TABLE DHT_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC)")

