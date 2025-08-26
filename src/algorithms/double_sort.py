def doubleSort(array, *args):
    """
    Double Sort (Cocktail Shaker Sort) with visualization support.
    Yields states (array, redBar1, redBar2, blueBar1, blueBar2).
    """
    n = len(array)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Pass from left to right
        for i in range(start, end):
            yield array[:], i, i + 1, -1, -1  # comparing
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                yield array[:], i, i + 1, -1, -1  # after swap

        if not swapped:
            break

        swapped = False
        end -= 1

        # Pass from right to left
        for i in range(end - 1, start - 1, -1):
            yield array[:], i, i + 1, -1, -1  # comparing
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                yield array[:], i, i + 1, -1, -1  # after swap

        start += 1

    yield array[:], -1, -1, -1, -1  # final sorted state
