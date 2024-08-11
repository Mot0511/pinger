import sys
import requests
import time
import random

url = sys.argv[1]

while True:
    requests.get(url)
    time.sleep(random.randint(1, 11))