from extract import extract_customers
from extract import extract_orders

from transform import transform_data
from validate import validate_data
from load import load_data

from logger import logger

MAX_RETRIES = 3

attempt = 0

while attempt < MAX_RETRIES:

    try:

        logger.info(
            "Pipeline Started"
        )

        customers = extract_customers()
        orders = extract_orders()

        logger.info(
            "Extraction Complete"
        )

        cleaned_data = transform_data(
            customers,
            orders
        )

        logger.info(
            "Transformation Complete"
        )

        validate_data(cleaned_data)

        logger.info(
            "Validation Passed"
        )

        load_data(cleaned_data)

        logger.info(
            "Load Successful"
        )

        print(
            "Pipeline completed successfully"
        )

        break

    except Exception as e:

        logger.error(
            f"Pipeline Failed: {e}"
        )

        print(
            f"Attempt {attempt + 1} Failed"
        )

        attempt += 1

if attempt == MAX_RETRIES:

    print(
        "Pipeline failed after maximum retries"
    )
