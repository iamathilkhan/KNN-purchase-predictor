# KNN Purchase Predictor

A machine learning application that predicts whether a user will purchase an advertised product based on their age and estimated salary using the K-Nearest Neighbors algorithm.

## Features

- Web-based interface for easy prediction
- Trained on social network advertisement data
- Real-time prediction results

## Dataset

- Source: Social_Network_Ads.csv
- Features: Age, Estimated Salary
- Target: Purchase decision (Purchased or Not Purchased)

## Technologies

- Python
- Pandas
- Scikit-learn
- Flask

## Installation

1. Ensure Python is installed on your system.
2. Install required dependencies:
   ```bash
   pip install pandas scikit-learn flask
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to http://127.0.0.1:5000/
3. Enter your age and estimated salary to get a purchase prediction.
