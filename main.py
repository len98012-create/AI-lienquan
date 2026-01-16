cat <<EOF > main.py
from core.controller import Controller
from core.vision import Vision
import time

def main():
    ctrl = Controller()
    vis = Vision()
    
    print("--- AI Liên Quân Super Ready ---")
    # Ví dụ: Tự động nhấn nút Bắt đầu nếu thấy ảnh matching_button.png
    while True:
        # Thêm logic xử lý tại đây
        print("AI đang quét màn hình...")
        time.sleep(5)

if __name__ == "__main__":
    main()
EOF
