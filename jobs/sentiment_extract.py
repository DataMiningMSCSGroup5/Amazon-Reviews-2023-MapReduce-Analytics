from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol
import json, re

class ExtractReviewText(MRJob):
    OUTPUT_PROTOCOL = RawValueProtocol
    def mapper(self, _, line):
        rec = json.loads(line)
        text = re.sub(r"\s+", " ", rec.get("reviewText", "")).strip()
        if text:
            rid = rec.get("review_id") or f"{rec['parent_asin']}_{rec['timestamp']}"
            yield None, f"{rid}\t{rec['rating']}\t{text}"
if __name__ == "__main__":
    ExtractReviewText.run()
