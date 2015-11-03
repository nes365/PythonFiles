import csv


def readCSVFile(filename):
    """ Reads a CSV file and returns it as a list of rows """
    data = []
    for row in csv.reader(open(filename)):
        data.append(row)
    return data
  
  