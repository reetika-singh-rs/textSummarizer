# src/textSummarizer/pipeline/stage_01_data_ingestion.py
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_ingestion import DataIngestion
from src.textSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info("Starting Data Ingestion Training Pipeline")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            
            logger.info("Data Ingestion Configuration Loaded")
            data_ingestion = DataIngestion(config=data_ingestion_config)
            
            logger.info("Starting File Download")
            data_ingestion.download_file()
            
            logger.info("Starting File Extraction")
            data_ingestion.extract_zip_file()
            
            logger.info("Data Ingestion Completed Successfully")
        except Exception as e:
            logger.error(f"Error in Data Ingestion Training Pipeline: {e}")
            raise e

from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_ingestion import DataIngestion
from src.textSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
         