from tqdm import tqdm
import time

def progress_bar():
    for i in tqdm(range(100), "Sending SMS..."):
        time.sleep(0.01)
    print("Successful SMS")

def call_progress_bar():
    for i in tqdm(range(100), "Calling..."):
        time.sleep(0.01)
    print("Successful call")
