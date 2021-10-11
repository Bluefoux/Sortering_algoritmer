import random
import time
from datetime import timedelta

start_time = time.time()

def insertionsort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        k = i-1
        while k >=0 and key < lst[k]:
            lst[k+1] = lst[k]
            k-=1
        lst[k+1] = key


if __name__ == "__main__":
    lst = []
    nmr_of_random = input("enter a number of random ")
    i=0
    while i < int(nmr_of_random):
        nmr = random.randrange(0, 100)
        lst.append(nmr)
        i+=1
    insertionsort(lst)
    print(lst)
    elapsed_time_secs= time.time() - start_time
    msg = "execution took: %s secs (wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
    print(msg)
