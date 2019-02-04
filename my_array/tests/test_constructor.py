from .. import Array
from array import array
import pytest

def test_boolean_list():
    a_list = [False, True, True]
    arr = Array(a_list)
    assert arr.dtype == 'b'

def test_integer_list():
    a_list = [4, 2]
    arr = Array(a_list)
    assert arr.dtype == 'q'

def test_float_list():
    a_list = [5.3, 2, 0]
    arr = Array(a_list)
    assert arr.dtype == 'd'

def test_float_last_list():
    a_list = [1, 2, 4.4]
    arr = Array(a_list)
    assert arr.dtype == 'd'

def test_empty_list():
    arr = Array([])
    assert arr.dtype == 'd'

def test_python_array():
    arr_py = array('q', [2, 5, 2])
    arr = Array(arr_py)
    assert arr.dtype == 'q'

    arr_py = array('d', [2, 5, 2.34])
    arr = Array(arr_py)
    assert arr.dtype == 'd'

    arr_py = array('b', [False, True])
    arr = Array(arr_py)
    assert arr.dtype == 'b'

    arr_py = array('b', [])
    arr = Array(arr_py)
    assert arr.dtype == 'b'


def test_mixed_data_type_error():
    with pytest.raises(TypeError):
        Array([1, 4, 'asf'])

def test_not_list_or_array_error():
    with pytest.raises(TypeError):
        Array('asdf')
