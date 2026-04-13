# Week 3 – Learning Notes

## Concepts Learned

### 1. Working with Pandas

* Reading CSV files using `pd.read_csv()`
* Handling missing data using `fillna()`
* Converting data types using `to_numeric()`

### 2. Data Cleaning Techniques

* Removing duplicates using `drop_duplicates()`
* Handling null values with mean substitution
* Fixing invalid or inconsistent data formats

### 3. Data Transformation

* Creating reusable transformation functions
* Applying sequential cleaning steps
* Generating summary statistics

### 4. Aggregations

* Using `value_counts()` for categorical analysis
* Calculating averages and counts

### 5. Code Structuring

* Modular programming approach
* Separation of concerns (loading, cleaning, saving)

## Challenges Faced

### 1. Handling Invalid Data Types

* Salary column contained non-numeric values like `"abc"`

### 2. Missing Values

* Multiple columns had null values requiring different strategies

### 3. Duplicate Records

* Identifying and removing duplicates without affecting valid data

### 4. Debugging Issues

* File path errors
* Data type conversion warnings

## Solutions Implemented

* Used `pd.to_numeric(errors='coerce')` to handle invalid values
* Applied mean imputation for missing numeric data
* Used `drop_duplicates()` to clean duplicate rows
* Structured code into reusable functions for clarity
* Added error handling using try-except blocks

## Key Takeaways

* Data cleaning is a critical step in any data pipeline
* Pandas provides powerful tools for handling structured data
* Writing modular and reusable code improves scalability
* Debugging is an essential skill in real-world data scenarios

## What I Would Do Differently

* Add logging instead of print statements
* Use configuration files instead of hardcoding paths
* Add validation checks before processing data

## Next Steps

* Learn advanced pandas operations (groupby, joins)
* Explore working with JSON data
* Introduce logging and configuration management
* Start building scalable ETL pipelines
