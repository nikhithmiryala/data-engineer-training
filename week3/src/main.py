from data_cleaning import (
    load_data,
    remove_duplicates,
    clean_salary,
    clean_age,
    clean_department,
    generate_metrics,
    save_outputs
)

def main():
    file_path = "week3/data/raw_data.csv"
    output_path = "week3/output"

    df = load_data(file_path)

    if df is None:
        return

    df = remove_duplicates(df)
    df = clean_salary(df)
    df = clean_age(df)
    df = clean_department(df)

    metrics = generate_metrics(df)

    save_outputs(df, metrics, output_path)

    print("Week 3 data processing completed successfully!")

if __name__ == "__main__":
    main()
