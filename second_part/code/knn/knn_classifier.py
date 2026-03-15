import numpy as np
from collections import Counter


class KNNClassfier:
    def __init__(self, k):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = np.array(X_train)
        self.y_train = np.array(y_train)

    def predict(self, X_test):
        return [self._predict(x) for x in X_test]

    def _euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def _predict(self, x):
        distances = [self._euclidean_distance(x, x_train) for x_train in self.X_train]

        k_indices = np.argsort(distances)[: self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # returns [most_commont, num_of_occurences]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
