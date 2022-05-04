# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph

# Imports of all the needed modules
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import math

# Collision Data
crash_data = pd.read_csv("Full_Collisions.csv", header=0)   # identify the header row

# All of the years in our data set
years = ("2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021")
# List for all the years' injuries/deaths.
injury_year = []
death_year = []
# (Temporary) total injuries/deaths for each year, used to append to the lists
itotal = 0
dtotal = 0
# Looping through each year
for n in range(len(years)):
  # Looping through the crash date column
  for i in range(len(crash_data["CRASH DATE"])-1):
    # Checking if the current line in the crash date is the corresponding year (i.. if it's in 2012, 2013, etc.)
    if (crash_data["CRASH DATE"])[i].split('/')[2] == years[n]:
      try:
        # Adding the number of injuries/deaths to the total
        itotal += int(crash_data["NUMBER OF PERSONS INJURED"][i])
        dtotal += int(crash_data["NUMBER OF PERSONS KILLED"][i])
      except:
        # Excluding lines with errors
        print("baad :<0>")
  # Adding the full totals (representing a year) to the corresponding list
  injury_year.append(itotal)
  death_year.append(dtotal)
  # Resetting the total variables in preperation for the next year
  itotal = 0
  dtotal = 0
print(injury_year)
print(death_year)

# Initialise the subplot function using number of columns

figure, axis = plt.subplots(2)
  
# Grapth of Deaths from collisions in Brooklyn
axis[0].plot(years, death_year, color='Red', marker='o')
axis[0].set_ylabel('People Killed')
axis[0].set_title('Vehicle Collisions in Brooklyn')
  
# Graoth of Injuries from collisions in Brooklyn
axis[1].plot(years, injury_year, color='Blue', marker='o')
axis[1].set_ylabel('People Injured')
axis[1].set_xlabel('Years')

  
# Shows the graph
plt.show()
