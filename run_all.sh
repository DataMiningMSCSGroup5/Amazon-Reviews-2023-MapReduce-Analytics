#!/usr/bin/env bash
set -e
DATA="beauty_reviews.jsonl"

python3 jobs/count_reviews.py           $DATA > output/review_counts.tsv
python3 jobs/avg_rating.py              $DATA > output/avg_rating.tsv
python3 jobs/top10_most_reviewed.py     $DATA > output/top10_results.tsv
python3 jobs/avg_helpfulness.py         $DATA > output/avg_helpfulness.txt
# python3 jobs/monthly_avg_rating.py      $DATA > output/monthly_avg.tsv
python3 jobs/rating_helpfulness_pairs.py $DATA > output/ratings_per_month.json
python3 jobs/sentiment_analysis.py       $DATA > output/sentiment_results.tsv
python3 jobs/word_counts.py --polarity pos $DATA > output/words_pos.tsv
python3 jobs/word_counts.py --polarity neg $DATA > output/words_neg.tsv

# post‑processing
python3 post_processing/avg_rating_hist.py
# python3 post_processing/review_counts_analysis.py
python3 post_processing/top_10_reviewed.py
python3 post_processing/plot_ratings_per_year_line_plus_bar.py
python3 post_processing/plot_ratings_per_year.py
python3 post_processing/plot_ratings_per_month.py
python3 post_processing/plot_ratings_month_by_year.py
python3 post_processing/plot_helpfulness_by_month.py
python3 post_processing/plot_helpfulness_by_rating.py
python3 post_processing/visualise_sentiment.py
python3 post_processing/word_count_compare.py
