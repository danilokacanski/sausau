from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


# Osnovna podešavanja Streamlit aplikacije
st.set_page_config(
    page_title="Car Evaluation App",
    page_icon="🚗",
    layout="centered"
)


# Putanja do glavnog foldera projekta i sačuvanog modela
BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "sausaufinal.joblib"


# Učitavanje sačuvanog pipeline-a
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()


# Opis klasa iz skupa podataka
class_names = {
    "unacc": "Unacceptable",
    "acc": "Acceptable",
    "good": "Good",
    "vgood": "Very good"
}


# Naslov i kratak opis aplikacije
st.title("Car Evaluation App")

st.write(
    "This application predicts the acceptability class of a car "
    "based on its basic characteristics."
)


# Korisnički unos
st.subheader("Car characteristics")

col1, col2 = st.columns(2)

with col1:
    buying = st.selectbox("Buying price", ["vhigh", "high", "med", "low"])
    doors = st.selectbox("Number of doors", ["2", "3", "4", "5more"])
    lug_boots = st.selectbox("Luggage boot size", ["small", "med", "big"])

with col2:
    maintenance = st.selectbox("Maintenance price", ["vhigh", "high", "med", "low"])
    persons = st.selectbox("Number of persons", ["2", "4", "more"])
    safety = st.selectbox("Safety level", ["low", "med", "high"])


# Predikcija
if st.button("Predict car class"):
    input_data = pd.DataFrame([
        {
            "buying": buying,
            "maintenance": maintenance,
            "doors": doors,
            "persons": persons,
            "lug_boots": lug_boots,
            "safety": safety
        }
    ])

    prediction = model.predict(input_data)[0]

    st.subheader("Result")

    st.write("Input data")
    st.dataframe(input_data)

    st.success(f"Prediction: {prediction} - {class_names[prediction]}")

    # Prikaz verovatnoća po klasama, ako izabrani model to podržava
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)[0]
        classes = model.classes_

        probability_data = pd.DataFrame({
            "class": classes,
            "probability": probabilities
        })

        st.write("Prediction probabilities")
        st.dataframe(probability_data)


# Pokretanje UI aplikacije iz glavnog foldera projekta:
# streamlit run app/ui.py

# Aplikacija će se otvoriti u browseru
