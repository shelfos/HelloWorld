import time
import os

def print_one_by_one(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.25)

os.system('cls')
text = "Hello World!"
print_one_by_one(text)