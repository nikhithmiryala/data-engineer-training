import pandas as pd
import json

def extract_customers():

    try:
        return pd.read_csv('../raw_data/customers.csv')

    except FileNotFoundError:
        raise FileNotFoundError(
            "customers.csv not found"
        )


def extract_orders():

    try:

        with open('../raw_data/orders.json') as file:
            data = json.load(file)

        return pd.DataFrame(data)

    except FileNotFoundError:
        raise FileNotFoundError(
            "orders.json not found"
        )
