from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from feature_extraction import extract_features

app = FastAPI()

model = joblib.load("model.pkl")

class URLRequest(BaseModel):
    url: str

@app.post("/predict")
def predict(request: URLRequest):

    features = extract_features(request.url)
    prediction = model.predict([features])[0]

    if prediction == -1:
        result = "Phishing"
    else:
        result = "Safe"

    return {"prediction": result}
