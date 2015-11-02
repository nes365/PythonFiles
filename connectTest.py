# -*- coding: utf-8 -*-
"""
Created on Fri Jan 02 13:04:02 2015

@author: nsouthor
"""

import pyodbc
# Connect to local SQLExpress instance using the native client 10.0 (other clients will anly allow SQL 2000 functionality)

cnxn=pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=localhost\SQLExpress;DATABASE=TestDB01;UID=testacc;PWD=testacc')
cursor=cnxn.cursor()

# A Couple of test queries to demonstrate that the connection is successful

cursor.execute("Select TABLE_NAME from INFORMATION_SCHEMA.TABLES")
tables=cursor.fetchall()

# Using translate to strip the brackets etc from the result

tables2=str(tables).translate(None, "[]()u,'")

# Using str(listname) to covert the list results into a string so some basic character stripping can take place
#print "Tables in testdb: ", str(tables).translate(None, "[]()u,'")

print "Tables in testdb: ", tables2


# Must figure out how to pass a variable into the SQL query, 
# for now, table name explicitly set to "Users"

cursor.execute("select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='Users'")
columns=cursor.fetchall()
print "Columns in table Users: ", str(columns).translate(None, "[]()u,'")
#val1 = "dave"

val1=raw_input('Enter first name of user ')

cursor.execute("Select * from Users where Firstname like ?", val1)
names=cursor.fetchall()
print "Users in table with first name:", val1, names

