import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# load existing dataset
diabetes = datasets.load_diabetes()

# select only one feature
bmi = diabetes.data[:, 3]
X = bmi.reshape(-1, 1)
y = diabetes.target

# split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# create and fit model
model = LinearRegression()
model.fit(X_train, y_train)

# make predictions for test data
y_pred = model.predict(X_test)

# calculate and show metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2_score = r2_score(y_test, y_pred)

print(f"Mean squared error (MSE): {mse}")
print(f"Mean squared error (MAE): {mae}")
print(f"Coefficient of determination {r2_score}")

# plot results
plt.scatter(X_test, y_test, color="black", label="Actual data")
plt.plot(X_test, y_pred, color="blue", linewidth=2, label="Linear regression line")
plt.xlabel("BMI")
plt.ylabel("Diabetes progression")
plt.legend()
plt.title("Linear Regression on Diabetes Dataset")
plt.show()
