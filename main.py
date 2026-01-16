cat <<EOF > main.py
from core.controller import Controller
from core.vision import Vision
from core.data_manager import DataManager
import time

def start_bot():
    ctrl = Controller()
    vis = Vision()
    dm = DataManager()
    
    dm.log("Hệ thống AI đang khởi động trên Linux...")
    # Thêm vòng lặp xử lý game tại đây
    
if __name__ == "__main__":
    start_bot()
EOF
