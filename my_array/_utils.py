'''
Utilities for our Array
'''

def get_dtype_of_list(data):
    if len(data) == 0:
        # hack - forcing array to be a float
        first_item = 0.0
    else:
        first_item = data[0]

    if isinstance(first_item, bool):
        dtype = 'b'
    elif isinstance(first_item, int):
        dtype = 'q'
    elif isinstance(first_item, float):
        dtype = 'd'
    else:
        raise TypeError('List must only contain bool, '
                        'ints, or floats')
    return dtype