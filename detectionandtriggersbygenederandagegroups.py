import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('DDS-test.csv')

# Create age groups
bins = [20, 30, 40, 50, 60, 70]
labels = ['20-29', '30-39', '40-49', '50-59', '60+']
data['Age Group'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Create plots
fig, ax = plt.subplots(2, 1, figsize=(15,10))

sns.barplot(x='Age Group', y='Drowsiness detected (Times)', hue='Gender', data=data, ax=ax[0])
ax[0].set_title('Drowsiness Detection by Gender and Age Group')

sns.barplot(x='Age Group', y='Alarm triggered (times)', hue='Gender', data=data, ax=ax[1])
ax[1].set_title('Alarm Triggers by Gender and Age Group')

plt.tight_layout()
plt.show()
