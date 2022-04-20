import time
import pickle
import numpy as np

from flask import Flask, jsonify, request
from influx import write_point

app = Flask(__name__)


with open("models/model.pkl", "rb") as fp:
    clf = pickle.load(fp)


def run_model(data):
    input_data = np.array(data).tolist()
    return clf.predict(input_data).tolist()


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    start = time.time()
    pred = run_model(data)
    elapsed = time.time() - start
    write_point("prod-model", "runtime", elapsed)
    write_point("prod-model", "batch_size", len(data))

    return jsonify(pred)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)
