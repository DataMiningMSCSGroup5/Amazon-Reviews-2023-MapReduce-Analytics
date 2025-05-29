#!/usr/bin/env bash
set -e
DATA="data/All_Beauty.jsonl.gz"

python3 jobs/count_reviews.py           $DATA > output/review_counts.tsv
python3 jobs/avg_rating.py              $DATA > output/avg_rating.tsv
python3 jobs/top10_most_reviewed.py     $DATA > output/top10.tsv
python3 jobs/avg_helpfulness.py         $DATA > output/avg_helpfulness.txt
python3 jobs/monthly_avg_rating.py      $DATA > output/monthly_avg.tsv
python3 jobs/rating_helpfulness_pairs.py $DATA > output/rating_help.tsv
python3 jobs/sentiment_extract.py       $DATA > output/reviews_for_nlp.tsv
python3 jobs/word_counts.py --polarity pos $DATA > output/words_pos.tsv
python3 jobs/word_counts.py --polarity neg $DATA > output/words_neg.tsv

# post‑processing
python3 post_processing/avg_rating_hist.py
python3 post_processing/review_counts_analysis.py
python3 post_processing/monthly_avg_rating_plot.py
python3 post_processing/sentiment_classify.py
python3 post_processing/helpfulness_rating_corr.py
python3 post_processing/pos_neg_word_compare.py
