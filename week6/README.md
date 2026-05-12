# Week 6 – Data Modeling and ETL Fundamentals

## Overview

This week focused on understanding how raw operational data is transformed into structured analytical datasets. Instead of only querying data, the goal was to design how data should be organized for reporting, dashboards, and business insights.

I worked on building a simple data warehouse model using a **star schema** and implemented a basic **ETL pipeline using Python**.


## What I Worked On

* Studied OLTP vs OLAP systems and their differences
* Learned dimensional modeling concepts (fact and dimension tables)
* Designed a **star schema for a sales system**
* Identified and created:

  * Fact table (fact_sales)
  * Dimension tables (customer, product, date)
* Built SQL schema for the data model
* Developed a Python-based ETL pipeline
* Converted raw transactional data into structured analytical tables
* Generated transformed outputs from raw datasets
* Documented ETL flow and data model design

## Project Structure

```id="s3k9qv"
week6/
│
├── sql/
│   └── schema.sql              # Star schema definition
│
├── data/
│   └── raw_sales.csv           # Raw input dataset (50+ records)
│
├── etl/
│   └── etl_script.py           # ETL pipeline script
│
├── output/
│   ├── dim_customer.csv
│   ├── dim_product.csv
│   ├── dim_date.csv
│   └── fact_sales.csv
│
├── diagrams/
│   └── er_diagram.png          # Star schema diagram
│
├── docs/
│   ├── etl_flow.md
│   └── data_model.md
│
└── README.md
```

## Data Model Overview

I designed a **Star Schema** consisting of:

### Fact Table: fact_sales

Stores transactional data like:

* Customer ID
* Product ID
* Date ID
* Sales amount

### Dimension Tables

* **dim_customer** → customer details (name, city)
* **dim_product** → product details (name, category)
* **dim_date** → time-based attributes (year, month, day)

## Model Relationship

* Fact table connects to all dimension tables
* Dimensions provide descriptive context
* Fact table stores measurable business values

This structure allows efficient reporting and analytics.

## ETL Process Summary

### 1. Extract

* Loaded raw sales data from CSV file

### 2. Transform

* Created dimension tables by removing duplicates
* Generated surrogate keys for dimensions
* Extracted date attributes (year, month, day)
* Mapped dimension keys into fact table

### 3. Load

* Saved structured data into separate CSV outputs
* Prepared data for analytical use cases

## Key Outputs

After running the ETL pipeline, the following datasets were generated:

* Cleaned customer dimension table
* Product dimension table
* Date dimension table
* Central fact_sales table

## What I Learned

* Difference between OLTP and OLAP systems
* How star schema simplifies analytics
* Importance of separating facts and dimensions
* How ETL pipelines structure raw data
* Role of surrogate keys in data modeling
* How transformation logic drives data quality

## Challenges Faced

* Understanding how fact and dimension tables connect
* Designing a proper star schema structure
* Mapping raw data into multiple dimension tables
* Handling transformations in Python efficiently
* Visualizing the overall data flow

## How I Solved Them

* Broke the model into smaller components (fact vs dimensions)
* Practiced schema design step-by-step
* Used pandas to simplify transformations
* Validated output at each ETL stage
* Referred to real-world star schema examples

## Next Steps

* Learn Slowly Changing Dimensions (SCD concepts)
* Explore ETL automation tools (Airflow basics)
* Connect data warehouse to SQL-based analytics
* Build dashboards using Power BI/Tableau
* Work with larger datasets for performance understanding

## Final Thoughts

This week helped me shift from writing queries to designing data systems. Understanding how data is structured for analytics is a key foundation for any data engineering role. The combination of data modeling and ETL gave me a clearer picture of how real-world data platforms are built.