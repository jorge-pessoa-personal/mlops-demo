from sklearn.linear_model import PassiveAggressiveClassifier
import numpy as np
import pickle

# --

X_train = np.load("dataset/X_train.npy")
X_test = np.load("dataset/X_test.npy")

y_train = np.load("dataset/y_train.npy")
y_test = np.load("dataset/y_test.npy")

# --

params = {
	"max_iter": 5,
	"loss": "hinge"
}

clf = PassiveAggressiveClassifier(**params)

clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)

with open("models/model.pkl", "wb") as fp:
	pickle.dump(clf, fp)

print(score)
