import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import seaborn as sns

def plot_category_over_time(input_path="./data/categorized.csv", output_path="src/assets/category_over_time.png"):
    df = pd.read_csv(input_path)
    df['creation_date'] = pd.to_datetime(df['creation_date'], errors='coerce')
    df['year'] = df['creation_date'].dt.year
    df = df[df['year'].notna()]
    
    timeline = df.groupby(['year', 'category']).size().unstack().fillna(0)

    plt.figure(figsize=(12, 6))
    timeline.plot(marker='o')
    plt.title("Category Trends Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Posts")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f" Category-over-time chart saved to {output_path}")


def plot_category_distribution(input_path="./data/categorized.csv", output_path="src/assets/category_distribution.png"):
    df = pd.read_csv(input_path)
    category_counts = df['category'].value_counts()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=category_counts.index, y=category_counts.values)
    plt.title("Post Distribution by Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Posts")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f" Category distribution chart saved to {output_path}")

def generate_wordcloud(input_path="./data/preprocessed.csv", output_image_path="src/assets/wordcloud.png"):
    df = pd.read_csv(input_path)
    text = " ".join(df["clean_title"].dropna().tolist())

    wordcloud = WordCloud(
        width=1000,
        height=600,
        background_color="white",
        max_words=200
    ).generate(text)

    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

    plt.figure(figsize=(12, 7))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_image_path)
    print(f" WordCloud image saved to {output_image_path}")

if __name__ == "__main__":
    generate_wordcloud()
