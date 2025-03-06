# Calculate no-show rate per GP practice
no_show_gp = df.groupby("GP_Practice")["NoShow"].mean()
print(no_show_gp)

# Distribution of ages by diagnosis
sns.boxplot(x='Diagnosis', y='Age', data=df)
plt.xticks(rotation=90)
plt.title("Age Distribution by Diagnosis")
plt.show()

# Proportion of male and female patients per diagnosis
gender_distribution = df.groupby(['Diagnosis', 'Gender']).size().unstack()
gender_distribution.plot(kind='bar', stacked=True)
plt.title("Gender Distribution by Diagnosis")
plt.show()