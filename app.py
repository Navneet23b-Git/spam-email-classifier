from flask import Flask, render_template, request, jsonify
import pickle
import re
import string

app = Flask(__name__)

# Load trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    return text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json.get("message")

    if not data:
        return jsonify({"error": "Empty message"}), 400

    cleaned = clean_text(data)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    label = "SPAM" if prediction == 1 else "HAM"

    return jsonify({"label": label})

if __name__ == "__main__":
    app.run(debug=True)