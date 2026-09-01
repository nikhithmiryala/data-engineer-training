import pandas as pd

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError("CSV file is empty")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

def clean_data(df):
    if df is None:
        return None
    
    df = df.fillna({
        'Age': df['Age'].mean(),
        'Salary': df['Salary'].mean()
    })
    return df

def generate_summary(df):
    if df is None:
        return None
    
    return df.describe()

def save_output(df, summary, output_path):
    df.to_csv(f"{output_path}/cleaned_data.csv", index=False)
    
    with open(f"{output_path}/summary.txt", "w") as f:
        f.write(str(summary))
