import nltk
nltk.download('vader_lexicon')

import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import matplotlib.pyplot as plt

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Load dataset (assuming JSONL format)
sentiment_counts = Counter()

with open('data/Digital_Music.jsonl', 'r') as file:
    for line in file:
        data = json.loads(line)
        review_text = data.get("text", "")
        if not review_text.strip():
            continue

        scores = sia.polarity_scores(review_text)
        compound = scores["compound"]

        if compound >= 0.05:
            sentiment = "positive"
        elif compound <= -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        sentiment_counts[sentiment] += 1

# Summary (c)
print("Sentiment Distribution:")
for sentiment, count in sentiment_counts.items():
    print(f"{sentiment.title()}: {count}")

# ✅ Now plot the results
plt.bar(sentiment_counts.keys(), sentiment_counts.values(), color=['green', 'gray', 'red'])
plt.title("Sentiment Distribution of Amazon Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.show()