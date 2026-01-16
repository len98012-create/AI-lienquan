cat <<EOF > core/vision.py
import cv2
import numpy as np
import os

class Vision:
    def __init__(self, device_id="emulator-5554"):
        self.device_id = device_id

    def capture(self):
        os.system(f"adb -s {self.device_id} shell screencap -p /sdcard/s.png")
        os.system(f"adb -s {self.device_id} pull /sdcard/s.png screen.png")
        return cv2.imread("screen.png")

    def find_object(self, template_path, threshold=0.8):
        img = self.capture()
        template = cv2.imread(template_path)
        # Logic nhận diện vật thể sẽ nằm ở đây
        return None 
EOF
