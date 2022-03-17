import time

def selection_sort(A, steps):
    start = time.perf_counter()
    for i in range(len(A)):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
        # print(A)
        s = listToString(A)
        steps.append(s)
    end = time.perf_counter()
    steps.append("Time : "+str(round((end-start)*1000,2))+"ms")


def bubble_sort(arr, steps):
    start = time.perf_counter()
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        s = listToString(arr)
        steps.append(s)
    end = time.perf_counter()
    steps.append("Time : "+str(round((end-start)*1000,2))+"ms")


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += str(ele) + " "
    return str1


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heap_sort(arr, steps):
    start = time.perf_counter()
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        s = listToString(arr)
        steps.append(s)
    end = time.perf_counter()
    steps.append("Time : "+str(round((end-start)*1000,2))+"ms")


def insertion_sort(arr, steps):
    start = time.perf_counter()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                # s = listToString(arr)
                # steps.append(s)
        arr[j + 1] = key
        s = listToString(arr)
        steps.append(s)
    end = time.perf_counter()
    steps.append("Time : "+str(round((end-start)*1000,2))+"ms")