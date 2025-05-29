"""
Classify sentiment with NLTK VADER.
Input: output/reviews_for_nlp.tsv
Output: output/reviews_with_sentiment.csv, figs/sentiment_dist.png
"""
import pandas as pd, matplotlib.pyplot as plt, nltk, pathlib
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon', quiet=True)
df = pd.read_csv("output/reviews_for_nlp.tsv",
                 sep="\t", names=["rid","rating","text"])

# Ensure text is string and handle missing values
df["text"] = df["text"].fillna("").astype(str)

sia = SentimentIntensityAnalyzer()
df["compound"] = df["text"].apply(lambda t: sia.polarity_scores(t)["compound"])
df["sentiment"] = pd.cut(df["compound"],
                         bins=[-1, -0.05, 0.05, 1],
                         labels=["negative","neutral","positive"])

out_csv = pathlib.Path("output/reviews_with_sentiment.csv")
df.to_csv(out_csv, index=False)

fig_path = pathlib.Path("figs/sentiment_dist.png")
fig_path.parent.mkdir(parents=True, exist_ok=True)
(df["sentiment"].value_counts(normalize=True)*100
    ).loc[["positive","neutral","negative"]].plot.bar(rot=0)
plt.ylabel("% of Reviews")
plt.title("Sentiment Distribution")
plt.tight_layout()
plt.savefig(fig_path, dpi=300)
print("Saved:", out_csv, "and", fig_path)
