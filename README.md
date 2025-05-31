# Amazon Review Analysis with MapReduce

This project analyzes Amazon Beauty Reviews dataset using MapReduce techniques to extract insights about product ratings, helpfulness, sentiment, and word frequencies.

## Project Structure

```
AmazonReviewAnalysiswithMapReduce/
├── download_dataset.py # Script to download the Amazon beauty reviews dataset
├── run_all.sh # Script to run all MapReduce jobs and visualizations
├── requirements.txt # Python dependencies
├── jobs/ # MapReduce job implementations
│   ├── avg_helpfulness.py
│   ├── avg_rating.py
│   ├── count_reviews.py
│   ├── monthly_avg_rating.py
│   ├── rating_helpfulness_pairs.py
│   ├── sentiment_analysis.py
│   ├── top10_most_reviewed.py
│   └── word_counts.py
├── post_processing/ # Visualization and analysis scripts
│   ├── avg_rating_hist.py
│   ├── plot_helpfulness_by_month.py
│   ├── plot_helpfulness_by_rating.py
│   ├── plot_ratings_per_month.py
│   ├── plot_ratings_per_month_over_time.py
│   ├── plot_ratings_per_year.py
│   ├── plot_ratings_per_year_line_plus_bar.py
│   ├── top_10_reviewed.py
│   ├── visualise_sentiment.py
│   ├── plot_ratings_over_time.py
│   └── word_count_compare.py
├── output/ # Results from MapReduce jobs (TSV/CSV/JSON files)
└── figs/ # Generated visualizations
```

## Getting Started

### Prerequisites

- Python 3.10+
- Pip package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DataMiningMSCSGroup5/AmazonReviewAnalysiswithMapReduce.git
   cd AmazonReviewAnalysiswithMapReduce
   ```

2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Downloading the Dataset

The project uses the Amazon Reviews 2023 dataset from the McAuley Lab. To download:

```bash
python download_dataset.py
```

This script downloads the "All_Beauty" category reviews and saves them to beauty_reviews.jsonl.

## MapReduce Job Catalog

| Job File | Purpose | Output |
|----------|---------|--------|
| avg_rating.py | Calculates average rating per product | avg_rating.tsv |
| top10_most_reviewed.py | Finds products with most reviews | top10_results.tsv |
| sentiment_analysis.py | Analyzes review text sentiment | sentiment_results.tsv |
| word_counts.py | Counts word frequency by sentiment | words_pos.tsv, words_neg.tsv |
| rating_helpfulness_pairs.py | Tracks ratings over time | ratings_per_month.json |
| avg_helpfulness.py | Average helpfulness score by rating | helpfulness_by_rating.tsv |

## Running the Analysis

### Option 1: Run All Jobs

To run all MapReduce jobs and generate all visualizations:

```bash
bash run_all.sh
```

### Option 2: Run Individual Jobs

You can run individual MapReduce jobs:

1. **Count Reviews** - Counts the total number of reviews:

   ```bash
   python jobs/count_reviews.py beauty_reviews.jsonl > output/review_counts.tsv
   ```

2. **Average Rating** - Calculates average rating per product:

   ```bash
   python jobs/avg_rating.py beauty_reviews.jsonl > output/avg_rating.tsv
   ```

3. **Top 10 Most Reviewed Products** - Identifies most popular products:

   ```bash
   python jobs/top10_most_reviewed.py beauty_reviews.jsonl > output/top10_results.tsv
   ```

4. **Average Helpfulness** - Analyzes how helpful users find reviews:

   ```bash
   python jobs/avg_helpfulness.py beauty_reviews.jsonl > output/avg_helpfulness.txt
   ```

5. **Rating-Helpfulness Pairs** - Analyzes ratings grouped by month:

   ```bash
   python jobs/rating_helpfulness_pairs.py beauty_reviews.jsonl > output/ratings_per_month.json
   ```

6. **Sentiment Analysis** - Analyzes text sentiment (positive/negative/neutral):

   ```bash
   python jobs/sentiment_analysis.py beauty_reviews.jsonl > output/sentiment_results.tsv
   ```

7. **Word Counts** - Extracts frequent words by sentiment polarity:

   ```bash
   python jobs/word_counts.py --polarity pos beauty_reviews.jsonl > output/words_pos.tsv
   python jobs/word_counts.py --polarity neg beauty_reviews.jsonl > output/words_neg.tsv
   ```

## Visualizations

After running the MapReduce jobs, generate visualizations using the scripts in `post_processing`:

### Example Visualizations

```bash
# Example: Generate histogram of average ratings
python post_processing/avg_rating_hist.py

# Example: Visualize sentiment distribution
python post_processing/visualise_sentiment.py
```

## Key Visualizations

The project generates several key visualizations:

- **Average Rating by Month** - Shows rating trends across months
- **Average Rating by Year** - Shows long-term rating trends
- **Sentiment Distribution** - Distribution of positive/neutral/negative reviews
- **Average Helpful Votes by Rating** - Relationship between ratings and helpfulness
- **Top 10 Most Reviewed Products** - Products with most reviews
- **Most Frequent Words** - Comparison of frequent words in positive vs negative reviews

<!-- ## License

[Your License Here] -->

## Acknowledgments

- McAuley Lab for the Amazon Reviews dataset
