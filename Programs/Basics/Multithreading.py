# Multithreading

import threading
import time

def task(taskName):
    print "Starting task ", taskName
    for i in range(3):
        print "performing task ", taskName
    print "Completed task ", taskName

# Main
# Creating threads for concurrent execution
thread1 = threading.Thread(target=task, args=("A",))
thread2 = threading.Thread(target=task, args=("B",))

# Starting the threads
thread1.start()
thread2.start()

# Waiting for threads to finish
thread1.join()
thread2.join()

