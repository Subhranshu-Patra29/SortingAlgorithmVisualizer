import math


def insertion_sort_gen(array, start=0, end=0):
    """Insertion Sort generator"""
    end = end or len(array)
    for i in range(start, end):
        temp_index = i
        temp_index_value = array[i]
        while temp_index != start and temp_index_value < array[temp_index - 1]:
            array[temp_index] = array[temp_index - 1]
            temp_index -= 1
            yield array[:], temp_index, temp_index + 1, -1, -1
        array[temp_index] = temp_index_value
        yield array[:], temp_index, i, -1, -1
    yield array[:], -1, -1, -1, -1


def heapify_gen(array, index, heap_size):
    """Heapify generator (Max Heap)"""
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and array[largest] < array[left_index]:
        largest = left_index

    if right_index < heap_size and array[largest] < array[right_index]:
        largest = right_index

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        yield array[:], index, largest, -1, -1
        yield from heapify_gen(array, largest, heap_size)


def heap_sort_gen(array):
    """Heap Sort generator"""
    n = len(array)

    for i in range(n // 2, -1, -1):
        yield from heapify_gen(array, i, n)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        yield array[:], 0, i, -1, -1
        yield from heapify_gen(array, 0, i)

    yield array[:], -1, -1, -1, -1


def median_of_3(array, first_index, middle_index, last_index):
    """Median-of-three pivot selection"""
    if (array[first_index] > array[middle_index]) != (array[first_index] > array[last_index]):
        return array[first_index]
    elif (array[middle_index] > array[first_index]) != (array[middle_index] > array[last_index]):
        return array[middle_index]
    else:
        return array[last_index]


def partition_gen(array, low, high, pivot):
    """Partition generator for QuickSort/Introsort"""
    i = low
    j = high
    while True:
        while array[i] < pivot:
            i += 1
            yield array[:], i, j, -1, -1
        j -= 1
        while pivot < array[j]:
            j -= 1
            yield array[:], i, j, -1, -1
        if i >= j:
            return i
        array[i], array[j] = array[j], array[i]
        yield array[:], i, j, -1, -1
        i += 1


def intro_sort_gen(array, start, end, size_threshold, max_depth):
    """Recursive Introsort generator"""
    while end - start > size_threshold:
        if max_depth == 0:
            yield from heap_sort_gen(array)
            return
        max_depth -= 1
        pivot = median_of_3(array, start, start + ((end - start) // 2), end - 1)
        p = yield from partition_gen(array, start, end, pivot)
        yield from intro_sort_gen(array, p, end, size_threshold, max_depth)
        end = p
    yield from insertion_sort_gen(array, start, end)


def intro_sort_visualizer(array, *args):
    """Wrapper function to start introsort visualization"""
    if len(array) == 0:
        yield array, -1, -1, -1, -1
        return
    max_depth = 2 * math.ceil(math.log2(len(array)))
    size_threshold = 16
    yield from intro_sort_gen(array, 0, len(array), size_threshold, max_depth)
    yield array[:], -1, -1, -1, -1  # Final state


# -------------------------------------------------
# 🔹 Testing standalone (prints array states)
# -------------------------------------------------
if __name__ == "__main__":
    import random
    nums = [random.randint(1, 50) for _ in range(10)]
    print("Unsorted:", nums)
    for state in intro_sort_visualizer(nums[:]):
        arr, r1, r2, b1, b2 = state
        print(arr, " red:", r1, r2, " blue:", b1, b2)
