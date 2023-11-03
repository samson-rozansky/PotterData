from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("20231103181138_0190.csv")

education = df['Education'].unique()

data = []

ed = df['Education'].value_counts()

for i, value in ed.items():
    data.append(value)


explode = (0.1, 0.1, 0.1, 0.4, 0.2, 0.6)

fig, ax = plt.subplots()
ax.pie(data,
       explode=explode,
       labels=education,
       autopct='%1.1f%%',
       shadow=True,
       startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('sob')
plt.show()