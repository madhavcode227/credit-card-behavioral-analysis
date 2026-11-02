# Credit Card Behavioral & Trend Pattern Analysis

SQL-driven analysis of synthetic credit card transaction data to identify spending trends, geographic hotspots, and customer segmentation patterns.

## Key Techniques
- CTEs and window functions (`LAG`, `NTILE`, `RANK`, `SUM() OVER PARTITION BY`)
- Monthly spend movement with month-over-month growth %
- Customer segmentation into spend quartiles
- Geographic hotspot ranking by city/state
- Category contribution trends over time

## Data
Synthetic dataset: 2,000 customers, ~74,000 transactions across 24 months, with realistic patterns:
- Card tier (basic/gold/platinum) correlates with spend (platinum ~3.2x basic)
- Transaction volume concentrated in major metro cities (Mumbai, Delhi, Bengaluru)
- 7 merchant categories with realistic amount distributions

## Files
- `generate_transactions.py` — synthetic data generation
- `build_db.py` — loads data into SQLite (`dim_customers`, `fact_transactions`)
- `monthly_spend_trend.sql` — MoM spend growth using LAG + running total
- `customer_segmentation.sql` — NTILE-based spend quartile segmentation
- `geographic_hotspots.sql` — city/state ranked by total spend (RANK)
- `contribution_trends.sql` — category % contribution per month

## Key Finding
Spend is highly concentrated: top cities account for the majority of total transaction volume, and platinum cardholders — despite being the smallest segment — contribute disproportionately to total spend.

## Author
Madhav Kapoor


