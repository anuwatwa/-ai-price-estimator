
import streamlit as st
import joblib
import numpy as np

# โหลดโมเดล
model = joblib.load("linear_regression_price_model_with_floors.pkl")

# หัวเว็บ
st.title("💡 Beam AI ประมาณราคาก่อสร้างเบื้องต้น")

# ขอบเขตของโมเดล
st.markdown("""
🔍 **ขอบเขตของโมเดล AI นี้**
- เหมาะกับบ้านพักอาศัยทั่วไป 1–2 ชั้น
- โมเดลถูกฝึกจากข้อมูลจริงของแบบบ้านมาตรฐาน
- ตัวแปรที่ใช้: ราคาต่อตร.ม. / พื้นที่ใช้สอยรวม / จำนวนชั้น
""")

# หมายเหตุแบบกรอบเตือน
st.warning("⚠️ โมเดลนี้ไม่รองรับอาคารพิเศษ เช่น บ้านหรู ตึกพาณิชย์ หรืออาคารที่มีโครงสร้างซับซ้อน")

# อินพุตจากผู้ใช้ พร้อมขอบเขตชัดเจน
price_per_sqm = st.number_input("ราคาต่อตารางเมตร (บาท)", min_value=6000, max_value=12000, value=9000, step=100)
area = st.number_input("พื้นที่ใช้สอย (ตร.ม.)", min_value=30.0, max_value=400.0, value=120.0, step=1.0)
floors = st.number_input("จำนวนชั้น", min_value=1, max_value=2, value=2, step=1)

# คำนวณและแสดงผล
if st.button("คำนวณราคาก่อสร้าง"):
    X = np.array([[price_per_sqm, area, floors]])
    y_pred = model.predict(X)
    st.success(f"✅ ราคาประมาณการ: {round(y_pred[0]):,} บาท")

