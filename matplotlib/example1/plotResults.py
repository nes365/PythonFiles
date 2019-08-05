#!/usr/bin/env python
import numpy
import csv
from matplotlib import pyplot as plt
from pylab import *

# Use numpy to import data from CSV file
data=numpy.genfromtxt('results.csv',delimiter=',')
# Create a data array for each column of data needed
cores=data[:,1]
time=data[:,2]

# Create a plot of results
plt.plot(cores,time,color="green",label="ICE8400")

# Set plot title
plt.title('Abaqus Run - Cores v Time')

# Display the legend defined in the plot function
legend(loc='upper right')

# Label the axes
plt.ylabel('Run Time')
plt.xlabel('#Cores')


# Display the plot on screen
#plt.show()

# Or save the plot to file using 72 dpi
savefig("results1.png",dpi=72)
