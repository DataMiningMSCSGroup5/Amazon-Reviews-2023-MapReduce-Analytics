from mrjob.job import MRJob
import json

class CountReviewsPerProduct(MRJob):
    def mapper(self, _, line):
        data = json.loads(line)
        asin = data.get("parent_asin")
        if asin:
            yield asin, 1

    def reducer(self, asin, counts):
        yield asin, sum(counts)

if __name__ == "__main__":
    CountReviewsPerProduct.run()
