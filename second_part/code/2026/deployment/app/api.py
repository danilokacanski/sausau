from pathlib import Path
from typing import Literal

import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel


# Kreiranje FastAPI aplikacije
# ovo se prikazuje u automatskoj dokumentaciji na /docs
app = FastAPI(
    title="Car Evaluation API",
    description="API for predicting car acceptability class using a saved ML pipeline.",
    version="1.0"
)


# Putanja do glavnog foldera projekta i sačuvanog modela
BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "sausaufinal.joblib"


# Učitavanje sačuvanog pipeline-a
model = joblib.load(MODEL_PATH)


# Opis ulaznih podataka koje API očekuje
# Literal ograničava vrednosti koje korisnik može da pošalje
class CarInput(BaseModel):
    buying: Literal["vhigh", "high", "med", "low"]
    maintenance: Literal["vhigh", "high", "med", "low"]
    doors: Literal["2", "3", "4", "5more"]
    persons: Literal["2", "4", "more"]
    lug_boots: Literal["small", "med", "big"]
    safety: Literal["low", "med", "high"]


# Opis klasa iz skupa podataka
class_names = {
    "unacc": "neprihvatljiv automobil",
    "acc": "prihvatljiv automobil",
    "good": "dobar automobil",
    "vgood": "veoma dobar automobil"
}


# Početna ruta (za proveru da li je API pokrenut)
@app.get("/")
def home():
    return {
        "message": "Car Evaluation API is running."
    }


# Ruta za predikciju
# API prima podatke o automobilu, priprema ih u DataFrame formatu i vraća predikciju modela
@app.post("/predict")
def predict(car: CarInput):
    input_data = pd.DataFrame([
        {
            "buying": car.buying,
            "maintenance": car.maintenance,
            "doors": car.doors,
            "persons": car.persons,
            "lug_boots": car.lug_boots,
            "safety": car.safety
        }
    ])

    prediction = model.predict(input_data)[0]

    response = {
        "prediction": str(prediction),
        "description": class_names.get(prediction, "nepoznata klasa")
    }

    # Ako model podržava predict_proba, vraćaju se i verovatnoće po klasama
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)[0]
        classes = model.classes_

        response["probabilities"] = {
            str(class_label): round(float(probability), 3)
            for class_label, probability in zip(classes, probabilities)
        }

    return response


# Pokretanje API-ja iz glavnog foldera projekta
# uvicorn app.api:app --reload

# Otvoriti http://127.0.0.1:8000/docs
