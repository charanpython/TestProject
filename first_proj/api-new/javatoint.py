# import threading
# import time
# 
# def addition(sp):
#     time.sleep(sp)
#     print('addition execution completed in',sp,'seconds')
# 
# def substraction(sp):
#     time.sleep(sp)
#     print('sub execution completed in',sp,'seconds')
# 
# def multiplication(sp):
#     time.sleep(sp)
#     print('multiplication execution completed in',sp,'seconds')
# 
# def division(sp):
#     time.sleep(sp)
#     print('division execution completed in',sp,'seconds')
# 
#     
# t1 = threading.Thread(target=addition,args=(5,))
# t1.start()
# 
# 
# t2 = threading.Thread(target=substraction,args=(3,))
# t2.start()
# 
# 
# t3 = threading.Thread(target=multiplication,args=(2,))
# t3.start()
# 
# 
# t4 = threading.Thread(target=division,args = (1,))
# t4.start()
# t4.join()
# 
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# print('All tasks are executed succesfully')

# import threading
# import time
# 
# class mythread(threading.Thread):
#     def __init__(self,name):
#         threading.Thread.__init__(self)
#         self.name = name
#     
#     def addition(self):
#         print('thread name is',self.name)
#         
# t1 = mythread('first')
# t1.start()
# 
# t2 = mythread('second')
# t2.start()



# import threading
# import time


# def ticket(name):
# #     lock.acquire()
#     print(name,'running')
#     time.sleep(5)
#     print(name,'comleted')
# #     lock.release()
# #     print(name,'lock released')
# 
# # lock = threading.Lock()
# t1 = threading.Thread(target=ticket,args=('thread-1',))
# t1.start()
# t2 = threading.Thread(target=ticket,args=('thread-2',))
# t2.start()
# t3 = threading.Thread(target=ticket,args=('thread-3',))
# t3.start()
# t4 = threading.Thread(target=ticket,args=('thread-4',))
# t4.start() 
# t1.join()
# t2.join()
# t3.join()
# t4.join()

    
# import threading
# 
# 
# a = ""
# def task1(name):
#     global a
#     
#     a = a+name
#     print('task1 completed')
#     
# def task2(name):
#     global a
#     
#     a = a+name
# 
#     print('task2 cmpleted')
#     
# thread_1 = threading.Thread(target=task1,args=('thread1',))
# thread_2 = threading.Thread(target=task2,args=('thread2',))
# thread_1.start()
# thread_2.start()
# thread_1.join()
# thread_2.join()
# 
# print('result',a)


# import queue
# 
# q = queue.PriorityQueue()
# q.put(4)
# q.put(6)
# q.put(3)

# print(q.qsize())

# for k in range(q.qsize()):
#     print(q.get())

# while not q.empty():
#     print(q.get())



# print(q.qsize())
# 
# while not q.empty():
#     print(q.get(),end = "")

# import queue
# import threading
# import time
# eggs = queue.Queue()
# 
# for k in range(20):
#     eggs.put(k)
# 
# # while not eggs.empty():
# #     print(eggs.get(),end= " ")
# 
# def eateggs(name,sp):
#     while not eggs.empty():
#         time.sleep(sp)
#         print(name,'eat eggs',eggs.get())
#     
# person_1 = threading.Thread(target=eateggs,args = ('person1',2))
# person_2 = threading.Thread(target=eateggs,args = ('person2',1))
# person_3 = threading.Thread(target=eateggs,args = ('person3',2))
# person_4 = threading.Thread(target=eateggs,args = ('person4',4))
# person_5 = threading.Thread(target=eateggs,args = ('person5',3))
# 
# person_1.start()
# person_2.start()
# person_3.start()
# person_4.start()
# person_5.start()

import multiprocessing
 
 
 
 
def addition():
    print('addition processd')

def subtraction():
    print('subtraction prcess')
     
     
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=addition)
    p2 = multiprocessing.Process(target=subtraction) 

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('final')   
    


















        























