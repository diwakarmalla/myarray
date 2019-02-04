def decorator(func):
    print(" i have decorated some function")
    return 5

def decorator2(func):
    print(" i have decorated some function")
    return func

import datetime
def decorator3(func):
    def wrapper(x):
        today = str(datetime.datetime.today())
        with open('log_square.txt', 'a') as f:
            f.write(today)
        return func(x)
    return wrapper


@decorator3
def square(x):
    return x ** 2



# syntatic sugar for `square = decorator(square)`

if __name__ == '__main__':
    # if I'm running this file as a sript
    print(square(10))