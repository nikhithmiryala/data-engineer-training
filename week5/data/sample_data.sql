INSERT INTO customers (name, city) VALUES
('Alice','NY'),('Bob','LA'),('Charlie','TX'),('David','FL'),
('Eve','NY'),('Frank','TX'),('Grace','LA'),('Hank','FL'),
('Ivy','NY'),('Jack','TX');

INSERT INTO products (product_name, price) VALUES
('Laptop',1000),('Phone',600),('Tablet',400),('Monitor',300),
('Keyboard',50),('Mouse',30),('Printer',200),('Camera',700),
('Speaker',150),('Headphones',120);

INSERT INTO orders (customer_id, order_date)
SELECT (RANDOM()*9+1)::int, CURRENT_DATE - (RANDOM()*30)::int
FROM generate_series(1,30);

INSERT INTO payments (order_id, amount, payment_method)
SELECT order_id, (RANDOM()*1000)::int, 'Card'
FROM orders;