def binary_search_insertion_gen(sorted_list, item, pivot_index):
    """Binary search insertion with visualization."""
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        middle = (left + right) // 2
        yield sorted_list[:], middle, pivot_index, -1, -1  # comparing positions
        if sorted_list[middle] < item:
            left = middle + 1
        else:
            right = middle - 1

    sorted_list.insert(left, item)
    yield sorted_list[:], left, pivot_index, -1, -1  # inserted position
    return sorted_list


def merge_insertion_sort_gen(collection, *args):
    """Merge-Insertion Sort as generator for visualization."""
    arr = collection[:]
    n = len(arr)

    if n <= 1:
        yield arr[:], -1, -1, -1, -1
        return arr

    # 1. Pairing step
    two_paired_list = []
    has_last_odd_item = (n % 2 == 1)
    for i in range(0, n - 1, 2):
        a, b = arr[i], arr[i + 1]
        if a < b:
            two_paired_list.append([a, b])
        else:
            two_paired_list.append([b, a])
        yield arr[:], i, i + 1, -1, -1

    # 2. Sort pairs by their first element
    two_paired_list.sort(key=lambda x: x[0])

    # 3. Build result with the smaller elements
    result = [p[0] for p in two_paired_list]
    result.append(two_paired_list[-1][1])  # append the biggest second
    yield result[:], -1, -1, -1, -1

    # 4. Insert last odd element if exists
    if has_last_odd_item:
        pivot = arr[-1]
        for state in binary_search_insertion_gen(result, pivot, n - 1):
            yield state
        result = state[0]  # final inserted result

    # 5. Insert remaining "second" elements from pairs
    for i in range(len(two_paired_list) - 1):
        pivot = two_paired_list[i][1]
        for state in binary_search_insertion_gen(result, pivot, i):
            yield state
        result = state[0]

    # Final state
    yield result[:], -1, -1, -1, -1
    return result
