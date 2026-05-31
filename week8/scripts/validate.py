def validate_data(df):

    if df.isnull().sum().sum() > 0:
        raise ValueError(
            "Null values found"
        )

    if df.duplicated().sum() > 0:
        raise ValueError(
            "Duplicate records found"
        )

    if df['amount'].dtype not in ['int64', 'float64']:
        raise ValueError(
            "Invalid amount datatype"
        )

    return True
