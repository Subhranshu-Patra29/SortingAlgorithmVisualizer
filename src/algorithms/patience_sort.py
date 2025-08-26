from bisect import bisect_left
from functools import total_ordering
from heapq import merge

@total_ordering
class Stack(list):
    def __lt__(self, other):
        return self[-1] < other[-1]

    def __eq__(self, other):
        return self[-1] == other[-1]

def patience_sort_visualize(collection, *args):
    """
    Generator version of patience sort for visualization.
    Yields (array_snapshot, red1, red2, blue1, blue2)
    """

    stacks: list[Stack] = []
    arr = collection[:]

    # Step 1: Build stacks
    for idx, element in enumerate(arr):
        new_stack = Stack([element])
        i = bisect_left(stacks, new_stack)
        if i != len(stacks):
            stacks[i].append(element)
        else:
            stacks.append(new_stack)

        # Flatten stacks for visualization
        flat = [x for stack in stacks for x in stack]
        yield flat, idx, -1, -1, -1   # highlight current element in red

    # Step 2: Merge stacks into sorted result
    sorted_list = list(merge(*(reversed(stack) for stack in stacks)))
    for i in range(len(sorted_list)):
        yield sorted_list[:i+1] + arr[i+1:], i, -1, -1, -1

    yield sorted_list, -1, -1, -1, -1
