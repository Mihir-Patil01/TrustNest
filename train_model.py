# train_model.py
import pandas as pd
import os
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# -------------------- PATHS --------------------
BASE = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE, "data", "flats.csv")
MODEL_PATH = os.path.join(BASE, "models", "rent_model.pkl")

# -------------------- LOAD DATA --------------------
df = pd.read_csv(DATA_PATH)

# Handle missing columns gracefully
for col in ["size", "rooms", "area", "number_of_bhk"]:
    if col not in df.columns:
        df[col] = 0

# Fill missing values
df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)
df["size"] = pd.to_numeric(df["size"], errors="coerce").fillna(0)
df["rooms"] = pd.to_numeric(df["rooms"], errors="coerce").fillna(0).astype(int)
df["area"] = pd.to_numeric(df["area"], errors="coerce").fillna(0)
df["number_of_bhk"] = pd.to_numeric(df["number_of_bhk"], errors="coerce").fillna(0).astype(int)
df["amenities"] = df["amenities"].fillna("")
df["lifestyle"] = df["lifestyle"].fillna("")

# -------------------- FEATURE ENGINEERING --------------------
df["amen_count"] = df["amenities"].apply(lambda x: len(x.split("|")) if x else 0)

le_location = LabelEncoder()
df["loc_enc"] = le_location.fit_transform(df["location"].astype(str))

le_connectivity = LabelEncoder()
le_utility = LabelEncoder()
le_lifestyle = LabelEncoder()

df["connectivity_enc"] = le_connectivity.fit_transform(df["connectivity"].astype(str))
df["utility_enc"] = le_utility.fit_transform(df["utility"].astype(str))
df["lifestyle_enc"] = le_lifestyle.fit_transform(df["lifestyle"].astype(str))

# -------------------- MODEL TRAINING --------------------
X = df[["size", "rooms", "area", "number_of_bhk", "amen_count", "loc_enc",
         "connectivity_enc", "utility_enc", "lifestyle_enc"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, preds))
print("R2:", r2_score(y_test, preds))

# -------------------- SAVE MODEL AS .PKL --------------------
bundle = {
    "model": model,
    "le_location": le_location,
    "le_connectivity": le_connectivity,
    "le_utility": le_utility,
    "le_lifestyle": le_lifestyle
}

os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

with open(MODEL_PATH, "wb") as f:
    pickle.dump(bundle, f)

print(f"✅ Model trained and saved as PKL at {MODEL_PATH}")
