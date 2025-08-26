# algorithms/natural_sort.py
import re

def naturalSort(array, *args):
    """
    Natural sort visualizer generator.
    Works with both strings and integers.
    Yields: (array_snapshot, red1, red2, blue1, blue2)
    """

    def alphanum_key(key):
        key = str(key)  # ensure string
        return [int(s) if s.isdigit() else s.lower()
                for s in re.split("([0-9]+)", key)]

    n = len(array)
    arr = array[:]  # copy to avoid mutating caller’s input

    # Bubble sort with natural comparison
    for i in range(n):
        for j in range(0, n - i - 1):
            # Highlight current comparison
            yield arr[:], j, j+1, -1, -1
            if alphanum_key(arr[j]) > alphanum_key(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Highlight after swap
                yield arr[:], j, j+1, -1, -1

    # Final clean frame
    yield arr[:], -1, -1, -1, -1
