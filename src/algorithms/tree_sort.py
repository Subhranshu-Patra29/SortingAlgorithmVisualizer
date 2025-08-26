from dataclasses import dataclass
from collections.abc import Iterator


@dataclass
class Node:
    val: int
    left: "Node | None" = None
    right: "Node | None" = None

    def __iter__(self) -> Iterator[int]:
        if self.left:
            yield from self.left
        yield self.val
        if self.right:
            yield from self.right

    def insert(self, val: int) -> None:
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)


def tree_sort_visualize(arr, *args):
    """
    Generator version of Tree Sort for visualization.
    Yields: (array_snapshot, redBar1, redBar2, blueBar1, blueBar2)
    """

    if not arr:
        yield [], -1, -1, -1, -1
        return

    # Step 1: Build the tree with visualization
    root = Node(arr[0])
    yield arr[:], 0, -1, -1, -1   # First element as root

    for i, item in enumerate(arr[1:], start=1):
        root.insert(item)
        # Highlight inserted element
        yield arr[:], i, -1, -1, -1

    # Step 2: Traverse tree in-order and rebuild sorted list
    sorted_arr = []
    for i, value in enumerate(root):
        sorted_arr.append(value)
        # Yield partial sorted array + highlight current value
        yield sorted_arr + arr[len(sorted_arr):], i, -1, -1, -1

    # Final yield: fully sorted
    yield sorted_arr, -1, -1, -1, -1
