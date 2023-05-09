import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('DDS-test.csv')




plt.figure(figsize=(10,6))
sns.scatterplot(x='Drowsiness detected (Times)', y='Alarm triggered (times)', data=data)
plt.title('Drowsiness Detection vs. Alarm Triggers')
plt.show()
