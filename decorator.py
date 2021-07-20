import logging
import sys


"""
Let’s assume we have a method

@your_decorator(True)
def factorial(n):
   if n < 2:
       return 1
   return factorial(n - 1) * n

You need to implement a function your_decorator(enable_logging) that implements caching. It means we should store input value and calculated output. Also it should log whether the cache was used in case enable_logging is True.
Example:
>>> print(factorial(3))
6
>>> print(factorial(3))
2019-02-28 15:57:30,689 Cache hit for number 3
6
>>> print(factorial(4))
2019-02-28 15:57:30,689 Cache hit for number 3
24
"""


def logging_service():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)


def my_decorator(enable_loggin):
    cache = dict()

    if enable_loggin:
        logging_service()

    def real_decorator(func):
        def wrapper(n):
            if n not in cache:
                cache[n] = func(n)
                return cache[n]
            else:
                logging.debug('Cache hit for number {}'.format(n))
                return cache[n]
        return wrapper
    return real_decorator


@my_decorator(enable_loggin=True)
def factorial(n):
    if n < 2:
        return 1
    return factorial(n - 1) * n

print(factorial(3))
print(factorial(3))
print(factorial(4))

