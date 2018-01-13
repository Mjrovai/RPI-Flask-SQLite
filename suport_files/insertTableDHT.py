#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  insertTableDHT.py
#  
# Developed by Marcelo Rovai, MJRoBot.org @ 9Jan18
#  
# Insert dada on table "DHT_data" 

import sqlite3 as lite
import sys

con = lite.connect('sensorsData.db')

with con:
    
    cur = con.cursor() 
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 20.5, 30)")
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 25.8, 40)")
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 30.3, 50)")


