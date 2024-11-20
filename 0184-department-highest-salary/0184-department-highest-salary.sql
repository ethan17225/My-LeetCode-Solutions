/* Write your PL/SQL query statement below */
select Department,Employee, Salary
from (
    select d.name as Department, e.name as Employee, salary as Salary,
            dense_rank() over(partition by d.name order by salary desc) as rank
    from Employee e
    join Department d on e.departmentId = d.id
)
where rank = 1;