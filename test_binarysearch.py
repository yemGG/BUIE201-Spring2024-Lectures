import binarysearch

def test_1():
    assert binarysearch.search_iterative1([1,2,3], 2) == 1
    
def test_2():
    assert binarysearch.search_iterative1([1,2,3], 4) == -1