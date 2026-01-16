import json
import os
import firebase_admin
from firebase_admin import credentials, firestore

class DataManager:
    def __init__(self):
        if os.path.exists("firebase_key.json"):
            cred = credentials.Certificate("firebase_key.json")
            if not firebase_admin._apps:
                firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            self.cloud = True
        else:
            self.cloud = False
            print("⚠️ Chạy chế độ Offline")

    def save_memory(self, key, value):
        if self.cloud:
            self.db.collection("ai_learning").document(key).set(value, merge=True)
        with open(f"logs/{key}.json", "w") as f:
            json.dump(value, f)
