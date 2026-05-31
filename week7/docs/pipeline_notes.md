# Week 7 – ETL Pipeline Notes

## Overview

This week focused on building a complete batch ETL (Extract, Transform, Load) pipeline using Python. The goal was to simulate how data engineers process and move data from multiple sources into a clean, structured dataset that can be used for reporting and analysis.

The project follows a modular design where each stage of the pipeline is separated into its own Python module.

## Data Sources

### 1. Customer Data (CSV)

File:
```

raw_data/customers.csv

```

Contains:
- Customer ID
- Customer Name
- City

### 2. Order Data (JSON)

File:
```

raw_data/orders.json

```

Contains:
- Order ID
- Customer ID
- Order Amount

## ETL Workflow

### Step 1: Extract

The pipeline reads data from two different source files:

- CSV file containing customer information
- JSON file containing order information

Python modules used:
- pandas
- json

Output:
- Customer DataFrame
- Order DataFrame

### Step 2: Transform

Several transformations were applied to improve data quality:

#### Remove Duplicates

Duplicate customer records were removed.

Example:

Before:
| customer_id | name |
|------------|------|
| 1 | Alice |
| 1 | Alice |

After:
| customer_id | name |
|------------|------|
| 1 | Alice |

#### Merge Datasets

Customer and order data were joined using:

```

customer_id

```

This created a single consolidated dataset.

#### Handle Missing Values

Null values in the amount column were replaced with:

```

0

```

This prevents issues during future reporting and aggregations.

### Step 3: Validate

Basic validation checks were performed:

#### Null Check

Verify no missing values exist.

#### Duplicate Check

Verify no duplicate rows remain.

#### Data Quality Check

Ensure merged data contains valid customer and order information.

### Step 4: Load

The cleaned dataset is written to:

```

processed_data/cleaned_data.csv

```

This file becomes the final output of the ETL process.

## Logging

A logging framework was added to monitor pipeline execution.

Log file:

```

logs/pipeline.log

```

The log captures:

- Pipeline start
- Extraction completion
- Transformation completion
- Validation results
- Load completion
- Pipeline finish

Example:

```

2025-08-10 10:15:01 - INFO - Pipeline Started
2025-08-10 10:15:02 - INFO - Data Extracted
2025-08-10 10:15:03 - INFO - Data Transformed
2025-08-10 10:15:04 - INFO - Validation Passed
2025-08-10 10:15:05 - INFO - Data Loaded Successfully
2025-08-10 10:15:05 - INFO - Pipeline Completed

```

## Challenges Faced

### Challenge 1
Understanding how to structure a pipeline into separate modules.

### Resolution
Separated the code into:
- extract.py
- transform.py
- validate.py
- load.py
- logger.py

### Challenge 2
Working with multiple file formats (CSV and JSON).

### Resolution
Used pandas and json libraries to read data from different sources.

### Challenge 3
Tracking pipeline execution.

### Resolution
Implemented Python logging to create an execution log.

## Key Learnings

- ETL pipelines follow a structured workflow.
- Modular code improves maintainability.
- Data validation is essential before loading data.
- Logging helps monitor and troubleshoot pipelines.
- Real-world data engineering involves integrating multiple data sources.

## Conclusion

This project provided hands-on experience building a complete ETL pipeline from scratch. It introduced concepts commonly used in production environments, including data extraction, transformation, validation, loading, and logging.