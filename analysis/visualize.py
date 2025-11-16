import os
import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Paths
# ==========================

PERFORMANCE_CSV = "prompt_performance.csv"
CHART_DIR = "charts"
os.makedirs(CHART_DIR, exist_ok=True)


# ==========================
# Load Data
# ==========================

df = pd.read_csv(PERFORMANCE_CSV)

prompts = df["prompt"]
accuracy = df["accuracy_%"]
halluc_rate = df["hallucination_rate_%"]


# ==========================
# Plot 1: Accuracy Bar Chart
# ==========================

plt.figure(figsize=(10, 6))
plt.bar(prompts, accuracy)
plt.xlabel("Prompt Type")
plt.ylabel("Accuracy (%)")
plt.title("Prompt-wise Accuracy Comparison")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

acc_path = os.path.join(CHART_DIR, "accuracy.png")
plt.savefig(acc_path)
plt.close()

print(f"[+] Saved accuracy chart → {acc_path}")


# ==========================
# Plot 2: Hallucination Rate Bar Chart
# ==========================

plt.figure(figsize=(10, 6))
plt.bar(prompts, halluc_rate)
plt.xlabel("Prompt Type")
plt.ylabel("Hallucination Rate (%)")
plt.title("Prompt-wise Hallucination Rate Comparison")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

hall_path = os.path.join(CHART_DIR, "hallucination.png")
plt.savefig(hall_path)
plt.close()

print(f"[+] Saved hallucination chart → {hall_path}")


print("\nAll charts generated successfully.")
