import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/raw/patient_health.csv")

# Overview of the dataset
print(df.info())
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Visualizing missing values
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Distribution of patient ages
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution of Patients")
plt.show()

# No-show rates per diagnosis
no_show_rates = df.groupby('Diagnosis')['NoShow'].mean()
no_show_rates.sort_values().plot(kind='bar')
plt.title("No-Show Rates by Diagnosis")
plt.show()