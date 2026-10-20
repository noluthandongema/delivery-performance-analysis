# Project plan

About 4 weeks at 4 to 6 hours a week. Finish each step before moving on, and commit to GitHub at the end of every step so your profile shows steady progress.

## Week 1: Setup and data

- [ ] Create a free GitHub account if you don't have one, and a new public repository called `delivery-performance-analysis`.
- [ ] Upload this folder to the repository (see "Uploading to GitHub" below).
- [ ] Download the Olist dataset from Kaggle and place the CSV files in `data/raw/` (see `data/README.md`).
- [ ] Run `python src/load_data.py` and confirm the tables load.
- [ ] Open `sql/01_late_delivery_by_state.sql` and run it. Write down what you notice.

## Week 2: Answer the business questions

Write one SQL file per question in the `sql/` folder.

- [ ] Q1: Overall late rate and the trend by month.
- [ ] Q2: Late rate by customer state (starter query included).
- [ ] Q3: Sellers with the most late orders (only count sellers with at least 30 orders, so small numbers don't mislead).
- [ ] Q4: Average review score for on-time vs late orders.
- [ ] Q5: Days from purchase to carrier handover vs carrier handover to customer.

## Week 3: Charts and findings

- [ ] Export each query result to CSV, or read it into pandas.
- [ ] Make one clear chart per question (bar charts and one line chart are enough).
- [ ] Pick your 3 to 5 strongest findings and write each as one sentence with a number.

## Week 4: Write-up and polish

- [ ] Fill in "Key findings" and "Recommendations" in the README, and add 2 or 3 charts.
- [ ] Fill in the "About me" section.
- [ ] Ask someone to read the README and tell you if the story is clear in two minutes.
- [ ] Pin the repository on your GitHub profile and link it from your CV and LinkedIn.

## Uploading to GitHub (no command line needed)

1. Create a new repository on github.com. Tick "Add a README" only if you plan to replace ours.
2. Click **Add file → Upload files** and drag in everything from this folder except `data/raw/`.
3. Click **Commit changes**.

Later, once you are comfortable, learn the basic `git add`, `git commit` and `git push` commands. Recruiters like seeing a commit history that shows regular work.

## Tips

- A finished small project beats an ambitious unfinished one.
- Every chart needs a title and a sentence saying what it means for the business.
- Your operations experience is the advantage here. Explain **why** a finding matters, such as which handover to fix, not just what the numbers say.
