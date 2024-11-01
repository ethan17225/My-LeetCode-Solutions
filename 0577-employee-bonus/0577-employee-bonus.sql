# Write your MySQL query statement below
select name, bonus
from Employee E
left join Bonus B on E.empId = B.empId
having bonus < 1000 or bonus is null