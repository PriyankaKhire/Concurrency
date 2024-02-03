# Mutex

import threading
import time

# Shared resource
shared_resource = 0

# Mutex
mutex = threading.Lock()

# Function to access and increment the shared resource
def increment(threadName):
    # we use the 'global' keyword to indicate that we want to modify the global shared_resource.
    global shared_resource
    for i in range(5):
        # Acquire the mutex to ensure exclusive access to the shared resource
        mutex.acquire()
        shared_resource += 1
        print "thread ",threadName, " has increamented the shared resource to", shared_resource
        time.sleep(1)
        # Release the mutex after modifying the shared resource
        mutex.release()

# Main
# Create two threads to increment the shared variable concurrently
thread1 = threading.Thread(target=increment, args=("Thread1",))
thread2 = threading.Thread(target=increment, args=("Thread2",))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

print "Final Value of the shared resource is ", shared_resource

