cat <<EOF > dashboard.py
import streamlit as st
import json
import os
import pandas as pd
from core.data_manager import DataManager

# Cấu hình trang
st.set_page_config(page_title="LQM AI Command Center", layout="wide", page_icon="🎮")
dm = DataManager()

st.title("🤖 TRUNG TÂM ĐIỀU KHIỂN SIÊU AI (KEY 9)")

# Cột chia giao diện
col1, col2 = st.columns([1, 2])

with col1:
    st.header("⚙️ Điều khiển & Cấu hình")
    
    # Trạng thái
    st.success("Hệ thống: ONLINE")
    
    # Cấu hình nhanh
    hero = st.selectbox("Chọn tướng", ["Valhein", "Arthur", "Krixi", "Nakroth"])
    mode = st.radio("Chế độ chơi", ["Leo Rank", "Đấu thường", "Luyện tập"])
    
    if st.button("LƯU CẤU HÌNH", type="primary"):
        config = {"hero": hero, "mode": mode}
        with open("config/settings.json", "w") as f:
            json.dump(config, f)
        dm.log_event(f"Người dùng cập nhật cấu hình: {hero} - {mode}")
        st.toast("Đã lưu cấu hình thành công!")

    st.markdown("---")
    if st.button("🔴 DỪNG KHẨN CẤP (Kill Switch)"):
        os.system("adb -s emulator-5554 shell input keyevent 3") # Về Home
        dm.log_event("KÍCH HOẠT DỪNG KHẨN CẤP!", "WARNING")

with col2:
    st.header("🧠 Nhật ký & Trí tuệ AI")
    
    # Tab hiển thị
    tab1, tab2 = st.tabs(["📜 Nhật ký hoạt động", "💡 Kiến thức đã học"])
    
    with tab1:
        if os.path.exists("logs/activity.log"):
            with open("logs/activity.log", "r") as f:
                logs = f.readlines()
                st.code("".join(logs[-20:]), language="log") # Xem 20 dòng cuối
        else:
            st.info("Chưa có nhật ký nào.")
            
    with tab2:
        if os.path.exists("logs/ai_memory.json"):
            with open("logs/ai_memory.json", "r") as f:
                memory = json.load(f)
            st.json(memory["learned_strategies"])
        else:
            st.info("AI chưa học được gì mới.")

# Footer
st.caption(f"Phiên bản AI: 2.0 | [KEY 9] Enabled | Thời gian server: {os.popen('date').read().strip()}")
EOF
