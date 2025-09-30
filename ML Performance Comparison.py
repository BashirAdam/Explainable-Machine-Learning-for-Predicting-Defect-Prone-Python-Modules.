import pandas as pd
import matplotlib.pyplot as plt

# Load model comparison results
df = pd.read_csv("model_comparison_results.csv")

# Plot accuracy comparison
plt.figure(figsize=(8,5))
plt.bar(df['Model'], df['Accuracy'], color='orange', alpha=0.7)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.savefig("figure_model_accuracy.png")
plt.show()

# Plot F1-score comparison
plt.figure(figsize=(8,5))
plt.bar(df['Model'], df['F1-score'], color='purple', alpha=0.7)
plt.title("Model F1-score Comparison")
plt.ylabel("F1-score")
plt.savefig("figure_model_f1score.png")
plt.show()
