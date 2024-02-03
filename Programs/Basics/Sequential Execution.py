# Sequential Execution

import time

# Function to simulate a task that takes some time to complete
def task(taskName):
    print "Starting task", taskName
    
    # Simulating some time-consuming task
    for i in range(3):
        print "."
        time.sleep(1)
        
    print "Completed task", taskName

# Main
# Sequential execution
task("A")
task("B")
