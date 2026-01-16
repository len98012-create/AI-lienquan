import streamlit as st
from core.data_manager import DataManager

st.title("🎮 Command Center - AI Liên Quân")
dm = DataManager()

if st.button("Kích hoạt Bypass Garena"):
    st.write("Đang thực hiện spoofing thiết bị...")
    # Gọi hàm bypass từ controller ở đây

st.subheader("🧠 Trí tuệ AI")
if st.checkbox("Tự động né chiêu"):
    st.info("Chế độ né chiêu đang chờ dữ liệu Vision...")

st.sidebar.write("Hệ điều hành: Linux (IDX)")
st.sidebar.write("Firebase: Connected" if dm.cloud else "Firebase: Offline")
