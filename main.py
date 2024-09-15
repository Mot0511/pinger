import sys
import requests
import time
import random
import datetime

url = sys.argv[1]

while True:
    requests.get(url)
    time.sleep(random.randint(1, 11))
    print(f'[{datetime.datetime.now()}] - Работает')