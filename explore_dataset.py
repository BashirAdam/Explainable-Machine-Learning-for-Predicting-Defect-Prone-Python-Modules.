import pandas as pd

# Load your dataset
df = pd.read_csv("static_analysis_dataset.csv")

# Show basic info
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nPreview of Dataset:")
print(df.head())

# Check for missing values
print("\nMissing Values per Column:")
print(df.isnull().sum())

# Summary statistics for numeric columns
print("\nSummary Statistics:")
print(df.describe())
