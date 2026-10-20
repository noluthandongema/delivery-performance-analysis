# Data

The raw data is not stored in this repository (it is large and belongs to Olist).

## How to get it

1. Create a free Kaggle account at kaggle.com.
2. Open the dataset: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
3. Click **Download** and unzip the file.
4. Copy the CSV files into a folder called `data/raw/` in this project.

The loader script expects at least these files:

- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_customers_dataset.csv`
- `olist_sellers_dataset.csv`

Any other CSV files in `data/raw/` are loaded too, as tables named after the file.

## Table names after loading

The loader turns each file name into a table name, for example `olist_orders_dataset.csv` becomes `orders`, `olist_order_items_dataset.csv` becomes `order_items`, and so on.
