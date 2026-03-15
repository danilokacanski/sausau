import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from knn_classifier import KNNClassfier


def run_on_custom(k, X_train, y_train, X_test):
    model = KNNClassfier(k)
    model.fit(X_train, y_train)

    plt.figure(figsize=(12, 5))

    for x, y in zip(X_train, y_train):
        plt.scatter(
            x[0],
            x[1],
            c="red" if y == 0 else "blue",
        )
    for x_test in X_test:
        plt.scatter(
            x_test[0], x_test[1], c="black", marker="x", s=100, label="Test point"
        )

    plt.title("Training data and test point(s)")
    plt.legend()
    plt.show()

    # 2nd plot - after classification

    y_pred = model.predict(X_test)
    for x, y in zip(X_train, y_train):
        plt.scatter(
            x[0],
            x[1],
            c="red" if y == 0 else "blue",
        )
    for x_test, pred in zip(X_test, y_pred):
        plt.scatter(
            x_test[0],
            x_test[1],
            c="red" if pred == 0 else "blue",
            marker="x",
            s=100,
        )

    plt.title("Predictions on test point(s)")
    plt.legend()
    plt.show()


def run_on_iris(k):
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    knn = KNNClassfier(k)
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    print(classification_report(y_test, y_pred, target_names=iris.target_names))


X_train = [
    [1, 2],
    [2, 3],
    [3, 3],
    [1, 1],
    [2, 1],  # class 0
    [6, 5],
    [7, 7],
    [8, 6],
    [7, 5],
    [6, 6],  # class 1
]
y_train = [0] * 5 + [1] * 5

X_test = [[4, 4], [5, 6]]

# Plot of custom dataset
# plt.figure(figsize=(12, 5))

# for x, y in zip(X_train, y_train):
#     plt.scatter(
#         x[0],
#         x[1],
#         c="red" if y == 0 else "blue",
#     )

# plt.show()

k = 5  # different for k = 3 i k = 5
run_on_custom(k=k, X_train=X_train, y_train=y_train, X_test=X_test)

# run_on_iris(k=4)  # run from k = 1 to k = 4
