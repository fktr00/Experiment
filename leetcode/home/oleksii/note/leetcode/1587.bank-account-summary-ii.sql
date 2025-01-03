--
-- @lc app=leetcode id=1587 lang=postgresql
--
-- [1587] Bank Account Summary II
--

-- @lc code=start
-- Write your PostgreSQL query statement below
select 
    name as "NAME",
    sum(amount) as "BALANCE"
from transactions as t join users as u using (account)
group by name
having sum(amount) > 10000

-- @lc code=end

