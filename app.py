from flask import Flask, request, jsonify
import joblib
from feature_extraction import extract_features

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "SecureURL AI Flask Backend Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if "url" not in data:
        return jsonify({"error": "No URL provided"}), 400

    url = data["url"]
    features = extract_features(url)

    prediction = model.predict([features])[0]

    if prediction == -1:
        result = "Phishing"
    else:
        result = "Safe"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
