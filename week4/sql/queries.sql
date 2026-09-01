-- 1. WHERE filter
SELECT * FROM customers
WHERE city = 'New York';

-- 2. ORDER BY
SELECT * FROM products
ORDER BY price DESC;

-- 3. Aggregate functions
SELECT 
    COUNT(*) AS total_orders,
    AVG(quantity) AS avg_quantity
FROM orders;

-- 4. GROUP BY
SELECT customer_id, SUM(quantity) AS total_items
FROM orders
GROUP BY customer_id;

-- 5. JOIN (INNER JOIN)
SELECT c.name, p.product_name, o.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;