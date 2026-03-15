from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# load dataset (keeping all features!)
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# create and fit LR, Ridge and Lasso regressors
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
y_pred_lr = lr_model.predict(X_test)

ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train, y_train)
y_pred_ridge = ridge_model.predict(X_test)

lasso_model = Lasso(alpha=0.1)
lasso_model.fit(X_train, y_train)
y_pred_lasso = lasso_model.predict(X_test)

# display and compare all results + discussion:
# - what are the differences?
# - what happened to mse?
# - what happened to coefficients?
# - what is conclusion?

print("LR MSE:", mean_squared_error(y_test, y_pred_lr))
print("LR Coefficients:", lr_model.coef_)
print("LR Intercept:", lr_model.intercept_)

print("Ridge MSE:", mean_squared_error(y_test, y_pred_ridge))
print("Ridge Coefficients:", ridge_model.coef_)
print("Ridge Intercept:", ridge_model.intercept_)

print("Lasso MSE:", mean_squared_error(y_test, y_pred_lasso))
print("Lasso Coefficients:", lasso_model.coef_)
print("Lasso Intercept:", lasso_model.intercept_)
