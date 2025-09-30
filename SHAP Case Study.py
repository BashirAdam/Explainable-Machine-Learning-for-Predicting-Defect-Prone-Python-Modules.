import shap
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")

# Split data
X = df.drop("Defect_Prone", axis=1)
y = df["Defect_Prone"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load trained model
with open("defect_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize SHAP explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer(X_test)

# Check shape to understand dimensions
print("SHAP values shape:", shap_values.values.shape)  
# Expected shape: (number_of_samples, number_of_features, number_of_classes)

# Select the first test sample
sample_index = 0  

# ✅ Fix: Select 1 sample, all features, class index 1 (defect-prone)
shap.plots.waterfall(shap_values[sample_index, :, 1])

# Optional: Display the actual feature values for this sample
print("Example sample features:\n", X_test.iloc[sample_index])
