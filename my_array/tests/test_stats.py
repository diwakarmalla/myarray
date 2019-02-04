from .. import Array

arr = Array([5, 8, -4])
arr2 = Array([-3, 5, 2, 10])

def test_sum():
    assert arr.sum() == 9
    assert arr2.sum() == 14

def test_max():
    assert arr.max() == 8

def test_min():
    assert arr.min() == -4

def test_mean():
    assert arr.mean() == 3

def test_median():
    assert arr.median() == 5