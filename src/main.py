from preprocess import preprocess
from categorize import categorize
from visualize import generate_wordcloud, plot_category_distribution, plot_category_over_time
from topic_model import perform_lda

import nltk
nltk.download('punkt')
nltk.download('punkt_tab') 

def main():
    print("\n Preprocessing...")
    preprocess("./data/nlp_stackoverflow_sample.csv", "./data/preprocessed.csv")

    print("\n Categorizing...")
    categorize("./data/preprocessed.csv", "./data/categorized.csv")

    print("\n Generating WordCloud...")
    generate_wordcloud("./data/preprocessed.csv", "src/assets/wordcloud.png")

    print("\n Plotting category distribution...")
    plot_category_distribution()

    print("\n Plotting category over time...")
    plot_category_over_time()

    print(" Performing LDA Topic Modelling...")
    perform_lda()

if __name__ == "__main__":
    main()
