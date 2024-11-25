# Write your MySQL query statement below
select distinct A.num as ConsecutiveNums
from Logs A
join Logs B on A.id - 1 = B.id
join Logs C on A.id + 1 = C.id
where A.num = B.num and B.num = C.num