import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")

# Plot LOC distribution
plt.figure(figsize=(8,5))
plt.hist(df['LOC'], bins=50, color='blue', alpha=0.7)
plt.title("Distribution of Lines of Code (LOC)")
plt.xlabel("LOC")
plt.ylabel("Frequency")
plt.savefig("figure_LOC_distribution.png")
plt.show()

# Plot Cyclomatic Complexity distribution
plt.figure(figsize=(8,5))
plt.hist(df['Cyclomatic_Complexity'], bins=50, color='green', alpha=0.7)
plt.title("Distribution of Cyclomatic Complexity")
plt.xlabel("Cyclomatic Complexity")
plt.ylabel("Frequency")
plt.savefig("figure_CC_distribution.png")
plt.show()
