
import tensorflow as tf
from cnnClassifer.constants.paths import *
from cnnClassifer.utils.common import read_yaml,create_directories,save_json
from cnnClassifer.entity.config_entity import EvaluationConfig



class Evaluation:

    def __init__(self, config: EvaluationConfig):
        self.config = config

        create_directories([self.config.root_dir])

    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=0.3
        )

        dataflow_kwargs = dict(
            target_size=tuple(self.config.params_image_size[:2]),
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path):
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(self.config.model_path)

        self._valid_generator()

        self.score = self.model.evaluate(
            self.valid_generator
        )

    def save_score(self):
        scores = {
            "loss": float(self.score[0]),
            "accuracy": float(self.score[1])
        }

        save_json(
            path=Path("artifacts/evaluation/score.json"), data=scores)