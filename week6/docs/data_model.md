# Week 6 – Data Model Documentation

## Overview

This document explains the data model designed for the Week 6 project. The model follows a **star schema**, which is commonly used in data warehousing for analytical workloads.

## What is Star Schema?

A star schema consists of:

* One central **fact table**
* Multiple surrounding **dimension tables**

It is optimized for:

* Fast querying
* Simpler joins
* Analytical reporting

## Tables in the Model

### 1. Fact Table: `fact_sales`

#### Purpose:

Stores transactional sales data.

#### Columns:

* `sale_id` (Primary Key)
* `customer_id` (Foreign Key)
* `product_id` (Foreign Key)
* `date_id` (Foreign Key)
* `amount` (Measure)

#### Role:

* Central table used for analysis
* Contains measurable metrics

### 2. Dimension Table: `dim_customer`

#### Purpose:

Stores customer-related attributes.

#### Columns:

* `customer_id` (Primary Key)
* `customer_name`
* `city`

### 3. Dimension Table: `dim_product`

#### Purpose:

Stores product details.

#### Columns:

* `product_id` (Primary Key)
* `product_name`
* `category`

### 4. Dimension Table: `dim_date`

#### Purpose:

Stores date-related attributes for time-based analysis.

#### Columns:

* `date_id` (Primary Key)
* `year`
* `month`
* `day`

## Relationships

```id="rel1"
fact_sales → dim_customer (customer_id)
fact_sales → dim_product (product_id)
fact_sales → dim_date (date_id)
```

* Fact table connects to all dimensions via foreign keys
* Dimensions are not directly connected to each other

## Why This Design?

### Benefits:

* Simplifies querying (fewer joins)
* Improves performance for analytical queries
* Separates descriptive data (dimensions) from measurable data (facts)
* Scales well with large datasets

## 🔄 OLTP vs OLAP

| Type | Description                                  |
| ---- | -------------------------------------------- |
| OLTP | Raw transactional data (normalized, complex) |
| OLAP | Analytical data (denormalized, optimized)    |

This project transforms OLTP-style data into an OLAP-friendly model.

## Key Concepts Applied

* Fact vs Dimension separation
* Surrogate keys for better joins
* Data normalization in dimensions
* Analytical modeling for reporting

## Real-World Relevance

This model is commonly used in:

* Business Intelligence (BI) tools
* Data warehouses
* Reporting dashboards
* Analytics platforms

## Conclusion

The star schema designed in this project provides a clean, scalable, and efficient way to organize data for analytics. It demonstrates how raw transactional data can be structured into a meaningful format for reporting and decision-making.
