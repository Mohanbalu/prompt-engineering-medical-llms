# Evaluating Prompting Strategies for Medical Diagnosis Using Gemini 2.0 Flash

**Author:** Mohan  
**Affiliation:** B.Tech Final-Year Student  
**Conference:** (Your conference name here)  
**Year:** 2025  

---

# Abstract

Accurate medical diagnosis using Large Language Models (LLMs) depends heavily on prompt design, especially when models operate under safety constraints and demonstrate varying levels of hallucination. This study evaluates the diagnostic accuracy and hallucination behavior of Google’s Gemini 2.0 Flash model across seven prompting strategies on a curated dataset of multiple-choice medical questions. The evaluated prompts include Zero-Shot, Instruction-Heavy, Few-Shot, Chain-of-Thought (CoT), Self-Consistency, Self-Verification, and Safety-Constrained prompting.

A structured experimental pipeline was developed to ensure reproducibility, incorporating automated prompt execution, multi-API key rotation to overcome rate limits, self-consistency sampling, hallucination detection, and model output evaluation. Results indicate substantial performance differences among prompting methods. Instruction-Heavy and Few-Shot prompting achieved the highest diagnostic accuracy, while Safety-Constrained and Self-Verification prompts showed the lowest hallucination rates. CoT improved reasoning depth but occasionally increased verbosity and non-deterministic answers.

Overall, the findings highlight how careful prompt selection can significantly improve reliability in LLM-based diagnostic systems. The study provides a reproducible framework for future evaluation of medical prompting techniques and demonstrates the feasibility of using lightweight LLMs for clinical-style question answering with controlled hallucinations.

---

# Introduction

Large Language Models (LLMs) have rapidly emerged as powerful tools for clinical reasoning, decision support, and automated medical education. Their ability to analyze patient symptoms, interpret clinical findings, and provide differential diagnoses has opened new possibilities for augmenting physicians and improving access to medical expertise. However, despite their impressive capabilities, LLM outputs remain highly sensitive to prompt design. Minor changes in prompt structure can significantly affect diagnostic accuracy, reasoning depth, and the rate of hallucinations—clinically unsafe responses that present fabricated facts or unwarranted certainty.

Hallucination remains one of the primary barriers preventing LLMs from being deployed in real-world medical environments. Unlike domains such as general knowledge or creative writing, clinical decision-making requires strict factual correctness and consistent reasoning grounded in evidence-based medicine. Therefore, evaluating how different prompting strategies influence hallucination behavior in LLMs is essential for developing reliable medical AI systems.

Previous work has explored broad prompting techniques such as Zero-Shot, Few-Shot, and Chain-of-Thought, but few studies systematically compare advanced safety-aware prompting in the specific context of medical multiple-choice questions. Furthermore, existing research often relies on large proprietary models that are expensive to run or require premium access. This creates a gap in understanding how lightweight, accessible models—especially those available under free-tier constraints—perform in medical diagnostic tasks.

To address this gap, the present study investigates the diagnostic abilities and hallucination tendencies of Google's Gemini 2.0 Flash model across seven prompting strategies: Zero-Shot, Instruction-Heavy, Few-Shot, Chain-of-Thought (CoT), Self-Consistency, Self-Verification, and Safety-Constrained prompting. Using a curated dataset of medical MCQs designed to test clinical reasoning, we analyze how each prompt influences accuracy and hallucination rate. We also implement a reproducible evaluation pipeline that includes self-consistency sampling, hallucination detection, multi-API key rotation to bypass rate limitations, and automated generation of performance metrics and visualizations.

The contributions of this work are threefold:

1. **Comprehensive evaluation of prompting strategies** for medical MCQ diagnosis using a widely accessible LLM.  
2. **A reproducible experimental framework** that integrates data processing, prompt execution, hallucination monitoring, and statistical analysis.  
3. **Insights into the trade-offs between reasoning depth, accuracy, and safety**, providing practical recommendations for designing reliable medical prompts.

---

# Methods

## 1. Dataset

A curated dataset of multiple-choice medical diagnosis questions was constructed to evaluate the reasoning and safety performance of the LLM. The dataset consists of clinically diverse cases covering internal medicine, emergency medicine, cardiology, infectious disease, and neurology. Each question includes a short clinical vignette, four answer choices (A–D), and a single correct answer label.

---

## 2. Prompting Strategies

Seven prompting strategies were evaluated:

1. Zero-Shot  
2. Instruction-Heavy  
3. Few-Shot  
4. Chain-of-Thought  
5. Self-Consistency  
6. Self-Verification  
7. Safety-Constrained  

All prompts were stored in `prompts/prompts.txt`.

---

## 3. Model Configuration

Experiments used **Gemini 2.0 Flash**, chosen for accessibility and speed.  
A **multi-API key rotation system** was implemented to bypass free-tier quota limits.

---

## 4. Experimental Pipeline

The `run_experiment.py` script automates:

- Prompt formatting  
- API querying  
- Retry logic  
- Self-consistency sampling  
- Answer extraction  
- Hallucination detection  
- CSV logging  

---

## 5. Evaluation Metrics

### • Diagnostic Accuracy  
\[
\text{Accuracy} = \frac{\text{Correct}}{\text{Total}}
\]

### • Hallucination Rate  
\[
\text{Hallucination Rate} = \frac{\text{Hallucinations}}{\text{Total}}
\]

---

# Experiments

This study tested all seven prompting strategies on all dataset questions.  
Each prompt type produced a CSV file under `results/`.

Self-consistency prompting ran **three independent samples** per question, with a majority vote selecting the final answer.

Visualization scripts generated accuracy and hallucination charts stored in `analysis/charts/`.

---

# Results

## 1. Accuracy Patterns

From `prompt_performance.csv`, the highest accuracy was achieved by:

- **Instruction-Heavy Prompt**  
- **Few-Shot Prompt**

CoT improved reasoning depth but did not always improve final answer extraction.

---

## 2. Hallucination Trends

Lowest hallucination rates were observed in:

- **Safety-Constrained Prompt**  
- **Self-Verification Prompt**

Zero-Shot and CoT prompting produced higher hallucination rates due to lack of structured guidance.

---

## 3. Figures

**Figure 1. Accuracy Comparison**  
*(analysis/charts/accuracy.png)*  

**Figure 2. Hallucination Rate Comparison**  
*(analysis/charts/hallucination.png)*  

---

# Discussion

Seven prompting strategies demonstrated unique strengths and weaknesses.  
Instruction-Heavy and Few-Shot prompting improved accuracy by reducing ambiguity, while Safety prompting minimized hallucination. Self-Verification offered a balanced trade-off, and Self-Consistency stabilized predictions through repeated sampling.

CoT was beneficial for reasoning visibility but increased output variability, contributing to hallucinations.

---

# Conclusion

Prompt design significantly influences LLM diagnostic performance.  
This study shows that even lightweight models like Gemini Flash can perform reliably with proper prompt engineering.  
Future work includes evaluating larger datasets, comparing multiple LLMs, and exploring automated prompt optimization.

---

# References

(References included separately in `references.bib`)
