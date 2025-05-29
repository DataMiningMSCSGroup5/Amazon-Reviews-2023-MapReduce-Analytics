from mrjob.job import MRJob
import json
from typing import Iterator, Tuple

class CountReviews(MRJob):
    """Count number of reviews per parent_asin."""

    def mapper(self, _, line: str) -> Iterator[Tuple[str, int]]:
        """Yield (parent_asin, 1) for each review."""
        try:
            rec = json.loads(line)
            asin = rec.get("parent_asin")
            if asin is not None:
                yield asin, 1
        except Exception:
            return

    def combiner(self, asin: str, counts: Iterator[int]) -> Iterator[Tuple[str, int]]:
        yield asin, sum(counts)

    def reducer(self, asin: str, counts: Iterator[int]) -> Iterator[Tuple[str, int]]:
        yield asin, sum(counts)

if __name__ == "__main__":
    CountReviews.run()
