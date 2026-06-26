# Write your MySQL query statement below
select product_name , sum(o.unit) as unit
from products p
left join Orders o 
on p.product_id = o.product_id
where extract(year_month from o.order_date ) = 202002
group by o.product_id
having sum(o.unit) >=100