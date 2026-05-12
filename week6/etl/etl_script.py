import pandas as pd

# Extract
df = pd.read_csv('data/raw_sales.csv')

# Transform

# Create dimension tables
dim_customer = df[['customer_name', 'city']].drop_duplicates().reset_index(drop=True)
dim_customer['customer_id'] = dim_customer.index + 1

dim_product = df[['product_name', 'category']].drop_duplicates().reset_index(drop=True)
dim_product['product_id'] = dim_product.index + 1

# Convert raw date column first
df['date'] = pd.to_datetime(
    df['date'],
    format='%Y-%m-%d',
    errors='coerce'
)

# Create date dimension
dim_date = df[['date']].drop_duplicates().copy()

dim_date['year'] = dim_date['date'].dt.year
dim_date['month'] = dim_date['date'].dt.month
dim_date['day'] = dim_date['date'].dt.day

dim_date.rename(columns={'date': 'date_id'}, inplace=True)

# Merge IDs back into fact table
fact = df.merge(dim_customer, on=['customer_name', 'city'])
fact = fact.merge(dim_product, on=['product_name', 'category'])
fact = fact.merge(dim_date, left_on='date', right_on='date_id')

fact_sales = fact[['customer_id', 'product_id', 'date_id', 'amount']]

# Load (save outputs)
dim_customer.to_csv('output/dim_customer.csv', index=False)
dim_product.to_csv('output/dim_product.csv', index=False)
dim_date.to_csv('output/dim_date.csv', index=False)
fact_sales.to_csv('output/fact_sales.csv', index=False)

print("ETL process completed successfully!")
