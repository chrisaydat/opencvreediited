import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('DDS-test.csv')
plt.figure(figsize=(10,6))
sns.boxplot(x='Gender', y='Alarm triggered (times)', data=data)
plt.title('Alarm Triggers vs. Gender')
plt.show()
