# DeepFake Image Classifier

A Flask-based deepfake image classification project with a TensorFlow training pipeline. The repository contains data ingestion, base model preparation, model training, evaluation, and a web API for inference.

## Key Features

- Data ingestion from a remote archive into `artifacts/data_ingestion`
- Base model creation and update stored in `artifacts/base_model`
- Model training and output saved to `artifacts/training/model.h5`
- Evaluation artifacts written to `artifacts/evaluation`
- Flask app in `app.py` for running inference and triggering training
- Web UI template in `templates/index.html`

## Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Configuration settings are stored in `config/config.yaml`:

- `artifacts_root`: top-level artifact directory
- `data_ingestion`: source URL, local zip path, and unzip directory
- `base_model`: base and updated model paths
- `prepare_callbacks`: TensorBoard and checkpoint locations
- `training`: trained model path
- `evaluation`: evaluation output path

## Project Structure

- `app.py`: Flask app with `/`, `/train`, and `/predict` endpoints
- `main.py`: orchestrates data ingestion, base model preparation, training, and evaluation pipelines
- `src/cnnClassifer/`: package implementation
  - `components/`: pipeline components including data ingestion, base model, training, evaluation, prediction
  - `config/`: configuration manager
  - `constants/`, `entity/`, `pipeline/`, `utils/`
- `templates/index.html`: frontend UI for image upload and prediction

## Usage

### Run the pipeline

```bash
python main.py
```

This will run the full pipeline:
1. Data ingestion
2. Base model preparation
3. Model training
4. Model evaluation

### Start the Flask app

```bash
python app.py
```

The app listens on `http://0.0.0.0:8000`.

### API Endpoints

- `GET /` - returns the web UI
- `GET/POST /train` - triggers `python main.py` to run the full pipeline
- `POST /predict` - returns prediction results

#### `/predict` payload options

1. Form upload:
   - field name: `file`

2. JSON body:
   ```json
   {
     "image": "<base64-encoded-image>"
   }
   ```

#### Response format

```json
{
  "prediction": "DeepFake Image" | "Real",
  "confidence": 92.37
}
```

## Model and Inference

- The prediction code loads the trained model from `artifacts/training/model.h5`
- Input images are resized to `224x224`
- Output labels are `DeepFake Image` or `Real`

## Notes

- The project currently uses package metadata in `setup.py` that references `Chicken-Disease-Classification`; the actual code implements a deepfake image classifier.
- Ensure `artifacts/` directories exist or are created by the pipeline before running training or prediction.

