# Multiprocessing

import multiprocessing
from multiprocessing import Process
import time

def task(taskName):
    print "Starting task ", taskName
    for i in range(3):
        print "performing task ", taskName
        time.sleep(1)
    print "Completed task ", taskName

# Main
# Creating processes for concurrent execution
process1 = Process(target=task, args=("A",))
process2 = Process(target=task, args=("B",))

if __name__ == '__main__': # this line for windows only
    multiprocessing.freeze_support() # this line for windows only
    # Starting the processes
    process1.start()
    process2.start()

    # Waiting for processes to finish
    process1.join()
    process2.join()


## Note: if you are running this program on windows machine please run it in cmd with following command
# >> python Multiprocessing.py    
