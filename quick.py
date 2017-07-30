import time
import random

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def pivotFirst(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark
    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
            rmark -= 1
        if lmark <= rmark:
            swap(x, lmark, rmark)
            lmark += 1
            rmark -= 1
    swap(x, pivot_idx, rmark)
    return rmark

def QuickSort(x, pivotMethod=pivotFirst):
    def _qsort(x, first, last):
        if first < last:
            splitpoint = pivotMethod(x, first, last)
            _qsort(x, first, splitpoint-1)
            _qsort(x, splitpoint+1, last)
    _qsort(x, 0, len(x)-1)
    return x

def BubbleSort(x):
    for i in range(len(x) - 1):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                swap(x, j, j+1)
    return x

arr = []
for i in range(100):
    arr.append(i + 1)
random.shuffle(arr)

print("처음 상태: {0}".format(arr))

t_before = time.clock()
arr_bubble = BubbleSort(arr)
t_after = time.clock()
print("버블 정렬 후 상태: {0}".format(arr_bubble))
print("걸린 시간:", (t_after - t_before))

t_before = time.clock()
arr_quick = QuickSort(arr)
t_after = time.clock()
print("퀵 정렬 후 상태: {0}".format(arr_quick))
print("걸린 시간:", (t_after - t_before))


