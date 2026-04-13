import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully")
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def remove_duplicates(df):
    return df.drop_duplicates()


def clean_salary(df):
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
    return df


def clean_age(df):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df


def clean_department(df):
    df['Department'] = df['Department'].fillna("Unknown")
    return df


def generate_metrics(df):
    metrics = {
        "total_records": len(df),
        "average_salary": df['Salary'].mean(),
        "average_age": df['Age'].mean(),
        "department_counts": df['Department'].value_counts().to_dict()
    }
    return metrics


def save_outputs(df, metrics, output_path):
    df.to_csv(f"{output_path}/cleaned_data.csv", index=False)

    with open(f"{output_path}/metrics.txt", "w") as f:
        for key, value in metrics.items():
            f.write(f"{key}: {value}\n")
