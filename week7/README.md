# Week 7 – Building a Complete Batch ETL Pipeline

## Project Overview

This week focused on building a complete batch ETL pipeline using Python.

In previous weeks, I learned Python fundamentals, data cleaning with pandas, SQL querying, database optimization, and data modeling concepts. This week combined those skills into a practical ETL project that simulates how data engineers process data in real-world environments.

The pipeline extracts data from multiple sources, applies cleaning and transformation logic, validates data quality, and loads the final dataset into a processed output file.

## Objectives

The main goals for this week were:

- Understand the ETL lifecycle
- Read data from multiple source formats
- Build reusable ETL functions
- Apply data validation techniques
- Implement logging
- Create a repeatable and maintainable pipeline

## Project Structure

```

week7/
│
├── raw_data/
│   ├── customers.csv
│   └── orders.json
│
├── processed_data/
│   └── cleaned_data.csv
│
├── scripts/
│   ├── main.py
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   └── logger.py
│
├── logs/
│   └── pipeline.log
│
├── docs/
│   └── pipeline_notes.md
│
└── README.md

```

## Dataset Information

### Customer Dataset

Source:
```

raw_data/customers.csv

```

Contains:
- Customer ID
- Customer Name
- City

Total Records:
- 50+

### Order Dataset

Source:
```

raw_data/orders.json

```

Contains:
- Order ID
- Customer ID
- Order Amount

Total Records:
- 50+

## ETL Process

### Extract

The pipeline reads data from:

- CSV file
- JSON file

The data is loaded into pandas DataFrames for processing.

### Transform

The following transformations are applied:

- Remove duplicate records
- Merge customer and order datasets
- Handle missing values
- Standardize the final structure

### Validate

Validation checks include:

- Null value detection
- Duplicate detection
- Basic data quality checks

The pipeline only continues if validation passes.

### Load

The final cleaned dataset is saved as:

```

processed_data/cleaned_data.csv

```

## Logging

A logging framework was added to track pipeline execution.

Log file:

```

logs/pipeline.log

```

The log records:

- Pipeline start
- Extraction completion
- Transformation completion
- Validation status
- Data load completion
- Pipeline completion

## How to Run

### Step 1

Navigate to the scripts folder:

```bash
cd week7/scripts
```

### Step 2

Run the pipeline:

```bash
python3 main.py
```

## Expected Output

After successful execution:

### Processed Data

```

processed_data/cleaned_data.csv

```

### Log File

```

logs/pipeline.log

```

## Challenges Faced

### Working with Multiple Data Sources

The project required reading both CSV and JSON files and combining them into a single dataset.

### Organizing Code

Separating ETL logic into multiple modules was initially challenging but improved readability and maintainability.

### Logging

Learning how to track pipeline execution through log files provided insight into production ETL practices.

## What I Learned

During this project I learned:

- ETL workflow design
- Reading multiple file formats
- Data transformation techniques
- Data validation practices
- Modular Python programming
- Logging and monitoring
- Building repeatable data pipelines

## Real-World Relevance

ETL pipelines are one of the core responsibilities of data engineers.

This project demonstrates a simplified version of what happens in production systems where data is extracted from various sources, transformed into usable formats, validated for quality, and loaded into reporting or analytical platforms.

## Final Thoughts

This week helped bridge the gap between individual Python scripts and a complete data engineering workflow. Building a modular ETL pipeline provided practical experience with concepts that are widely used in enterprise data environments and serves as a strong foundation for future topics such as Airflow, Spark, and cloud-based data pipelines.