import os
from firebase_admin import credentials, firestore, initialize_app

class DataManager:
    def __init__(self):
        # Kiểm tra nếu đang chạy Emulator
        if os.getenv('FIRESTORE_EMULATOR_HOST'):
            # Khi dùng Emulator, không cần file JSON thật
            if not firebase_admin._apps:
                initialize_app(options={'projectId': 'demo-lienquan-ai'})
            self.db = firestore.client()
            self.cloud = True
            print("🚀 [EMULATOR]: Đang chạy chế độ mô phỏng cục bộ")
        else:
            # Chế độ Cloud thật (Cần file key)
            # ... (giữ nguyên code cũ của bạn)
