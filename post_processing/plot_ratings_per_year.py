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

# Assuming df["month"] is in "YYYY-MM" format
df["year"] = df["month"].str[:4]  # Extract YYYY

# Group by year and compute average rating
yearly_avg = df.groupby("year")["average_rating"].mean()

# Plotting
plt.figure(figsize=(10, 5))
yearly_avg.plot(kind="bar", color="mediumseagreen")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.title("Average Rating per Year")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("average_rating_per_year.png")
plt.show()

