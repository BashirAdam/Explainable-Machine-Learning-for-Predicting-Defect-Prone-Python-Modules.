import shap
import matplotlib.pyplot as plt
import pandas as pd
import joblib

# Load model and dataset
df = pd.read_csv("cleaned_dataset.csv")
model = joblib.load("defect_prediction_model.pkl")

X = df[['LOC', 'Cyclomatic_Complexity', 'Maintainability_Index',
        'PEP8_Violations', 'Security_Issues']]

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# Bar chart
shap.summary_plot(shap_values, X, plot_type="bar")
plt.savefig("feature_importance.png", bbox_inches="tight")
print("Feature importance chart saved as feature_importance.png")
