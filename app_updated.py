
import streamlit as st
import joblib
import numpy as np

# โหลดโมเดล
model = joblib.load("linear_regression_price_model_with_floors.pkl")

# หัวเว็บ
st.title("💡 Beam AI ประมาณราคาก่อสร้างเบื้องต้น")

# ขอบเขตของโมเดล (markdown)
st.markdown("""
🔍 **ขอบเขตของโมเดล AI นี้**
- ใช้สำหรับพยากรณ์ราคาก่อสร้าง *เบื้องต้น*
- เหมาะกับบ้านพักอาศัยทั่วไปที่มี **1–2 ชั้น**
- โมเดลเรียนรู้จากข้อมูลจริงของแบบบ้านมาตรฐานจำนวน 9 แบบ
- ปัจจัยที่ใช้ในการพยากรณ์:
  - ✅ ราคาต่อตารางเมตร (บาท/ตร.ม.)
  - ✅ พื้นที่ใช้สอยรวม (ตร.ม.)
  - ✅ จำนวนชั้นของอาคาร
""")

# กรอบคำเตือน
st.warning("⚠️ โมเดลนี้ไม่รองรับอาคารพิเศษ เช่น บ้านหรู, ตึกพาณิชย์, หรืออาคารเฉพาะทางที่มีโครงสร้างซับซ้อน")

# อินพุตจากผู้ใช้ พร้อมกำหนดขอบเขต
price_per_sqm = st.number_input("ราคาต่อตารางเมตร (บาท):", min_value=6000, max_value=12000, value=9000)
area = st.number_input("พื้นที่ใช้สอย (ตร.ม.):", min_value=30, max_value=400, value=120)
floors = st.number_input("จำนวนชั้น:", min_value=1, max_value=2, value=2)

# ทำนายราคาก่อสร้าง
if st.button("คำนวณราคาก่อสร้าง"):
    x = np.array([[price_per_sqm, area, floors]])
    y_pred = model.predict(x)
    st.success(f"✅ ราคาประมาณการ: {round(y_pred[0]):,} บาท")
