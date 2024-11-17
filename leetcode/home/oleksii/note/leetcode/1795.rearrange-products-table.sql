--
-- @lc app=leetcode id=1795 lang=postgresql
--
-- [1795] Rearrange Products Table
--

-- @lc code=start
select *
from(
select 
    p.product_id,
    unnest(array['store1', 'store2', 'store3']) as store,
    unnest(array[p.store1, p.store2, p.store3]) as price
from products as p)
where price is not null
-- @lc code=end

