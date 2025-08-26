def beadSort(array, *args):
    """
    Bead Sort (Gravity Sort) adapted for visualization.
    Works only for non-negative integers.
    Yields states for visualization: (array, red1, red2, blue1, blue2).
    """

    if any(not isinstance(x, int) or x < 0 for x in array):
        raise TypeError("Bead Sort requires non-negative integers only.")

    n = len(array)
    if n == 0:
        return

    max_val = max(array)

    # Create "abacus" representation: each rod has beads stacked
    beads = [[0] * n for _ in range(max_val)]

    for col, num in enumerate(array):
        for row in range(num):
            beads[row][col] = 1

    # Let beads fall down step by step
    for row in range(max_val):
        # Count beads on this row
        sum_row = sum(beads[row])
        for col in range(n):
            if col < n - sum_row:
                beads[row][col] = 0
            else:
                beads[row][col] = 1

        # Update array after this row has settled
        for col in range(n):
            array[col] = sum(beads[r][col] for r in range(max_val))

        # Yield the current state
        yield array[:], -1, -1, row % n, -1
