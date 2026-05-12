# Week 6 – ETL Flow Documentation

##cOverview

This document explains the ETL (Extract, Transform, Load) process implemented in this project. The goal is to convert raw, unstructured sales data into a structured format suitable for analytical reporting using a star schema.

## ETL Process Breakdown

### 1. Extract Phase

#### Source:

* Raw data is stored in a CSV file:

  ```
  week6/data/raw_sales.csv
  ```

#### Description:

* The dataset contains transactional sales data including:

  * Customer details
  * Product details
  * Sales date
  * Transaction amount

#### Implementation:

* Data is loaded using Python (pandas):

  ```python
  df = pd.read_csv('data/raw_sales.csv')
  ```

### 2. Transform Phase

This is the most critical phase where raw data is cleaned and structured.

### Step 1: Create Customer Dimension

* Extract unique customers from raw data
* Remove duplicates
* Assign surrogate keys (`customer_id`)

```python
dim_customer = df[['customer_name', 'city']].drop_duplicates()
```

### Step 2: Create Product Dimension

* Extract unique products
* Assign `product_id`

```python
dim_product = df[['product_name', 'category']].drop_duplicates()
```

### Step 3: Create Date Dimension

* Convert date column into structured format
* Extract:

  * Year
  * Month
  * Day

```python
dim_date['year'] = dim_date['date'].dt.year
```

### Step 4: Create Fact Table

* Combine all dimensions
* Map surrogate keys
* Retain measurable metric (`amount`)

```python
fact_sales = fact[['customer_id', 'product_id', 'date_id', 'amount']]
```

### Key Transformation Logic

* Deduplication ensures dimension tables are clean
* Surrogate keys improve join efficiency
* Data is normalized into dimension tables and a central fact table

### 3. Load Phase

#### Target:

* Structured output files:

  ```
  week6/output/
  ```

#### Files Generated:

* dim_customer.csv
* dim_product.csv
* dim_date.csv
* fact_sales.csv

#### Implementation:

```python
to_csv()
```

## Data Flow Summary

```id="flow1"
Raw CSV → Data Cleaning → Dimension Tables → Fact Table → Output Files
```

## Key Learnings

* ETL separates raw data from analytical structure
* Transformation logic is the core of data engineering
* Proper structuring improves query performance and reporting
* Dimensional modeling simplifies analytics

## Conclusion

The ETL pipeline successfully transforms raw transactional data into a structured star schema format, making it ready for reporting and analytics.
