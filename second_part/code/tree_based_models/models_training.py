import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(
        n_estimators=100, learning_rate=0.1, random_state=42
    ),
}

for name, model in models.items():
    print(f"\n---------- {name} ----------\n")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    if name == "Decision Tree":
        plt.figure(figsize=(20, 10))
        plot_tree(
            model,
            filled=True,
            feature_names=data.feature_names,
            class_names=data.target_names,
            rounded=True,
        )
        plt.title("Decision Tree")
        plt.show()

    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=data.target_names))
