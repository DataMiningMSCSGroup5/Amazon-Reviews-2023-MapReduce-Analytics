from mrjob.job import MRJob
import json
from typing import Tuple, Iterator

class AvgRating(MRJob):
    """Average star rating per parent_asin."""

    def mapper(self, _, line: str) -> Iterator[Tuple[str, Tuple[int, float]]]:
        """Yield (parent_asin, (1, rating)) for each review."""
        try:
            rec = json.loads(line)
            asin = rec.get("parent_asin")
            rating = rec.get("rating")
            if asin is None or rating is None:
                return
            yield asin, (1, float(rating))
        except Exception:
            return

    def combiner(self, asin: str, pairs: Iterator[Tuple[int, float]]) -> Iterator[Tuple[str, Tuple[int, float]]]:
        n, s = 0, 0.0
        for c, r in pairs:
            n += c
            s += r
        yield asin, (n, s)

    def reducer(self, asin: str, pairs: Iterator[Tuple[int, float]]) -> Iterator[Tuple[str, float]]:
        n, s = 0, 0.0
        for c, r in pairs:
            n += c
            s += r
        if n > 0:
            yield asin, round(s / n, 3)
        else:
            yield asin, 0.0

if __name__ == "__main__":
    AvgRating.run()
