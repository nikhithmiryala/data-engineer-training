import sys
import os
import pandas as pd

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)

from scripts.transform import transform_data


def test_transform():

    customers = pd.DataFrame({
        'customer_id': [1],
        'name': ['Alice'],
        'city': ['NY']
    })

    orders = pd.DataFrame({
        'customer_id': [1],
        'amount': [100]
    })

    result = transform_data(
        customers,
        orders
    )

    assert len(result) == 1
