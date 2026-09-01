def load_data(df):

    df.to_csv(
        '../processed_data/cleaned_data.csv',
        index=False
    )
