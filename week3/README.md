# Week 3 – Data Cleaning Project (Pandas)

## Overview

This week was focused on getting hands-on with real-world data problems. Instead of just writing basic Python, I worked with a messy dataset and cleaned it using pandas—similar to what data engineers do in real scenarios.

The goal was to take raw, unstructured data and turn it into something usable and meaningful.

## What I Worked On

* Loaded a CSV file that contained missing and incorrect data
* Cleaned the dataset by fixing null values, duplicates, and formatting issues
* Used pandas to transform and process the data
* Created reusable functions for each step of the process
* Generated summary metrics to understand the dataset better
* Saved the cleaned data into a new file

## Project Structure

```
week3/
│
├── data/
│   └── raw_data.csv
│
├── src/
│   ├── data_cleaning.py
│   └── main.py
│
├── output/
│   ├── cleaned_data.csv
│   └── metrics.txt
│
├── docs/
│   └── learning_notes.md
│
└── README.md
```

## About the Dataset

The dataset I used was intentionally messy to simulate real-world scenarios. It included:

* Missing values (Age, Salary, Department)
* Duplicate rows
* Invalid entries (e.g., text in numeric fields like Salary)
* Incomplete records

## What Cleaning Steps I Performed

Here’s how I approached cleaning the data:

1. **Loaded the data**

   * Used pandas to read the CSV file
   * Added basic error handling in case the file is missing or invalid

2. **Removed duplicates**

   * Identified and removed repeated rows to avoid data redundancy

3. **Fixed invalid salary values**

   * Converted salary column to numeric
   * Replaced invalid entries with average salary

4. **Handled missing values**

   * Filled missing Age values with the average age
   * Filled missing Salary values with the average salary
   * Replaced missing Department values with `"Unknown"`

## What I Generated

After cleaning, I created some basic insights:

* Total number of records
* Average age
* Average salary
* Count of employees per department

These were saved into a text file for easy reference.

## Output Files

After running the script, the following files are created:

* `cleaned_data.csv` → Final cleaned dataset
* `metrics.txt` → Summary of key statistics

## How to Run This Project

### Step 1: Install pandas (if not installed)

```
pip3 install pandas
```

### Step 2: Run the script

```
python3 week3/src/main.py
```

## What I Learned

* How messy real-world data can be
* How to clean and preprocess data using pandas
* The importance of handling missing and invalid values
* Writing reusable and modular code
* Structuring a small data project properly

## Challenges I Faced

* Dealing with invalid values like `"abc"` in numeric columns
* Deciding how to handle missing values properly
* Structuring the code so it stays clean and reusable
* Debugging small issues like file paths and data types

## How I Solved Them

* Used pandas functions like `fillna()` and `to_numeric()`
* Broke the logic into smaller functions
* Tested each step separately before combining
* Added basic error handling

## What I Can Improve Next

* Add logging instead of print statements
* Make the script configurable (instead of hardcoding paths)
* Handle larger datasets more efficiently
* Explore more advanced pandas features

## Final Thoughts

This week helped me understand that data cleaning is a major part of a data engineer’s job. Writing code is just one part—the real challenge is making messy data reliable and usable.
