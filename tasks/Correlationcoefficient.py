from tkinter import TRUE
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("cardiovascular_dataset.csv")
df = df.drop('id', axis=1)
print(df)

# Correlation Matrix - Internally uses Pearson Correlation
cor = df.corr()

# Plotting Heatmap
plt.figure(figsize = (12,6))
sns.heatmap(cor, annot=True)
plt.show()
