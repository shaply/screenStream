import pyautogui
import time
import base64
from io import BytesIO
import threading

class ssCapture():
    def __init__(self):
        image = pyautogui.screenshot()
        buffer = BytesIO()
        image.save(buffer,format='jpeg')
        byte_data = buffer.getvalue()
        base64_data = base64.b64encode(byte_data)
        self.base64 = base64_data.decode()
        
        self.stop_event = threading.Event()

    def capture(self):
        print("Capture starting...")
        while not self.stop_event.is_set():
            image = pyautogui.screenshot()
            buffer = BytesIO()
            image.save(buffer,format='jpeg')
            byte_data = buffer.getvalue()
            base64_data = base64.b64encode(byte_data)
            self.base64 = base64_data.decode()
            time.sleep(0.5)
            # print("Captured...")
        print("Capture ending...")

screenVar = ssCapture()
