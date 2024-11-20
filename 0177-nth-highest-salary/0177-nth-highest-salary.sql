CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
   select salary into result
    from (
        select salary, dense_rank() over(order by salary desc) as "rank"
        from employee
    )
    where "rank" = N and rownum=1;
     
   RETURN result;
END;