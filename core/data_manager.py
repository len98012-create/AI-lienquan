cat <<EOF > core/data_manager.py
import json
import os
from datetime import datetime

class DataManager:
    def __init__(self):
        self.log_path = "logs/activity.log"
        self.memory_path = "logs/ai_memory.json"
        self.config_path = "config/settings.json"
        self._ensure_directories()

    def _ensure_directories(self):
        os.makedirs("logs", exist_ok=True)
        os.makedirs("config", exist_ok=True)
        if not os.path.exists(self.memory_path):
            with open(self.memory_path, 'w') as f: json.dump({"matches": [], "learned_strategies": {}}, f)

    def log_event(self, message, level="INFO"):
        """Ghi lại hoạt động vào file text"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(log_entry)
        print(log_entry.strip())

    def save_learning(self, key, knowledge):
        """Lưu kiến thức mới vào bộ nhớ JSON"""
        with open(self.memory_path, 'r+') as f:
            data = json.load(f)
            data["learned_strategies"][key] = knowledge
            f.seek(0)
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.truncate()
        self.log_event(f"Đã lưu kiến thức mới: {key}")

    def load_config(self):
        """Đọc cấu hình"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f: return json.load(f)
        return {"mode": "auto_rank", "hero": "Valhein", "aggressive": True}
EOF
