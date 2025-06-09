import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model/model.pkl")

# Atur tampilan halaman
st.set_page_config(page_title="Prediksi Status Mahasiswa", layout="wide")

# Judul
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Prediksi Status Mahasiswa</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #646464;'>Dropout | Enrolled | Graduate</h4>", unsafe_allow_html=True)
st.write("")

# Form input
st.markdown("### Masukkan Nilai Fitur Mahasiswa")
with st.form(key="prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        approved_sem2 = st.number_input("Curricular Units 2nd Sem Approved", min_value=0, max_value=50, step=1)
        grade_sem2 = st.number_input("Curricular Units 2nd Sem Grade", min_value=0.0, max_value=20.0, step=0.1)
        tuition_up_to_date = st.selectbox("Tuition Fees Up To Date", [1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak")
        age = st.number_input("Age at Enrollment", min_value=15, max_value=70, step=1)
        gender = st.selectbox("Gender", [0, 1], format_func=lambda x: "Perempuan" if x == 0 else "Laki-laki")

    with col2:
        approved_sem1 = st.number_input("Curricular Units 1st Sem Approved", min_value=0, max_value=50, step=1)
        grade_sem1 = st.number_input("Curricular Units 1st Sem Grade", min_value=0.0, max_value=20.0, step=0.1)
        scholarship = st.selectbox("Scholarship Holder", [1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak")
        application_mode = st.selectbox("Application Mode", [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 27, 39, 42, 43, 44, 51, 53, 57])
        debtor = st.selectbox("Debtor", [1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak")

    submit_button = st.form_submit_button(label="Prediksi Status Mahasiswa")

# Hasil prediksi
if submit_button:
    input_data = np.array([[
        approved_sem2, approved_sem1, grade_sem2, grade_sem1,
        tuition_up_to_date, scholarship, age, application_mode,
        gender, debtor
    ]])

    pred = model.predict(input_data)[0]
    status_dict = {
        0: ("Dropout", "#FF4B4B"),
        1: ("Enrolled", "#FFC107"),
        2: ("Graduate", "#4CAF50")
    }

    pred_label, color = status_dict[pred]
    st.markdown(
        f"<h3 style='text-align: center;'>Hasil Prediksi:</h3>"
        f"<div style='background-color: {color}; padding: 1rem; border-radius: 10px; text-align: center;'>"
        f"<span style='font-size: 2rem; color: white;'>{pred_label}</span></div>",
        unsafe_allow_html=True
    )
