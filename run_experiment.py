import pandas as pd
import os
import csv
import time
import random
from datetime import datetime
import google.generativeai as genai

# ====================================================
# 1. MULTI-API KEY SETUP (ROTATION FOR QUOTA LIMITS)
# ====================================================

API_KEYS = [
    "AIzaSyC_pXZYyiNcDWxgzbLAjSJI3CU6Ptm2zW0",
    "AIzaSyBCOIJYWQPXUzbq0eNF_9fO3Njmaacw6VA",
    "AIzaSyAyPlGEedkDkUL3z4ZNgCZmHG8-RyHx1hY"
]

CURRENT_KEY_INDEX = 0

def configure_gemini():
    """Switch to the current API key."""
    genai.configure(api_key=API_KEYS[CURRENT_KEY_INDEX])
    print(f"[USING KEY #{CURRENT_KEY_INDEX+1}]")

configure_gemini()


# ====================================================
# 2. MODEL SETUP (YOUR ACCOUNT SUPPORTS ONLY 2.0 FLASH)
# ====================================================

MODEL_ID = "gemini-2.0-flash"


# ====================================================
# 3. Gemini Client (AUTO KEY SWITCH + BACKOFF)
# ====================================================

class GeminiClient:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model = genai.GenerativeModel(self.model_name)

    def switch_key(self):
        """Switch to next API key and reload model."""
        global CURRENT_KEY_INDEX
        CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(API_KEYS)
        print(f"[ROTATING KEY → Now using KEY #{CURRENT_KEY_INDEX+1}]")
        configure_gemini()
        self.model = genai.GenerativeModel(self.model_name)

    def generate(self, prompt: str) -> str:
        """Generate response with quota handling."""
        MAX_RETRIES = len(API_KEYS)  # each retry tries next key

        for attempt in range(MAX_RETRIES):
            try:
                response = self.model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": 0.2,
                        "max_output_tokens": 512
                    }
                )
                return response.text.strip()

            except Exception as e:
                msg = str(e).lower()

                # QUOTA / RATE LIMIT → SWITCH KEY
                if "quota" in msg or "429" in msg or "rate limit" in msg:
                    print(f"[KEY #{CURRENT_KEY_INDEX+1}] QUOTA HIT → SWITCHING KEY...")
                    self.switch_key()
                    continue

                print("Non-retriable Gemini error:", e)
                return "ERROR"

        print("All API keys exhausted.")
        return "ERROR"


gemini = GeminiClient(MODEL_ID)


# ====================================================
# 4. File Paths
# ====================================================

DATASET_PATH = "dataset/medical_dataset.csv"
PROMPTS_PATH = "prompts/prompts.txt"
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)


# ====================================================
# 5. Load Dataset
# ====================================================

dataset = pd.read_csv(DATASET_PATH)


# ====================================================
# 6. Load Prompts
# ====================================================

def load_prompts():
    with open(PROMPTS_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    blocks = [b.strip() for b in text.split("========") if b.strip()]

    return {
        "zero_shot": blocks[0],
        "instruction_heavy": blocks[1],
        "few_shot": blocks[2],
        "cot": blocks[3],
        "self_consistency": blocks[4],
        "self_verification": blocks[5],
        "safety": blocks[6],
    }

prompts = load_prompts()


# ====================================================
# 7. Format Question
# ====================================================

def format_question(row):
    return (
        f"{row['question']}\n"
        f"A: {row['A']}\n"
        f"B: {row['B']}\n"
        f"C: {row['C']}\n"
        f"D: {row['D']}\n"
    )


# ====================================================
# 8. Extract letter A/B/C/D
# ====================================================

def extract_answer(text: str):
    if not text:
        return None
    segment = text[:25].upper()
    for ch in ["A", "B", "C", "D"]:
        if ch in segment:
            return ch
    return None


# ====================================================
# 9. Query with Delay
# ====================================================

GLOBAL_DELAY = 5.5   # safe for free-tier, avoids 429 bursts

def query_model(prompt: str):
    time.sleep(GLOBAL_DELAY)
    return gemini.generate(prompt)


# ====================================================
# 10. Run Experiment
# ====================================================

def run_experiment(prompt_name, base_prompt):
    print(f"\n=== Running: {prompt_name} ===")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    out_path = f"{RESULTS_DIR}/{prompt_name}_{timestamp}.csv"

    rows = []

    for _, row in dataset.iterrows():
        q_text = format_question(row)
        final_prompt = base_prompt.replace("{QUESTION}", q_text)

        # ---------------------
        # Self-consistency mode
        # ---------------------
        if prompt_name == "self_consistency":
            samples = []
            extracted = []

            for _ in range(3):  # keep at 3 to save quota
                out = query_model(final_prompt)
                samples.append(out)
                extracted.append(extract_answer(out))

            final_answer = (
                max(set(extracted), key=extracted.count)
                if any(extracted) else None
            )

            output = f"SAMPLES={samples}\nVOTE={final_answer}"
            detected = final_answer

        # ---------------------
        # Normal prompts
        # ---------------------
        else:
            out = query_model(final_prompt)
            detected = extract_answer(out)
            output = out

        correct = (detected == row["answer"])
        hallucination = (detected is None and "INSUFFICIENT" not in output)

        rows.append({
            "id": row["id"],
            "prompt_type": prompt_name,
            "question": row["question"],
            "model_output": output,
            "detected_answer": detected,
            "correct_answer": row["answer"],
            "correct": correct,
            "hallucination": hallucination,
            "timestamp": datetime.now().isoformat()
        })

    pd.DataFrame(rows).to_csv(out_path, index=False)
    print(f"Saved → {out_path}")


# ====================================================
# 11. RUN ALL PROMPTS
# ====================================================

for name, prompt in prompts.items():
    run_experiment(name, prompt)

print("\nAll experiments completed using MULTI-API rotation.")
