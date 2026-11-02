import pandas as pd
import sqlite3

customers = pd.read_csv("customers.csv")
transactions = pd.read_csv("transactions.csv", parse_dates=["transaction_date"])

conn = sqlite3.connect("transactions.db")
customers.to_sql("dim_customers", conn, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", conn, if_exists="replace", index=False)
conn.close()
print(f"DB built: {len(customers)} customers, {len(transactions)} transactions")
