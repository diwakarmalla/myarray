import multiprocessing as mp
import time
import os
import random

q = mp.Queue()  #FIFO
a_list = []

def worker(a_list):
    a_list_square = [val ** 2 for val in a_list]
    q.put(a_list_square)

if __name__ == '__main__':
    nums = [random.randint(1, 50) for i in range(10**7)]
    chunk = len(nums) // 8
    procs = []
    t = time.time()
    for i in range(8):
        start = i * chunk
        stop = (i + 1) * chunk
        current_nums = nums[start:stop]
        p = mp.Process(target=worker, args=(current_nums,))
        procs.append(p)
        p.start()

    results = [q.get() for i in range(8)]
    total_time = time.time() - t
    print("total time for mp", total_time)

    final_result = []
    for result in results:
        final_result += result

    total_time_cat = time.time() - t
    print("total time for mp after concat", total_time_cat)

    for p in procs:
        p.join()

    t = time.time()
    result2 = [num ** 2 for num in nums]
    total_time = time.time() - t
    print("total time for list comp", total_time)




    # pid = os.getpid()
    # print(f'Main has pid {pid}')
    # p1 = mp.Process(target=worker, args=(5, 1))
    # p2 = mp.Process(target=worker, args=(15, 2))
    # p1.start()
    # p2.start()

    # print(f'first item in queue {q.get()}')
    # print(f'second item in queue {q.get()}')
    # print('the list ', a_list)