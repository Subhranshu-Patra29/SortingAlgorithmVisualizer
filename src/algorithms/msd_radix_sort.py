# algorithms/msd_radix_sort.py

def msdRadixSort(array, left=0, right=None, *args):
    """
    MSD Radix Sort (bitwise, in-place) visualizer generator.
    Yields: (array_snapshot, red1, red2, blue1, blue2)
      - red1/red2: active indices (scans / swaps)
      - blue1/blue2: current subarray boundaries [left..right]
    """
    if right is None:
        right = len(array) - 1

    n = right - left + 1
    if n <= 0:
        yield array, -1, -1, -1, -1
        return

    # Support negatives by shifting all keys for bit tests (no data change)
    sub_min = min(array[left:right + 1]) if n > 0 else 0
    shift = -sub_min if sub_min < 0 else 0

    # Highest bit to inspect
    max_val = max((x + shift) for x in array[left:right + 1]) if n > 0 else 0
    start_bit = max_val.bit_length() - 1
    if start_bit < 0:
        yield array[:], -1, -1, -1, -1
        return

    # Run recursive in-place MSD partitioning
    yield from _msd_radix_inplace_gen(array, left, right, start_bit, shift)

    # Final clean frame
    yield array[:], -1, -1, -1, -1


def _msd_radix_inplace_gen(a, lo, hi, bit, shift):
    """In-place MSD partition on bit, then recurse. hi is inclusive."""
    if lo >= hi or bit < 0:
        return

    i, j = lo, hi
    # Two-pointer partition: zeros to left, ones to right on current bit
    while i <= j:
        # advance i while bit == 0
        while i <= j and (((a[i] + shift) >> bit) & 1) == 0:
            yield a[:], i, -1, lo, hi
            i += 1
        # retreat j while bit == 1
        while i <= j and (((a[j] + shift) >> bit) & 1) == 1:
            yield a[:], j, -1, lo, hi
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
            yield a[:], i, j, lo, hi
            i += 1
            j -= 1

    # Now zeros are in [lo .. i-1], ones in [i .. hi]
    mid = i
    # Optional: show partition completion for this segment
    yield a[:], -1, -1, lo, hi

    # Recurse on zero block
    if lo < mid - 1:
        yield from _msd_radix_inplace_gen(a, lo, mid - 1, bit - 1, shift)
    # Recurse on one block
    if mid < hi:
        yield from _msd_radix_inplace_gen(a, mid, hi, bit - 1, shift)
