'''This programe will demonstrate the threading concept.'''


import threading
import time

def numbers():
    for i in range(1,6):
        time.sleep(2) # make the execution to wait for 2 sec
        print(i)

def letters():
    for i in "ABCDE":
        time.sleep(2)
        print(i)

t1 = threading.Thread(target=numbers)
t2 = threading.Thread(target=letters)

T = time.time()

t1.start()  #starts the execution of thread
t2.start()

t1.join()
t2.join() # wait for the thread to complete

final_time = time.time() - T

print(final_time)
    