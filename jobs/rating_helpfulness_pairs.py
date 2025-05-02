from mrjob.job import MRJob, protocol
import json

class RatingHelpfulness(MRJob):
    OUTPUT_PROTOCOL = protocol.RawValueProtocol
    def mapper(self, _, line):
        rec = json.loads(line)
        hv = rec.get("helpful_vote", 0)
        total = rec.get("total_vote", hv) or 1
        score = hv / total
        yield None, f"{rec['rating']}\t{score}"
if __name__ == "__main__":
    RatingHelpfulness.run()
