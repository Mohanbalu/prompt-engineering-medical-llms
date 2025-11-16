# 📘 Medical Diagnosis with LLMs: Evaluating Prompt Strategies on Gemini 2.0 Flash

This project evaluates seven prompting strategies for clinical diagnosis tasks using Google’s Gemini 2.0 Flash model.  
The goal is to measure **diagnostic accuracy**, **hallucination rate**, and **reasoning stability** across diverse prompting techniques on a curated medical MCQ dataset.

This project is fully reproducible and designed for **conference publication**.

---

## 🚀 Project Overview

Large Language Models (LLMs) can support clinical reasoning, but their reliability depends heavily on prompt design.  
This study systematically evaluates seven prompting strategies using a unified dataset and a reproducible experiment pipeline.

### Prompt strategies evaluated:
1. Zero-Shot  
2. Instruction-Heavy  
3. Few-Shot  
4. Chain-of-Thought (CoT)  
5. Self-Consistency (3 samples)  
6. Self-Verification  
7. Safety-Constrained Prompt  

The experiments compute:
- **Accuracy**
- **Hallucination Rate**
- **Prompt stability**
- **Multi-sample reasoning (self-consistency)**

---

## 📂 Project Structure

PAPER-2/
│
├── analysis/
│ ├── analysis.py
│ ├── prompt_performance.csv
│ ├── summary.txt
│ ├── visualize.py
│ └── charts/
│ ├── accuracy.png
│ └── hallucination.png
│
├── dataset/
│ ├── medical_dataset.csv
│ └── medical_dataset.json
│
├── prompts/
│ └── prompts.txt
│
├── results/
│ ├── *.csv (one file per prompt type)
│
├── scripts/
│ └── run_experiment.py
│
├── paper/
│ ├── sections/
│ │ ├── abstract.md
│ │ ├── introduction.md
│ │ ├── methods.md
│ │ ├── experiments.md
│ │ ├── results.md
│ │ ├── discussion.md
│ │ └── conclusion.md
│ ├── references.bib
│ └── figures/
│ └── pipeline_diagram.png
│
├── venv/
│
├── README.md
└── requirements.txt

markdown
Copy code

---

## 📊 Evaluation Pipeline

The entire project is powered by the following components:

### ✔ **Dataset Loader**
Reads medical MCQs from CSV format.

### ✔ **Prompt Loader**
Loads all seven prompting templates from a unified `prompts.txt`.

### ✔ **Experiment Engine**
`run_experiment.py` automates:
- Prompt formatting  
- API calls  
- Multi-API key rotation  
- Error handling  
- Self-consistency sampling (majority voting)  
- Answer extraction  
- Hallucination detection  
- CSV export  

### ✔ **Analysis Script**
`analysis.py` generates:
- Accuracy per prompt  
- Hallucination rate per prompt  
- Summary table  
- Final metrics for the paper  

### ✔ **Visualization**
`visualize.py` creates bar charts for:
- Accuracy  
- Hallucination rate  

These visualizations appear in your paper.

---

## 📦 Installation

### 1. Clone the project
git clone https://github.com/<your-repo>/paper-2
cd paper-2

shell
Copy code

### 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate # Windows

shell
Copy code

### 3. Install dependencies
pip install -r requirements.txt

yaml
Copy code

---

## ▶️ Running the Experiments

Run all prompt types:

python run_experiment.py

css
Copy code

All results will be stored in:

results/

yaml
Copy code

---

## 📈 Generate Analysis

python analysis.py

yaml
Copy code

Outputs:

- `analysis/summary.txt`
- `analysis/prompt_performance.csv`

---

## 📊 Generate Charts

python visualize.py

css
Copy code

Charts saved to:

analysis/charts/

yaml
Copy code

---

## 📝 Paper Assembly

Your paper sections (Markdown files) are located in:

paper/sections/

yaml
Copy code

These can be merged into a final PDF using LaTeX, Typst, or Markdown → PDF export.

---

## 🧠 Key Findings (High-Level)

- Instruction-Heavy and Few-Shot prompting yield the highest accuracy  
- Safety prompts minimize hallucination  
- CoT increases reasoning depth but reduces answer stability  
- Self-Verification offers the best safety–accuracy tradeoff  
- Lightweight models can be effective with proper prompting  

---

## 📚 Citation

If you reuse this work, please cite your final conference paper.

---

## 🤝 Contributors

- **Mohan — Lead Researcher & Developer**  
- **ChatGPT — Technical assistant for pipeline, prompts, and paper generation**

---

## 📄 License

This project may be shared for academic and research purposes.