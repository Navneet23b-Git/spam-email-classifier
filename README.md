# 📧 NoEmailSpam – Email Spam Detection API

A Machine Learning based Email Spam Detection web application built using Flask and deployed on Vercel.

## 🚀 Live Demo
🔗 https://your-vercel-url.vercel.app

---

## 📌 Project Overview

This project uses Natural Language Processing (NLP) and Machine Learning to classify emails/messages as:

- 🚨 **SPAM**
- ✅ **HAM (Not Spam)**

The model was trained offline and deployed using a lightweight Flask API.

---

## 🧠 Machine Learning Details

- Text Cleaning (Lowercase + Punctuation Removal)
- CountVectorizer (Top 3000 features)
- Multiple Models Tested:
  - Naive Bayes
  - Logistic Regression (SGD)
  - KNN
- Best performing model selected based on accuracy
- Model saved using `pickle`

---

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-Learn
- HTML + CSS
- JavaScript (Fetch API)
- Vercel (Deployment)
- GitHub (Version Control)

---
## 📂 Project Structure

```bash
EmailSpamDetection/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── vercel.json
└── templates/
    └── index.html
```

## ⚙️ How It Works

1. User enters email text.
2. Frontend sends POST request to `/predict`.
3. Flask loads saved model.
4. Model predicts SPAM or HAM.
5. Result is displayed instantly.

---

## 👨‍💻 Author

Navneet  
B.Tech CSE | Machine Learning Enthusiast

---

⭐ If you like this project, feel free to star the repository!
