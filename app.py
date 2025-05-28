
import streamlit as st
import joblib
import numpy as np

model = joblib.load("linear_regression_price_model_with_floors.pkl")

st.title("🚧 ระบบพยากรราคาก่อสร้างเบื้องต้น")

price_per_sqm = st.number_input("ราคาต่อตารางเมตร (บาท):", value=9000)
area = st.number_input("พื้นที่ใช้สอย (ตร.ม.):", value=120)
floors = st.number_input("จำนวนชั้น:", value=2)

if st.button("คำนวณราคาก่อสร้าง"):
    x = np.array([[price_per_sqm, area, floors]])
    y_pred = model.predict(x)
    st.success(f"✅ ราคาประมาณการ: {round(y_pred[0]):,} บาท")
