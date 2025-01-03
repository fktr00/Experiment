--
-- @lc app=leetcode id=3374 lang=postgresql
--
-- [3374] First Letter Capitalization II
--

-- @lc code=start
-- Write your PostgreSQL query statement below
select 
    u.content_id,
    content_text as original_text,
    initcap(content_text) as converted_text
from user_content as u

-- @lc code=end

