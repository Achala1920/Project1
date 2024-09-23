import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("health_data.csv")
print(df)
# Summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Checking for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Data type information
print("\nData Types:")
print(df.dtypes)

#Converting data[age]
df['age'] = (df['age'] / 365).astype(int)
print(df)
df.to_csv("cardiovascular_dataset.csv")

#View all duplicate rows
duplicates = df.duplicated()
duplicate_rows = df[duplicates]

# Print or inspect duplicate rows
print(duplicate_rows)





