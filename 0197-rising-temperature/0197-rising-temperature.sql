# Write your MySQL query statement below
SELECT W1.id 
FROM Weather w1
JOIN Weather w2
ON datediff(w1.recordDate,w2.recordDate) = 1
AND w1.temperature > W2.temperature;

