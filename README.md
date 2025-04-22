# NLP StackOverflow Categorization Project (ANLP Assignment 2)

This project analyzes and categorizes Stack Overflow posts tagged with [nlp].

## Folder Structure
anlp-assignment-template/ ├── src/ # Source code files for all components │ ├── scraper.py # Collects StackOverflow posts using StackExchange API │ ├── preprocess.py # Cleans and prepares raw text data │ ├── categorize.py # Performs rule-based categorization │ ├── visualize.py # Generates WordCloud and category charts │ └── topic_model.py # Performs topic modeling using LDA │ ├── data/ # Datasets and output CSVs │ ├── nlp_stackoverflow_sample.csv # Raw dataset collected (~6,248 posts) │ ├── preprocessed.csv # Cleaned text after preprocessing │ ├── categorized.csv # Posts with assigned categories │ └── category_summary.csv # Category-wise post count summary │ ├── assets/ # Visual assets (WordClouds, Charts) │ ├── wordcloud.png │ ├── category_distribution.png │ └── category_over_time.png │ ├── requirements.txt # Python dependencies ├── main.py # Runs full processing pipeline end-to-end └── README.md # Project overview and instructions


## How to Run

```bash
# Activate your environment, then run:
python src/main.py
```

### Requirements
Install dependencies with:

```bash
pip install -r requirements.txt
```

> Note: Ensure you have NLTK stopwords and punkt downloaded:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# or you can download: 
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

## Output
- Categorized dataset with ≥100 labeled posts
- WordCloud
- Bar graph of categories
- Topic modeling results
- Category timeline

## Dataset
The dataset used was collected via the StackExchange API and includes ~6,248 posts. You can find the dataset and all outputs here:

[data/nlp_stackoverflow_sample.csv]


## 👩‍💻 Author
**Aeman Fatima** — [a1946845]
