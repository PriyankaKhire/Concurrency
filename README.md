![Concurrency](https://github.com/PriyankaKhire/Concurrency/assets/12015512/befbb18b-d58e-4cdf-b755-b3c050f064a3)
# Introduction
  Concurrency means multiple computations are happening at the same time. </br>
  **Example:**
  - Multiple processors in a computer
  - Multiple applications running on one computer
  
## How Concurrent Modules Communicate
### Shared memory
  Concurrent modules communicate by reading from and writing to shared memory objects.
  ![Shared memory](https://github.com/PriyankaKhire/Concurrency/assets/12015512/01c45846-abc6-4df8-8676-45dc453412ba)
  #### In the above image, A and B can be:
  - two processors (or processor cores) in the same computer, sharing the same physical memory.
  - two programs running on the same computer, sharing a common filesystem with files they can read and write.
  - two threads in the same Java program, sharing the same Java objects.
### Message passing
  Concurrent modules communicate by sending messages through a communication channel. Modules send off messages, and incoming messages to each module are queued up for handling. </br>
  ![Screenshot 2024-02-02 184009](https://github.com/PriyankaKhire/Concurrency/assets/12015512/200ba155-921e-4a9d-a8a7-4355a5edfa57)
  #### In the above image, A and B can be:
  - two computers in a network, communicating over the network connection.
  - web browser and a web server – A opens a connection to B, asks for a web page, and B sends the web page data back to A.
  - two programs running on the same computer whose input and output have been connected by a pipe, like ```ls | grep``` typed into a command prompt.

## Different types of Concurrent Modules: Processes and Threads
### Process
 A process is an instance of a running program. The process, has its own private section of the machine’s memory. A process can’t access another process’s memory or objects at all. Processes help computers run multiple programs at the same time, like when you have a web browser open while also listening to music.
 #### Example:
 Imagine your computer is a kitchen: each process is like a chef working on a different recipe. They have their own ingredients (memory and resources) and work independently from each other. 
### Thread
A thread is a locus of control inside a running program. Threads help programs do multiple things at once, like multitasking on a computer. Threads are within the same process address space, thus, much of the information present in the memory description of the process can be shared across threads.
  #### Example:
   Imagine you're cooking dinner: you might have one thread chopping vegetables while another thread is boiling water. 
![Screenshot 2024-02-02 191525](https://github.com/PriyankaKhire/Concurrency/assets/12015512/76c8c2b7-3ee7-47f9-aeb8-f8ee52d7c2f2)

## Time Slicing
When processor switches between threads, it's called time slicing. </br>
![Screenshot 2024-02-02 192444](https://github.com/PriyankaKhire/Concurrency/assets/12015512/310baa84-8c4a-4ee2-96f2-f6d473f7fb2c) </br>
The above figure shows, three threads T1, T2, and T3 might be time-sliced on a machine that has only two actual processors. </br>
At first one processor is running thread T1 and the other is running thread T2, and then the second processor switches to run thread T3. Thread T2 simply pauses, until its next time slice on the same processor or another processor.

## Race Condition
It's like a race between different parts of the program to access shared resources, and the result can be unpredictable or incorrect if the timing isn't managed properly.
### Example:
Let's consider a simple example of a bank account where two processes, Process A and Process B, are trying to withdraw money simultaneously.
1. Process A checks the account balance and finds it to be $100.
2. Process B also checks the account balance and finds it to be $100.
3. Process A decides to withdraw $50 from the account.
4. Before Process A completes its withdrawal, Process B also decides to withdraw $50 from the account.
5. Process A subtracts $50 from the balance, making it $50.
6. Process B also subtracts $50 from the balance, making it $50.
7. Both processes complete, and the final balance is incorrect ($50 instead of $0).

In this scenario, a race condition occurs because the outcome (the final balance) depends on the order in which the processes execute their operations. Depending on the timing, both processes read the same balance, perform their operations independently, and the final balance is incorrect because they don't account for each other's actions.



# Good Reads
- <a href="https://web.mit.edu/6.005/www/fa14/classes/17-concurrency/#:~:text=Concurrency%20means%20multiple%20computations%20are,cores%20on%20a%20single%20chip)">MIT course on Concurrency</a>
- <a href="https://stackoverflow.com/questions/5201852/what-is-a-thread-really">Stack overflow: What is a thread</a>
