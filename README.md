# NLP StackOverflow Categorization Project (ANLP Assignment 2)

This project analyzes and categorizes Stack Overflow posts tagged with [nlp].

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
