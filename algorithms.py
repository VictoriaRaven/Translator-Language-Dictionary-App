# ---------------- Algorithms ----------------
def selection_sort(arr):
    """Selection sort - returns a new sorted list. O(n^2)"""
    a = list(arr)
    n = len(a)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return a

def binary_search(sorted_list, target):
    """Binary search on a sorted list. Returns index or -1. O(log n)"""
    lo, hi = 0, len(sorted_list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1