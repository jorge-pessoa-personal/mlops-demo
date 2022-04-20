from sklearn.linear_model import PassiveAggressiveClassifier
import numpy as np
import pickle
import os
import uuid

import neptune.new as neptune

# --

X_train = np.load("dataset/X_train.npy")
X_test = np.load("dataset/X_test.npy")

y_train = np.load("dataset/y_train.npy")
y_test = np.load("dataset/y_test.npy")

# --

params = {
 "max_iter": 100,
 "loss": "hinge"
}

h = uuid.uuid4().hex[:5]
run = neptune.init(
 project="mlops-demo",
 api_token=os.environ["NEPTUNE_API_KEY"],
 name=f"model-train-{h}"
)

clf = PassiveAggressiveClassifier(**params)

clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)

with open("models/model.pkl", "wb") as fp:
 pickle.dump(clf, fp)

run["scores/score"] = score
run["params"] = params
run["pickled_model"].upload("models/model.pkl")

print(score)
