import pandas as pd
import matplotlib.pyplot as plt

# Read the TSV
df = pd.read_csv("output/top10_results.tsv", sep="\t", header=None, names=["ASIN", "Reviews"],encoding="utf-16")

# Clean ASIN column (remove quotes if present)
df["ASIN"] = df["ASIN"].str.replace('"', '')

# Sort by number of reviews (descending) for clarity
df = df.sort_values(by="Reviews", ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(df["ASIN"], df["Reviews"], color='skyblue')
plt.xlabel("Product ASIN")
plt.ylabel("Number of Reviews")
plt.title("Top 10 Most Reviewed Products")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figs/top10_reviews.png")
plt.show()
