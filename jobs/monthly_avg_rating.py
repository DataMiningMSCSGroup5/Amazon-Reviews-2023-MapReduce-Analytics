from mrjob.job import MRJob
import json, datetime

class MonthlyAvgRating(MRJob):
    """Average rating per calendar month."""
    def mapper(self, _, line):
        rec = json.loads(line)
        month = datetime.datetime.utcfromtimestamp(rec["timestamp"]/1000).strftime("%Y-%m")
        yield month, (1, rec["rating"])

    def combiner(self, month, pairs):
        n, s = 0, 0.0
        for c, r in pairs:
            n += c; s += r
        yield month, (n, s)

    def reducer(self, month, pairs):
        n, s = 0, 0.0
        for c, r in pairs:
            n += c; s += r
        yield month, round(s / n, 3)

if __name__ == "__main__":
    MonthlyAvgRating.run()
