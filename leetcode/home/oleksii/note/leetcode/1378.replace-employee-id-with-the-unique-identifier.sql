--
-- @lc app=leetcode id=1378 lang=postgresql
--
-- [1378] Replace Employee ID With The Unique Identifier
--

-- @lc code=start
-- Write your PostgreSQL query statement below
select 
    em.unique_id,
    e.name
from employees as e 
left join employeeuni as em on e.id=em.id 
-- @lc code=end

