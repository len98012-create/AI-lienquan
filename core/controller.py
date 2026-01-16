mkdir -p core logs data
cat <<EOF > core/controller.py
import os
import time

class Controller:
    def __init__(self, device_id="emulator-5554"):
        self.device_id = device_id

    def tap(self, x, y):
        os.system(f"adb -s {self.device_id} shell input tap {x} {y}")

    def swipe(self, x1, y1, x2, y2, duration=200):
        os.system(f"adb -s {self.device_id} shell input swipe {x1} {y1} {x2} {y2} {duration}")

    def back(self):
        os.system(f"adb -s {self.device_id} shell input keyevent 4")
EOF
