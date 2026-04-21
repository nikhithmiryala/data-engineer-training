# Week 4 – Working with Databases and SQL

## Overview

This week was all about moving from Python-based data processing to working directly with databases using SQL. Instead of handling data in files, I learned how data is stored, managed, and queried inside a relational database.

The focus was on understanding how tables relate to each other and how to retrieve meaningful information using SQL queries.

## What I Worked On

* Set up a local PostgreSQL database
* Created multiple related tables (customers, products, orders)
* Inserted sample data into each table
* Wrote SQL queries to filter, sort, and analyze data
* Used aggregation functions to calculate metrics
* Performed joins to combine data from multiple tables
* Documented query outputs and explanations

## Project Structure

```
week4/
│
├── sql/
│   ├── schema.sql            # Table creation + data insertion
│   └── queries.sql           # All SQL queries
│
├── screenshots/              # Query output screenshots
│
├── docs/
│   └── query_explanations.md # Explanation of each query
│
└── README.md
```

## Database Setup

I used PostgreSQL as the database for this project.

### Steps:

1. Installed PostgreSQL on macOS
2. Started the database service
3. Created a database:

   ```sql
   CREATE DATABASE training_db;
   ```
4. Connected to it:

   ```sql
   \c training_db;
   ```

## Tables Created

I designed three related tables to simulate a simple business scenario:

### 1. Customers

* Stores customer details
* Primary Key: `customer_id`

### 2. Products

* Stores product information
* Primary Key: `product_id`

### 3. Orders

* Stores purchase transactions
* References both customers and products
* Foreign Keys:

  * `customer_id`
  * `product_id`

This structure helped me understand how relationships work in databases.

## Relationships

* One customer can have multiple orders
* One product can appear in multiple orders
* Orders act as a bridge between customers and products

This is a basic example of relational database design.

## Queries I Implemented

### 1. Filtering Data (WHERE)

* Retrieved specific records based on conditions
* Example: customers from a particular city

### 2. Sorting Data (ORDER BY)

* Sorted products based on price

### 3. Aggregations

* Used functions like:

  * COUNT()
  * AVG()
  * SUM()

### 4. Grouping Data (GROUP BY)

* Grouped orders by customer
* Calculated total items per customer

### 5. Joining Tables (INNER JOIN)

* Combined data from customers, orders, and products
* Displayed customer name, product, and quantity together

## Output

* Query results were executed in PostgreSQL
* Results were stored in as CSV files:

```
week4/screenshots/
```

##  How to Run This Project

### Step 1: Create Database

```bash
psql postgres
```

```sql
CREATE DATABASE training_db;
\c training_db;
```

### Step 2: Run Schema File

```bash
psql training_db -f week4/sql/schema.sql
```

### Step 3: Run Queries

```bash
psql training_db -f week4/sql/queries.sql
```

## What I Learned

* How relational databases are structured
* Difference between primary keys and foreign keys
* Writing SQL queries for real-world scenarios
* Using aggregation functions for analysis
* Combining tables using joins
* Thinking in terms of relationships instead of flat data

## Challenges I Faced

* Understanding how tables connect through keys
* Writing JOIN queries correctly
* Debugging SQL syntax errors
* Visualizing how data flows across multiple tables

## How I Solved Them

* Practiced simple queries before moving to joins
* Broke complex queries into smaller parts
* Re-ran queries multiple times to verify results
* Used sample data to clearly understand relationships

## What I Can Improve Next

* Learn advanced joins (LEFT JOIN, RIGHT JOIN)
* Write more complex queries with multiple conditions
* Optimize queries for performance
* Integrate SQL with Python (pandas + database)
* Explore database design and normalization further

## Final Thoughts

This week gave me a strong foundation in SQL and databases. It helped me understand how real-world data is stored and accessed, which is essential before building larger data pipelines.