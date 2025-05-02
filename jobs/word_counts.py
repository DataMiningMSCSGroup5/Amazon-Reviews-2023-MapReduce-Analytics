from mrjob.job import MRJob
import json, re, string, nltk
nltk.download('stopwords', quiet=True)
STOP = set(nltk.corpus.stopwords.words('english')) | set(string.punctuation)
TOKEN = re.compile(r"[A-Za-z']{3,}")

class WordCounts(MRJob):
    def configure_args(self):
        super().configure_args()
        self.add_passthru_arg('--polarity', default='all', help='pos|neg|all')

    def mapper(self, _, line):
        rec = json.loads(line)
        rating = float(rec['rating'])
        pol = self.options.polarity
        if (pol == 'pos' and rating < 4) or (pol == 'neg' and rating > 2):
            return
        words = TOKEN.findall(rec.get('reviewText', '').lower())
        for w in words:
            if w not in STOP:
                yield w, 1

    def combiner(self, w, c):
        yield w, sum(c)

    def reducer(self, w, c):
        yield w, sum(c)

if __name__ == "__main__":
    WordCounts.run()
