# Phishing URL Detection Using Machine Learning

A Python-based cybersecurity project that uses a Random Forest machine learning algorithm to classify URLs as potentially phishing or legitimate.

## Features

- URL feature extraction
- Machine learning-based URL classification
- Random Forest classifier
- Dataset-based model training
- Prediction of phishing and legitimate URLs

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- Regular Expressions

## Project Structure

```text
Phishing-URL-Detection/
├── dataset/
├── models/
│   └── phishing_model.pkl
├── detector.py
├── feature_extraction.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Phishing-URL-Detection
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Train the Model

```bash
python3 train_model.py
```

## Run the Detector

```bash
python3 detector.py
```

Enter a URL when prompted to receive a prediction.

## Model Performance

The current test split achieved approximately 99.98% accuracy. This result is preliminary and requires further validation against data leakage and real-world URLs.

## Disclaimer

This project is for educational and cybersecurity research purposes only. Predictions are not a guarantee that a URL is safe or malicious.

## Author

Mayur Deveedutta Maharana