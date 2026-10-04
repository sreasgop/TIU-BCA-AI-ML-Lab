# Question: 
# 1. Implement Linear Regression on a dataset and visualize the regression line.



# Code: 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load the Diabetes dataset
diabetes = load_diabetes()

# Use one feature (BMI, index 2) so the regression line can be plotted in 2D
# np.newaxis transforms the 1D slice into a 2D array of shape (n_samples, 1)
X = diabetes.data[:, np.newaxis, 2]
y = diabetes.target

# 2. Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Make predictions on the test set
y_pred = model.predict(X_test)

# 5. Evaluate model performance
print(f"Slope (Coefficient): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred):.2f}")
print(f"R² Score: {r2_score(y_test, y_pred):.4f}")

# 6. Visualize the data points and the fitted regression line
plt.figure(figsize=(8, 5))

# Plot actual test data points
plt.scatter(X_test, y_test, color='black', label='Actual Test Data')

# Plot the regression line using predictions on X_test
plt.plot(X_test, y_pred, color='blue', linewidth=2, label='Regression Line')

plt.title('Linear Regression on Diabetes Dataset (BMI vs Disease Progression)')
plt.xlabel('Normalized Body Mass Index (BMI)')
plt.ylabel('Disease Progression Measure')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



# Output:
# Slope (Coefficient): 998.58
# Intercept: 152.00
# Mean Squared Error (MSE): 4061.83
# R² Score: 0.2334