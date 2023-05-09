import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('DDS-test.csv')

# Pivot the data to get it in a matrix format
drowsiness_pivot = data.pivot_table(index='Region', columns='ID', values='Drowsiness detected (Times)')
alarm_pivot = data.pivot_table(index='Region', columns='ID', values='Alarm triggered (times)')

# Draw the heatmaps
fig, ax = plt.subplots(2, 1, figsize=(15,10))

sns.heatmap(drowsiness_pivot, ax=ax[0], cmap="YlGnBu")
ax[0].set_title('Drowsiness Detection by Region')

sns.heatmap(alarm_pivot, ax=ax[1], cmap="YlGnBu")
ax[1].set_title('Alarm Triggers by Region')

plt.tight_layout()
plt.show()
