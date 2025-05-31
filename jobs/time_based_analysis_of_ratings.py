from mrjob.job import MRJob
import json
import datetime

class RatingsByMonth(MRJob):
    """Emit (month, rating) for all reviews."""

    def mapper(self, _, line):
        try:
            rec = json.loads(line)
            rating = rec.get("rating")
            timestamp = rec.get("timestamp")
            if rating is not None and timestamp is not None:
                month = datetime.datetime.utcfromtimestamp(timestamp / 1000).strftime("%Y-%m")
                yield month, float(rating)
        except:
            pass

    def reducer(self, month, ratings):
        # Collect all ratings into a list for the month
        yield month, list(ratings)

if __name__ == "__main__":
    RatingsByMonth.run()
