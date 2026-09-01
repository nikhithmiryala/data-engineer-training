def transform_data(customers, orders):

    customers = customers.drop_duplicates()

    merged = customers.merge(
        orders,
        on='customer_id',
        how='inner'
    )

    merged['amount'] = merged['amount'].fillna(0)

    return merged
