import logging
from datetime import datetime

logging.basicConfig(
    filename="audit.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_action(user_id: str, action: str, details: str = ""):
    log_message = f"User: {user_id} | Action: {action} | Details: {details}"
    logging.info(log_message)
