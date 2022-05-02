# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph

# Imports of all the needed modules
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import math

# Crash Data
crash_data = pd.read_csv("Vehicle_Collisions_Data.csv", header=0)   # identify the header row

# Initialise the subplot function using number of columns
figure, axis = plt.subplots(2)
  
# Grapth of Deaths from collisions in Brooklyn
axis[0].plot(crash_data['Year'], crash_data['Deaths'], color='Red', marker='o')
axis[0].set_ylabel('People Killed')
axis[0].set_title('Vehicle Collisions in Brooklyn')
  
# Graoth of Injuries from collisions in Brooklyn
axis[1].plot(crash_data['Year'], crash_data['Injuries'], color='Blue', marker='o')
axis[1].set_ylabel('People Injured')
axis[1].set_xlabel('Years')

  
# Shows the graph
plt.show()
