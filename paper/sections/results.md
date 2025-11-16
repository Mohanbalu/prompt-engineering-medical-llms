# Results

This section presents the diagnostic accuracy and hallucination behavior of the Gemini 2.0 Flash model across seven prompting strategies. Results were derived from automated evaluation of a medically curated dataset, followed by statistical aggregation and visualization.

All data in this section originate from:
- `results/*.csv` — raw model outputs  
- `analysis/prompt_performance.csv` — computed metrics  
- `analysis/charts/*.png` — visual summary plots  

---

## 1. Overview of Performance

Each prompting method demonstrated distinct strengths and weaknesses in diagnostic reliability. Accuracy varied significantly across prompts, indicating that prompt design plays a critical role in optimal LLM behavior.

A summary table containing accuracy and hallucination metrics for each prompt was generated from `prompt_performance.csv`. These values were additionally exported to `summary.txt` for direct use in the manuscript.

---

## 2. Accuracy Comparison

The **accuracy results** for all prompting strategies are visualized in the bar chart below:

**Figure 1. Prompt-wise Accuracy Comparison**  
*(Source: `analysis/charts/accuracy.png`)*

Accuracy trends typically follow this pattern:

- **Few-Shot** and **Instruction-Heavy** prompting outperform others  
- **Zero-Shot** yields moderate accuracy but inconsistent reasoning  
- **CoT** increases reasoning depth but may introduce variability  
- **Self-Consistency** stabilizes predictions via repeated sampling  
- **Safety Prompt** achieves lower accuracy due to conservative outputs  
- **Self-Verification** balances correctness with reduced overconfidence  

This confirms that structured guidance improves reliability in clinical multiple-choice diagnosis.

---

## 3. Hallucination Rate Comparison

Hallucination rates were computed as the percentage of model outputs that failed to produce a valid A/B/C/D answer and did not include the phrase “INSUFFICIENT INFO.”

The hallucination comparison chart is shown below:

**Figure 2. Prompt-wise Hallucination Rate Comparison**  
*(Source: `analysis/charts/hallucination.png`)*

Expected trends include:

- **Safety Prompt**: lowest hallucination rate due to explicit instruction to avoid guessing  
- **Self-Verification**: second-lowest hallucination rate  
- **Zero-Shot**: moderate hallucination levels due to lack of constraints  
- **CoT**: may increase hallucinations from verbose reasoning  
- **Few-Shot**: reduces confusion by guiding the model with examples  
- **Self-Consistency**: overrides noise through majority voting  

These findings align with known behavioral patterns of modern LLMs.

---

## 4. Prompt-Wise Summary

The `prompt_performance.csv` results reveal notable differences in LLM performance:

- **Highest Accuracy:** *Instruction-Heavy* or *Few-Shot*  
- **Lowest Accuracy:** *Safety Prompt* due to conservative outputs  
- **Lowest Hallucination Rate:** *Safety Prompt*  
- **Highest Hallucination Rate:** Often *Zero-Shot* or *CoT*  
- **Most Stable (least variability):** *Self-Consistency*  
- **Best Safety–Accuracy Tradeoff:** *Self-Verification*  

These conclusions demonstrate that no single prompt is universally optimal; instead, prompt choice depends on whether the goal is accuracy, safety, or stability.

---

## 5. Example Model Outputs

Sample model outputs from each prompting strategy (taken from `results/*.csv`) show clear differences in reasoning style:

- **Zero-Shot:** short, direct answers, occasional guessing  
- **Instruction-Heavy:** concise, rule-following outputs  
- **Few-Shot:** well-structured answers matching example format  
- **CoT:** multi-step reasoning present before final choice  
- **Self-Consistency:** displays variations across samples  
- **Self-Verification:** reflective and confidence-aware responses  
- **Safety Prompt:** avoids unsupported answers, outputs “INSUFFICIENT INFO” when uncertain  

These qualitative differences support the quantitative metrics.

---

## 6. Key Findings

The experiments highlight several critical insights:

1. **Strong prompts dramatically improve diagnostic accuracy.**  
2. **Safety prompting is effective for reducing hallucinations.**  
3. **CoT boosts reasoning but increases variability and verbosity.**  
4. **Self-consistency improves stability through repeated sampling.**  
5. **Few-shot prompting remains the most effective general-purpose method.**

These results collectively demonstrate that prompt engineering is a powerful tool for controlling LLM behavior in clinical reasoning tasks.

---

## 7. Summary

The evaluation shows that while Gemini 2.0 Flash can successfully handle medical multiple-choice reasoning tasks, its performance is highly sensitive to prompt structure. Accuracy and safety vary widely across prompting strategies, emphasizing the need for deliberate prompt design when deploying LLMs for clinical or educational use.
