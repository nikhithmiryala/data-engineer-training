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

from scripts.validate import validate_data


def test_validation():

    df = pd.DataFrame({
        'amount': [100]
    })

    assert validate_data(df) is True
