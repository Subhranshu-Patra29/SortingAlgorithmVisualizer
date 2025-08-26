def circleSort(array, *args):
    """
    Circle Sort adapted for visualization.
    Yields states (array, redBar1, redBar2, blueBar1, blueBar2).
    """

    def circle_sort_util(arr, low, high):
        swapped = False
        left = low
        right = high

        while left < right:
            yield arr[:], left, right, -1, -1  # just comparison

            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right], arr[left]
                swapped = True
                yield arr[:], left, right, -1, -1  # after swap

            left += 1
            right -= 1

        # middle element check (safe index check)
        if left == right and right + 1 <= high and arr[left] > arr[right + 1]:
            yield arr[:], left, right + 1, -1, -1
            arr[left], arr[right + 1] = arr[right + 1], arr[left]
            swapped = True
            yield arr[:], left, right + 1, -1, -1

        if high - low > 1:
            mid = low + (high - low) // 2
            left_swapped = yield from circle_sort_util(arr, low, mid)
            right_swapped = yield from circle_sort_util(arr, mid + 1, high)
            swapped = swapped or left_swapped or right_swapped

        return swapped

    swapped = True
    while swapped:
        swapped = yield from circle_sort_util(array, 0, len(array) - 1)

    yield array[:], -1, -1, -1, -1  # final state (all sorted)
