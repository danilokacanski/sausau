import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


def visualize_iris(iris_dataset):
    plt.figure(figsize=(8, 6))

    X = iris_dataset.data
    y = iris_dataset.target

    for i, target_name in enumerate(iris_dataset.target_names):
        plt.scatter(X[y == i, 2], X[y == i, 3], label=target_name)

    plt.xlabel("Petal length (cm)")
    plt.ylabel("Petal width (cm)")
    plt.title("Iris Dataset - Petal Length vs Petal Width")
    plt.legend()
    plt.grid(True)
    plt.show()


iris = load_iris()
visualize_iris(iris)
