import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load positive and negative word counts with UTF-16 encoding
pos = pd.read_csv("output/words_pos.tsv", sep="\t", header=None, names=["word", "pos"], encoding="utf-16")
neg = pd.read_csv("output/words_neg.tsv", sep="\t", header=None, names=["word", "neg"], encoding="utf-16")

# Join on words (outer join to include all words), fill missing values with 0, convert to int
diff = pos.set_index("word").join(neg.set_index("word"), how="outer").fillna(0).astype(int)

# Compute difference
diff["diff"] = diff["pos"] - diff["neg"]

# Sort by difference (optional)
diff = diff.sort_values("diff", ascending=False)

# Save to CSV
diff.to_csv("output/pos_neg_topwords.csv", encoding="utf-8")
print("Saved output/pos_neg_topwords.csv")

df = pd.read_csv("../output/pos_neg_topwords.csv", index_col=0)
# Create frequency dicts
pos_freq = df["pos"].to_dict()
neg_freq = df["neg"].to_dict()

# Positive word cloud
wc_pos = WordCloud(width=800, height=400, background_color="white", colormap="Greens").generate_from_frequencies(pos_freq)
wc_neg = WordCloud(width=800, height=400, background_color="white", colormap="Reds").generate_from_frequencies(neg_freq)

plt.figure(figsize=(20, 12))
plt.subplot(1, 2, 1)
plt.imshow(wc_pos, interpolation="bilinear")
plt.axis("off")
plt.title("Positive Word Cloud")

plt.subplot(1, 2, 2)
plt.imshow(wc_neg, interpolation="bilinear")
plt.axis("off")
plt.title("Negative Word Cloud")

plt.tight_layout()
plt.savefig("figs/wordclouds_pos_neg.png")
plt.show()