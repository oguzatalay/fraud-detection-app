# 🔍 Fraud Detection Web App

**End-to-end credit card fraud detection with machine learning & web deployment.**

---

## 📈 Project Overview

This project aims to build a **user-friendly web application** that detects fraudulent credit card transactions using machine learning. Users upload a transaction file (CSV format), and the system instantly reports how many transactions are **safe** and how many are **fraudulent**.

The application is designed to be understandable even for users without technical background.

---

## 🛠️ How to Use This App

This app is currently in **demo mode** and is designed to help users test how the fraud detection system works — no real bank data required.

Follow the steps below to experience how it functions:

### ✅ Step-by-Step Instructions

#### 1. 🔍 Download the Sample File  
Look for the green button labeled **“Download Sample CSV”**.  
🔹 This file contains dummy transaction data, including a few fraudulent entries so you can test the system properly.

![image](https://github.com/user-attachments/assets/beffdb62-72a6-4940-b5e5-d32c66e2321f)

#### 2. 📂 Upload the CSV File  
Click the **“Choose File”** button to select the sample file you just downloaded.  
🔹 Once selected, the file name should appear next to the button.  
Then click the blue **“Predict Fraud”** button.

![image](https://github.com/user-attachments/assets/4498e6f3-f120-415e-81df-8691a9b5cf8e)

#### 3. 📊 View the Results  
The app will instantly analyze the data and return:  
✅ Number of safe transactions detected  
🚨 Number of fraudulent transactions caught

![image](https://github.com/user-attachments/assets/87e1eaf6-7864-4bed-87da-cafa1c60cc5e)

---

### 🌟 Demo Limitation Note

This interface is a **prototype** for demonstration purposes only.

- In a real-world deployment, the uploaded file structure would be securely defined to match real bank transaction schemas.
- No real data is stored or processed.

---

## 📚 Key Features

- 📁 **File Upload Interface** – Upload your own transaction CSV file
- 🚀 **Real-Time Prediction** – Instant detection of frauds
- 📥 **Sample File Download** – No data? No problem. Try the system with a sample file
- 🎨 **Stylish & Interactive UI** – Animated buttons and modern design

---

## 🧵 Behind the Scenes

- ✅ Data preprocessing with scaling & class balancing (SMOTE)
- ✅ Multiple ML models tested: Logistic Regression, SMOTE-enhanced, and XGBoost
- ✅ XGBoost selected for final deployment with `scale_pos_weight` to handle imbalance
- ✅ Flask used to build backend API & render web interface
- ✅ Hosted on Render (Free tier)

---

## 📊 Why It Matters

- 🏦 Financial institutions lose millions to fraud annually
- 🙋‍♂️ Customers are protected when fraud is caught early
- 🧠 Machine learning gives businesses the upper hand

This app is a small but effective demonstration of what is possible.

---

## 🙏 Thank You!

This project is dedicated to making **complex technology accessible to everyone.**  
Let’s detect fraud — the smart way. 💼💙

# This project was handcrafted with curiosity, caffeine, and a surprising number of unexpected bugs.
```
