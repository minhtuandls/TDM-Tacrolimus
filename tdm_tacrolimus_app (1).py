
import streamlit as st
import math

st.title("TDM Tacrolimus Calculator")
st.write("**Prototype App - Dựa trên mô hình Excel**")

st.header("1. Nhập dữ liệu")
ten_benh_nhan = st.text_input("Tên bệnh nhân")
tuoi = st.number_input("Tuổi", min_value=0, max_value=120, step=1)
can_nang = st.number_input("Cân nặng (kg)", min_value=0.0, step=0.1)
lieu_hien_tai = st.number_input("Liều hiện tại (mg/ngày)", min_value=0.0, step=0.1)

st.header("2. Nhập nồng độ")
concentration_now = st.number_input("Nồng độ đáy hiện tại (ng/mL)", min_value=0.0, step=0.1)

target_options = {
    "Giai đoạn ghép sớm (8 ng/mL)": 8,
    "Giai đoạn duy trì (5 ng/mL)": 5,
    "Nguy cơ thải ghép cao (10 ng/mL)": 10
}
target_choice = st.selectbox("Chọn nồng độ mục tiêu", list(target_options.keys()))
target_concentration = target_options[target_choice]

if st.button("Tính toán"):
    if concentration_now > 0:
        new_dose = lieu_hien_tai * target_concentration / concentration_now
        rounded_dose = round(new_dose / 0.5) * 0.5
        split_dose = rounded_dose / 2

        st.success(f"Liều khuyến nghị mới: {new_dose:.2f} mg/ngày")
        st.info(f"Liều sau làm tròn: {rounded_dose:.1f} mg/ngày")
        st.info(f"Chia 2 lần/ngày: {split_dose:.1f} mg/mỗi lần")

        if rounded_dose > 10:
            st.warning("**Cảnh báo:** Liều sau khi làm tròn >10 mg/ngày")

        if concentration_now < 3 or concentration_now > 20:
            st.warning("**Cảnh báo:** Nồng độ đáy bất thường (<3 hoặc >20 ng/mL)")
    else:
        st.error("Vui lòng nhập nồng độ đáy hiện tại lớn hơn 0.")
