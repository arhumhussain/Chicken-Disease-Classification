
from cnnClassifer.config.configuration import ConfiguartionManager
from cnnClassifer.components.training import Training
from cnnClassifer.components.prepare_callback import PrepareCallback
from cnnClassifer import logger





STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfiguartionManager()
        callbacks_config = config.get_callback_config()
        callbacks= PrepareCallback(config=callbacks_config)
        callback_list = callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )


if __name__ == "__main__":
    logger.info(f">>>>>>>  {STAGE_NAME} Started <<<<<<<<")
    try:

        obj =ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} Sucessfully Completed<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e