import cv2
import numpy as np
import os

class Vision:
    def __init__(self, device_id="emulator-5554"):
        self.device_id = device_id

    def capture(self):
        """Chụp ảnh màn hình tốc độ cao"""
        os.system(f"adb -s {self.device_id} shell screencap -p /sdcard/s.png")
        os.system(f"adb -s {self.device_id} pull /sdcard/s.png screen.png")
        return cv2.imread("screen.png")

    def find_button(self, template_path):
        """Tìm tọa độ nút bấm trên màn hình"""
        screen = self.capture()
        template = cv2.imread(template_path)
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.8: # Độ khớp trên 80%
            return max_loc 
        return None
