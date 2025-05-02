
# Amazon-Reviews-2023 — MapReduce Analytics

A fully-reproducible pipeline (Python 3 + [mrjob]) that crunches the 2023 Amazon
product‑review dumps into tidy CSVs and publication‑ready figures.

```
amazon-mapreduce/
├── jobs/                  # all MapReduce scripts (*.py)
├── post_processing/       # pandas / matplotlib helpers
├── output/                # *.tsv / *.csv created by MR and post-processing
├── figs/                  # PNG figures for the report / slides
├── report/                # LaTeX source (amazon_mapreduce_report.tex)
├── env.yml                # exact conda environment
└── README.md              # this file
```

## 1  Quick start

```bash
# clone
git clone https://github.com/<you>/amazon-mapreduce.git && cd amazon-mapreduce

# environment
conda env create -f env.yml
conda activate amazon-mr

# sample data
wget -P data/ https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/raw/review_categories/Digital_Music.jsonl.gz

# run core jobs
python jobs/count_reviews.py data/All_Beauty.jsonl.gz  > output/review_counts.tsv
python jobs/avg_rating.py  data/All_Beauty.jsonl.gz  > output/avg_rating.tsv
python jobs/top10_most_reviewed.py  data/All_Beauty.jsonl.gz  > output/top10.tsv
python jobs/avg_helpfulness.py  data/All_Beauty.jsonl.gz  > output/avg_helpfulness.txt

# post‑process
python post_processing/review_counts_analysis.py
python post_processing/avg_rating_hist.py
```

Figures land in **`figs/`**; CSV/TSV intermediates land in **`output/`**.

## 2  Running on Hadoop / EMR

```bash
python jobs/top10_most_reviewed.py -r hadoop \
       --hadoop-streaming-jar /path/to/hadoop-streaming.jar \
       s3://my-bucket/amazon2023/*.jsonl.gz  > output/top10.tsv
```

Supply an `mrjob.conf` (template in `configs/`) with your S3 bucket and EMR settings.

## 3  Job catalogue

| Script | Purpose |
|--------|---------|
| `count_reviews.py` | reviews per **parent_asin** |
| `avg_rating.py` | average ★ per product |
| `top10_most_reviewed.py` | 10 busiest products |
| `avg_helpfulness.py` | global mean helpful‑vote ratio |
| `sentiment_extract.py` | (MR) dump review text for NLP |
| `monthly_avg_rating.py` | monthly ★ time‑series |
| `rating_helpfulness_pairs.py` | rating ↔︎ helpfulness pairs |
| `word_counts.py` | token frequency (with polarity flag) |

## 4  LaTeX report

```bash
cd report
latexmk -pdf amazon_mapreduce_report.tex
```

Or upload the `.tex` to Overleaf—no extra packages required beyond TeX Live 2022.

## 5  License

MIT — see `LICENSE`.

[mrjob]: https://github.com/Yelp/mrjob
