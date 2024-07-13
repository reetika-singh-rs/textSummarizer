import sys
import os

# Add the parent directory of the current file to the sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from textSummarizer.logging_init import logger

# Example usage of logger
logger.info("Script started")
# Add your main script logic here
logger.info("Script finished")
