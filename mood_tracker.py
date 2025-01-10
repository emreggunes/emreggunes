import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Load the dataset
file_path = '/mnt/data/Mood_Tracker_Data.xlsx'
df = pd.ExcelFile(file_path).parse('Sheet1')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Handle missing and infinite values
df.replace([float('inf'), -float('inf')], float('nan'), inplace=True)
df.dropna(inplace=True)

# Correlation of Metrics with Mood (Bar Chart)
correlation_matrix = df.drop(columns=['Date']).corr()
mood_correlation = correlation_matrix['Mood (1-10)'].sort_values(ascending=False)
plt.figure(figsize=(10, 6))
mood_correlation.drop("Mood (1-10)").plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Correlation of Metrics with Mood', fontsize=14)
plt.ylabel('Correlation Coefficient', fontsize=12)
plt.xlabel('Metrics', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Work Hours and Mood (Scatter Plot with Regression Line)
plt.figure(figsize=(8, 6))
sns.regplot(data=df, x="Work Hours", y="Mood (1-10)", scatter_kws={"color": "blue", "s": 50}, line_kws={"color": "red"})
plt.title("Relationship Between Work Hours and Mood", fontsize=14)
plt.xlabel("Work Hours", fontsize=12)
plt.ylabel("Mood (1-10)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Sleep Hours and Mood (Scatter Plot with Regression Line)
plt.figure(figsize=(8, 6))
sns.regplot(data=df, x="Sleep Hours", y="Mood (1-10)", scatter_kws={"color": "green", "s": 50}, line_kws={"color": "red"})
plt.title("Relationship Between Sleep Hours and Mood", fontsize=14)
plt.xlabel("Sleep Hours", fontsize=12)
plt.ylabel("Mood (1-10)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Social Time and Mood (Scatter Plot with Regression Line)
plt.figure(figsize=(8, 6))
sns.regplot(data=df, x="Social Time (Hours)", y="Mood (1-10)", scatter_kws={"color": "orange", "s": 50}, line_kws={"color": "red"})
plt.title("Relationship Between Social Time and Mood", fontsize=14)
plt.xlabel("Social Time (Hours)", fontsize=12)
plt.ylabel("Mood (1-10)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Weekly Process for Screen Time Compared with Mood (Time Series Plot)
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Screen Time (Hours)'], label="Screen Time (Hours)", marker='o')
plt.plot(df['Date'], df['Mood (1-10)'], label="Mood (1-10)", marker='s')
plt.title("Weekly Process of Screen Time and Mood", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Steps and Mood (Boxplot)
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="Mood (1-10)", y="Steps", palette="pastel")
plt.title("Distribution of Steps Across Different Mood Levels", fontsize=14)
plt.xlabel("Mood (1-10)", fontsize=12)
plt.ylabel("Steps", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Regression Analysis Coefficients (Bar Chart)
X = df.drop(columns=['Date', 'Mood (1-10)'])
y = df['Mood (1-10)']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
coefficients = model.params[1:]
variables = coefficients.index
plt.figure(figsize=(10, 6))
coefficients.plot(kind='bar', color='teal', edgecolor='black')
plt.title("Regression Coefficients for Mood Analysis", fontsize=14)
plt.xlabel("Variables", fontsize=12)
plt.ylabel("Coefficient Value", fontsize=12)
plt.axhline(0, color='red', linestyle='--', linewidth=1)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
