import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# ---------------- LOAD CSV ----------------
df = pd.read_csv(r"C:\\Users\\mihir\\OneDrive\\Desktop\\AIProject\\TRUSTNESTFX\\trustnestfx\\ml_model\\Metro_House_Rent.csv")

# ---------------- TARGET COLUMN ----------------
target = "rent_amount"  # EXACT column name from your screenshot

# ---------------- CONVERT CATEGORICAL → NUMBERS ----------------
df = pd.get_dummies(df, drop_first=True)

# ---------------- SPLIT X / y ----------------
X = df.drop(target, axis=1)
y = df[target]

# ---------------- TRAIN ----------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# ---------------- SAVE MODEL ----------------
joblib.dump(model, "rent_model.pkl")

print("MODEL TRAINED ✅")
print("Saved model as rent_model.pkl")
