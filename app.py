# app.py

from flask import Flask, request, render_template, send_file
import pickle
import pandas as pd
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open('fraud_detection_xgboost.pkl', 'rb') as file:
    model = pickle.load(file)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download-sample')
def download_sample():
    return send_file("transactions_demo.csv", as_attachment=True)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Uploaded file
        uploaded_file = request.files['file']
        if not uploaded_file:
            return render_template('index.html', prediction_text="⚠️ No file uploaded.")

        # Read CSV file into DataFrame
        df = pd.read_csv(uploaded_file)

        # Check if enough features are provided
        if df.shape[1] < 1:
            return render_template('index.html', prediction_text="⚠️ Uploaded file has no features.")

        # Predict on entire batch
        predictions = model.predict(df)

        # Summarize results
        total = len(predictions)
        frauds = np.sum(predictions == 1)
        safes = np.sum(predictions == 0)

        prediction_text = f"✅ {safes} safe transactions detected. 🚨 {frauds} fraudulent transactions detected."

        return render_template('index.html', prediction_text=prediction_text)

    except Exception as e:
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


