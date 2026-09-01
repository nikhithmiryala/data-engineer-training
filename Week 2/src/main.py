from data_processing import read_csv_file, clean_data, generate_summary, save_output

def main():
    file_path = "data/sample_data.csv"
    output_path = "output"

    df = read_csv_file(file_path)
    cleaned_df = clean_data(df)
    summary = generate_summary(cleaned_df)

    save_output(cleaned_df, summary, output_path)

    print("Processing complete!")

if __name__ == "__main__":
    main()
