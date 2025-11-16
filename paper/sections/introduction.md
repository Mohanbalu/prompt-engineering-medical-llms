# Introduction

Large Language Models (LLMs) have rapidly emerged as powerful tools for clinical reasoning, decision support, and automated medical education. Their ability to analyze patient symptoms, interpret clinical findings, and provide differential diagnoses has opened new possibilities for augmenting physicians and improving access to medical expertise. However, despite their impressive capabilities, LLM outputs remain highly sensitive to prompt design. Minor changes in prompt structure can significantly affect diagnostic accuracy, reasoning depth, and the rate of hallucinations—clinically unsafe responses that present fabricated facts or unwarranted certainty.

Hallucination remains one of the primary barriers preventing LLMs from being deployed in real-world medical environments. Unlike domains such as general knowledge or creative writing, clinical decision-making requires strict factual correctness and consistent reasoning grounded in evidence-based medicine. Therefore, evaluating how different prompting strategies influence hallucination behavior in LLMs is essential for developing reliable medical AI systems.

Previous work has explored broad prompting techniques such as Zero-Shot, Few-Shot, and Chain-of-Thought, but few studies systematically compare advanced safety-aware prompting in the specific context of medical multiple-choice questions. Furthermore, existing research often relies on large proprietary models that are expensive to run or require premium access. This creates a gap in understanding how lightweight, accessible models—especially those available under free-tier constraints—perform in medical diagnostic tasks.

To address this gap, the present study investigates the diagnostic abilities and hallucination tendencies of Google's Gemini 2.0 Flash model across seven prompting strategies: Zero-Shot, Instruction-Heavy, Few-Shot, Chain-of-Thought (CoT), Self-Consistency, Self-Verification, and Safety-Constrained prompting. Using a curated dataset of medical MCQs designed to test clinical reasoning, we analyze how each prompt influences accuracy and hallucination rate. We also implement a reproducible evaluation pipeline that includes self-consistency sampling, hallucination detection, multi-API key rotation to bypass rate limitations, and automated generation of performance metrics and visualizations.

The contributions of this work are threefold:

1. **Comprehensive evaluation of prompting strategies** for medical MCQ diagnosis using a widely accessible LLM.  
2. **A reproducible experimental framework** that integrates data processing, prompt execution, hallucination monitoring, and statistical analysis.  
3. **Insights into the trade-offs between reasoning depth, accuracy, and safety**, providing practical recommendations for designing reliable medical prompts.

This study demonstrates that prompt engineering plays a critical role in reducing hallucination and improving diagnostic reliability in LLMs. The insights gained may guide future research in clinical AI systems, medical education, and safe deployment of LLM-based diagnostic tools.
