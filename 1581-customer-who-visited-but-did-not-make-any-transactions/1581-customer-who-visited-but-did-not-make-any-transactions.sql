# Write your MySQL query statement below
SELECT v.customer_id ,COUNT(v.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON t.visit_id=v.visit_id
WHERE t.transaction_id is null
GROUP BY customer_id