from mrjob.job import MRJob
import json
import datetime
from typing import Tuple, Iterator

class MonthlyAvgRating(MRJob):
    """Average rating per calendar month."""

    def mapper(self, _, line: str) -> Iterator[Tuple[str, Tuple[int, float]]]:
        """Extract month and rating, yield (month, (1, rating))."""
        try:
            rec = json.loads(line)
            timestamp = rec.get("timestamp")
            rating = rec.get("rating")
            if timestamp is None or rating is None:
                return
            month = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime("%Y-%m")
            yield month, (1, float(rating))
        except Exception:
            return

    def combiner(self, month: str, pairs: Iterator[Tuple[int, float]]) -> Iterator[Tuple[str, Tuple[int, float]]]:
        n, s = 0, 0.0
        for c, r in pairs:
            n += c
            s += r
        yield month, (n, s)

    def reducer(self, month: str, pairs: Iterator[Tuple[int, float]]) -> Iterator[Tuple[str, float]]:
        n, s = 0, 0.0
        for c, r in pairs:
            n += c
            s += r
        if n > 0:
            yield month, round(s / n, 3)
        else:
            yield month, 0.0

if __name__ == "__main__":
    MonthlyAvgRating.run()
