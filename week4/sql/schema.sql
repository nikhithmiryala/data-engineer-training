-- Customers Table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50)
);

-- Products Table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL
);

-- Orders Table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    product_id INT REFERENCES products(product_id),
    quantity INT
);

-- Customers
INSERT INTO customers (name, city) VALUES
('Alice', 'New York'),
('Bob', 'Chicago'),
('Charlie', 'Dallas');

-- Products
INSERT INTO products (product_name, price) VALUES
('Laptop', 1000),
('Phone', 500),
('Tablet', 300);

-- Orders
INSERT INTO orders (customer_id, product_id, quantity) VALUES
(1, 1, 1),
(2, 2, 2),
(1, 3, 3),
(3, 1, 1);