cat <<EOF > core/data_manager.py
import json
import os

class DataManager:
    def __init__(self):
        self.memory_path = "logs/ai_memory.json"
        if not os.path.exists("logs"): os.makedirs("logs")
        
    def save(self, data):
        with open(self.memory_path, 'w') as f:
            json.dump(data, f, indent=4)
            
    def log(self, msg):
        print(f"[LOG]: {msg}")
EOF
