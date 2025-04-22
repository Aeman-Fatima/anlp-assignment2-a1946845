import requests
import time
import pandas as pd

BASE_URL = "https://api.stackexchange.com/2.3/questions"
SITE = "stackoverflow"
TAG = "nlp"
PAGE_SIZE = 100
MAX_PAGES = 10 

def fetch_questions():
    all_questions = []
    for page in range(1, MAX_PAGES + 1):
        print(f"Fetching page {page}...")
        params = {
            "page": page,
            "pagesize": PAGE_SIZE,
            "order": "desc",
            "sort": "creation",
            "tagged": TAG,
            "site": SITE,
            "filter": "!9_bDE(fI5"
        }
        if API_KEY:
            params["key"] = API_KEY

        response = requests.get(BASE_URL, params=params)
        if response.status_code != 200:
            print(f"Request failed: {response.status_code}")
            break
        data = response.json()
        all_questions.extend(data.get("items", []))

        if not data.get("has_more", False):
            break

        time.sleep(1) 
    return all_questions

def save_to_csv(posts, filename="../data/nlp_stackoverflow_sample.csv"):
    records = []
    for post in posts:
        if "accepted_answer_id" in post:
            records.append({
                "question_id": post.get("question_id"),
                "title": post.get("title", ""),
                "description": post.get("body", ""),
                "tags": ",".join(post.get("tags", [])),
                "accepted_answer_id": post.get("accepted_answer_id"),
                "view_count": post.get("view_count", 0),
                "creation_date": post.get("creation_date")
            })
    df = pd.DataFrame(records)
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} posts to {filename}")

if __name__ == "__main__":
    posts = fetch_questions()
    save_to_csv(posts)
    print("API fetch code is commented out to avoid accidental usage.")
