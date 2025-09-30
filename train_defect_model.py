# train_defect_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
import pickle

# Step 1: Load dataset
df = pd.read_csv("cleaned_dataset.csv")

# Features and target
X = df[['LOC', 'Cyclomatic_Complexity', 'Maintainability_Index', 'PEP8_Violations', 'Security_Issues']]
y = df['Defect_Prone']

# Step 2: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Step 3: Define models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost": XGBClassifier(eval_metric='logloss', random_state=42),
    "LightGBM": LGBMClassifier(random_state=42)
}

# Step 4: Train and evaluate each model
results = []
for name, model in models.items():
    print(f"\nTraining {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy: {acc}")
    print(f"Classification Report for {name}:\n{classification_report(y_test, y_pred)}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")

    results.append({
        "Model": name,
        "Accuracy": acc,
        "Precision": prec,
        "Recall": rec,
        "F1-score": f1
    })

    # Save the best model (Random Forest for now)
    if name == "Random Forest":
        with open("defect_prediction_model.pkl", "wb") as f:
            pickle.dump(model, f)

# Step 5: Create a performance comparison table
results_df = pd.DataFrame(results)
results_df.to_csv("model_comparison_results.csv", index=False)
print("\nModel comparison saved to model_comparison_results.csv")
print(results_df)
