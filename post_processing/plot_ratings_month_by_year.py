import json
import matplotlib.pyplot as plt
import seaborn as sns
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

df["year"] = df["month"].str[:4]
df["only_month"] = df["month"].str[-2:]

# Create pivot table: rows = year, columns = month
pivot = df.pivot_table(values="average_rating", index="year", columns="only_month", aggfunc="mean")

# Optional: sort columns in calendar order
pivot = pivot[[f"{i:02}" for i in range(1, 13)]]

# Plot as heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(pivot, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=0.5, linecolor='gray')
plt.title("Heatmap of Average Ratings by Year and Month")
plt.xlabel("Month")
plt.ylabel("Year")
plt.tight_layout()
plt.savefig("average_ratings_year_and_month_heatmap.png")
plt.show()