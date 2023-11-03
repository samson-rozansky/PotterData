import csv
with open("20231103181138_0190.csv") as bruh:
    from matplotlib import pyplot as plt
    import numpy as np
    import random
    reader = csv.DictReader(bruh)
    Experience = {}
    for row in reader:
        try:
            Experience[row["Experience (Years)"]] += 1
        except:
            Experience[row["Experience (Years)"]] = 1
    x = [i for i in Experience.keys()] # X-axis points 
    y = [i for i in Experience.values()]  # Y-axis points 
    
    plt.plot(x, y)  # Plot the chart 
    plt.show()  # display 