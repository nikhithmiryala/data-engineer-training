from extract import extract_customers, extract_orders
from transform import transform_data
from validate import validate_data
from load import load_data
from logger import logger

logger.info("Pipeline Started")

# Extract
customers = extract_customers()
orders = extract_orders()

logger.info("Data Extracted")

# Transform
cleaned_data = transform_data(customers, orders)

logger.info("Data Transformed")

# Validate
if validate_data(cleaned_data):
    logger.info("Validation Passed")

    # Load
    load_data(cleaned_data)

    logger.info("Data Loaded Successfully")

else:
    logger.error("Validation Failed")

logger.info("Pipeline Completed")
