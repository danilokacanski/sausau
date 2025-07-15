import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf = DecisionTreeClassifier(random_state=0)
path = clf.cost_complexity_pruning_path(X_train, y_train)

# potential effective pruning parameters
ccp_alphas = path.ccp_alphas

clfs = []
for alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=0, ccp_alpha=alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)

# last clasffifier removal (with 1 node) - most pruned one
clfs = clfs[:-1]
ccp_alphas = ccp_alphas[:-1]

depths = [clf.tree_.max_depth for clf in clfs]
train_accuracies = [clf.score(X_train, y_train) for clf in clfs]
test_accuracies = [clf.score(X_test, y_test) for clf in clfs]

fig, ax = plt.subplots(2, 1, figsize=(8, 10))

# 1st subplot: depth / cc_alpha
ax[0].plot(ccp_alphas, depths, marker="o", color="green", drawstyle="steps-post")
ax[0].set_xlabel("ccp_alpha")
ax[0].set_ylabel("Depth")
ax[0].set_title("Depth / ccp_alpha")

# 2nd subplot: accuracy / ccp_alpha
ax[1].plot(
    ccp_alphas,
    train_accuracies,
    marker="o",
    label="Train data",
    drawstyle="steps-post",
)
ax[1].plot(
    ccp_alphas, test_accuracies, marker="o", label="Test data", drawstyle="steps-post"
)
ax[1].set_xlabel("ccp_alpha")
ax[1].set_ylabel("Accuracy")
ax[1].set_title("Accuracy / ccp_alpha")
ax[1].legend()

plt.tight_layout()
plt.show()
