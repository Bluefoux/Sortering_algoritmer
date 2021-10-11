import random
import time
from datetime import timedelta

start_time = time.time()

def heapcount(lst, num, i):
    largest = i
    num_1 = (2*i)+1
    num_2 = (2*i)+2
    if num_1 < num and lst[i] < lst[num_1]:
        largest = num_1
    if num_2 < num and lst[largest] < lst[num_2]:
        largest = num_2
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapcount(lst, num, largest)

def heapsort(lst):
    legnth = len(lst)
    for i in range((legnth//2)-1, -1, -1):
        heapcount(lst, legnth, i)
    for i in range(legnth-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapcount(lst, i, 0)

if __name__ == "__main__":
    lst = []
    nmr_of_random = input("enter a number of random ")
    i=0
    while i < int(nmr_of_random):
        nmr = random.randrange(0, 100)
        lst.append(nmr)
        i+=1
    heapsort(lst)
    print(lst)
    elapsed_time_secs= time.time() - start_time
    msg = "execution took: %s secs (wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
    print(msg)
