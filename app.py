import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")

# Judul Aplikasi
st.title("Prediksi Status Mahasiswa (Dropout, Enrolled, Graduate)")

# Input dari pengguna
st.header("Masukkan Nilai Fitur:")

col1, col2 = st.columns(2)

with col1:
    approved_sem2 = st.number_input("Curricular Units 2nd Sem Approved", min_value=0, max_value=50, step=1)
    grade_sem2 = st.number_input("Curricular Units 2nd Sem Grade", min_value=0.0, max_value=20.0, step=0.1)
    tuition_up_to_date = st.selectbox("Tuition Fees Up To Date", [1, 0])
    age = st.number_input("Age at Enrollment", min_value=15, max_value=70, step=1)
    gender = st.selectbox("Gender (0 = Female, 1 = Male)", [0, 1])

with col2:
    approved_sem1 = st.number_input("Curricular Units 1st Sem Approved", min_value=0, max_value=50, step=1)
    grade_sem1 = st.number_input("Curricular Units 1st Sem Grade", min_value=0.0, max_value=20.0, step=0.1)
    scholarship = st.selectbox("Scholarship Holder", [1, 0])
    application_mode = st.selectbox("Application Mode (contoh: 1, 17, 39)", [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 27, 39, 42, 43, 44, 51, 53, 57])
    debtor = st.selectbox("Debtor (1 = Ya, 0 = Tidak)", [1, 0])

# Buat prediksi
if st.button("Prediksi Status Mahasiswa"):
    input_data = np.array([[
        approved_sem2, approved_sem1, grade_sem2, grade_sem1,
        tuition_up_to_date, scholarship, age, application_mode,
        gender, debtor
    ]])

    pred = model.predict(input_data)[0]
    status_dict = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    st.success(f"Prediksi Status Mahasiswa: **{status_dict[pred]}**")
