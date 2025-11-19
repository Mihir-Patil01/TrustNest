import joblib

path = "models/rent_model.pkl"

obj = joblib.load(path)
print("✅ Model file loaded successfully.")
print("Type:", type(obj))
print("Contents:", obj)
