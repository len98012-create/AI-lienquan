from core.controller import Controller
from core.vision import Vision
from core.data_manager import DataManager
import time

def run_ai():
    ctrl = Controller()
    vis = Vision()
    dm = DataManager()

    # Bước 1: Bypass bảo mật khi khởi động
    ctrl.bypass_hardware()
    
    print("🚀 AI LIÊN QUÂN ĐÃ KÍCH HOẠT")
    
    while True:
        # Ví dụ logic: Tìm nút 'Bắt đầu'
        # pos = vis.find_button("data/start_btn.png")
        # if pos:
        #     ctrl.human_tap(pos[0], pos[1])
        
        print("AI đang quan sát trận đấu...")
        time.sleep(2) # Quét mỗi 2 giây để tránh nóng máy ảo

if __name__ == "__main__":
    run_ai()
