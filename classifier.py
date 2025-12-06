import pandas as pd

CATEGORIES = {
    "hate_speech": ["go back", "these people", "ethnic", "hate"],
    "violence": ["fight", "attack", "burn", "riot"],
    "cyberbullying": ["stupid", "idiot", "useless", "dumb"],
    "fraud": ["send money", "mpesa", "reward", "win", "investment"]
}

def classify_text(text):
    t = text.lower()
    for cat, words in CATEGORIES.items():
        for w in words:
            if w in t:
                return cat
    return "clean"

df = pd.read_csv("tweets.csv")
df["classification"] = df["text"].apply(classify_text)
df.to_csv("classified_tweets.csv", index=False)

print("Classification complete. Saved to classified_tweets.csv")
