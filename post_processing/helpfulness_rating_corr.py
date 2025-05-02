"""
Compute Pearson correlation and scatter plot between helpfulness and rating.
Input: rating_help.tsv from MR job.
"""
import pandas as pd, matplotlib.pyplot as plt, pathlib
from scipy.stats import pearsonr

df = pd.read_csv("output/rating_help.tsv", sep="\t",
                 names=["rating","help"])
r, p = pearsonr(df["rating"], df["help"])
print(f"Pearson r = {r:.3f} (p={p:.2e})")

sample = df.sample(min(10000, len(df)))
sample.plot.scatter(x="rating", y="help", alpha=0.2)
plt.title("Helpfulness vs Rating")
plt.tight_layout()
fig_path = pathlib.Path("figs/help_vs_rating.png")
fig_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(fig_path, dpi=300)
print("Saved", fig_path)
