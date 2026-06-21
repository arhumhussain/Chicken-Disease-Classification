from cnnClassifer.config.configuration import ConfiguartionManager
from cnnClassifer.components.base_model import BaseModel
from cnnClassifer import logger


STAGE_NAME = "Base Model Praparation"

class BaseModelPipeline:
    def __init__(self):
         pass
    
    def main(self):
        config = ConfiguartionManager()
        base_model_config = config.get_base_model_config()
        base_model = BaseModel(config=base_model_config)
        base_model.get_base_model()
        base_model.updated_model()

if __name__ == "__main__":
    logger.info(f">>>>>>>  {STAGE_NAME} Started <<<<<<<<")
    try:

        obj =BaseModelPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} Sucessfully Completed<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

    
