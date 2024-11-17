--
-- @lc app=leetcode id=1068 lang=postgresql
--
-- [1068] Product Sales Analysis I
--

-- @lc code=start
-- Write your PostgreSQL query statement below
select
    p.product_name,
    s.year,
    s.price
from sales as s
join product as p on p.product_id=s.product_id

-- @lc code=end

