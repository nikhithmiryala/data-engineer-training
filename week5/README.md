# Week 5 – Advanced SQL and Performance Optimization

## Overview

This week was focused on going beyond basic SQL and learning how to write more efficient, structured, and scalable queries. Instead of just retrieving data, the goal was to understand how queries perform and how to optimize them.

I worked with multiple related tables and practiced combining, aggregating, and structuring data in a way that reflects real-world data engineering tasks.


## What I Worked On

* Created multiple related tables (customers, orders, products, payments)
* Inserted a larger dataset (50+ records) to simulate real-world scenarios
* Wrote complex SQL queries using different types of JOINs
* Used aggregation with GROUP BY to generate insights
* Implemented subqueries and Common Table Expressions (CTEs)
* Created indexes to improve query performance
* Analyzed query execution plans to understand performance differences

## Project Structure

```id="0p4k1l"
week5/
│
├── sql/
│   ├── schema.sql           # Table creation scripts
│   ├── queries.sql          # All SQL queries
│   └── indexes.sql          # Index creation scripts
│
├── data/
│   └── sample_data.sql      # Sample dataset (50+ records)
│
├── screenshots/             # Query outputs and execution plans
│
├── docs/
│   └── performance_notes.md # Performance comparison notes
│
└── README.md
```

## Database Setup

I used PostgreSQL for this project.

### Steps:

1. Created a database:

   ```sql
   CREATE DATABASE training_db_week5;
   ```
2. Connected to the database:

   ```sql
   \c training_db_week5;
   ```
3. Executed:

   * `schema.sql` → to create tables
   * `sample_data.sql` → to insert data
   * `queries.sql` → to run queries
   * `indexes.sql` → to optimize performance

## Tables Created

### 1. Customers

Stores customer details like name and city

### 2. Products

Contains product information and pricing

### 3. Orders

Stores order details and links to customers

### 4. Payments

Stores payment details linked to orders

## Relationships

* One customer → multiple orders
* One order → one payment
* Orders connect customers and payments

This helped me understand how data flows across multiple tables.

## Queries I Implemented

### 1. Complex JOINs

* Combined data across customers, orders, and payments
* Used:

  * INNER JOIN
  * LEFT JOIN

### 2. Aggregations

* Calculated total orders per city
* Used:

  * COUNT()
  * SUM()
  * GROUP BY

### 3. Subqueries

* Filtered customers based on recent orders
* Helped break complex logic into smaller parts

### 4. CTEs (Common Table Expressions)

* Created temporary result sets
* Made queries more readable and structured

## Performance Optimization

### Indexing

* Created indexes on frequently used columns
* Example:

  * `customer_id` in orders
  * `order_id` in payments

### Execution Plan Analysis

* Used `EXPLAIN ANALYZE` to measure query performance
* Compared:

  * Before indexing → slower (sequential scan)
      + PostgreSQL performed a Sequential Scan, Entire table was scanned, Slower and inefficient.
  
  * After indexing → faster (Bitmap index scan/Bitmap heap scan)
      + Bitmap Index Scan → identifies matching rows using index.
      + Bitmap Heap Scan → retrieves rows efficiently in batches.


## Output

* Query results executed in pgAdmin
* Screenshots saved in:

```id="s8n3mn"
week5/screenshots/
```

## How to Run This Project

### Step 1: Create Database

```bash id="cbsywi"
psql postgres
```

```sql id="lzpnlj"
CREATE DATABASE training_db_week5;
\c training_db_week5;
```

### Step 2: Run SQL Files

```bash id="79tt2c"
psql training_db_week5 -f week5/sql/schema.sql
psql training_db_week5 -f week5/data/sample_data.sql
psql training_db_week5 -f week5/sql/queries.sql
psql training_db_week5 -f week5/sql/indexes.sql
```


## What I Learned

* How to write more efficient and structured SQL queries
* Difference between various JOIN types
* When to use subqueries vs CTEs
* How indexing improves query performance
* How to read and analyze execution plans
* Importance of writing clean and readable SQL


## Challenges I Faced

* Understanding when to use different types of JOINs
* Writing complex queries without making them confusing
* Interpreting execution plans
* Measuring performance improvements accurately


## How I Solved Them

* Practiced simple queries before combining them
* Broke complex queries into smaller steps
* Used CTEs to improve readability
* Compared query performance before and after indexing

## What I Can Improve Next

* Learn advanced SQL concepts (window functions, partitions)
* Optimize queries for very large datasets
* Work with real production-scale data
* Integrate SQL with Python for ETL pipelines
* Explore database tuning and indexing strategies

## Final Thoughts

This week helped me think more like a data engineer by focusing not just on getting results, but on how efficiently those results are produced. Understanding performance and optimization is a key step toward working with large-scale data systems.
