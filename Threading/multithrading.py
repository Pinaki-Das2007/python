import threading
import time

def print_numbers():
    for i in range(1,6):
        print(f"Number: {i}")

def print_letters():
    for letter in "abcde":
        print(f"Letter: {letter}")


t = time.time()
print_numbers()
print_letters()
finished_time = time.time() - t
print(f"Finished in: {finished_time} seconds")