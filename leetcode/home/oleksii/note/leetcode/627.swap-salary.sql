--
-- @lc app=leetcode id=627 lang=postgresql
--
-- [627] Swap Salary
--

-- @lc code=start
-- Write your PostgreSQL query statement below
update Salary
set sex = case when sex='f' then 'm' 
               when sex='m' then 'f'
          end;

-- @lc code=end

