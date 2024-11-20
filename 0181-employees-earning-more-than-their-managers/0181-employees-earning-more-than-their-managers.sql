/* Write your PL/SQL query statement below */
select name as Employee
from employee e
where salary > (
    select salary
    from employee m
    where e.managerId = m.id
)