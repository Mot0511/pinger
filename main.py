import sys
import requests
import time
import random

url = sys.argv[0]

while True:
    requests.get('https://sinus-server.onrender.com')
    time.sleep(random.randint(1, 11))