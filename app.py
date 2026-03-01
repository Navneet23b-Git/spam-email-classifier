from flask import Flask, request, jsonify
import pickle
import re
import string

app = Flask(__name__)

# Load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(f'[{string.punctuation}]', '', text)
    return text

@app.route("/")
def home():
    return "Email Spam Detection API Running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["email"]
    cleaned = clean_text(data)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    result = "SPAM 🚨" if prediction == 1 else "HAM ✅"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run()