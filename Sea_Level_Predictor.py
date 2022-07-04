import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level')

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    plt.xlim(1850, 2075)
    years_extended = np.arange(1880, 2051, 1)
    line = [slope*x + intercept for x in years_extended]
    plt.plot(years_extended, line)

    # Create second line of best fit
    x = df.iloc[120:]['Year']
    y = df.iloc[120:]['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    second_years = np.arange(2000, 2051, 1)
    line_2 = [slope*x + intercept for x in second_years]
    plt.plot(second_years, line_2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()
