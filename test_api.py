import requests
import json

# Base URL (use your actual host if needed)
BASE_URL = "http://127.0.0.1:5000"

# Prepare test payload (this should match the Flask backend format)
payload = {
    "location": "Pune",
    "size_sqft": 850,
    "bhk": 2,
    "asking_rent": 12000,
    "amenities": {"wifi": 1, "parking": 1, "lift": 0, "ac": 1}
}

# 1️⃣ Test health route
try:
    health = requests.get(f"{BASE_URL}/health")
    print("Health Check:", health.status_code, health.text)
except Exception as e:
    print("❌ Health check failed:", e)

# 2️⃣ Test predict route
try:
    print("\n➡️ Sending payload to /predict:", json.dumps(payload, indent=2))
    res = requests.post(f"{BASE_URL}/predict", json=payload)

    print("Status Code:", res.status_code)
    if res.status_code == 200:
        print("✅ JSON Response:")
        print(json.dumps(res.json(), indent=2))
    else:
        print("⚠️ Raw Response:", res.text)
except Exception as e:
    print("❌ Error sending request:", e)
