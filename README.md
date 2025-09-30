# Explainable Machine Learning for Predicting Defect-Prone Python Modules Using Static Analysis Metrics  

## 📌 Overview  
This repository contains the code, dataset preparation scripts, and experimental results for the paper:  

**Explainable Machine Learning for Predicting Defect-Prone Python Modules Using Static Analysis Metrics**  

The project explores how static analysis metrics (complexity, maintainability, style violations, and security issues) can be combined with explainable machine learning (XAI) to predict defect-prone Python modules.  

We evaluate multiple machine learning models — **Logistic Regression, Random Forest, XGBoost, and LightGBM** — and use **SHAP (SHapley Additive Explanations)** to interpret predictions globally and locally.  

---

## 📂 Repository Structure  
├── data/
│ ├── python_projects/ # Cloned Python projects used for analysis
│ ├── static_analysis_dataset.csv # Raw extracted dataset
│ └── cleaned_dataset.csv # Final dataset for ML
│
├── scripts/
│ ├── Extract_Static_Metrics.py # Runs Radon, Pylint, Flake8, Bandit to extract metrics
│ ├── prepare_ml_dataset.py # Creates defect-prone labels and cleaned dataset
│ ├── train_defect_models.py # Trains Logistic Regression, RF, XGBoost, LightGBM
│ ├── explain_model.py # Global SHAP explanations
│ └── shap_case_study.py # Local SHAP explanation for one file
│
├── figures/
│ ├── Model_Accuracy.png
│ ├── Model_F1Score.png
│ ├── SHAP_Global.png
│ ├── SHAP_Interaction.png
│ └── SHAP_CaseStudy.png
│
├── defect_prediction_model.pkl # Saved trained model
├── model_comparison_results.csv # Results of ML experiments
├── requirements.txt # Python dependencies
└── README.md # This file
## ⚙️ Installation  

Clone the repository:  
```bash
git clone https://github.com/<your-username>/Explainable-Defect-Prediction.git
cd Explainable-Defect-Prediction
pip install -r requirements.txt
📊 Usage
Step 1: Extract Metrics

Run static analysis tools on the selected Python projects:

python scripts/Extract_Static_Metrics.py

Step 2: Prepare Dataset

Label files as defect-prone or not:

python scripts/prepare_ml_dataset.py

Step 3: Train Models

Train and compare ML models:

python scripts/train_defect_models.py

Step 4: Explainability

Generate SHAP visualizations:

python scripts/explain_model.py
python scripts/shap_case_study.py

📈 Results
Model	Accuracy	Precision	Recall	F1-score
Logistic Regression	0.75	0.67	0.75	0.71
Random Forest	0.82	0.83	0.70	0.76
XGBoost	0.82	0.83	0.71	0.76
LightGBM	0.82	0.83	0.71	0.77

LightGBM achieved the best overall performance.

SHAP analysis revealed that Cyclomatic Complexity, LOC, PEP8 Violations, and Security Issues were the most important factors for defect prediction.

🖼 Figures

Figure 1: Model Accuracy Comparison

Figure 2: Model F1-score Comparison

Figure 3: SHAP Global Feature Importance

Figure 4: SHAP Feature Interaction

Figure 5: SHAP Local Case Study
