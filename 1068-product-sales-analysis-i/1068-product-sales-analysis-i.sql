# Write your MySQL query statement below
SELECT pd.product_name, s.year, s.price
FROM Sales s
JOIN Product pd 
ON pd.product_id=s.product_id;