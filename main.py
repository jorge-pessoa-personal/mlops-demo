import pickle
import numpy as np

from flask import Flask, jsonify, request


app = Flask(__name__)


with open("models/model.pkl", "rb") as fp:
    clf = pickle.load(fp)


def run_model(data):
    input_data = np.array(data).tolist()
    return clf.predict(input_data).tolist()


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    pred = run_model(data)
    return jsonify(pred)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)
