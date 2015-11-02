# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 14:15:41 2014

@author: NSouthor
"""

import numpy as np

# Importing a csv file into an array called "data"
data=np.loadtxt(r'C:\Users\nsouthor\Documents\Training & Certification\Python\SC\PatientData\inflammation-01.csv',delimiter=',')
# Assigning a value to a variable
weight_kg=55

# Combining print statements with the output of a variable
print 'weight in KG:', weight_kg,'Kg'
# Maths with a variable
print 'weight in pounds:', 2.2 * weight_kg,'lbs'

weight_lb = 2.2 * weight_kg

print 'weight in KG:', weight_kg,'Kg', 'and weight in pounds:', weight_lb,'lbs'
weight_kg = 100.0
print 'weight in kilograms is now:', weight_kg,'Kg',  'and weight in pounds is still:', weight_lb,'lbs'

# Printing the data array
print data

# Displaying the data type
print 'Data type is:', type(data)

# Displaying the data shape - N dimensional array
print 'Data shape is:', data.shape

# Displaying data from various areas of the array
print 'First value in data:', data[0,0]
print 'Middle value in data:', data[2,20]

print 'First column of each row is:', data[0:5,0:1]

print 'Second column of each row is:', data[0:5,1:2]

print 'First and second columns of each row are', data[0:5,0:2]

print 'First to tenth columns of each row are', data[0:5,0:10]

small = data[:3,36:]
print 'Print the last 4 entries of the first 3 rows', small

# Array mathmatics
doubledata = data * 2.0

print 'Original:'
print data[:3,36:]
print 'doubledata:'
print doubledata[:3,36:]

tripledata = doubledata + data
print 'tripledata:'
print tripledata[:3,36:]

# Statistical methods applied to arrays
print 'Mean value of all data:', data.mean()
print 'Max inflammation:', data.max()
print 'Minimum inflamation:', data.min()
print 'Standard deviation:', data.std()

# Partial statistics
# Selecting the data we want to use and putting it into a new temporary array
patient_0 = data[0,:]   # 0 on the first axis, everything else on the second
print 'Max inflammation for patient 0:', patient_0.max()

# Instead of storing the data in an array of its own we can combine the selection and method
print 'Max inflammation for patient 2:', data[2,:].max()

# Performing operations on an array axis. Axis 0 is downwards, axis 1 is left to right
# To print the mean of each column top to bottom.
""" 0,0,1,3,1,2,4,7,8,3,3,3,10,5,7,4,7,7,12,18,6,13,11,11,7,7,4,6,8,8,4,4,5,7,3,4,2,3,0,0
    0,1,2,1,2,1,3,2,2,6,10,11,5,9,4,4,7,16,8,6,18,4,12,5,12,7,11,5,11,3,3,5,4,4,5,5,1,1,0,1
    0,1,1,3,3,2,6,2,5,9,5,7,4,5,4,15,5,11,9,10,19,14,12,17,7,12,11,7,4,2,10,5,4,2,2,3,2,2,1,1
    0,0,2,0,4,2,2,1,6,7,10,7,9,13,8,8,15,10,10,7,17,4,4,7,6,15,6,4,9,11,3,5,6,3,3,4,2,3,2,1
    0,1,1,3,3,1,3,5,2,4,4,7,6,5,3,10,8,10,6,17,9,14,9,7,13,9,12,6,7,7,9,6,3,2,2,4,2,0,1,1 """
# i.e. mean of 0,0,0,0,0 and then 0,1,1,0,1 etc

print 'Mean values of columns, axis 0'
print data.mean(axis=0)

print 'Shape of axis 0 is', data.mean(axis=0).shape


# Plotting!

from matplotlib import  pyplot as plt
# Create a heat map for the array 'data'
plt.imshow(data)
plt.show()

# Create a plot of mean values in columns, axis 0
ave_inflammation=data.mean(axis=0)
plt.plot(ave_inflammation)
plt.show()


# print maximum inflammation per day
print 'Max inflammation per day'
plt.plot(data.max(axis=0))
plt.show()

# Minimum inflammation per day
print 'Min inflammation per day'
plt.plot(data.min(axis=0))
plt.show()



# Adding labels to plots

plt.figure(figsize=(10.0,3.0))

plt.subplot(1,3,1)
plt.ylabel('average')
plt.plot(data.mean(0))

plt.subplot(1,3,2)
plt.ylabel('min')
plt.plot(data.min(0))

plt.subplot(1,3,3)
plt.ylabel('max')
plt.plot(data.max(0))

plt.tight_layout()
plt.show()


































