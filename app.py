from flask import Flask, request
from model import predict
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi :*"

@app.route('/predict', methods=['GET', 'POST'])
def predict_images():
    data = request.files['file']
    if data == None:
        return 'Got Nothing'
    else:
        prediction = predict.predict(data)

    return json.dumps(str(prediction))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)