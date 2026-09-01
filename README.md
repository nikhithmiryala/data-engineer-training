# Data Engineer Training Project

## Project Overview
This project demonstrates a basic data engineering workflow using Python and Git.  
The goal is to practice virtual environments, Git branching, pull requests, and CSV data processing.

---

## Branches
This repository contains the following branches:

1. **feature-script**
   - Added `script.py` to read a CSV file (`data.csv`) and print a summary.
   - Demonstrates Python CSV handling and basic data analysis.

2. **feature-readme**
   - Added `README.md` file with setup instructions, project overview, and notes on learnings.
   - Demonstrates documentation best practices for projects.

3. **feature-enhancement**
   - Added improvements to the Python script, such as:
     - Calculating column statistics (e.g., average age)
     - Printing a more detailed summary
   - Demonstrates iterative development and pull request workflow.

---

## Setup Instructions (macOS)

### 1. Install Python 3
- Download from [Python.org](https://www.python.org/downloads/macos/)
- Open `.pkg` file → follow installer instructions

### 2. Verify Installation
```bash
python3 --version

### 3. Create Project Folder
mkdir data-engineer-training
cd data-engineer-training

### 4. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 5. Install Git and Configure
git config --global user.name "nikhithmiryala"
git config --global user.email "nikhithmiryala97@gmail.com"
git config --list

### 6. Clone Repository
git clone https://github.com/nikhithmiryala/data-engineer-training.git
cd data-engineer-training

### 7. Branching Workflow
git checkout -b feature-script
git add script.py
git commit -m "Added Python CSV script"
git push origin feature-script

git checkout -b feature-readme
git add README.md
git commit -m "Added README.md"
git push origin feature-readme

git checkout -b feature-enhancement
# Make script improvements
git add script.py
git commit -m "Enhanced CSV script with summary stats"
git push origin feature-enhancement


### How to Run
1.Activate the virtual environment: 
source venv/bin/activate

2.Run the Python script:
python script.py

3.Output:
-Displays total rows, column headers, each row
-If using feature-enhancement, also displays column statistics (e.g., average age