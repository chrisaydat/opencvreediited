import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('DDS-test.csv')
plt.figure(figsize=(10,6))
sns.scatterplot(x='Age', y='Drowsiness detected (Times)', data=data)
plt.title('Drowsiness Detection vs. Age')
plt.show()
