from pathlib import Path

import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "sausaufinal.joblib"


# Učitavanje sačuvanog modela
# Model se ovde ne trenira ponovo, već se koristi prethodno sačuvan pipeline
model = joblib.load(MODEL_PATH)


# Novi primer za predikciju
# Nazivi kolona moraju biti isti kao u trening skupu
new_car = pd.DataFrame([
    {
        "buying": "med",
        "maintenance": "med",
        "doors": "5more",
        "persons": "more",
        "lug_boots": "big",
        "safety": "high"
    }
])


# Predikcija klase
prediction = model.predict(new_car)
predicted_class = prediction[0]


# Opis klasa iz skupa podataka
class_names = {
    "unacc": "neprihvatljiv automobil",
    "acc": "prihvatljiv automobil",
    "good": "dobar automobil",
    "vgood": "veoma dobar automobil"
}


print("Ulazni podaci")
print(new_car)

print("\nPredikcija modela")
print(predicted_class, "-", class_names.get(predicted_class, "nepoznata klasa"))


# Verovatnoće po klasama, ako izabrani model to podržava
if hasattr(model, "predict_proba"):
    probabilities = model.predict_proba(new_car)[0]
    classes = model.classes_

    print("\nVerovatnoće po klasama")
    for class_label, probability in zip(classes, probabilities):
        print(f"{class_label}: {probability:.3f}")
