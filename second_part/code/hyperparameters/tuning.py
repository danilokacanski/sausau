import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


data = load_breast_cancer()
X, y = data.data, data.target
feature_names = data.feature_names
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)


def tune_knn():
    k_range = list(range(1, 30))
    train_scores_knn = []
    test_scores_knn = []

    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        train_scores_knn.append(knn.score(X_train, y_train))
        test_scores_knn.append(knn.score(X_test, y_test))

    plt.figure(figsize=(10, 4))
    plt.plot(
        k_range,
        [1 - score for score in test_scores_knn],
        marker="o",
    )
    plt.xlabel("Number of Neighbors (k)")
    plt.ylabel("Error")
    plt.legend()
    plt.grid(True)
    plt.show()


def tune_rf():
    param_grid_rf = {
        "n_estimators": [10, 50, 100, 200],
        "max_depth": [None, 5, 10, 20],
        "criterion": ["entropy", "gini"],
    }

    rf = RandomForestClassifier(random_state=42)
    grid_search_rf = GridSearchCV(rf, param_grid_rf, cv=5, scoring="accuracy")
    grid_search_rf.fit(X_train, y_train)
    print("Best parameters:", grid_search_rf.best_params_)

    # print(dir(grid_search_rf))
    best_rf = grid_search_rf.best_estimator_
    y_pred_rf = best_rf.predict(X_test)
    print("Test accuracy:", accuracy_score(y_test, y_pred_rf))

    importances = best_rf.feature_importances_
    for name, importance in zip(feature_names, importances):
        print(f"{name}: {importance:.2f}")
