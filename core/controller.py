cat <<EOF > core/controller.py
import os
import time

class Controller:
    def __init__(self, device_id="emulator-5554"):
        self.device_id = device_id

    def shell(self, command):
        return os.popen(f"adb -s {self.device_id} shell {command}").read()

    def tap(self, x, y):
        os.system(f"adb -s {self.device_id} shell input tap {x} {y}")

    def swipe(self, x1, y1, x2, y2, duration=200):
        os.system(f"adb -s {self.device_id} shell input swipe {x1} {y1} {x2} {y2} {duration}")
EOF
