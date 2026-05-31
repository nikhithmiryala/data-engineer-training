import pandas as pd
import json

def extract_customers():
    return pd.read_csv('../raw_data/customers.csv')

def extract_orders():
    with open('../raw_data/orders.json') as file:
        data = json.load(file)
    return pd.DataFrame(data)
