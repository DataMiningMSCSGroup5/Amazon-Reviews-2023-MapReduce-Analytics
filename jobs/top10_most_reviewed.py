from mrjob.job import MRJob
from mrjob.step import MRStep
import json
import heapq

class Top10MostReviewed(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_reviews,
                   combiner=self.combiner_sum_reviews,
                   reducer=self.reducer_sum_reviews),
            MRStep(mapper=self.mapper_prepare_sort,
                   reducer=self.reducer_find_top10)
        ]

    def mapper_get_reviews(self, _, line):
        try:
            rec = json.loads(line)
            asin = rec.get("parent_asin")
            if asin:
                yield asin, 1
        except:
            pass

    def combiner_sum_reviews(self, asin, counts):
        yield asin, sum(counts)

    def reducer_sum_reviews(self, asin, counts):
        yield asin, sum(counts)

    def mapper_prepare_sort(self, asin, total_reviews):
        # Flip key and value to sort by total_reviews
        yield None, (total_reviews, asin)

    def reducer_find_top10(self, _, asin_count_pairs):
        top_10 = heapq.nlargest(10, asin_count_pairs)
        for count, asin in top_10:
            yield asin, count

if __name__ == "__main__":
    Top10MostReviewed.run()
