from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

X = np.array([
    [10,1,1,0,0,0],
    [120,0,5,1,3,1],
    [15,1,2,0,0,0],
    [200,0,7,1,5,1],
    [25,1,1,0,0,0]
])

y = [1, -1, 1, -1, 1]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model created successfully.")
