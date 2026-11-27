
import joblib
import pandas as pd
from feature_extraction import extract_features

# Load trained model
model = joblib.load("models/phishing_model.pkl")

def detect_url(url):

    features = extract_features(url)

    # Convert features into DataFrame
    input_data = pd.DataFrame([features])

    # Predict using ML model
    prediction = model.predict(input_data)[0]

    print("\n===== PHISHING URL DETECTOR =====")
    print("URL:", url)
    print("Predicted Class:", prediction)

    if prediction == 0:
        print("Result: Phishing")
    else:
        print("Result: Legitimate")

if __name__ == "__main__":

    url = input("Enter URL to analyze: ")
    detect_url(url)
