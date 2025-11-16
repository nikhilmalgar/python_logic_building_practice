'''This programe demonstrates the concept of the Multiprocessing.'''

import multiprocessing
import time

def square():
    for i in range(5):
        time.sleep(1)
        print(i*i)

def cube():
    for i in range(5):
        time.sleep(1.5)
        print(i*i*i)

if __name__=="__main__":

    #create 2 process
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)

    t=time.time()

    #start the process
    p1.start()
    p2.start()

    # wait for the process to  complete
    p1.join()
    p2.join()

    final_Time = time.time() -t
    print(final_Time)
