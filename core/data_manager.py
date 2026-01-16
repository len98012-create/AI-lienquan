import json
import os
import firebase_admin
from firebase_admin import credentials, firestore, remote_config

class DataManager:
    def __init__(self):
        # Đường dẫn file key (Sẽ ưu tiên file người dùng nạp vào)
        key_path = "firebase_key.json"
        
        if os.path.exists(key_path):
            cred = credentials.Certificate(key_path)
            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            self.cloud = True
            print("🔥 [SUCCESS]: AI DA KET NOI VOI FIREBASE")
        else:
            self.cloud = False
            print("⚠️ [WARNING]: Chạy chế độ Offline (Khong tim thay firebase_key.json)")

    # [KEY 9] LẤY CHIẾN THUẬT TỪ REMOTE CONFIG
    def get_remote_strategy(self):
        if not self.cloud:
            return {"mode": "Phòng thủ", "range": 500} # Mặc định khi offline
        
        try:
            template = remote_config.get_template()
            # Giả sử bạn đặt tên tham số trên Firebase là 'ai_strategy'
            strategy = template.parameters.get('ai_strategy').default_value.value
            return json.loads(strategy)
        except Exception as e:
            print(f"❌ Lỗi lấy config: {e}")
            return None

    def save_memory(self, key, value):
        # Tạo thư mục logs nếu chưa có
        if not os.path.exists("logs"):
            os.makedirs("logs")
            
        if self.cloud:
            self.db.collection("ai_learning").document(key).set(value, merge=True)
            
        with open(f"logs/{key}.json", "w", encoding="utf-8") as f:
            json.dump(value, f, ensure_ascii=False, indent=4)
