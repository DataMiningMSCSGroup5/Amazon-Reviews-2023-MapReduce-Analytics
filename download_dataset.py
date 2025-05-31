from datasets import load_dataset
import json

print("Downloading the Amazon Reviews dataset...")
# Load the raw review dataset
dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_All_Beauty", split="full", trust_remote_code=True)

# Save to JSONL format
print("Saving the dataset to beauty_reviews.jsonl...")
with open("beauty_reviews.jsonl", "w") as f:
    for item in dataset:
        if "text" in item and item["text"].strip():
            json.dump(item, f)
            f.write("\n")
