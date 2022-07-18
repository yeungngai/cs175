# ----------------------------------------------------
# Lab 6, Exercise 2: Queues
#
#
# Purpose of code: This program prompts user to enter a number of items that will be dequeued from a bounded queue
# and a circular queue. The program then prints out the runtime of each execution.
#
#
# Author: Yi Yang
# Collaborators/references: None
# ----------------------------------------------------


from queues import BoundedQueue, CircularQueue
import time


def main():
    '''
    This is the main function to test the runtime of dequeuing items from a bounded queue and a circular queue
    '''

    capacity = int(input("Enter the number of items: "))
    boundedQueueTest = BoundedQueue(capacity)
    circularQueueTest = CircularQueue(capacity)

    bqtotalTime = 0
    for i in range(1, 5):
        for a in range(0, capacity):
            boundedQueueTest.enqueue(a)

        bqstart = time.time()
        for j in range(0, capacity):
            boundedQueueTest.dequeue()

        bqend = time.time()
        bqtime_interval = bqend - bqstart
        bqtotalTime = bqtotalTime + bqtime_interval

    avgbqDequeueTime = bqtotalTime / 5

    print("For Bounded Queue, the total runtime of dequeuing " + str(capacity) + " items is:\n" + str(avgbqDequeueTime)
          + " seconds.")

    cqtotalTime = 0
    for i in range(1, 5):
        for a in range(0, capacity):
            circularQueueTest.enqueue(a)

        cqstart = time.time()
        for j in range(0, capacity):
            circularQueueTest.dequeue()

        cqend = time.time()
        cqtime_interval = cqend - cqstart
        cqtotalTime = cqtotalTime + cqtime_interval

    avgcqDequeueTime = cqtotalTime / 5

    print("For Circular Queue, the total runtime of dequeuing " + str(capacity) + " items is:\n" + str(avgcqDequeueTime)
          + " seconds.")


main()

