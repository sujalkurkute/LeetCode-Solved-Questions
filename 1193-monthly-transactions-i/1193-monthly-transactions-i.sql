# Write your MySQL query statement below
select left(trans_date,7) AS  month,
country ,
count(id) AS trans_count,
sum(if(state ='approved',1,0)) AS approved_count,
sum(amount) AS trans_total_amount,
sum(if(state ='approved',amount,0)) AS approved_total_amount
FROM Transactions
group by month,country ;
