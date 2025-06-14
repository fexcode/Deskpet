import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(module)s - %(levelname)s| : %(message)s",
    filename="debug.log",
)
logger = logging.getLogger(__name__)
