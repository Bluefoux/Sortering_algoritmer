import random

def quicksort(lst2):
    quicksort_sort(lst2, 0, len(lst2)-1)

def partition(lsta, startindex, endindex):
    small_index = (startindex-1)
    piv = lsta[endindex]
    for k in range(startindex, endindex):
        if lsta[k] <= piv:
            small_index +=1
            lsta[small_index], lsta[k] = lsta[k], lsta[small_index]
    lsta[small_index+1], lsta[endindex] = lsta[endindex], lsta[small_index+1]
    return small_index+1

def quicksort_sort(lst1, startindex, endindex):
    if startindex < endindex:
        pi_index = partition(lst1, startindex, endindex)
        quicksort_sort(lst1, startindex, pi_index-1)
        quicksort_sort(lst1, pi_index+1, endindex)

if __name__ == "__main__":
    lst = []
    nmr_of_random = input("enter a number of random ")
    for i in range(int(nmr_of_random)):
        nmr = random.randrange(-1000, 1000)
        lst.append(nmr)
    quicksort(lst)
    print(lst)
