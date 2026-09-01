# Week 4 – Query Explanations

## Overview

This document explains each SQL query used in the Week 4 project in simple terms. The goal is to clearly understand what each query does and why it is useful.

## 1. Filtering Data using WHERE

```sql
SELECT * FROM customers
WHERE city = 'New York';
```

### Explanation:

This query retrieves all customers who are located in **New York**.

### Why it’s useful:

Filtering helps in narrowing down data based on specific conditions. In real-world scenarios, this is commonly used to find records that meet certain criteria.

## 2. Sorting Data using ORDER BY

```sql
SELECT * FROM products
ORDER BY price DESC;
```

### Explanation:

This query retrieves all products and sorts them by price in **descending order** (highest to lowest).

### Why it’s useful:

Sorting allows us to organize data in a meaningful way, such as finding the most expensive or cheapest products quickly.

## 3. Aggregate Functions (COUNT, AVG)

```sql
SELECT 
    COUNT(*) AS total_orders,
    AVG(quantity) AS avg_quantity
FROM orders;
```

### Explanation:

* `COUNT(*)` → Counts the total number of orders
* `AVG(quantity)` → Calculates the average number of items per order

### Why it’s useful:

Aggregate functions help summarize large datasets into key metrics, which are important for reporting and analysis.

## 4. Grouping Data using GROUP BY

```sql
SELECT customer_id, SUM(quantity) AS total_items
FROM orders
GROUP BY customer_id;
```

### Explanation:

This query groups all orders by `customer_id` and calculates the total quantity of items each customer has ordered.

### Why it’s useful:

Grouping helps analyze data at a category level (e.g., per customer, per region). It is widely used in reporting and dashboards.

## 5. Joining Tables using INNER JOIN

```sql
SELECT c.name, p.product_name, o.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;
```

### Explanation:

This query combines data from three tables:

* `orders`
* `customers`
* `products`

It shows:

* Customer name
* Product name
* Quantity ordered

### Why it’s useful:

JOINs allow us to combine related data from multiple tables. This is essential in relational databases where data is stored separately but linked through keys.

## Key Takeaways

* **WHERE** → Filters data
* **ORDER BY** → Sorts data
* **COUNT, AVG, SUM** → Summarize data
* **GROUP BY** → Aggregates data by category
* **JOIN** → Combines multiple tables

## Final Note

Understanding these basic queries is crucial because they form the foundation of almost all database operations in real-world data engineering tasks.
