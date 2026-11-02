WITH customer_spend AS (
    SELECT customer_id, SUM(amount) AS total_spend, COUNT(*) AS txn_count
    FROM fact_transactions
    GROUP BY customer_id
),
scored AS (
    SELECT customer_id, total_spend, txn_count,
           NTILE(4) OVER (ORDER BY total_spend ASC) AS spend_quartile
    FROM customer_spend
)
SELECT
    CASE spend_quartile
        WHEN 4 THEN 'High Spender'
        WHEN 3 THEN 'Mid-High Spender'
        WHEN 2 THEN 'Mid-Low Spender'
        ELSE 'Low Spender'
    END AS segment,
    COUNT(*) AS num_customers,
    ROUND(AVG(total_spend), 2) AS avg_spend,
    ROUND(SUM(total_spend), 2) AS total_segment_spend
FROM scored
GROUP BY spend_quartile
ORDER BY spend_quartile DESC;
