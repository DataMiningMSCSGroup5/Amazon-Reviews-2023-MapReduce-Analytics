from mrjob.job import MRJob
import json

class AvgRating(MRJob):
    """Average star rating per parent_asin."""
    def mapper(self, _, line):
        rec = json.loads(line)
        yield rec["parent_asin"], (1, float(rec["rating"]))

    def combiner(self, asin, pairs):
        n, s = 0, 0.0
        for c, r in pairs:
            n += c; s += r
        yield asin, (n, s)

    def reducer(self, asin, pairs):
        n, s = 0, 0.0
        for c, r in pairs:
            n += c; s += r
        yield asin, round(s / n, 3)

if __name__ == "__main__":
    AvgRating.run()
