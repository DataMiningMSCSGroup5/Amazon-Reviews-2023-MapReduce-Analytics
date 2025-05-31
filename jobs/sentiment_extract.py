from mrjob.job import MRJob
import json
from textblob import TextBlob

class SentimentAnalysis(MRJob):
    def mapper(self, _, line):
        try:
            data = json.loads(line)
            text = data.get("text", "")
            if text.strip():
                polarity = TextBlob(text).sentiment.polarity
                if polarity > 0.1:
                    yield "positive", 1
                elif polarity < -0.1:
                    yield "negative", 1
                else:
                    yield "neutral", 1
        except:
            pass

    def reducer(self, sentiment, counts):
        yield sentiment, sum(counts)

if __name__ == "__main__":
    SentimentAnalysis.run()
