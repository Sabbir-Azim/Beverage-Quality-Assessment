from Beverage import logger
from src.Beverage.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{'>>'*20} {STAGE_NAME} started {'<<'*20}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{'>>'*20} {STAGE_NAME} completed {'<<'*20}")
except Exception as e:
    logger.exception(e)
    raise e