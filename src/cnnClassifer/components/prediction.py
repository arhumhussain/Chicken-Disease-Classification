import os
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline:

    def __init__(self, filename):
        self.filename = filename

    def predict(self):

        model = load_model(
            os.path.join(
                "artifacts",
                "training",
                "model.h5"
            )
        )

        test_image = image.load_img(
            self.filename,
            target_size=(224, 224)
        )

        test_image = image.img_to_array(test_image)

        test_image = test_image / 255.0

        test_image = np.expand_dims(
            test_image,
            axis=0
        )

        prediction = model.predict(test_image)

        result = np.argmax(prediction, axis=1)[0]
        confidence = float(np.max(prediction)) * 100.0

        print("Raw Prediction:", prediction)
        print("Class:", result)

        if result == 0:
            label = "DeepFake Image"
        else:
            label = "Real"

        return {"prediction": label, "confidence": round(confidence, 2)}