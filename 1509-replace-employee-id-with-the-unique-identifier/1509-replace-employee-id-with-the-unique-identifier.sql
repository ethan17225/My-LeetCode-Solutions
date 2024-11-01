# Write your MySQL query statement below
select unique_id, name
from Employees E
LEFT JOIN EmployeeUNI EU ON E.id = EU.id
