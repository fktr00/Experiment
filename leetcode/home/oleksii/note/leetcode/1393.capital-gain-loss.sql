--
-- @lc app=leetcode id=1393 lang=postgresql
--
-- [1393] Capital Gain/Loss
--

-- @lc code=start
-- Write your PostgreSQL query statement below
select 
    stock_name,
    sum(case 
        when s.operation='Buy' then -price 
        else price
    
    end) as capital_gain_loss
from stocks as s
group by s.stock_name
-- @lc code=end

