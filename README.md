# NLP StackOverflow Question Categorizer

Scrapes NLP-tagged questions from Stack Overflow via the StackExchange API, cleans and tokenizes the text, sorts each question into a category with a rule-based classifier, and runs LDA topic modeling on top. Produces a categorized dataset plus a wordcloud, a category bar chart, and a category-over-time chart.

**Stack:** Python · pandas · NLTK · gensim (LDA) · WordCloud · matplotlib/seaborn

## How It Works

1. `src/scraper.py` — pulls `[nlp]`-tagged questions from the StackExchange API
2. `src/preprocess.py` — strips HTML/special characters, lowercases, tokenizes, removes stopwords (NLTK)
3. `src/categorize.py` — rule-based classifier sorting posts into categories (Implementation Issues, Task-Specific NLP, Error Fixes, Library-Specific Problems, Conceptual Understanding, etc.)
4. `src/topic_model.py` — LDA topic modeling over the cleaned corpus (gensim)
5. `src/visualize.py` — wordcloud, category distribution bar chart, category-over-time chart

## How to Run

```bash
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
python src/main.py
```

## Output

- Categorized dataset (~6,248 Stack Overflow posts collected via the StackExchange API)
- Wordcloud
- Bar chart of category distribution
- Topic modeling results
- Category-over-time chart

Dataset: `data/nlp_stackoverflow_sample.csv`
