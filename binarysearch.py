def search_iterative0(arr, x):
    if x in arr:
        return arr.index(x)
    return None

def search_iterative1(arr, x):
    index = 0
    for y in arr:
        if y == x:
            break
        index += 1
    else:
        return None
    return index;
    
def search_iterative1_5(arr, x):
    for index in range(arr):
        if arr[index] == x:
            return index
    return -1;

def search_iterative2(arr, x):
    for index, y in enumerate(arr):
        if y == x:
            return index
    return -1;

def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
   
def binary_search_recursive(arr, x):
    if len(arr) == 0:
        return None;

    midindex = len(arr) // 2
    if (arr[midindex] == x):
        return midindex
    elif arr[midindex] > x:
        return binary_search_recursive(arr[:midindex], x)
    else: #arr[midindex] < x:
        retindex = binary_search_recursive(arr[midindex + 1:], x)
        if retindex == None:
            return None
        else:
            return midindex + 1 + retindex    

def binary_search_recursive2(arr, x, low, high):
    if high < low:
        return -1;

    midindex = (high + low) // 2
    if (arr[midindex] == x):
        return midindex
    elif arr[midindex] > x:
        return binary_search_recursive2(arr, x, low, midindex - 1)
    else: #arr[midindex] < x:
        return binary_search_recursive2(arr, x, midindex + 1, high)




#import timeit

#print (timeit.timeit("search_iterative1([i for i in range(10000)], 99999)", number=100, setup="from __main__ import search_iterative1") / 100)