"""Load the Olist CSV files into a SQLite database.

Usage:
    python src/load_data.py
    python src/load_data.py --raw data/raw --db data/olist.db

Each CSV becomes a table. "olist_orders_dataset.csv" becomes "orders",
"olist_order_items_dataset.csv" becomes "order_items", and so on.
Empty cells are stored as NULL. Dates stay as text in ISO format
(YYYY-MM-DD HH:MM:SS), which SQLite can compare and calculate with.
"""

import argparse
import csv
import re
import sqlite3
from pathlib import Path


def table_name(csv_path: Path) -> str:
    """Turn 'olist_order_items_dataset.csv' into 'order_items'."""
    name = csv_path.stem
    name = re.sub(r"^olist_", "", name)
    name = re.sub(r"_dataset$", "", name)
    return re.sub(r"\W+", "_", name).lower()


def load_csv(conn: sqlite3.Connection, csv_path: Path) -> int:
    """Load one CSV file into its own table. Returns the number of rows."""
    table = table_name(csv_path)
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        columns = [re.sub(r"\W+", "_", col).lower() for col in header]

        conn.execute(f'DROP TABLE IF EXISTS "{table}"')
        col_defs = ", ".join(f'"{c}" TEXT' for c in columns)
        conn.execute(f'CREATE TABLE "{table}" ({col_defs})')

        placeholders = ", ".join("?" for _ in columns)
        insert_sql = f'INSERT INTO "{table}" VALUES ({placeholders})'

        count = 0
        batch = []
        for row in reader:
            batch.append([value if value != "" else None for value in row])
            if len(batch) >= 10000:
                conn.executemany(insert_sql, batch)
                count += len(batch)
                batch = []
        if batch:
            conn.executemany(insert_sql, batch)
            count += len(batch)

    conn.commit()
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Load Olist CSV files into SQLite.")
    parser.add_argument("--raw", default="data/raw", help="folder containing the CSV files")
    parser.add_argument("--db", default="data/olist.db", help="SQLite database file to create")
    args = parser.parse_args()

    raw_dir = Path(args.raw)
    csv_files = sorted(raw_dir.glob("*.csv"))
    if not csv_files:
        raise SystemExit(
            f"No CSV files found in {raw_dir}. See data/README.md for how to download the data."
        )

    db_path = Path(args.db)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as conn:
        for csv_path in csv_files:
            rows = load_csv(conn, csv_path)
            print(f"Loaded {rows:>8,} rows into table '{table_name(csv_path)}'")

    print(f"\nDone. Database saved to {db_path}")


if __name__ == "__main__":
    main()
