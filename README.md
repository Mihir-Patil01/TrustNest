# TrustNest : AI Based accommodation assistant

TrustNest – Smart Accommodation System

An AI-powered desktop application that helps users find the best rental accommodations such as Flats, PGs, and Hostels based on location, price, livability, amenities, and personal preferences.

🚀 Overview

TrustNest is a JavaFX-based intelligent rental search system that provides users with personalized accommodation recommendations.
The system integrates AI/ML (Python backend + Flask API) to predict fair rent prices, classify listings, and enhance decision-making.

The app supports:
✔ Searching flats, PGs, and hostels
✔ Filtering by budget, location, BHK, type
✔ Owner listing system
✔ Student-friendly preference filtering
✔ AI-powered fairness check (backend-enabled)
✔ Clean UI with dynamic listing cards

🏗 Tech Stack
Frontend:
Java
JavaFX
Scene Builder
JSON & HTTP communication (via OkHttp)

Backend
Python
Flask API
Pandas
Scikit-learn
Joblib
Trained ML models (.pkl)
Data Storage
Local CSV for listings
In-memory user storage
Real-time backend responses for AI predictions

🔥 Features
User Side
Browse and search accommodations
Apply filters (Budget, Location, Type, BHK, Amenities)
View rental fairness (Predicted vs Listed price)
Mark favorites
Owner Side
Add property listings with images
Automatically visible on client UI

AI Features
Preference-based ranking
Rent fairness classification
Predicted price generation


📁 Project Structure
TrustNest/
│
├── frontend/
│   ├── TrustNestApp.java
│   ├── models/
│   └── ui/
│
├── backend/
│   ├── app.py (Flask)
│   ├── models/rent_model.pkl
│   └── data/flats.csv
│
└── README.md


🔌 How It Works
1. User interacts through JavaFX UI

Search → Enter filters → Click Search


2. JavaFX sends POST request

Backend URL such as:

http://<server-ip>:5000/search


3. Flask backend processes request

Loads ML model → Filters flats → Predicts rent → Returns JSON


4. JavaFX displays results

Dynamic UI cards display:
Name
Location
Price
Predicted Rent
Fairness

🧪 How to Run
Frontend 
javac TrustNestApp.java
java TrustNestApp

Backend 
python app.py


Backend server example:

http://192.168.x.x:5000


👨‍💻 My Role
You developed the entire frontend using JavaFX and handled local data storage, UI design, filtering system, user flow, and integration logic.


🎯 Outcome
A fully working, smart accommodation system with:
Clean UI
Owner + User flows
Intelligent recommendations
Real-time backend communication




