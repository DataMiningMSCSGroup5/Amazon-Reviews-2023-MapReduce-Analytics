import json
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd

# Load MapReduce output
month_ratings = defaultdict(list)

with open("output/ratings_per_month.json", "r", encoding="utf-16") as f:
    for line in f:
        month, ratings = line.strip().split("\t")
        ratings = json.loads(ratings)
        month = month.strip('"')
        month_ratings[month].extend(ratings)

# Create DataFrame
data = {
    "month": [],
    "average_rating": []
}

for month in sorted(month_ratings.keys()):
    avg = sum(month_ratings[month]) / len(month_ratings[month])
    data["month"].append(month)
    data["average_rating"].append(avg)

df = pd.DataFrame(data)

# Extract year and compute yearly average
df["year"] = df["month"].str[:4]
yearly_avg = df.groupby("year")["average_rating"].mean().reset_index()

# Plotting
plt.figure(figsize=(12, 6))

# Bar chart
plt.bar(yearly_avg["year"], yearly_avg["average_rating"], color='mediumseagreen', alpha=0.6, label='Bar: Avg Rating')

# Line plot
plt.plot(yearly_avg["year"], yearly_avg["average_rating"], marker='o', color='blue', linewidth=2, label='Line: Avg Rating')

# Labels and formatting
plt.title("Average Rating per Year (Bar + Line Comparison)")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.legend()
plt.tight_layout()
plt.savefig("figs/average_rating_per_year_with_line.png")
plt.show()
