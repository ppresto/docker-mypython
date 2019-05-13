#!/usr/bin/env python3.7

# https://docs.python.org/3/glossary.html#term-decorator
# https://docs.python.org/3/library/functions.html#classmethod
# https://docs.python.org/3/library/functions.html#staticmethod
# https://docs.python.org/3/library/functions.html#property

"""
def inspect(func, *args):   #  '*args' collect all additional args and store into this variableself.
    print(f"Running {func.__name__}")
    val = func(*args)
    print(val)
    return val

def combine (a, b):
    return a + b

inspect(combine, 1, 2)


# create a decorated function that returns a function
def inspect(func):
    def wrapped_func(*args, **kwargs):  # get args and keyword args
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
        print(f"Result: {val}")
        return val
    return wrapped_func

@inspect   #decorate
def combine (a, b):
    return a + b

combine(1, b=2)
"""

class User:
    base_url = 'https://example.com/api'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# You can call this class without creatin a new instance.
# for example...   User.query().  helpful if you want to initialize an object.
    @classmethod
    def query(cls, query_string):
        return cls.base_url + '?' + query_string

    #called by User.name()
    @staticmethod
    def name():
        return 'Lucas Presto'

# user = User()
# user.full_name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

print(User.name())
print(User.query('name=Lucas'))
user = User('Jessica', 'Presto')
print(user.base_url)
print(user.full_name)
user.first_name = 'Patrick'
print(user.full_name)
