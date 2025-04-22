import pandas as pd

def assign_category(text):
    text = str(text).lower()

    if any(keyword in text for keyword in ["how to", "how do", "implement", "apply", "use", "create", "run", "build"]):
        return "Implementation Issues"
    elif any(keyword in text for keyword in ["tokenize", "lemmatize", "similarity", "summarize", "stem", "classification"]):
        return "Task-Specific NLP"
    elif any(keyword in text for keyword in ["error", "traceback", "fix", "exception", "debug", "issue"]):
        return "Error Fixes"
    elif any(keyword in text for keyword in ["spacy", "nltk", "transformers", "huggingface", "gensim", "word2vec"]):
        return "Library-Specific Problems"
    elif any(keyword in text for keyword in ["what is", "meaning of", "difference between", "define", "explain"]):
        return "Conceptual Understanding"
    else:
        return "Implementation Issues" if "how" in text else "Uncategorized"


def categorize(input_path="./data/preprocessed.csv", output_path="./data/categorized.csv"):
    df = pd.read_csv(input_path)
    df["category"] = df["combined_text"].apply(assign_category)
    df.to_csv(output_path, index=False)
    print(f" Categorised posts saved to {output_path}")

    print("\n Category Breakdown:")
    print(df["category"].value_counts())

    summary = df.groupby("category")["question_id"].apply(list)
    summary.to_csv("./data/category_summary.csv")
    print("\n Category summary saved to category_summary.csv")

if __name__ == "__main__":
    categorize()
