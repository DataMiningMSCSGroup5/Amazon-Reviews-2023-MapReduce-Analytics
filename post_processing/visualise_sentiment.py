import matplotlib.pyplot as plt
import csv

# Read TSV
sentiments = {}

with open("output/sentiment_results.tsv", "r", encoding="utf-8") as f:
    tsv_reader = csv.reader(f, delimiter="\t")
    for row in tsv_reader:
        if len(row) == 2:
            sentiment = row[0].strip('"')
            try:
                count = int(row[1])
                sentiments[sentiment] = count
            except ValueError:
                continue

# Plot
labels = list(sentiments.keys())
values = list(sentiments.values())
colors = ["red", "gray", "green"]  # Optional: Neg/Neutral/Pos

plt.figure(figsize=(8, 5))
plt.bar(labels, values, color=colors)
plt.title("Sentiment Distribution of Amazon Beauty Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("figs/sentiment_distribution.png")
plt.show()
