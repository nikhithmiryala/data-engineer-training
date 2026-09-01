import logging
import os

# Get week8 directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Logs folder
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Create logs directory if missing
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "pipeline.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
