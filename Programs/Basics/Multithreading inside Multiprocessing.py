# Multithreading inside Multiprocessing

import threading
import multiprocessing
from multiprocessing import Process
import time


def task(processName, threadName):
    print " Starting task for process ", processName, " and thread ", threadName
    for i in range(3):
        print " performing task for process ", processName, " and thread ", threadName
        time.sleep(1)
    print " Completed task for process ", processName, " and thread ", threadName

def threadExecution(processName):
    # Note the comma in args=(processName, "Thread1",)
    thread1 = threading.Thread(target=task, args=(processName, "Thread1",))
    thread2 = threading.Thread(target=task, args=(processName, "Thread2",))

    # Start the thread
    thread1.start()
    thread2.start()

    # Wait for threads to finish execution
    thread1.join()
    thread2.join()

def processExecution():
    # Note the comma in args=("Process1",)
    process1 = Process(target=threadExecution, args=("Process1",))
    process2 = Process(target=threadExecution, args=("Process2",))

    # Start the process
    process1.start()
    process2.start()

    # Wait for all the processes to finish execution
    process1.join()
    process2.join()

# Main
if __name__ == '__main__': # this line for windows only
    multiprocessing.freeze_support() # this line for windows only
    # Start the process
    processExecution()
