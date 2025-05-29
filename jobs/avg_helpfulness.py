from mrjob.job import MRJob
import json
from typing import Tuple, Iterator

class AvgHelpfulness(MRJob):
    """Compute global average helpfulness score from Amazon reviews."""

    KEY = "all"

    def mapper(self, _, line: str) -> Iterator[Tuple[str, Tuple[int, float]]]:
        """Extract helpfulness votes and yield (count, ratio) pairs."""
        try:
            rec = json.loads(line)
        except Exception:
            return  # skip malformed lines

        helpful, total = None, None
        if "helpful" in rec and isinstance(rec["helpful"], list) and len(rec["helpful"]) == 2:
            helpful, total = rec["helpful"]
        elif "helpful_vote" in rec:
            helpful = rec["helpful_vote"]
            total = rec.get("total_vote", helpful)
        if helpful is None or total is None:
            return
        try:
            helpful = float(helpful)
            total = float(total)
        except Exception:
            return
        if total > 0:
            yield self.KEY, (1, helpful / total)

    def combiner(self, _, pairs: Iterator[Tuple[int, float]]) -> Iterator[Tuple[str, Tuple[int, float]]]:
        """Aggregate counts and ratios locally."""
        n, s = 0, 0.0
        for c, sc in pairs:
            n += c
            s += sc
        yield self.KEY, (n, s)

    def reducer(self, _, pairs: Iterator[Tuple[int, float]]) -> Iterator[Tuple[str, float]]:
        """Aggregate globally and compute the average helpfulness."""
        n, s = 0, 0.0
        for c, sc in pairs:
            n += c
            s += sc
        if n > 0:
            yield "average_helpfulness", round(s / n, 4)
        else:
            yield "average_helpfulness", 0.0

if __name__ == "__main__":
    AvgHelpfulness.run()
