import os
import time
import random

class Controller:
    def __init__(self, device_id="emulator-5554"):
        self.device_id = device_id

    def shell(self, command):
        return os.popen(f"adb -s {self.device_id} shell {command}").read()

    def human_tap(self, x, y):
        """Nhấn với tọa độ và thời gian ngẫu nhiên như người thật"""
        offset_x = x + random.randint(-4, 4)
        offset_y = y + random.randint(-4, 4)
        duration = random.randint(70, 150)
        # Sử dụng swipe ngắn để giả lập lực nhấn giữ của ngón tay
        self.shell(f"input swipe {offset_x} {offset_y} {offset_x} {offset_y} {duration}")
        time.sleep(random.uniform(0.1, 0.3))

    def human_swipe(self, x1, y1, x2, y2):
        """Vuốt có gia tốc (nhanh lúc đầu, chậm lúc sau)"""
        duration = random.randint(200, 400)
        self.shell(f"input swipe {x1} {y1} {x2} {y2} {duration}")

    def bypass_hardware(self):
        """Ngụy trang thiết bị thành Samsung S24 Ultra"""
        print("🛡️ Đang nạp profile ngụy trang...")
        self.shell("setprop ro.product.model SM-S928B")
        self.shell("setprop ro.product.brand samsung")
        self.shell("setprop ro.build.id UP1A.231005.007")
