# Write your MySQL query statement below
select user_id, max(time_stamp) as last_stamp
from Logins
-- where Extract(Year from time_stamp) = 2020 
-- where Year( time_stamp) = 2020 
where time_stamp like "%2020%"
group by user_id

