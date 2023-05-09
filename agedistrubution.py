import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('DDS-test.csv')

plt.figure(figsize=(10,6))
sns.histplot(data=data, x="Age", bins=10, kde=True)
plt.title('Age Distribution among Participants')
plt.show()

