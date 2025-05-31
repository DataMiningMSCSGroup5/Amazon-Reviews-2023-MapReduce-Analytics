import json
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd

# Load MapReduce output
month_ratings = defaultdict(list)

with open("output/ratings_per_month.json", "r", encoding="utf-16") as f:
    for line in f:
        # Remove tab separation and parse
        month, ratings = line.strip().split("\t")
        ratings = json.loads(ratings)
        month = month.strip('"')
        month_ratings[month].extend(ratings)

# Convert to DataFrame
data = {
    "month": [],
    "average_rating": []
}

for month in sorted(month_ratings.keys()):
    avg_rating = sum(month_ratings[month]) / len(month_ratings[month])
    data["month"].append(month)
    data["average_rating"].append(avg_rating)

df = pd.DataFrame(data)

df["only_month"] = df["month"].str[-2:]  # Extract MM
monthly_avg = df.groupby("only_month")["average_rating"].mean()

plt.figure(figsize=(10, 5))
monthly_avg.plot(kind="bar", color="skyblue")
plt.xlabel("Month (MM)")
plt.ylabel("Average Rating")
plt.title("Average Rating by Month (Across Years)")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("figs/average_rating_by_month.png")
plt.show()
