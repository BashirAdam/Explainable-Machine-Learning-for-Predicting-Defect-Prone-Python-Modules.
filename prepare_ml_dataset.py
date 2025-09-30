import pandas as pd

# Load dataset
df = pd.read_csv("static_analysis_dataset.csv")

# Step 1: Create defect-prone label
df['Defect_Prone'] = df['Pylint_Score'].apply(lambda x: 1 if x < 5.0 else 0)

# Step 2: Select features for ML
ml_df = df[['LOC', 'Cyclomatic_Complexity', 'Maintainability_Index',
            'PEP8_Violations', 'Security_Issues', 'Defect_Prone']]

# Step 3: Save cleaned dataset
ml_df.to_csv("cleaned_dataset.csv", index=False)

print("Cleaned dataset created and saved as cleaned_dataset.csv")
print("\nDefect-prone files count:")
print(ml_df['Defect_Prone'].value_counts())
