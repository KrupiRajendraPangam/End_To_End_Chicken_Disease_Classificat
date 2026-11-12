import os
import numpy as np


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "..")
        )
        self.model_path = os.path.join(project_root, "model", "model.h5")
        self.model = None

    def _load_model(self):
        if self.model is not None:
            return
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(
                f"Model not found at {self.model_path}. "
                "Ensure model/model.h5 is present for inference."
            )
        from tensorflow.keras.models import load_model

        self.model = load_model(self.model_path)

    def predict(self):
        from tensorflow.keras.preprocessing import image

        self._load_model()
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(self.model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = "Healthy"
        else:
            prediction = "Coccidiosis"
        return [{"image": prediction}]
