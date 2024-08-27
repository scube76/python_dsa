# Producer ----Queue----- Consumer
# FIFO
# List can be used as queues via arr.insert(0,'Value')
# from collections import deque
# queue = deque()
# queue.appendleft(45)
# # print(queue)

# class Queue:
#     def __init__(self):
#         self.container = deque()
#     def enqueue(self,val):
#         self.container.appendleft(val)
#     def dequeue(self):
#         return self.container.pop()
#     def is_empty(self):
#         return len(self.container)==0
#     def size(self):
#         return len(self.container)
    
# pq = Queue()

# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.01 AM',
#     'price': 131.10
# })
# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.02 AM',
#     'price': 132
# })
# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.03 AM',
#     'price': 135
# })

# print(pq.container)
# print(pq.dequeue())


# Multithreading --> Doing multiple tasks at the same time and each task is a thread

# import time
# import threading

# lock = threading.Lock()

# def calSquare(arr):
#     for i in arr:
#         time.sleep(0.2)
#         with lock:
#             print("Square =",i*i)

# def calCube(arr):
#     for i in arr:
#         time.sleep(0.2)
#         with lock:
#             print("Cube =",i*i*i)

# t = time.time()
# arr = [1,2,3]
# task1 = threading.Thread(target=calSquare,args=(arr,))
# task2 = threading.Thread(target=calCube,args=(arr,))

# task1.start()
# task2.start()

# task1.join()
# task2.join()
# # Without Multithreading 
# # calSquare(arr)
# # calCube(arr)

# print(f"Total Time Taken: => {time.time() - t}")
# print("Done...")

# Multiprocessing --> Every process has their own address space(VM). Thus program var are not shared by process. You need to use interprocess communication technique if you want to share data between two process

# import time
# import multiprocessing

# global_arr = []

# def calSquare(arr):
#     for i in arr:
#         # time.sleep(0.2)
#         # print("Square =",i*i)
#         global_arr.append(i*i)

#     print('Result inside calSquare',global_arr)

# # def calCube(arr):
# #     for i in arr:
# #         time.sleep(0.2)
# #         print("Cube =",i*i*i)
# if __name__ =='__main__':
#     # t = time.time()
#     arr = [1,2,3]
#     p1 = multiprocessing.Process(target=calSquare,args=(arr,))
#     # p2 = multiprocessing.Process(target=calCube,args=(arr,))

#     p1.start()
#     # p2.start()

#     p1.join()
#     # p2.join()

#     # print(f"Total Time Taken: => {time.time() - t}")
#     print("global_arr outside calSquare",global_arr)
#     print("Done...")


# Multithreading and multitasking both are ways to achieve multitasking 
# Refer Figure 1 --> Only difference between multiprocess and multithreading


# Shared memory in multiprocess -> Refer Figure 2

# import multiprocessing

# def calSquare(lst,result,v):# Child Process
#     v.value = 7.96
#     for idx, element in enumerate(lst):
#         result[idx] = element*element

# if __name__ == '__main__':# Parent Process
#     lst = [2,4,6,8]
#     result = multiprocessing.Array('i',4)#Shared memmory i=integer and d=double
#     v = multiprocessing.Value('d',0.8)
#     p1 = multiprocessing.Process(target = calSquare,args=(lst,result,v))
#     p1.start()
#     p1.join()
#     print(result[:])
#     print('Value =',v.value)

# Shared memory in multiprocess using queues -> refer figure 3 (Queue is shared memory)

# import multiprocessing

# def calSquare(lst,q):# Child Process
#     for i in lst:
#         q.put(i*i)

# if __name__ == '__main__':# Parent Process
#     lst = [2,4,6,8]
#     q = multiprocessing.Queue()
#     p1 = multiprocessing.Process(target = calSquare,args=(lst,q))
#     p1.start()
#     p1.join()
#     while q.empty() is False:
#         print(q.get())


# Lock
# import time
# import multiprocessing

# def deposit(balance, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         balance.value = balance.value + 1
#         lock.release()

# def withdraw(balance, lock):
#     for i in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         balance.value = balance.value - 1
#         lock.release()

# if __name__ == '__main__':
#     balance = multiprocessing.Value('i', 200)
#     lock = multiprocessing.Lock()
#     d = multiprocessing.Process(target=deposit, args=(balance,lock))
#     w = multiprocessing.Process(target=withdraw, args=(balance,lock))
#     d.start()
#     w.start()
#     d.join()
#     w.join()
#     print(balance.value)

#  Parallel Processing / Multiprocessing Pool --> We have  multiple cores inside of our CPU instead of giving one core a heavy task, different cores are assigned the task each solving different parts of that one task and at last aggreagating the result

# Map -- Dividing the resources  
# Reduce -- Aggregating the resources
# Refer Figure 4

# import multiprocessing

# def f(n):
#     return n*n

# if __name__ =='__main__':
#     arr = [2,3,4,5]
#     pool = multiprocessing.Pool()
#     result = pool.map(f,arr)
#     print(result)

# Pool(Multi-core) VS Serial Processing(Single-core)
# import multiprocessing
# import time

# def f(n):
#     sum = 0
#     for i in range(1000):
#         sum +=i
#     return sum

# if __name__ == '__main__':
#     t1 = time.time()
#     pool = multiprocessing.Pool()
#     result = pool.map(f,range(1000000))
#     pool.close()
#     pool.join()
#     print('Pool time', time.time()-t1)

#     t2 = time.time()
#     result2 =[]
#     for i in range(1000000):
#         result2.append(f(i))
    
#     print('Serial Processing time',time.time()-t2)


# Exercise question 1
from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.container = deque()
    def enqueue(self,val):
        self.container.appendleft(val)
    def dequeue(self):
        return self.container.pop()
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)

queue = Queue()
lock = threading.Lock()

def placeOrder(orders):
    for order in orders:
        time.sleep(0.5)
        with lock:
            queue.enqueue(order)
            print('order added',order)
def serveOrder():
    time.sleep(1)

    while not queue.is_empty():
        time.sleep(2)
        with lock:
            print('order served',queue.dequeue())

if __name__ =='__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target =placeOrder,args=(orders,))
    t2 = threading.Thread(target= serveOrder)
    t1.start()
    t2.start()
    t1.join()
    t2.join()