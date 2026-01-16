cat <<EOF > core/data_manager.py
import json
import os
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

class DataManager:
    def __init__(self):
        self.log_path = "logs/activity.log"
        self.local_memory_path = "logs/ai_memory.json"
        self.use_cloud = False
        
        # --- CẤU HÌNH FIREBASE ---
        # Kiểm tra xem có file key không để kích hoạt chế độ Cloud
        if os.path.exists("firebase_key.json"):
            try:
                if not firebase_admin._apps:
                    cred = credentials.Certificate("firebase_key.json")
                    firebase_admin.initialize_app(cred)
                self.db = firestore.client()
                self.use_cloud = True
                print("✅ [CLOUD] Đã kết nối Firebase thành công!")
            except Exception as e:
                print(f"❌ [CLOUD] Lỗi kết nối Firebase: {e}")
        else:
            print("⚠️ [LOCAL] Chạy chế độ Offline (Chưa có firebase_key.json)")

        self._ensure_directories()

    def _ensure_directories(self):
        os.makedirs("logs", exist_ok=True)
        if not os.path.exists(self.local_memory_path):
            with open(self.local_memory_path, 'w') as f: 
                json.dump({"matches": [], "learned_strategies": {}}, f)

    def log_event(self, message, level="INFO"):
        """Ghi log vào file và đẩy lên Cloud nếu có lỗi nghiêm trọng"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] [{level}] {message}"
        
        # 1. Ghi Local
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
        
        # 2. Đẩy lên Cloud (Chỉ log quan trọng)
        if self.use_cloud and level in ["ERROR", "WARNING", "VICTORY"]:
            self.db.collection("logs").add({
                "timestamp": datetime.now(),
                "level": level,
                "message": message
            })

    def save_learning(self, key, knowledge):
        """Lưu kiến thức mới vào cả File và Firestore"""
        # 1. Lưu Local
        with open(self.local_memory_path, 'r+') as f:
            data = json.load(f)
            data["learned_strategies"][key] = knowledge
            f.seek(0)
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.truncate()

        # 2. Lưu Cloud (Đồng bộ vĩnh viễn)
        if self.use_cloud:
            self.db.collection("ai_brain").document("strategies").set(
                {key: knowledge}, merge=True
            )
            print(f"☁️ Đã đồng bộ kiến thức '{key}' lên Mây!")

    def load_config(self):
        # Ưu tiên lấy config từ Cloud để điều khiển từ xa
        if self.use_cloud:
            doc = self.db.collection("config").document("settings").get()
            if doc.exists:
                return doc.to_dict()
        
        # Nếu mất mạng thì dùng file local
        if os.path.exists("config/settings.json"):
            with open("config/settings.json", 'r') as f: return json.load(f)
        return {"hero": "Valhein", "mode": "rank"}
EOF
