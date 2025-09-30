import pandas as pd

# Load the updated CSV
df = pd.read_csv("static_analysis_dataset.csv")

# Show Pylint score summary
print("Pylint Score Summary:")
print(df['Pylint_Score'].describe())

# Optional: Check first 10 rows to verify data
print("\nFirst 10 rows:")
print(df[['project', 'file', 'Pylint_Score']].head(10))
