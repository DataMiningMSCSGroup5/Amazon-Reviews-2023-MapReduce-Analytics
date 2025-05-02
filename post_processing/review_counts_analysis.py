"""
Load review_counts.tsv -> produce sorted CSV and top-20 bar chart.
Run:
    python post_processing/review_counts_analysis.py
Requires: pandas, matplotlib
"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

in_path = Path("output/review_counts.tsv")
out_csv = Path("output/review_counts_sorted.csv")
fig_path = Path("figs/top20_reviews.png")
fig_path.parent.mkdir(parents=True, exist_ok=True)

df = (pd.read_csv(in_path, sep="\t", names=["parent_asin", "n_reviews"])
        .sort_values("n_reviews", ascending=False))

df.to_csv(out_csv, index=False)

top20 = df.head(20)
top20.plot.barh(x="parent_asin", y="n_reviews", figsize=(10,6))
plt.gca().invert_yaxis()
plt.title("Top-20 Most-Reviewed Products")
plt.tight_layout()
plt.savefig(fig_path, dpi=300)
print("Saved:", out_csv, "and", fig_path)
