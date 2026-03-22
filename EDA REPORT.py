import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_excel(r"C:\Users\LENOVO\OneDrive\Desktop\clean_tele_data.xlsx")
print(df.head())
df.info()
# GRAPH 1: Churn Distribution
sns.countplot(x='Churn', data=df)
plt.title("Churn Distribution")
plt.show()
# GRAPH 2: Monthly Charges vs Churn
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.show()
# GRAPH 3: Contract vs Churn
sns.countplot(x='Contract', hue='Churn', data=df)
plt.xticks(rotation=30)
plt.title("Contract vs Churn")
plt.show()
# GRAPH 4: Internet Service vs Churn
sns.countplot(x='InternetService', hue='Churn', data=df)
plt.xticks(rotation=30)
plt.title("Internet Service vs Churn")
plt.show()
# GRAPH 5: Tenure vs Churn
sns.boxplot(x='Churn', y='tenure', data=df)
plt.title("Tenure vs Churn")
plt.show()
# GRAPH 6: Correlation Heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()