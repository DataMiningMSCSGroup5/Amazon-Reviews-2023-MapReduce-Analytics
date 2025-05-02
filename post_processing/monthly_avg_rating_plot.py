"""
Plot monthly average ratings time series from monthly_avg.tsv
"""
import pandas as pd, matplotlib.pyplot as plt, pathlib

ts = (pd.read_csv("output/monthly_avg.tsv", sep="\t",
                  names=["month","avg"])
        .sort_values("month"))
ts.plot(x="month", y="avg", figsize=(10,4))
plt.xticks(rotation=45)
plt.title("Monthly Average Rating")
plt.tight_layout()
fig_path = pathlib.Path("figs/monthly_avg_rating.png")
fig_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(fig_path, dpi=300)
print("Saved", fig_path)
