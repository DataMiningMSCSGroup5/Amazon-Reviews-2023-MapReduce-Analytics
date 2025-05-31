import pandas as pd
import matplotlib.pyplot as plt
import pathlib

# Load MapReduce output from TSV
data = []
with open("output/helpfulness_by_rating.tsv", "r", encoding="utf-16") as f:
    for line in f:
        rating, avg = line.strip().split("\t")
        data.append((float(rating.strip('"')), float(avg)))

df = pd.DataFrame(data, columns=["rating", "avg_helpful_vote"])

# Plot
plt.figure(figsize=(8, 5))
plt.plot(df["rating"], df["avg_helpful_vote"], marker='o', color='darkorange')
plt.title("Average Helpful Votes per Star Rating (MapReduce)")
plt.xlabel("Star Rating")
plt.ylabel("Average Helpful Votes")
plt.grid(True)
plt.tight_layout()

# Save figure
fig_path = pathlib.Path("figs/avg_helpful_votes_per_rating.png")
fig_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(fig_path, dpi=300)
print("Saved plot to", fig_path)
