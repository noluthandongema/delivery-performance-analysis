# Delivery Performance Analysis: Why Do Orders Arrive Late?

> **Status:** work in progress. Sections marked TODO get filled in as the analysis is completed.

## Business problem

Late deliveries lead to unhappy customers, bad reviews and repeat contacts to support. This project analyses real e-commerce orders to find out **where and why deliveries run late**, and what an operations team could change to reduce it.

Written from an operations and logistics point of view: dispatch, carriers, handover times and service levels.

## Data

[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle): about 100,000 real orders from 2016 to 2018, with purchase, carrier handover and delivery dates, the estimated delivery date, sellers, customer locations and review scores.

The raw files are not stored in this repository. See [`data/README.md`](data/README.md) for how to download them.

## Business questions

1. What percentage of delivered orders arrive after the estimated delivery date, and how does that change month by month?
2. Which customer states have the worst late-delivery rates?
3. Which sellers account for the most late orders?
4. How much does a late delivery lower the customer review score?
5. Where is the time lost: seller to carrier handover, or carrier to customer?

## Tools

SQL (SQLite), Python (pandas, matplotlib), Excel/Sheets for the summary tables. TODO: update this list to match what you actually used.

## Key findings

TODO: add 3 to 5 findings, each with a number and a chart. Example format:

- **Finding 1:** X% of orders arrived late overall, rising to Y% in [month].
- **Finding 2:** ...

## Recommendations

TODO: add 2 or 3 concrete actions an operations manager could take, for example:

1. ...
2. ...

## How to run it

```bash
# 1. Install the requirements
pip install -r requirements.txt

# 2. Put the Olist CSV files in data/raw/ (see data/README.md)

# 3. Load them into a SQLite database
python src/load_data.py

# 4. Run the queries in the sql/ folder against data/olist.db
```

## Project structure

```
delivery-performance-analysis/
├── README.md
├── PLAN.md              step-by-step plan
├── requirements.txt
├── data/
│   └── README.md        how to download the data
├── src/
│   └── load_data.py     loads the CSV files into SQLite
├── sql/
│   └── 01_late_delivery_by_state.sql
├── notebooks/           analysis and charts (to be added)
└── outputs/             charts and summary tables (to be added)
```

## About me

TODO: two lines about your background in operations, logistics and remote support, and what you are looking for next. Add a link to your LinkedIn.
