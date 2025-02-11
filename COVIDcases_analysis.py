# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:19:21 2020

@author: Antonio Garcia marin
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator

def Countryinclude(country):
    #Slice and create the dataframes
    df_country = df.loc[df['location'] == country]
    # Convert the 'date' column to datetime, handling errors, and ensuring correct format
    df_country['date'] = pd.to_datetime(df_country['date'], format='%Y-%m-%d', errors='coerce')
    # Select the last 730 data points - 2 years
    df_country = df_country.tail(730)
    # Starting to plot data from the country
    x = df_country['date']
    y = df_country['new_cases_per_million']
    plt.scatter(x,y, label=country, linewidth=0.2, alpha=1, marker='.')
    plt.title('COVID cases')
    plt.xlabel('Date')
    plt.ylabel('New cases per million of habitants')
    plt.legend(loc='best')
    
#read the real-time data online from this website.
df = pd.read_csv("https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.csv", header=0)

#Plot everything in one Figure
plot1 = plt.figure(1)

#Call the function. Just write the countries you want in the plot.
Countryinclude('Czech Republic')
Countryinclude('Spain')
Countryinclude('Poland')
Countryinclude('Italy')
Countryinclude('France')
Countryinclude('Germany')

#set a limit for axis
#plt.ylim(0, 10000)
#plt.xlim()

# Set the number of x-ticks to 24
n = 24
ax = plt.gca()

# Force the x-axis to show only 30 ticks
ax.xaxis.set_major_locator(MaxNLocator(n))

# Format the date labels to look cleaner (e.g., rotating, showing only month/year)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
