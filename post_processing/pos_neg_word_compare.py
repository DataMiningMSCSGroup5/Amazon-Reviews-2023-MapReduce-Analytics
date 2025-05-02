"""
Merge positive and negative word count outputs and create CSV diff.
"""
import pandas as pd, pathlib

pos = pd.read_csv("output/words_pos.tsv", sep="\t", header=None, names=["word","pos"])
neg = pd.read_csv("output/words_neg.tsv", sep="\t", header=None, names=["word","neg"])
diff = pos.set_index("word").join(neg.set_index("word"), how="outer").fillna(0).astype(int)
diff.to_csv("output/pos_neg_topwords.csv")
print("Saved output/pos_neg_topwords.csv")
