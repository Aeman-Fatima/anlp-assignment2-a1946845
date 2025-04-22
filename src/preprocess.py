import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

def clean_text(text):
    text = re.sub(r'<.*?>', '', str(text))  # remove HTML
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # remove special chars
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return ' '.join(tokens)

def preprocess(input_path="./data/nlp_stackoverflow_sample.csv", output_path="./data/preprocessed.csv"):
    df = pd.read_csv(input_path)
    df['clean_title'] = df['title'].apply(clean_text)
    df['clean_description'] = df['description'].apply(clean_text)
    df['combined_text'] = df['clean_title'] + ' ' + df['clean_description']
    df.to_csv(output_path, index=False)
    print(f"✅ Preprocessed data saved to {output_path}")

if __name__ == "__main__":
    preprocess()
