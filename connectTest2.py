# -*- coding: utf-8 -*-
"""
connectTest2.py
Uses PYODBC to connect to a database using a trusted connection and then execute a simple SQL command
Created on Fri Apr 03 13:03:18 2015
@author: NSouthor
"""

import pyodbc
import sys
# Create a connection string
connection_str = """
Driver={SQL Server Native Client 11.0};
Server=localhost\SQLEXPRESS;
Database=TestDB01;
Trusted_Connection=yes;
"""
# Connect to local SQLExpress instance using the native client 11.0 (other clients will only allow SQL 2000 functionality)
try:
    db_connection = pyodbc.connect(connection_str)
    db_connection.autocommit = True
    db_connection.autocommit = False
    db_cursor = db_connection.cursor()
except pyodbc.DatabaseError, e:
    print 'Database connection error: %s' % e
except Exception, e:
    print 'General error: %s' % e
    
    
# A Couple of test queries to demonstrate that the connection is successfull
    db_cursor.execute("SELECT * from TestTable01")
    data=db_cursor.fetchall()





