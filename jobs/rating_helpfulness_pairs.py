from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol
import json
from typing import Iterator

class RatingHelpfulness(MRJob):
    """Yield rating and helpfulness ratio pairs."""
    OUTPUT_PROTOCOL = RawValueProtocol

    def mapper(self, _, line: str) -> Iterator[tuple[None, str]]:
        try:
            rec = json.loads(line)
            rating = rec.get("rating")
            helpful = rec.get("helpful_vote", 0)
            total = rec.get("total_vote", helpful)
            if rating is None or total is None or total == 0:
                return
            score = float(helpful) / float(total)
            yield None, f"{rating}\t{score}"
        except Exception:
            return

if __name__ == "__main__":
    RatingHelpfulness.run()
