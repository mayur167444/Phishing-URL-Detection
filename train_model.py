
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
data = pd.read_csv("dataset/LegitPhish Dataset/url_features_extracted1.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)

# Remove rows with missing target labels
data = data.dropna(subset=["ClassLabel"])

# Separate features and labels
X = data.drop(columns=["URL", "ClassLabel"])
y = data["ClassLabel"].astype(int)

# Handle missing feature values
X = X.apply(pd.to_numeric, errors="coerce")
X = X.fillna(0)

# Handle missing values
X = X.fillna(0)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

# Train model
print("\nTraining model...")
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

print("\n===== MODEL RESULTS =====")
print("Accuracy:", accuracy_score(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Save model
joblib.dump(model, "models/phishing_model.pkl")

print("\nModel saved successfully as phishing_model.pkl")
