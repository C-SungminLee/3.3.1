# a321_crashs_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import math

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
crash_data = pd.read_csv("Vehicle_Collisions_Data.csv", header=0)   # identify the header row

# Get the angles from 0 to 2 pie (360 degree) in narray object

# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(2)
  
# For Sine Function
axis[0].plot(crash_data['Year'], crash_data['Deaths'], color='Red', marker='o')
axis[0].set_ylabel('People Killed')
axis[0].set_title('Vehicle Collisions in Brooklyn')
  
# For Cosine Function
axis[1].plot(crash_data['Year'], crash_data['Injuries'], color='Blue', marker='o')
axis[1].set_ylabel('People Injured')
axis[1].set_xlabel('Years')

  
# Combine all the operations and display
plt.show()
# TODO #2: Use matplotlib to make a line graph





plt.show()

'''
# TODO #3: Plot LOWESS in a line graph
plt.plot(crash_data['Year'], crash_data['LOWESS'], color='blue')
plt.show()

# TODO #4: Use matplotlib to make a bar chart
plt.bar(crash_data['Year'], crash_data['Anomaly'], align='center', color='green')
plt.ylabel('crasherature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in crasheratures')
min_anomaly = crash_data['Anomaly'][0]
max_anomaly = crash_data['Anomaly'][0]
min_year = crash_data['Year'][0]
max_year = crash_data['Year'][0]
sum_anomaly = 0
avg_anomaly = 0

# find the min, max and calculate the sum
for i in range(len(crash_data['Anomaly'])):
  if (crash_data['Anomaly'][i] < min_anomaly):
    min_anomaly = crash_data['Anomaly'][i]
    min_year = crash_data['Year'][i]
  # new code inside the same for loop
  if (crash_data['Anomaly'][i] > max_anomaly):
    max_anomaly = crash_data['Anomaly'][i]
    max_year = crash_data['Year'][i]
  sum_anomaly += crash_data['Anomaly'][i]

# calculate average
avg_anomaly = sum_anomaly/len(crash_data['Anomaly'])
# print the statistical values
print("The maximum anomaly is:", max_anomaly, "which occured in", max_year)
print("The minimum anomaly is:", min_anomaly, "which occured in", min_year)
print("The average anomaly is:", avg_anomaly)

'''