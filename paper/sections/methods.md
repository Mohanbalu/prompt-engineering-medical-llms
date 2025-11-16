# Methods

## 1. Dataset

A curated dataset of multiple-choice medical diagnosis questions was constructed to evaluate the reasoning and safety performance of the LLM. The dataset consists of clinically diverse cases covering internal medicine, emergency medicine, cardiology, infectious disease, and neurology. Each question includes:

- A short clinical vignette  
- Four answer choices (A, B, C, D)  
- A single correct answer label  

The dataset was stored in standardized CSV and JSON formats to ensure reproducibility and compatibility with the experimental pipeline. All questions were manually verified to avoid ambiguity, ensure medical correctness, and maintain consistency in answer formatting.

---

## 2. Prompting Strategies

Seven prompting strategies were evaluated to measure their effect on diagnostic accuracy and hallucination rate:

1. **Zero-Shot Prompt**  
   The model receives only the question and answer choices, without any additional instructions.

2. **Instruction-Heavy Prompt**  
   The model is explicitly given step-by-step rules: avoid guessing, use evidence-based reasoning, and output only an A/B/C/D choice or “INSUFFICIENT INFO”.

3. **Few-Shot Prompt**  
   Two high-quality example question–answer pairs are provided before the test question to guide the model.

4. **Chain-of-Thought (CoT)**  
   The model is instructed to reason step-by-step and then output a final A/B/C/D answer.

5. **Self-Consistency Prompt**  
   The model is queried multiple times (three samples) using the same prompt; the final answer is selected by majority vote.

6. **Self-Verification Prompt**  
   The model first provides an internal answer, then re-evaluates its own certainty to detect and suppress potential hallucinations.

7. **Safety Prompt**  
   The model is instructed to prioritize factual correctness, avoid fabrication, and output “INSUFFICIENT INFO” if uncertain.

All prompt templates were stored in a single `prompts.txt` file for version control and reproducibility.

---

## 3. Model Configuration

Experiments were conducted using Google's **Gemini 2.0 Flash** model, accessed through the `google-generativeai` Python SDK. This model was selected because:

- It is lightweight and accessible under free-tier constraints,  
- It offers fast inference suitable for large prompt batches,  
- It provides strong reasoning capabilities relative to its cost.  

Because free-tier usage is subject to strict rate limits, a **multi-API key rotation mechanism** was implemented. When one key reached its quota limit or triggered a 429 rate-limit error, the pipeline automatically switched to the next key without interrupting the experiment.

---

## 4. Experimental Pipeline

A fully automated experiment engine (`run_experiment.py`) was developed. The pipeline performs:

1. **Prompt Construction**  
   Inserts each clinical question into the corresponding prompt template.

2. **Model Execution**  
   Sends each prompt to Gemini 2.0 Flash with built-in:
   - Global request delay to avoid micro-throttling  
   - Quota-aware retry logic  
   - Automatic API-key switching on 429 errors  

3. **Self-Consistency Sampling**  
   For the self-consistency prompt, three independent model outputs are collected and aggregated by majority vote.

4. **Answer Extraction**  
   Answers are parsed from the model’s text output using pattern detection for A/B/C/D choices.

5. **Hallucination Detection**  
   A hallucination is flagged when:
   - The model fails to output A/B/C/D  
   - The output contains additional fabricated details  
   - The answer is non-parsable and does NOT include “INSUFFICIENT INFO”

6. **Logging & Storage**  
   Each response is saved as a CSV file in `results/` with:
   - Prompt type  
   - Model output  
   - Extracted answer  
   - Correctness flag  
   - Hallucination flag  
   - Timestamp  

This ensures a complete record for further auditing and analysis.

---

## 5. Evaluation Metrics

Two primary evaluation metrics were used:

### **5.1 Diagnostic Accuracy**
\[
\text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Questions}}
\]

Accuracy was computed separately for each prompt strategy.

---

### **5.2 Hallucination Rate**
\[
\text{Hallucination Rate} = \frac{\text{Responses Marked as Hallucinations}}{\text{Total Questions}}
\]

A lower hallucination rate indicates safer model behavior, especially in clinical contexts.

---

## 6. Statistical Analysis & Visualization

The `analysis.py` script aggregates all prompt-wise results and computes:

- Total questions per prompt  
- Correct vs. incorrect predictions  
- Accuracy percentage  
- Hallucination count  
- Hallucination percentage  

The visualization script (`visualize.py`) generates two charts:

- **Accuracy comparison bar chart**  
- **Hallucination rate comparison bar chart**

Both charts are exported to the `analysis/charts/` directory and later included in the conference paper.

---

## 7. Reproducibility

To ensure reproducibility:

- All datasets, prompts, scripts, and results are stored in a clear directory structure  
- The model inference script is deterministic except for self-consistency sampling  
- The entire experiment can be re-run end-to-end using the provided Python scripts  
- No proprietary or paid resources were used  

This methodology supports transparent scientific evaluation and facilitates future benchmarking on larger or more complex clinical datasets.
