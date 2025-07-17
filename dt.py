from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=0),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=0),
    "Gradient Boosting": GradientBoostingClassifier(
        n_estimators=100, learning_rate=0.1, random_state=0
    ),
}

for name, model in models.items():
    print(f"------------------------ Training {name} model ------------------------ ")
    print()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    if name == "Decision Tree":
        plt.figure(figsize=(15, 12))
        plot_tree(
            model,
            filled=True,
            feature_names=data.feature_names,
            class_names=data.target_names,
        )
        plt.show()

    print(classification_report(y_test, y_pred, target_names=data.target_names))
