#!/usr/bin/env python
"""
word_counts.py  (improved)

• Emits (word, 1) for reviews filtered by rating polarity.
• Works with 2023 schema ("text") and older ("reviewText").
• Removes punctuation, stop‑words, numbers, and tokens ≤2 chars.
Usage:
    python jobs/word_counts.py               data/*.jsonl.gz > words_all.tsv
    python jobs/word_counts.py --polarity pos data/*.jsonl.gz > words_pos.tsv
    python jobs/word_counts.py --polarity neg data/*.jsonl.gz > words_neg.tsv
"""
from mrjob.job import MRJob
import json, re, string, nltk, unicodedata

# download once per interpreter
nltk.download("stopwords", quiet=True)
STOP = set(nltk.corpus.stopwords.words("english")) | set(string.punctuation)

TOKEN = re.compile(r"[A-Za-z]{3,}")   # ≥3 alpha chars

TEXT_KEYS = ("text", "reviewText", "review_body")

class WordCounts(MRJob):
    def configure_args(self):
        super().configure_args()
        self.add_passthru_arg("--polarity", default="all",
                              help="pos | neg | all (pos=rating>=4, neg=rating<=2)")

    def mapper(self, _, line):
        rec = json.loads(line)
        rating = float(rec.get("rating") or rec.get("overall") or -1)

        pol = self.options.polarity
        if (pol == "pos" and rating < 4) or (pol == "neg" and rating > 2):
            return
        if pol == "neg" and rating == 3:
            return  # neutral row

        text_raw = next((rec.get(k) for k in TEXT_KEYS if k in rec), "")
        for tok in TOKEN.findall(str(text_raw).lower()):
            if tok not in STOP:
                yield tok, 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == "__main__":
    WordCounts.run()