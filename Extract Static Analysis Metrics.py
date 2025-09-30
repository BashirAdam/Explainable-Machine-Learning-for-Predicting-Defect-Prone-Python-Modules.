import os
import json
import pandas as pd
from tqdm import tqdm
import subprocess
import sys  # Added to call modules via python -m

BASE_DIR = "python_projects"
OUTPUT_CSV = "static_analysis_dataset.csv"

def run_radon(file_path):
    """Run Radon for CC and MI."""
    try:
        # Cyclomatic Complexity
        result = subprocess.run(
            [sys.executable, "-m", "radon", "cc", "-j", file_path],
            capture_output=True,
            text=True
        )
        cc_data = json.loads(result.stdout)
        avg_cc = sum(item['complexity'] for item in cc_data[file_path]) / len(cc_data[file_path]) if cc_data[file_path] else 0
        
        # Maintainability Index
        mi_result = subprocess.run(
            [sys.executable, "-m", "radon", "mi", "-j", file_path],
            capture_output=True,
            text=True
        )
        mi_data = json.loads(mi_result.stdout)
        mi_score = mi_data[file_path]["mi"]
        
        return avg_cc, mi_score
    except Exception:
        return 0, 0

# ---------- FIXED FUNCTION ----------
def run_pylint(file_path):
    """Run pylint and get global score."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pylint", file_path, "-f", "json"],
            capture_output=True,
            text=True
        )
        pylint_data = json.loads(result.stdout.strip())

        # Extract global score correctly
        if isinstance(pylint_data, list):
            for item in pylint_data:
                if isinstance(item, dict) and "score" in item:
                    return item["score"]

        # Fallback to parsing text output if JSON doesn't include the score
        text_result = subprocess.run(
            [sys.executable, "-m", "pylint", file_path],
            capture_output=True,
            text=True
        )
        for line in text_result.stdout.splitlines():
            if "Your code has been rated at" in line:
                try:
                    return float(line.split("rated at")[1].split("/")[0].strip())
                except:
                    return 0
        return 0
    except Exception as e:
        print(f"Pylint error on {file_path}: {e}")
        return 0
# -----------------------------------

def run_flake8(file_path):
    """Run flake8 for PEP8 violations."""
    try:
        result = subprocess.run([sys.executable, "-m", "flake8", file_path], capture_output=True, text=True)
        violations = len(result.stdout.strip().split("\n")) if result.stdout else 0
        return violations
    except:
        return 0

def run_bandit(file_path):
    """Run bandit for security issues."""
    try:
        result = subprocess.run([sys.executable, "-m", "bandit", "-f", "json", "-q", file_path], capture_output=True, text=True)
        bandit_data = json.loads(result.stdout)
        return len(bandit_data.get("results", []))
    except:
        return 0

def analyze_project():
    rows = []
    for project in tqdm(os.listdir(BASE_DIR)):
        project_path = os.path.join(BASE_DIR, project)
        for root, _, files in os.walk(project_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    try:
                        loc = sum(1 for line in open(file_path, encoding="utf-8", errors="ignore"))
                    except:
                        loc = 0
                    cc, mi = run_radon(file_path)
                    pylint_score = run_pylint(file_path)
                    pep8_violations = run_flake8(file_path)
                    security_issues = run_bandit(file_path)

                    rows.append({
                        "project": project,
                        "file": file_path,
                        "LOC": loc,
                        "Cyclomatic_Complexity": cc,
                        "Maintainability_Index": mi,
                        "Pylint_Score": pylint_score,
                        "PEP8_Violations": pep8_violations,
                        "Security_Issues": security_issues
                    })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = analyze_project()
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Dataset saved to {OUTPUT_CSV}")
