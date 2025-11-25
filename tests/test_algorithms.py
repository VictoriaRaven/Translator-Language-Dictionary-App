from yourmodule.algorithms import selection_sort, binary_search

def test_selection_sort_basic():
    assert selection_sort([3,1,2]) == [1,2,3]

def test_selection_sort_empty():
    assert selection_sort([]) == []

def test_selection_sort_duplicates():
    assert selection_sort([4,4,1,2]) == [1,2,4,4]

def test_binary_search_found():
    arr = [1,2,3,4,5]
    assert binary_search(arr, 3) == 2

def test_binary_search_not_found():
    assert binary_search([1,2,4,5], 3) == -1