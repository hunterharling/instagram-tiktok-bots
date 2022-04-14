import time
import random

def wait():
    t = random.uniform(2, 5)
    time.sleep(t)
    print(f"waiting: {t}")
