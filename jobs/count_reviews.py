from mrjob.job import MRJob
import json

class CountReviews(MRJob):
    """Count number of reviews per parent_asin (Amazon 2023 schema)."""
    def mapper(self, _, line):
        rec = json.loads(line)
        yield rec["parent_asin"], 1

    def combiner(self, asin, counts):
        yield asin, sum(counts)

    def reducer(self, asin, counts):
        yield asin, sum(counts)

if __name__ == "__main__":
    CountReviews.run()
