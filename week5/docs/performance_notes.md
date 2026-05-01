# Week 5 – Performance Notes (SQL Optimization)

## Overview

This document summarizes the performance analysis conducted on SQL queries before and after applying indexing. The goal was to understand how query execution changes and how indexes improve performance in a relational database.


## Test Scenario

### Query Used for Testing

```sql
EXPLAIN ANALYZE
SELECT * 
FROM orders 
WHERE customer_id = 5;
```

### Purpose

* Retrieve all orders for a specific customer
* Measure execution performance
* Compare behavior before and after indexing

## Performance Before Indexing

### Execution Plan (Observation)

* **Scan Type:** Sequential Scan (Seq Scan)
* The database scanned the entire `orders` table row by row

### Key Findings

* Slower execution time
* Inefficient for large datasets
* No optimization for filtering condition

### Explanation

* PostgreSQL scanned the entire orders table row by row
* No index was available to optimize filterings


### Sample Output (Simplified)

```
Seq Scan on orders
Filter: (customer_id = 5)
Execution Time: ~0.20 ms
```

## Performance After Indexing

### Index Created

```sql
CREATE INDEX idx_customer_id ON orders(customer_id);
```

### Execution Plan (Observation)

* **Scan Type:** Bitmap Index Scan
* Database directly accessed relevant rows using index

### Key Findings

* Faster execution time
* Reduced number of scanned rows
* More efficient filtering

### Explanation

* Instead of a simple Index Scan, PostgreSQL used:

** Bitmap Index Scan: 
Uses the index to find matching row locations

** Bitmap Heap Scan:
Fetches rows in batches from the table
Reduces random disk reads

### Sample Output (Simplified)

```
Index Scan using idx_customer_id on orders
Index Cond: (customer_id = 5)
Execution Time: ~0.05 ms
```

## Performance Comparison

| Metric         | Before Index | After Index        |
| -------------- | ------------ | ------------------ |
| Scan Type      | Seq Scan     | Index Scan         |
| Rows Scanned   | Full Table   | Filtered Rows Only |
| Execution Time | Higher       | Lower              |
| Efficiency     | Low          | High               |


## Key Insights

* **Sequential Scan** reads the entire table → inefficient for large datasets
* **Index Scan** directly locates required rows → much faster
* Indexes significantly improve query performance when filtering on specific columns
* Proper indexing is critical for scaling databases


## Important Considerations

* Indexes improve read performance but may slightly slow down inserts/updates
* Not all columns need indexing → should be used strategically
* Best used on:

  * Frequently filtered columns
  * Columns used in JOIN conditions

## Conclusion

Applying indexes improved query performance by reducing execution time and minimizing unnecessary data scanning. PostgreSQL used a smarter strategy (Bitmap Heap Scan) instead of simple Index Scan. This exercise demonstrated the importance of query optimization and how indexing plays a key role in efficient data retrieval.

## Next Steps

* Experiment with composite indexes
* Analyze more complex queries with joins
* Explore advanced performance tuning techniques
* Work with larger datasets to observe bigger performance differences and deeper optimization
