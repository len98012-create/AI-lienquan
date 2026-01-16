cat <<EOF > core/vision.py
import cv2
import numpy as np
import os

class Vision:
    def __init__(self, device_id="emulator-5554"):
        self.device_id = device_id

    def take_screenshot(self):
        os.system(f"adb -s {self.device_id} shell screencap -p /sdcard/screen.png")
        os.system(f"adb -s {self.device_id} pull /sdcard/screen.png ./screen.png")
        return cv2.imread("screen.png")

    def find_template(self, template_path, threshold=0.8):
        screen = self.take_screenshot()
        template = cv2.imread(template_path)
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        return list(zip(*loc[::-1])) # Trả về tọa độ tìm thấy
EOF
