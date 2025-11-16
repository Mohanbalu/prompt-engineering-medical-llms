# Discussion

The experimental results demonstrate that prompting strategy has a substantial impact on the diagnostic accuracy, stability, and hallucination behavior of the Gemini 2.0 Flash model. This section provides deeper analysis of the observed trends, implications for clinical AI usage, and the broader relevance of these findings within the context of LLM safety research.

---

## 1. Impact of Prompt Structure on Diagnostic Accuracy

The results show that **explicit guidance** significantly improves model performance in clinical multiple-choice questions:

- **Instruction-Heavy** and **Few-Shot prompting** achieved the highest accuracy.  
- These prompts reduce ambiguity by clearly specifying expected behavior.  
- Few-shot examples serve as strong priors, helping the model align with clinical reasoning patterns.

This aligns with prior studies showing that structured instructions and contextual examples help LLMs reduce reasoning drift and conform to domain-specific expectations.

---

## 2. Trade-Offs Between Reasoning Depth and Stability

Chain-of-Thought (CoT) prompting produced detailed reasoning, but this depth came at a cost:

- CoT answers were often verbose, making answer extraction more difficult.  
- Long reasoning chains introduced variance, which sometimes reduced accuracy.  
- CoT also produced more hallucinations when reasoning went off track.

Although CoT is valuable for transparency, it is less reliable in environments requiring strict answer formats, such as medical MCQs.

---

## 3. Effectiveness of Self-Consistency and Self-Verification

### 3.1 Self-Consistency  
Self-consistency improved prediction stability by averaging multiple outputs:

- Reduced the impact of noisy or unstable responses  
- Helped override occasional incorrect reasoning  
- Delivered accuracy comparable to Few-Shot prompting  

However, repeated sampling increased execution time and API usage, which may limit scalability.

### 3.2 Self-Verification  
Self-verification showed strong potential for safety:

- The model cross-checked its own prediction  
- Reduced overconfident hallucinations  
- Achieved one of the lowest hallucination rates  

This technique is promising for clinical applications where safety must be prioritized.

---

## 4. Safety vs. Accuracy Trade-Off

The Safety-Constrained prompt yielded the lowest hallucination rate but at the cost of reduced accuracy:

- The model frequently responded with “INSUFFICIENT INFO”  
- This minimized harmful fabrications  
- But also led to missed correct diagnoses  

This result supports the idea that **suppressing hallucinations often reduces output assertiveness**.  
Safety prompts are therefore ideal in systems where avoiding misinformation is more important than maximizing accuracy.

---

## 5. Implications for Medical AI Deployment

These findings highlight key considerations for deploying LLMs in healthcare:

### • Prompt design should be treated as a core safety mechanism  
The wide performance gap across prompts demonstrates that poorly designed prompts can produce unsafe behavior even with advanced models.

### • Accuracy alone is insufficient  
A model with high accuracy but high hallucination risk is unsuitable for clinical use.

### • Balanced prompting strategies may be optimal  
Self-Verification and Few-Shot prompting offer a good blend of accuracy and safety.

### • Lightweight models can perform adequately with good prompts  
Gemini 2.0 Flash, despite being a free-tier model, achieved competitive results under structured prompting.

---

## 6. Limitations

Several limitations should be acknowledged:

1. **Dataset Scale**  
   The study used a small curated dataset of medical MCQs. Larger datasets would improve statistical power.

2. **Domain Breadth**  
   Only general clinical reasoning questions were included; specialized fields may show different trends.

3. **Model Variability**  
   LLM outputs are inherently non-deterministic, especially under chain-of-thought prompting.

4. **Free-Tier API Constraints**  
   Quota limits restricted sample sizes, particularly for self-consistency sampling.

Despite these limitations, the study provides meaningful insights into the interaction between prompts, accuracy, and hallucination behavior.

---

## 7. Future Work

Future research can build on this study by exploring:

- More advanced safety-tuned prompt templates  
- Larger clinical datasets  
- Comparison across multiple LLMs (e.g., GPT-4, Claude, Llama)  
- Use of reinforcement learning or confidence calibration techniques  
- Automated prompt optimization  
- Evaluation on real-world medical vignettes or diagnostic reasoning tasks  

---

## 8. Summary

The experiments reveal a clear conclusion:  
**Prompt engineering significantly influences both the diagnostic capability and safety of LLMs in medical tasks.**

Structured guidance, examples, and self-checking mechanisms can reduce hallucination risk and improve reliability—demonstrating that prompt design is as important as model architecture for trustworthy clinical AI.
