from queue import Queue

line = Queue(range(1, 11))
for x in range(0, 10):
    line.dequeue()
