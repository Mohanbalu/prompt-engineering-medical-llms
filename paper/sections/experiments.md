# Experiments

This section describes the execution of the prompting experiments, the evaluation environment, and the procedural steps followed to benchmark Gemini 2.0 Flash across seven prompting strategies. All experiments were conducted using the automated pipeline described in the Methods section to ensure consistency and reproducibility.

---

## 1. Experimental Setup

### 1.1 Hardware & Environment
All experiments were run on a standard personal computer with:

- Intel/AMD CPU  
- 8–16 GB RAM  
- Windows operating system  
- Python 3.10 virtual environment  

No GPU was required, as all inference was performed using the cloud-based Gemini API.

### 1.2 Software Dependencies
The following key Python libraries were used:

google-generativeai
pandas
matplotlib

Dependencies were installed via `pip` and the environment was managed using a local virtual environment (`venv/`).

### 1.3 Model & API Keys
The Gemini 2.0 Flash model was used for all experiments.  
To address strict free-tier rate limits, a **multi-API key rotation** system was implemented:

- When an API key hit usage quota → switch automatically to next key  
- Prevents interruptions and ensures the experiment finishes  
- Eliminates manual reruns during long evaluations  

This mechanism ensured uninterrupted execution of all prompts.

---

## 2. Execution Pipeline

The experiments were conducted using the `run_experiment.py` script, which performs the following sequence for each prompting strategy:

1. Load the dataset  
2. Load the selected prompt template  
3. Insert the question into the template  
4. Query the Gemini model  
5. Extract A/B/C/D from the output  
6. Detect hallucinations  
7. Save results to CSV  

Each prompt type produces its own timestamped CSV file in the `results/` directory.

### 2.1 Self-Consistency Runs
For the self-consistency prompt, each question was queried **three times**, and a majority vote determined the final answer.

This allowed evaluation of Gemini’s reasoning stability under repeated sampling.

---

## 3. Prompt Types Tested

The following prompting strategies were executed:

1. **Zero-Shot** – baseline evaluation  
2. **Instruction-Heavy** – strongest rules enforced  
3. **Few-Shot** – examples provided  
4. **Chain-of-Thought (CoT)** – stepwise reasoning  
5. **Self-Consistency (3 samples)** – majority voting  
6. **Self-Verification** – model checks its own uncertainty  
7. **Safety-Constrained Prompt** – prevents hallucination and restricts guesses  

Each prompt targets a different reasoning pathway, allowing comparison of both accuracy and hallucination behavior.

---

## 4. Output Logging

For every question and prompt:

- The raw model response  
- Extracted answer  
- Correctness label  
- Hallucination flag  
- Timestamp  

were recorded.  
This ensures complete transparency and supports manual auditing.

---

## 5. Visualization

After all experiments finished, the `visualize.py` script generated:

- **Accuracy comparison** (`accuracy.png`)  
- **Hallucination rate comparison** (`hallucination.png`)  

These visual outputs are used directly in the Results section of the paper.

---

## 6. Experiment Duration

Because of API rate limits, delays, and multi-key rotation, the full experiment (all questions × 7 prompts) typically completed in:

- **12–20 minutes**, depending on  
  - API key availability  
  - network speed  
  - occasional backoff delays  

Self-consistency runs required additional time due to repeated sampling.

---

## 7. Reproducibility & Reruns

The experiment can be re-run at any time by executing:

python run_experiment.py

Since prompts, dataset, and scripts are all version-controlled, the results will be reproducible, apart from minor randomness in self-consistency samples.

---

## 8. Summary

These experiments tested a range of prompting strategies using a robust, automated, and quota-tolerant pipeline. The generated results form the foundation for the accuracy and hallucination analysis presented in the Results section of the paper.
