from statistics import median
from array import array
from collections import Counter
import random
from . import _utils

import requests

options_max_values = 20

stat_doc = \
'''
Finds {name} of all the values in the array

Returns
-------
int or float
'''

def add_doc(func):
    func.__doc__ = stat_doc.format(name=func.__name__)
    return func

class Array:
    '''
    This is a single-dimensional numeric
    array for scientific computing.

    This array will compute lots of
    basic statistics.

    Attributes
    ----------
    data: list
        List of numbers

    Methods
    -------
    TODO
    '''


    def __init__(self, data):
        # Allow user to pass only an array or a list
        if isinstance(data, array):
            # TODO - check for cases where typecode is not 'b', 'q', or 'd'
            self._data = data
        elif isinstance(data, list):
            dtype = _utils.get_dtype_of_list(data)

            # if there is mixed data types in the list
            # such that the first element is integer and the next float                
            try:
                self._data = array(dtype, data)
            except TypeError:
                self._data = array('d', data)
        else:
            raise TypeError('Array constructor only accepts lists or arrays')
        # b - boolean (1 byte integer)
        # q - interger (8 bytes)
        # d - float (8 bytes)
        self.dtype = self._data.typecode

    
    @property
    def data(self):
        return self._data

    # data is read only
    # @data.setter
    # def data(self, value):
    #     self._data = value


    @property
    def dtype(self):
        # getter
        return self.__dict__['dtype']

    #dtype is writeable for now
    @dtype.setter
    def dtype(self, value):
        self.__dict__['dtype'] = value

    @add_doc
    def sum(self):
        return sum(self.data)

    @add_doc
    def max(self):
        return max(self.data)

    @add_doc
    def min(self):
        return min(self.data)

    @add_doc
    def mean(self):
        return self.sum() / len(self)

    @add_doc
    def median(self):
        return median(self.data)

    def __repr__(self):
        final_str = ''
        # TODO: validate against even/odd number
        # TODO: CHeck if you array is a float. Limit decimals with an option
        # TODO: If dtype is 'b' then output True or False for each value
        half_max = options_max_values // 2
        if len(self) < options_max_values:
            for val in self.data:
                final_str += f'{val:5}\n'
        else:
            for val in self.data[:half_max]:
                final_str += f'{val:5}\n'
            final_str += '...\n'
            for val in self.data[-half_max:]:
                final_str += f'{val:5}\n'
        return final_str

    def __len__(self):
        return len(self.data)
    
    def sort(self, reverse=False):
        data = sorted(self, reverse=reverse)
        return Array(data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.data[key]
        elif isinstance(key, slice):
            return Array(self.data[key])
        elif isinstance(key, list):
            # TODO: getitem with a list
            raise NotImplementedError('Not done yet. Will do soon!!')
        else:
            raise TypeError('key must be an int, slice, or a list')

    def __setitem__(self, key, value):
        if isinstance(key, int):
            # TODO: Change data type of array if given float
            self.data[key] = value
        # TODO: Can you set items with a slice or list

    def __add__(self, other):
        # return an array that has `value` added to each element
        if isinstance(other, (bool, int, float)):
            data = [val + other for val in self]
        elif isinstance(other, Array):
            if len(self) != len(other):
                raise ValueError(f'Arrays must be same length {len(self)} != {len(other)}')
            data = [val1 + val2 for val1, val2 in zip(self, other)]
        else:
            raise TypeError('other must be a bool, int, float, or an Array')
        return Array(data)

    def __sub__(self, value):
        # return an array that has `value` added to each element
        data = [val - value for val in self]
        return Array(data)

    def __mul__(self, value):
        # return an array that has `value` added to each element
        data = [val * value for val in self]
        return Array(data)

    def __truediv__(self, value):
        # return an array that has `value` added to each element
        data = [val / value for val in self]
        return Array(data)

    def __floordiv__(self, value):
        # return an array that has `value` added to each element
        data = [val // value for val in self]
        return Array(data)

    def __pow__(self, value):
        # return an array that has `value` added to each element
        data = [val ** value for val in self]
        return Array(data)

    def __mod__(self, value):
        # return an array that has `value` added to each element
        data = [val % value for val in self]
        return Array(data)

    # TODO: implement the right-side operators like __radd__
    # TODO: implement array to array arithmetic operations just like we did in __add__

    # Implement >

    def __gt__(self, other):
        # return an array that has `value` added to each element
        if isinstance(other, (bool, int, float)):
            data = [val > other for val in self]
        elif isinstance(other, Array):
            if len(self) != len(other):
                raise ValueError(f'Arrays must be same length {len(self)} != {len(other)}')
            data = [val1 > val2 for val1, val2 in zip(self, other)]
        else:
            raise TypeError('other must be a bool, int, float, or an Array')
        return Array(data)

    # TODO: Implement the rest of the comparison operators

    # Use collection module to find mode

    ## Class method to create a random array

    def mode(self):
        c = Counter(self)
        return c.most_common(1)

    # TODO: What happens if there are ties
    # TODO: Create parameters for users to control output

    # MAKE ALTERNATE CONSTRUCTOR

    # arr = Array([1, 5, 6])

    # arr1 = Array.create_random(low, high, n) 
    # This would produce a random array of numbers between low and high
    # This is a class method

    @classmethod
    def create_random_ints(cls, low, high, n):
        data = [random.randint(low, high) for i in range(n)]
        return cls(data)
        # does the same thing `Array(data)`

    @classmethod
    def create_from_dict(cls, d):
        if not isinstance(d, dict):
            raise TypeError('d must be a dictionary')
        data = list(d.keys())
        return cls(data)

    @classmethod
    def create_from_list_of_strings(cls, strings):
        data = [int(string) for string in strings]
        return cls(data)

    @classmethod
    def create_random_uniform(cls, low, high, n):
        data = [random.uniform(low, high) for i in range(n)]
        return cls(data)

    @classmethod
    def return_non_array(cls):
        return 5

    @classmethod
    def create_from_string(cls, string):
        if not isinstance(string, str):
            raise TypeError('Must be a string')
        data = []
        for s in string.split():
            data.append(int(s))
        return cls(data)

    # Make one classmethod that generates random numbers 
    # Make another that converts lists of strings that are digits into an array

    @classmethod
    def get_stock_data(cls, symbol, date_range='5y'):
        BASE_URL = 'https://api.iextrading.com/1.0/'
        end_point = f'/stock/{symbol}/chart/{date_range}'
        url = BASE_URL + end_point

        # pip3 install requests
        req = requests.get(url)
        data_json = req.json()
        data = [day['close'] for day in data_json]
        return cls(data)

# Write method to write all data to a file of users choice

    def write(self, file_name):
        with open(file_name, 'w') as f:
            for val in self:
                f.write(f'{val}\n')


def read_file(file_name):
    # TODO: Convert to integer?
    data = [float(line.strip('\n')) for line in open(file_name)]
    return Array(data)

from functools import reduce
from operator import add

def concat(arrays):
    # input: list or tuple or Arrays
    # output is a single concatenated Array
    py_arrays = [arr.data for arr in arrays]
    data = reduce(add, py_arrays)
    return Array(data)

def concat2(arrays):
    py_arrays = [arr.data for arr in arrays]
    return Array(sum(py_arrays[1:], py_arrays[0]))

def concat3(arrays):
    # don't use - mutates underlying data
    arr_final = arrays[0].data
    for arr in arrays[1:]:
        arr_final += arr.data
    return Array(arr_final)

