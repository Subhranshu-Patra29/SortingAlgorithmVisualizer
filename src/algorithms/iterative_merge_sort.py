def merge_gen(array, low, mid, high):
    """Merge two sorted halves of array[low:mid] and array[mid:high+1]."""
    left = array[low:mid]
    right = array[mid:high + 1]
    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
        # yield snapshot (array, highlight range)
        yield array[:], low, high, -1, -1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
        yield array[:], low, high, -1, -1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
        yield array[:], low, high, -1, -1


def iter_merge_sort_gen(array, *args):
    """Iterative merge sort as a generator for visualization."""
    n = len(array)
    size = 1
    while size < n:
        for low in range(0, n, 2 * size):
            mid = min(low + size, n)
            high = min(low + 2 * size - 1, n - 1)
            if mid < high + 1:  # ensure two halves exist
                yield from merge_gen(array, low, mid, high)
        size *= 2
    yield array[:], -1, -1, -1, -1  # final state
