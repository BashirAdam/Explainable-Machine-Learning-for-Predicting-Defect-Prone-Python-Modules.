# Explainable Machine Learning for Predicting Defect-Prone Python Modules Using Static Analysis Metrics

This repository contains the full implementation, datasets, and visualizations for the paper:

> **Explainable Machine Learning for Predicting Defect-Prone Python Modules Using Static Analysis Metrics**  
> Submitted to *SoftwareX (Elsevier)* — 2025  

The project integrates static analysis metrics with explainable machine learning models (Random Forest, XGBoost, LightGBM) to predict defect-prone Python modules and provide transparent explanations using SHAP.

---

##  Overview

Software defect prediction helps identify buggy code before release.  
This project:
- Extracts static analysis metrics (complexity, maintainability, style, and security)
- Trains four machine learning models
- Evaluates model performance
- Uses **SHAP** to explain predictions both globally and locally

---

## 📂 Repository Structure

| File / Folder | Description |
|----------------|-------------|
| `python_projects/` | Contains the cloned open-source Python projects used for analysis |
| `Clone Projects.py` | Script to automatically clone selected GitHub repositories |
| `Extract Static Analysis Metrics.py` | Extracts metrics using Radon, Pylint, Flake8, and Bandit |
| `check_pylint.py` | Helper script for collecting maintainability and style metrics |
| `static_analysis_dataset.csv` | Raw metrics extracted from all analyzed files |
| `prepare_ml_dataset.py` | Cleans and merges datasets for ML training |
| `cleaned_dataset.csv` | Cleaned dataset after preprocessing |
| `train_defect_model.py` | Trains ML models (Logistic Regression, Random Forest, XGBoost, LightGBM) |
| `model_comparison_results.csv` | Contains accuracy, precision, recall, and F1-scores of all models |
| `defect_prediction_model.pkl` | Saved trained model (LightGBM) |
| `explain_model.py` | Global SHAP explanation of model predictions |
| `SHAP Case Study.py` | Local SHAP case study for an individual file |
| `Generate Feature Importance Chart.py` | Creates feature importance visualizations |
| `ML Performance Comparison.py` | Generates performance comparison charts |
| `feature_importance.png` | SHAP global importance plot |
| `figure_model_accuracy.png` | Model accuracy comparison |
| `figure_model_f1score.png` | Model F1-score comparison |
| `figure_CC_distribution.png` | Distribution of Cyclomatic Complexity |
| `figure_LOC_distribution.png` | Distribution of Lines of Code (LOC) |
| `static_analysis_dataset.csv` | Dataset containing all metrics |
| `cleaned_dataset.csv` | Preprocessed and balanced dataset for ML models |

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install pandas numpy scikit-learn xgboost lightgbm shap matplotlib seaborn radon pylint flake8 bandit tqdm 
```

---

## How to Run
Run the following scripts in order:
1. Clone Projec
'python "Clone Projects.py"'

