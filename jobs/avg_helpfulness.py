from mrjob.job import MRJob
import json

class AvgHelpfulness(MRJob):
    """Compute global average helpfulness score."""
    def mapper(self, _, line):
        rec = json.loads(line)
        if "helpful" in rec:
            helpful, total = rec["helpful"]
        elif "helpful_vote" in rec:
            helpful = rec["helpful_vote"]
            total = rec.get("total_vote", helpful)
        else:
            return
        if total > 0:
            yield "all", (1, helpful / total)

    def combiner(self, _, pairs):
        n, s = 0, 0.0
        for c, sc in pairs:
            n += c; s += sc
        yield "all", (n, s)

    def reducer(self, _, pairs):
        n, s = 0, 0.0
        for c, sc in pairs:
            n += c; s += sc
        yield "average_helpfulness", round(s / n, 4)

if __name__ == "__main__":
    AvgHelpfulness.run()
