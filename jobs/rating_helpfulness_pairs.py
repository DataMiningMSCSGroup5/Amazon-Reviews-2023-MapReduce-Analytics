from mrjob.job import MRJob
import json

class HelpfulnessByRating(MRJob):
    """Compute average helpful votes per rating level."""

    def mapper(self, _, line):
        try:
            review = json.loads(line)
            rating = review.get("rating")
            helpful = review.get("helpful_vote", 0)
            if rating is not None:
                yield float(rating), (1, helpful)
        except:
            pass

    def combiner(self, rating, values):
        total_reviews, total_helpful = 0, 0
        for count, helpful in values:
            total_reviews += count
            total_helpful += helpful
        yield rating, (total_reviews, total_helpful)

    def reducer(self, rating, values):
        total_reviews, total_helpful = 0, 0
        for count, helpful in values:
            total_reviews += count
            total_helpful += helpful
        avg_helpful = total_helpful / total_reviews if total_reviews > 0 else 0
        yield rating, round(avg_helpful, 3)

if __name__ == "__main__":
    HelpfulnessByRating.run()
