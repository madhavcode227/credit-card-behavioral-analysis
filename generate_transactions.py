import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()
random.seed(42)
np.random.seed(42)

NUM_CUSTOMERS = 2000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2025, 12, 31)

CARD_TYPES = ["basic", "gold", "platinum"]
CARD_WEIGHTS = [0.55, 0.30, 0.15]
CARD_SPEND_MULTIPLIER = {"basic": 1.0, "gold": 1.8, "platinum": 3.2}

MERCHANT_CATEGORIES = ["groceries", "dining", "travel", "electronics", "fuel", "entertainment", "utilities"]
CATEGORY_WEIGHTS = [0.25, 0.18, 0.10, 0.12, 0.15, 0.10, 0.10]

CHANNELS = ["POS", "online", "ATM"]
CHANNEL_WEIGHTS = [0.55, 0.35, 0.10]

CITIES = [
    ("Mumbai", "Maharashtra"), ("Delhi", "Delhi"), ("Bengaluru", "Karnataka"),
    ("Pune", "Maharashtra"), ("Chennai", "Tamil Nadu"), ("Hyderabad", "Telangana"),
    ("Kolkata", "West Bengal"), ("Ahmedabad", "Gujarat"), ("Jaipur", "Rajasthan"),
    ("Chandigarh", "Punjab")
]
CITY_WEIGHTS = [0.22, 0.20, 0.16, 0.09, 0.08, 0.08, 0.06, 0.05, 0.03, 0.03]

customers = []
for i in range(1, NUM_CUSTOMERS + 1):
    city, state = CITIES[np.random.choice(len(CITIES), p=CITY_WEIGHTS)]
    customers.append({
        "customer_id": i,
        "card_type": np.random.choice(CARD_TYPES, p=CARD_WEIGHTS),
        "home_city": city,
        "home_state": state,
        "signup_date": START_DATE + timedelta(days=random.randint(0, 180))
    })
customers_df = pd.DataFrame(customers)
customers_df.to_csv("customers.csv", index=False)
print(f"Generated {len(customers_df)} customers")

transactions = []
txn_id = 1
for _, cust in customers_df.iterrows():
    card_mult = CARD_SPEND_MULTIPLIER[cust["card_type"]]
    num_txns = int(np.random.gamma(shape=3, scale=8 * card_mult))
    num_txns = max(num_txns, 3)

    for _ in range(num_txns):
        days_offset = random.randint(0, (END_DATE - cust["signup_date"]).days)
        txn_date = cust["signup_date"] + timedelta(days=days_offset)
        category = np.random.choice(MERCHANT_CATEGORIES, p=CATEGORY_WEIGHTS)

        base_amounts = {"groceries": 40, "dining": 55, "travel": 220, "electronics": 300, "fuel": 35, "entertainment": 60, "utilities": 90}
        amount = round(np.random.gamma(shape=2.2, scale=base_amounts[category] / 2.2) * card_mult, 2)

        if random.random() < 0.85:
            txn_city, txn_state = cust["home_city"], cust["home_state"]
        else:
            txn_city, txn_state = CITIES[np.random.choice(len(CITIES), p=CITY_WEIGHTS)]

        transactions.append({
            "transaction_id": txn_id,
            "customer_id": cust["customer_id"],
            "transaction_date": txn_date.date(),
            "amount": amount,
            "merchant_category": category,
            "channel": np.random.choice(CHANNELS, p=CHANNEL_WEIGHTS),
            "txn_city": txn_city,
            "txn_state": txn_state
        })
        txn_id += 1

transactions_df = pd.DataFrame(transactions)
transactions_df.to_csv("transactions.csv", index=False)
print(f"Generated {len(transactions_df)} transactions")
