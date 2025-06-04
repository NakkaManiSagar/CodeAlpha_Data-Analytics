# Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load and clean data
df = pd.read_csv('books.csv')

# Clean 'Price' column: remove unwanted characters and convert to float
df['Price'] = df['Price'].replace('Â', '', regex=True)
df['Price'] = df['Price'].replace('£', '', regex=True)
df['Price'] = df['Price'].astype(float)

# Step 3: Display data info
print("First 5 rows of data:")
print(df.head())

print("\nData types and non-null counts:")
print(df.info())

print("\nSummary of data:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# ------------------------- GRAPH 1: BAR PLOT -------------------------
plt.figure(figsize=(12, 6))
sns.barplot(x='Price', y='Title', data=df, palette='viridis')
plt.title('Book Price by Title')
plt.xlabel('Price (£)')
plt.ylabel('Book Title')
plt.tight_layout()
plt.show()

# ------------------------- GRAPH 2: BOX PLOT -------------------------
plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Price'], color='orange')
plt.title('Box Plot of Book Prices')
plt.xlabel('Price (£)')
plt.tight_layout()
plt.show()

# ------------------------- GRAPH 3: HISTOGRAM -------------------------
plt.figure(figsize=(6, 4))
plt.hist(df['Price'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Book Prices')
plt.xlabel('Price (£)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ------------------------- GRAPH 4: CORRELATION HEATMAP -------------------------
plt.figure(figsize=(6, 4))
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
