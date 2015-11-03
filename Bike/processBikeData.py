# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:44:00 2015

@author: NSouthor
"""

import os
import csv
os.chdir("C:\\Users\\nsouthor\\Documents\\GitHub\\PythonFiles\\Bike")

def readFiles(filePath):
    # get all files in the folder
    fileListing = os.listdir(filePath)
    for myFile in fileListing:
        # Create the file path
        myFilePath = os.path.join(filePath, myFile)
        # Check to make sure it's a file and not a folder
        if (os.path.isfile(myFilePath) and myFilePath.endswith(".csv")):
            with open(myFilePath, 'r', encoding='utf-8') as csvfile:
                # Sniff to find the format
                fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
                csvfile.seek(0)
                # Create a csv reader
                myReader = csv.reader(csvfile, dialect=fileDialect)
                # Read each row
                for row in myReader:
                    # Do processing
                    print(row)
    return
    
if __name__ == '__main__':
    # Print list of available dialects
    print(csv.list_dialects())
    # Path for current file
    currentPath = os.path.dirname(__file__)
    # Path for the filename that we want to read
    #filePath = os.path.abspath(os.path.join(currentPath, os.pardir,'data'))
    filePath = os.path.abspath(currentPath)
        
    readFiles(filePath)