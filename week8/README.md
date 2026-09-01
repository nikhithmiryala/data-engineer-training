# Week 8 – Data Quality Checks, Testing, and Pipeline Reliability

## Introduction

This week focused on improving the ETL pipeline created in Week 7 by adding reliability features that are commonly used in production environments.

While the previous pipeline successfully extracted, transformed, and loaded data, it did not include safeguards for handling bad data, missing files, or unexpected failures.

The goal of this project was to enhance the pipeline with validation, testing, logging, and error handling to ensure it produces consistent and trustworthy results.

## Project Objective

Enhance the existing ETL pipeline by:

- Adding data quality checks
- Validating incoming data
- Implementing error handling
- Creating automated tests
- Improving logging
- Adding retry logic
- Increasing overall pipeline reliability

## Project Structure

```text
week8/
│
├── raw_data/
│   ├── customers.csv
│   └── orders.json
│
├── processed_data/
│   └── cleaned_data.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   ├── logger.py
│   └── main.py
│
├── tests/
│   ├── test_transform.py
│   └── test_validate.py
│
├── logs/
│   └── pipeline.log
│
├── docs/
│   └── reliability_notes.md
│
└── README.md
```

## Data Sources

### customers.csv

Contains:

- Customer ID
- Customer Name
- City

### orders.json

Contains:

- Order ID
- Customer ID
- Order Amount

The datasets are linked through:

```text
customer_id
```

## Pipeline Workflow

### Step 1 – Extract

The pipeline reads data from:

- CSV files
- JSON files

Both datasets are loaded into pandas DataFrames for processing.

### Step 2 – Transform

The transformation layer performs:

- Duplicate removal
- Dataset merging
- Missing value handling
- Data standardization

The result is a unified dataset ready for validation.

### Step 3 – Validate

Before loading the data, several quality checks are performed.

Validation includes:

#### Null Value Check

Ensures no missing values exist in required fields.

#### Duplicate Detection

Ensures duplicate records are not loaded.

#### Data Type Validation

Verifies that critical columns contain the expected data types.

Only datasets that pass validation continue to the next stage.

### Step 4 – Load

Validated data is saved into:

```text
processed_data/cleaned_data.csv
```

This file represents the final processed output.

### Step 5 – Logging

Pipeline execution details are written to:

```text
logs/pipeline.log
```

Logs include:

- Start time
- Extraction status
- Transformation status
- Validation results
- Load status
- Error messages

### Step 6 – Retry Logic

To improve reliability, the pipeline automatically retries execution when failures occur.

Configuration:

```text
Maximum Retries = 3
```

This prevents temporary issues from causing immediate pipeline failures.

## Running the Pipeline

Navigate to the scripts folder:

```bash
cd week8/scripts
```

Run:

```bash
python3 main.py
```

Expected output:

```text
Pipeline completed successfully
```

## Running Unit Tests

Navigate to the Week 8 directory:

```bash
cd week8
```

Execute:

```bash
pytest
```

Expected result:

```text
2 passed
```


## Sample Failure Test

To test error handling:

Rename the customer file:

```bash
mv raw_data/customers.csv raw_data/customers_backup.csv
```

Run the pipeline again.

Expected behavior:

```text
Attempt 1 Failed
Attempt 2 Failed
Attempt 3 Failed
Pipeline failed after maximum retries
```

Restore the file after testing:

```bash
mv raw_data/customers_backup.csv raw_data/customers.csv
```

## Challenges Faced

### File Path Management

Different execution locations caused issues locating files and logs.

Solution:
- Implemented more reliable path handling using Python's os module.

### Designing Validation Rules

Identifying meaningful validation checks required understanding common data quality issues.

Solution:
- Focused on nulls, duplicates, and data types.

### Testing Failure Scenarios

Creating realistic failure conditions was necessary to verify error handling and retry behavior.

Solution:
- Simulated missing files and validation failures.

## What I Learned

This project helped me understand:

- Data quality validation techniques
- Error handling strategies
- Retry mechanisms
- Automated testing using pytest
- Logging best practices
- Reliable ETL design
- Production readiness concepts

## Future Improvements

Potential enhancements include:

- Database loading instead of CSV output
- Email or alert notifications on failures
- Configuration-driven pipelines
- More advanced schema validation
- Integration with workflow orchestration tools such as Apache Airflow

## Final Thoughts

This project demonstrated that building a successful ETL pipeline involves more than simply moving data from one place to another.

Reliability, testing, validation, and monitoring are equally important components of a production-ready data engineering solution. By implementing these improvements, the pipeline became more resilient, maintainable, and trustworthy.