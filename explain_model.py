import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load model and data
model = joblib.load("defect_prediction_model.pkl")
df = pd.read_csv("cleaned_dataset.csv")

# Separate features and target
X = df[['LOC', 'Cyclomatic_Complexity', 'Maintainability_Index', 'PEP8_Violations', 'Security_Issues']]

# Create SHAP explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# Summary plot
shap.summary_plot(shap_values, X, plot_type="bar")

# Individual prediction explanation
sample_index = 0
shap.force_plot(explainer.expected_value[1], shap_values[1][sample_index], X.iloc[sample_index], matplotlib=True)
plt.show()
