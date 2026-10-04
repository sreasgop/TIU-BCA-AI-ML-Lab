# Question: 
# 2. Implement Logistic Regression for binary classification and evaluate the model using Accuracy and Confusion Matrix.



# Code: 
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report

# 1. Load the real-world binary classification dataset
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target  # 0: Malignant, 1: Benign

# 2. Split dataset into train (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Standardize features (recommended for Logistic Regression gradient convergence)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train the Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# 5. Predict labels on the test set
y_pred = model.predict(X_test_scaled)

# 6. Evaluation Deliverables: Accuracy and Confusion Matrix
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"Accuracy Score: {acc * 100:.2f}%\n")
print("Confusion Matrix:")
print(cm)
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=cancer.target_names))

# 7. Plot Confusion Matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=cancer.target_names)
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix - Logistic Regression (Breast Cancer)")
plt.tight_layout()
plt.show()



# Output: 
# Accuracy Score: 98.25%

# Confusion Matrix:
# [[41  1]
#  [ 1 71]]

# Classification Report:
#               precision    recall  f1-score   support

#    malignant       0.98      0.98      0.98        42
#       benign       0.99      0.99      0.99        72

#     accuracy                           0.98       114
#    macro avg       0.98      0.98      0.98       114
# weighted avg       0.98      0.98      0.98       114