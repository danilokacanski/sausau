import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from sklearn.datasets import make_blobs


class KMeansClustering:
    def __init__(self, k: int, max_iters: int):
        self.k = k
        self.max_iters = max_iters
        self.centroids = []
        self.X = None
        self.labels = None

    def fit(self, X):
        self.X = np.array(X)
        n_samples, _ = self.X.shape

        random_indices = np.random.choice(n_samples, self.k, replace=False)
        self.centroids = self.X[random_indices]

        for iteration in range(self.max_iters):
            self.labels = self._assign_clusters()

            previous_centroids = self.centroids.copy()

            for i in range(self.k):
                points = self.X[self.labels == i]
                if len(points) > 0:
                    self.centroids[i] = points.mean(axis=0)

            self._plot_iteration(iteration)

            if np.allclose(self.centroids, previous_centroids):
                print(f"Converged at iteration {iteration}")
                break

    def _assign_clusters(self):
        labels = []

        for point in self.X:
            min_distance = float("inf")
            closest_cluster = None

            for i, centroid in enumerate(self.centroids):
                distance = self._euclidean_distance(centroid, point)

                if distance < min_distance:
                    min_distance = distance
                    closest_cluster = i

            labels.append(closest_cluster)

        return np.array(labels)

    def _euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def _plot_iteration(self, iteration):
        cmap = get_cmap("tab10")
        plt.figure(figsize=(12, 9))
        for i in range(self.k):
            points = self.X[self.labels == i]
            plt.scatter(points[:, 0], points[:, 1], s=50, color=cmap(i))
            plt.scatter(
                self.centroids[i, 0],
                self.centroids[i, 1],
                color=cmap(i),
                marker="X",
                edgecolors="black",
                s=200,
                label=f"Centroid {i}",
            )

        plt.title(f"Iteration {iteration + 1}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.grid(True)
        plt.show()


X, y = make_blobs(n_samples=500, centers=4, cluster_std=2.5, random_state=42)

plt.figure(figsize=(7, 7))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="tab10", s=50)
plt.title("Generated Clusters using make_blobs")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()

kmeans = KMeansClustering(k=4, max_iters=15)
kmeans.fit(X)
