from mrjob.job import MRJob
import json
from typing import Iterator, Tuple

class BinaryHelpfulness(MRJob):
    """Compute the proportion of reviews that were helpful (helpful_votes > 0)."""

    def mapper(self, _, line: str) -> Iterator[Tuple[str, Tuple[int, int]]]:
        try:
            rec = json.loads(line)
            helpful = rec.get("helpful_vote")
            if helpful is not None:
                is_helpful = 1 if helpful > 0 else 0
                yield "all", (1, is_helpful)  # (total_reviews, helpful_reviews)
        except:
            pass

    def combiner(self, key, values):
        total, helpful = 0, 0
        for t, h in values:
            total += t
            helpful += h
        yield key, (total, helpful)

    def reducer(self, key, values):
        total, helpful = 0, 0
        for t, h in values:
            total += t
            helpful += h
        yield "proportion_helpful", round(helpful / total, 4)

if __name__ == "__main__":
    BinaryHelpfulness.run()
