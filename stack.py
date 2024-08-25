# # List can be used as Stack(LIFO)
# # Recommended approach to use stack and queques are using collections.deque(uses linked list internally) rather than using list/ dynamic array
# from collections import deque
# # stack = deque()
# # print(dir(stack))

# # stack.append('link 1')
# # stack.append('link 2')
# # stack.append('link 3')
# # stack.append('link 4')
# # stack.append('link 5')
# # stack.append('link 6')

# # print(stack)
# # print(stack.pop())
# # print(stack)

# class Stack:
#     def __init__(self):
#         self.container = deque()
#     def push(self,val):
#         self.container.append(val)
#     def pop(self):
#         return self.container.pop()
#     def peek(self):
#         return self.container[-1]
#     def isEmpty(self):
#         return len(self.container)==0
#     def size(self):
#         return len(self.container)  

# def isBalanced(s):
#     match_dict = {
#         ')':'(',
#         ']':'[',
#         '}':'{'
#     }
#     stack = []

#     for ch in s:
#         if ch == '(' or ch == '{' or ch == '[':
#             stack.append(ch)
#         else:
#             if stack and stack[-1] == match_dict[ch]:
#                 stack.pop()
#             else:
#                 return False
        
#     return len(stack)==0


         
# def reverseString(s):
#     stack = Stack()

#     for ch in s:
#         stack.push(ch)
    
#     reverse_string = ''

#     while stack.size()!=0:
#         reverse_string += stack.pop() 
#     return reverse_string

# if __name__ == '__main__':
#     print(reverseString('Ello governurr'))

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
import multiprocessing
import time

def f(n):
    sum = 0
    for i in range(1000):
        sum +=i
    return sum

if __name__ == '__main__':
    t1 = time.time()
    pool = multiprocessing.Pool()
    result = pool.map(f,range(1000000))
    pool.close()
    pool.join()
    print('Pool time', time.time()-t1)

    t2 = time.time()
    result2 =[]
    for i in range(1000000):
        result2.append(f(i))
    
    print('Serial Processing time',time.time()-t2)