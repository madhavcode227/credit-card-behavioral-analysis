WITH monthly AS (
    SELECT strftime('%Y-%m', transaction_date) AS txn_month,
           SUM(amount) AS total_spend,
           COUNT(*) AS txn_count
    FROM fact_transactions
    GROUP BY txn_month
)
SELECT
    txn_month,
    total_spend,
    txn_count,
    LAG(total_spend) OVER (ORDER BY txn_month) AS prev_month_spend,
    ROUND(100.0 * (total_spend - LAG(total_spend) OVER (ORDER BY txn_month)) / LAG(total_spend) OVER (ORDER BY txn_month), 1) AS mom_growth_pct,
    ROUND(SUM(total_spend) OVER (ORDER BY txn_month), 2) AS running_total_spend
FROM monthly
ORDER BY txn_month;
