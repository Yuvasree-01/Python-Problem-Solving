-- # Write your MySQL query statement below
-- select name,amount as balance from Users

SELECT 
    u.name AS NAME, 
    SUM(t.amount) AS BALANCE
FROM 
    Users u
JOIN 
    Transactions t ON u.account = t.account
GROUP BY 
    u.account
HAVING 
    SUM(t.amount) > 10000;
