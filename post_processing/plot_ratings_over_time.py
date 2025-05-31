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

# Plotting
# Plotting
plt.figure(figsize=(12, 6))
plt.plot(df["month"], df["average_rating"], marker='o')

# Show every 6th month
xticks = df["month"][::6]
plt.xticks(ticks=range(0, len(df["month"]), 6), labels=xticks, rotation=45)

plt.xlabel("Month")
plt.ylabel("Average Rating")
plt.title("Average Rating per Month Over Time")
plt.grid(True)
plt.tight_layout()
plt.savefig("average_rating_over_time.png")
plt.show()

