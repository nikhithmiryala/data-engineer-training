def validate_data(df):

    if df.isnull().sum().sum() > 0:
        print("Validation Failed: Null values found")
        return False

    if df.duplicated().sum() > 0:
        print("Validation Failed: Duplicate rows found")
        return False

    return True
