from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifer.components.prediction import PredictionPipeline
from cnnClassifer.utils.common import decodeImage

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)



@app.route("/", methods= ["GET"])
@cross_origin()
def home():
    return render_template("index.html")



@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")

    return "Training Completed Sucessfully"



@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    # Accept multipart file upload (from the HTML form) or a base64 JSON payload
    # 1) File upload via FormData (key: 'file')
    if 'file' in request.files:
        file = request.files['file']
        file.save(clApp.filename)

    else:
        # 2) JSON body containing base64 image string under 'image'
        image_b64 = None
        if request.is_json:
            data = request.get_json()
            image_b64 = data.get('image')
        else:
            image_b64 = request.form.get('image')

        if not image_b64:
            return jsonify({'error': 'No image provided'}), 400

        decodeImage(image_b64, clApp.filename)

    # Call prediction method (note the parentheses)
    result = clApp.classifier.predict()
    return jsonify(result)



if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8000)