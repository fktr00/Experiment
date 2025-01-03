--
-- @lc app=leetcode id=1890 lang=postgresql
--
-- [1890] The Latest Login in 2020
--

-- @lc code=start
-- Write your PostgreSQL query statement below
select user_id, max(time_stamp) as last_stamp
from logins as l
where extract(year from l.time_stamp) = 2020
group by user_id

-- @lc code=end

