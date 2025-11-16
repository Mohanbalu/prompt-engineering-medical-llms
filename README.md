# Prompt Engineering for Medical LLMs

This repository contains code for experimenting with different prompt engineering techniques to improve the performance of Large Language Models (LLMs) on medical question answering tasks. It leverages the Gemini 2.0 Flash model through the Google Generative AI API.

## Features and Functionality

*   **Multi-API Key Rotation:** Implements a rotation mechanism across multiple Google Generative AI API keys to mitigate quota limits.
*   **Prompt Engineering Experiments:**  Tests various prompt types, including zero-shot, instruction-heavy, few-shot, chain-of-thought (CoT), self-consistency, self-verification, and safety-focused prompts, on a medical question answering dataset.
*   **Automatic Key Switching and Backoff:**  Handles quota and rate limit errors by automatically switching to the next available API key.
*   **Result Saving:** Saves the results of each experiment to a CSV file in the `results/` directory, including model output, detected answer, correctness, and hallucination status.
*   **Analysis:**  Provides scripts to analyze the experimental results, compute accuracy and hallucination rates for each prompt type, and generate a summary report and visualizations.
*   **Self-Consistency Implementation:** Includes specific handling for the "self-consistency" prompt type, where the model generates multiple responses, and the most frequent answer is selected.

## Technology Stack

*   **Python 3.6+**
*   **pandas:** For data manipulation and analysis.
*   **google-generativeai:** For interacting with the Gemini model.
*   **matplotlib:** For creating visualizations.
*   **os:** For interacting with the operating system.
*   **csv:**  For reading and writing CSV files.
*   **time:** For introducing delays.
*   **datetime:** For generating timestamps.

## Prerequisites

1.  **Python 3.6 or higher:** Make sure you have Python installed.
2.  **Google Generative AI API Key(s):** You need one or more API keys from Google AI Studio.

    *   Go to [makersuite.google.com](https://makersuite.google.com/) and create a project.
    *   Get your API key(s) and add them to the `API_KEYS` list in `run_experiment.py`.
3.  **Install required Python packages:**

    ```bash
    pip install pandas google-generativeai matplotlib
    ```

## Installation Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Mohanbalu/prompt-engineering-medical-llms.git
    cd prompt-engineering-medical-llms
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install pandas google-generativeai matplotlib
    ```

3.  **Configure API Keys:**  Edit `run_experiment.py` and replace the placeholder API keys with your actual keys.  Make sure to have at least one API key.

    ```python
    API_KEYS = [
        "YOUR_API_KEY_1",
        "YOUR_API_KEY_2",
        "YOUR_API_KEY_3"
    ]
    ```

## Usage Guide

1.  **Run the experiments:**

    ```bash
    python run_experiment.py
    ```

    This script will:

    *   Load the medical question answering dataset from `dataset/medical_dataset.csv`.
    *   Load the prompts from `prompts/prompts.txt`.
    *   Iterate through each prompt and question in the dataset.
    *   Query the Gemini model with the formatted prompt.
    *   Extract the answer from the model's response.
    *   Determine if the answer is correct and whether the model hallucinated.
    *   Save the results to a CSV file in the `results/` directory (e.g., `results/zero_shot_20231027_1030.csv`).
    *   Rotate API keys if quota limits are reached.  A delay of 5.5 seconds is implemented between each query to avoid rate limiting.

2.  **Analyze the results:**

    ```bash
    python analysis/analysis.py
    ```

    This script will:

    *   Load all CSV files from the `results/` directory.
    *   Compute accuracy and hallucination statistics for each prompt type.
    *   Print the performance table to the console.
    *   Save the statistics to `analysis/prompt_performance.csv`.
    *   Save a summary report to `analysis/summary.txt`.

3.  **Visualize the results:**

    ```bash
    python analysis/visualize.py
    ```

    This script will:

    *   Load the prompt performance data from `analysis/prompt_performance.csv`.
    *   Generate bar charts comparing the accuracy and hallucination rates for different prompt types.
    *   Save the charts to the `analysis/charts/` directory as `accuracy.png` and `hallucination.png`.

## API Documentation

This project uses the `google-generativeai` library to interact with the Gemini model. Refer to the official [Google Generative AI API documentation](https://ai.google.dev/) for details on the API methods and parameters.  Specifically, the `genai.GenerativeModel.generate_content()` method is used to generate responses from the model.

The `GeminiClient` class in `run_experiment.py` encapsulates the API calls and handles key rotation.

## Contributing Guidelines

Contributions are welcome! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Test your changes thoroughly.
5.  Submit a pull request.

Please ensure your code follows the existing style and includes appropriate comments.

## License Information

This project does not currently have a license specified. All rights are reserved.

## Contact/Support Information

For questions or support, please contact the repository owner through GitHub.