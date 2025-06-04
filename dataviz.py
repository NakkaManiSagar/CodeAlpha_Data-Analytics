# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
print(os.getcwd())


# Step 2: Load data
df = pd.read_csv("books.csv")

# Step 3: Clean Price column
df['Price'] = df['Price'].replace('Â', '', regex=True)
df['Price'] = df['Price'].replace('£', '', regex=True)
df['Price'] = df['Price'].astype(float)

# Step 4: Set a theme
sns.set(style="whitegrid")

# ----------------- VISUAL 1: Bar Plot -----------------
plt.figure(figsize=(12, 6))
sns.barplot(x='Price', y='Title', data=df, palette='cubehelix')
plt.title("Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.tight_layout()
plt.savefig("barplot.png")
plt.show()

# ----------------- VISUAL 2: Histogram -----------------
plt.figure(figsize=(8, 4))
plt.hist(df['Price'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

# ----------------- VISUAL 3: Box Plot -----------------
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Price"], color='salmon')
plt.title("Box Plot of Book Prices")
plt.xlabel("Price (£)")
plt.tight_layout()
plt.savefig("boxplot.png")
plt.show()

# ----------------- VISUAL 4: Correlation Heatmap -----------------
plt.figure(figsize=(5, 4))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()
