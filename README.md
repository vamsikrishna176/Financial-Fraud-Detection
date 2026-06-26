# 💳 Financial Fraud Detection using Machine Learning

## 📌 Overview

This project detects fraudulent credit card transactions using a Random Forest Classifier. It includes a machine learning model and a Streamlit web application for predicting whether a transaction is Fraud or Normal.

## 🚀 Features

- Credit Card Fraud Detection
- Data Preprocessing
- Random Forest Classifier
- Model Evaluation
- Streamlit Web Application
- Interactive Prediction Interface

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib

## 📂 Project Structure

```
Financial-Fraud-Detection/
│── data/
│── models/
│── app.py
│── train_model.py
│── predict.py
│── requirements.txt
│── README.md
```

## ⚠️ Note

The dataset (`creditcard.csv`) and trained model (`fraud_model.pkl`) are **not included** in this repository because of their large file size.

To generate the trained model, run:

```bash
python train_model.py
```

After the model is created, launch the Streamlit application:

```bash
streamlit run predict.py
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/vamsikrishna176/Financial-Fraud-Detection.git
```

Go to the project folder:

```bash
cd Financial-Fraud-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train_model.py
```

Run the application:

```bash
streamlit run predict.py
```

## 👨‍💻 Author

**Bollu Vamsi Krishna**

GitHub: https://github.com/vamsikrishna176