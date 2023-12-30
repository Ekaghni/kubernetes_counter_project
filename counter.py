import os
import time

file_path = '/data/counter-data/counter.txt'

os.makedirs(os.path.dirname(file_path), exist_ok=True)

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if lines:
            counter = int(lines[-1].strip()) + 1
        else:
            counter = 1
except FileNotFoundError:
    counter = 1

while True:
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    print("file path---->",file_path)
    with open(file_path, 'a') as file:
        file.write(f"{counter}\n")
    
    print(counter,flush=True)
    time.sleep(5)
    counter += 1

