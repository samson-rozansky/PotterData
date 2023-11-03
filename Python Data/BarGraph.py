import csv
with open("20231103181138_0190.csv") as bruh:
    from matplotlib import pyplot as plt
    import numpy as np
    import random
    reader = csv.DictReader(bruh)
    Experience = {}
    for row in reader:
        try:
            Experience[row["Marital Status"]] += 1
        except:
            Experience[row["Marital Status"]] = 1
    fig, ax = plt.subplots()
    materials = [i for i in Experience.keys()]
    x_pos = np.arange(len(materials))
    CTEs = [i for i in Experience.values()]
    plt.rcParams["figure.autolayout"] = True
    ax.bar(x_pos, CTEs, alpha=0.5)
    ax.set_ylabel('Amt of people on the job')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(materials)
    ax.set_title('The Types of occupations people are in the DataSet')
    ax.yaxis.grid(True)
    plt.xticks(range(len(Experience)), Experience.keys(), rotation='vertical')


    # Save the figure and show
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()