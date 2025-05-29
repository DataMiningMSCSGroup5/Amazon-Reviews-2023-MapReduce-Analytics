#!/usr/bin/env python
"""
Extract review_id, rating, and cleaned text – one TSV line per review.
Works for both 2018 and 2023 Amazon dumps.
"""

from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol
import json, re

TEXT_KEYS = ("text", "reviewText", "review_body")  # try in this order

class ExtractReviewText(MRJob):
    OUTPUT_PROTOCOL = RawValueProtocol

    def mapper(self, _, line):
        rec = json.loads(line)

        # -------- text field --------
        text_raw = next((rec[k] for k in TEXT_KEYS if k in rec), "")
        text = re.sub(r"\s+", " ", str(text_raw)).strip()
        if not text:
            return                               # skip blanks

        # -------- other fields --------
        rid     = rec.get("review_id") or f"{rec.get('parent_asin')}_{rec['timestamp']}"
        rating  = rec.get("rating")     or rec.get("overall")
        if rating is None:                       # safety net
            return

        safe = text.replace("\t", " ")           # keep TSV aligned
        yield None, f"{rid}\t{rating}\t{safe}"

if __name__ == "__main__":
    ExtractReviewText.run()
