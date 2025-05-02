from mrjob.job import MRJob
import json, heapq

class Top10MostReviewed(MRJob):
    """Output top 10 products with most reviews."""
    def mapper(self, _, line):
        rec = json.loads(line)
        yield rec["parent_asin"], 1

    def combiner(self, asin, counts):
        yield asin, sum(counts)

    def reducer_init(self):
        self.heap = []  # (count, asin)

    def reducer(self, asin, counts):
        total = sum(counts)
        heapq.heappush(self.heap, (total, asin))
        if len(self.heap) > 10:
            heapq.heappop(self.heap)

    def reducer_final(self):
        for count, asin in sorted(self.heap, reverse=True):
            yield asin, count

if __name__ == "__main__":
    Top10MostReviewed.run()
