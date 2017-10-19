import os
import time

while True:
    os.system("taskkill /f /im wuauclt.exe")
    time.sleep(600)


