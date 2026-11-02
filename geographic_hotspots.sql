SELECT
    txn_city,
    txn_state,
    COUNT(*) AS txn_count,
    ROUND(SUM(amount), 2) AS total_spend,
    ROUND(AVG(amount), 2) AS avg_txn_amount,
    RANK() OVER (ORDER BY SUM(amount) DESC) AS spend_rank
FROM fact_transactions
GROUP BY txn_city, txn_state
ORDER BY total_spend DESC;
