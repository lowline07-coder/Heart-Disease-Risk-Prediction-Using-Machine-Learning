import streamlit as st
import pickle
import pandas as pd

model = pickle.load(
    open("heart_disease_model.pkl", "rb")
)

scaler = pickle.load(
    open("heart_scaler.pkl", "rb")
)

st.title("Heart Disease Prediction")

age = st.number_input("Age", 1, 120, 40)

sex = st.selectbox(
    "Sex",
    ["M", "F"]
)

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["ATA", "NAP", "ASY", "TA"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure",
    50,
    250,
    120
)

cholesterol = st.number_input(
    "Cholesterol",
    50,
    700,
    200
)

fasting_bs = st.selectbox(
    "Fasting Blood Sugar",
    [0, 1]
)

resting_ecg = st.selectbox(
    "Resting ECG",
    ["Normal", "LVH", "ST"]
)

max_hr = st.number_input(
    "Maximum Heart Rate",
    50,
    250,
    150
)

exercise_angina = st.selectbox(
    "Exercise Angina",
    ["Y", "N"]
)

oldpeak = st.number_input(
    "Old Peak",
    0.0,
    10.0,
    1.0
)

st_slope = st.selectbox(
    "ST Slope",
    ["Up", "Flat", "Down"]
)

input_df = pd.DataFrame({
    'Age':[age],
    'RestingBP':[resting_bp],
    'Cholesterol':[cholesterol],
    'FastingBS':[fasting_bs],
    'MaxHR':[max_hr],
    'Oldpeak':[oldpeak]
})

input_df['Sex_M'] = 1 if sex == "M" else 0

input_df['ChestPainType_ATA'] = 1 if chest_pain == "ATA" else 0
input_df['ChestPainType_NAP'] = 1 if chest_pain == "NAP" else 0
input_df['ChestPainType_TA'] = 1 if chest_pain == "TA" else 0

input_df['RestingECG_Normal'] = 1 if resting_ecg == "Normal" else 0
input_df['RestingECG_ST'] = 1 if resting_ecg == "ST" else 0

input_df['ExerciseAngina_Y'] = 1 if exercise_angina == "Y" else 0

input_df['ST_Slope_Flat'] = 1 if st_slope == "Flat" else 0
input_df['ST_Slope_Up'] = 1 if st_slope == "Up" else 0

input_scaled = scaler.transform(input_df)

if st.button("Predict"):

    prediction = model.predict(
        input_scaled
    )

    if prediction[0] == 1:

        st.error(
            "Heart Disease Detected"
        )

    else:

        st.success(
            "No Heart Disease Detected"
        )