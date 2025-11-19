# models/model.py
import pickle
import numpy as np

def load_model(model_path):
    """Load the trained model and encoders from a .pkl file."""
    with open(model_path, "rb") as f:
        bundle = pickle.load(f)
    return bundle


def predict_rent(flat, bundle):
    """Predict rent price for a given flat dictionary."""
    try:
        model = bundle["model"]
        le_location = bundle["le_location"]
        le_connectivity = bundle["le_connectivity"]
        le_utility = bundle["le_utility"]
        le_lifestyle = bundle["le_lifestyle"]

        # Prepare features
        X = [[
            float(flat.get("size", 0)),
            int(flat.get("rooms", 0)),
            float(flat.get("area", 0)),
            int(flat.get("number_of_bhk", 0)),
            len(flat.get("amenities", "").split("|")) if flat.get("amenities") else 0,
            
            # Safe encoding — if unseen category, fallback to 0
            le_location.transform([flat["location"]])[0] if flat.get("location") in le_location.classes_ else 0,
            le_connectivity.transform([flat["connectivity"]])[0] if flat.get("connectivity") in le_connectivity.classes_ else 0,
            le_utility.transform([flat["utility"]])[0] if flat.get("utility") in le_utility.classes_ else 0,
            le_lifestyle.transform([flat["lifestyle"]])[0] if flat.get("lifestyle") in le_lifestyle.classes_ else 0
        ]]

        pred = model.predict(X)[0]
        return round(float(pred), 2)

    except Exception as e:
        print("⚠️ Prediction error:", e)
        return 0.0
