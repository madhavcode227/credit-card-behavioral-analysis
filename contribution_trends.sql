WITH monthly_category AS (
    SELECT strftime('%Y-%m', transaction_date) AS txn_month,
           merchant_category,
           SUM(amount) AS category_spend
    FROM fact_transactions
    GROUP BY txn_month, merchant_category
)
SELECT
    txn_month,
    merchant_category,
    category_spend,
    ROUND(100.0 * category_spend / SUM(category_spend) OVER (PARTITION BY txn_month), 1) AS pct_of_month_spend
FROM monthly_category
ORDER BY txn_month, category_spend DESC;
