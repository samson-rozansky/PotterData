import csv
with open("20231103181138_0190.csv") as bruh:
    from matplotlib import pyplot as plt
    import numpy as np
    import random
    reader = csv.DictReader(bruh)
    Education = {}
    for row in reader:
        try:
            Education[row["Education"]] += 1
        except:
            Education[row["Education"]] = 1
    # Creating dataset
    
    explode = [random.randrange(0,3)/10 for i in range(6)]
    # Creating plot
    fig = plt.figure(figsize =(10, 7))
    plt.pie([i for i in Education.values()], labels = Education.keys(),explode=explode, shadow=True)
    
    # show plot
    plt.show()