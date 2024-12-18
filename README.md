# LLM_Project

## Motivation

Legal data plays a crucial role in decision-making, policy formulation, and justice dispensation. However, its complexity often hinders accessibility and effective use. This project aims to leverage the capabilities of large language models (LLMs) to collect, process, and analyze legal data. By doing so, the project provides insights into legal precedents, improves access for legal professionals, and facilitates innovations like automated legal advice.

### The initiative includes:
- Data collection and preprocessing.
- Prompt engineering and fine-tuning of LLMs.
- Feature extraction and summarization for structured legal datasets.

## Research Objective

The primary goal is to develop a global dataset for the legal domain enriched with insights obtained from legal cases. This includes automated analysis and annotation of legal texts, identifying active/passive agents, moral decisions, legal principles, and relationships.

### Applications:
- Cross-jurisdictional pattern discovery.
- Comparative legal studies.
- AI-based legal decision predictions and compliance analysis.

## Methodology

### 1. Domain Understanding
The project started with extensive research, including:
- Insights from legal professionals.
- Analysis of real-world cases on forums like Reddit and Quora.
- Understanding variability in legal interpretations across jurisdictions.

### 2. Data Collection
Raw legal data was extracted from Reddit subreddits across multiple countries (India, UK, Canada, etc.) using a custom Python script. Data format:
- Title
- Case Text
- Upvote Ratio

### 3. Feature Extraction
Key features extracted using LLMs:
- Active Agent
- Passive Agent
- Action Done by Active Agent
- Domain
- Ethical Issues
- Consequences (severity, utility, duration)
- Moral Intentions
- Ethical Principles Upheld/Violated
- Relationship Between Agents
- Moral Decision

### 4. Summarization
Cases were summarized using a predefined template for accuracy:
The <active agent> did <action> to <passive agent> which led to <consequence>. The <active agent> had <good/bad/neutral> moral intention, however, the <action> violated <ethical principle> which caused <ethical issue>.


### 5. Augmentation
Data augmentation techniques were used to generate multiple instances of legal cases by varying:
- Context
- Agents
- Ethical issues

### 6. Validation
Results from Llama-3 were validated using Gemma LLM with additional feedback. This ensured accuracy and consistency.

## Problems and Solutions

### Compute Resource Limitations
**Solution**: Used Kaggle's free GPU access for computational tasks.

### Access to High-Quality Models
**Solution**: Utilized Together.ai for affordable API access.

### Prompt Engineering Challenges
**Solution**: Refined prompts through legal case analysis and manual feature extraction.

### Model Hallucination
**Solution**: Split data into smaller packets to refresh LLMs and avoid memory issues.

### Limited Augmentation Diversity
**Solution**: Enhanced prompts to specify diverse domains explicitly.

### Irrelevant Validation Comments
**Solution**: Cross-validation using Gemma LLM for consistent evaluation.

## Conclusion

This project successfully developed a structured, LLM-aided legal dataset. The output includes:
- Feature extraction for key legal entities.
- Case summaries.
- Tools for data augmentation and evaluation.

This dataset provides a foundation for legal research, comparative studies, and AI-based decision-making in the legal domain.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Kaggle API
- Together.ai API Key

### Dependencies
Install required libraries:

pip install pandas spacy tqdm json re togetherai
### Usage
Feature Extraction
Run the feature extraction script:


python feature_extraction.py
Summarization
Summarize case texts:

python summarization.py
Evaluation
Validate and rate summaries and features:

python evaluation.py

Augmentation
Generate augmented cases:
python augmentation.py

## Outputs
-Extracted Features: feature_extraction.csv
-Summaries: summary.csv
-Evaluated Data: evaluated_data.json
-Augmented Cases: augmented_cases.json

## References
Dataset Generation in LLMs
LegalLens: Violation Identification

## Acknowledgements
Guidance by Dr. Raghava and Ms. Aisha.
Kaggle for computational resources.
Together.ai for API access.
