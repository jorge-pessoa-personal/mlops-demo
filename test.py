import pickle
import numpy as np

# --

X_test = np.load("dataset/X_test.npy")
y_test = np.load("dataset/y_test.npy")

# --

def test_output():
    with open("models/model.pkl", "rb") as fp:
        clf = pickle.load(fp)

    sample = clf.predict(X_test[0:1])
    assert len(sample) == 1


def test_score():
    with open("models/model.pkl", "rb") as fp:
        clf = pickle.load(fp)

    score = clf.score(X_test, y_test)
    assert score > 0.1

