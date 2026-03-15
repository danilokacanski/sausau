from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# load data
iris = load_iris()
X = iris.data
y = iris.target

# split dataset (stratify!)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# create and train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# make predictions
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap="Blues")
plt.show()

# save model
# with open(f"iris_model.pkl", "wb") as file:
#     pickle.dump(model, file)

# X_test[0] = [4.4 3.  1.3 0.2]
# print(model.predict(X_test[0].reshape(1, -1)))
# [0]
