import os
import pandas as pd

RESULTS_DIR = "results"
OUT_DIR = "analysis"
os.makedirs(OUT_DIR, exist_ok=True)

def load_all_results():
    """Load all CSV result files from results/ folder."""
    files = [f for f in os.listdir(RESULTS_DIR) if f.endswith(".csv")]

    all_data = []
    for file in files:
        path = os.path.join(RESULTS_DIR, file)
        df = pd.read_csv(path)

        # Extract prompt name from filename
        df["file_name"] = file
        df["prompt_type"] = df["prompt_type"].astype(str)

        all_data.append(df)

    return pd.concat(all_data, ignore_index=True)


def compute_stats(df):
    """Compute accuracy and hallucination stats for each prompt."""
    stats = []

    for prompt in df["prompt_type"].unique():
        sub = df[df["prompt_type"] == prompt]

        total = len(sub)
        correct = sub["correct"].sum()
        halluc = sub["hallucination"].sum()

        stats.append({
            "prompt": prompt,
            "total_questions": total,
            "correct": correct,
            "incorrect": total - correct,
            "accuracy_%": round((correct / total) * 100, 2),
            "hallucinations": halluc,
            "hallucination_rate_%": round((halluc / total) * 100, 2)
        })

    return pd.DataFrame(stats)


def save_summary(stats_df):
    """Save a readable text summary for the research paper."""
    summary_path = os.path.join(OUT_DIR, "summary.txt")

    with open(summary_path, "w") as f:
        f.write("=== LLM MEDICAL DIAGNOSIS – PROMPT PERFORMANCE SUMMARY ===\n\n")

        for _, row in stats_df.iterrows():
            f.write(f"Prompt       : {row['prompt']}\n")
            f.write(f"Total Qs     : {row['total_questions']}\n")
            f.write(f"Correct      : {row['correct']}\n")
            f.write(f"Incorrect    : {row['incorrect']}\n")
            f.write(f"Accuracy     : {row['accuracy_%']}%\n")
            f.write(f"Hallucinated : {row['hallucinations']}\n")
            f.write(f"Halluc. Rate : {row['hallucination_rate_%']}%\n")
            f.write("----------------------------------------------------------\n")

    print(f"\n📄 Summary saved to: {summary_path}")


def main():
    print("Loading results...")
    df = load_all_results()

    print("Computing statistics...")
    stats_df = compute_stats(df)

    print("\n=== PERFORMANCE TABLE ===")
    print(stats_df.to_string(index=False))

    out_csv = os.path.join(OUT_DIR, "prompt_performance.csv")
    stats_df.to_csv(out_csv, index=False)
    print(f"\n📊 Prompt statistics saved to: {out_csv}")

    save_summary(stats_df)


if __name__ == "__main__":
    main()
