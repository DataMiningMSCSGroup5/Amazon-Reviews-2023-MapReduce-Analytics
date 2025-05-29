from mrjob.job import MRJob
import json
import heapq
from typing import Iterator, Tuple

class Top10MostReviewed(MRJob):
    """Output top 10 products with most reviews."""

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

    def reducer_init(self):
        self.heap = []  # (count, asin)

    def reducer(self, asin: str, counts: Iterator[int]):
        total = sum(counts)
        heapq.heappush(self.heap, (total, asin))
        if len(self.heap) > 10:
            heapq.heappop(self.heap)

    def reducer_final(self):
        for count, asin in sorted(self.heap, reverse=True):
            yield asin, count

if __name__ == "__main__":
    Top10MostReviewed.run()
