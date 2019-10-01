## Second Highest Salary --MySQL

select id,
max(salary) as second_max 
from 
Employee
where second_max < ( Select max(salary) from Employee
)



## Nth highest Salary. -SQL Server


SELECT * FROM (
SELECT e.*, 
ROW_NUMBER() OVER (ORDER BY salary DESC) rn 
FROM Employee e
)
WHERE rn = N;
#N is the Nth highest salary


SELECT TOP 1 salary
FROM (
SELECT DISTINCT TOP 3 salary
FROM Employee
ORDER BY salary DESC
) AS temp
ORDER BY salary



# Rank Score

SELECT 
Score,
DENSE_RANK() OVER ( ORDER BY Score  DESC)  as rn
from 
Scores
;



#Consecutive numbers/Orders

SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;
