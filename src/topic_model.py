import pandas as pd
from gensim import corpora, models
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

stop_words = set(stopwords.words("english"))
tokenizer = RegexpTokenizer(r'\b[a-zA-Z]{3,}\b')  # only alphabetic tokens, length ≥3

def clean_text(text):
    tokens = tokenizer.tokenize(text.lower())
    return [t for t in tokens if t not in stop_words]


def perform_lda(input_path="./data/preprocessed.csv", num_topics=5):
    df = pd.read_csv(input_path)
    documents = df["combined_text"].dropna().tolist()
    texts = [clean_text(doc) for doc in documents]

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10, random_state=42)

    print("\n Top Words per Topic:\n")
    for idx, topic in lda_model.show_topics(formatted=False):
        words = ", ".join([word for word, _ in topic])
        print(f"Topic {idx + 1}: {words}")

if __name__ == "__main__":
    perform_lda()
