""" Test for unused private/protected functions and classes """

# pylint:disable=too-few-public-methods,missing-class-docstring,missing-function-docstring
# pylint:disable=unused-variable

def _unused():  # [unused-private-function]
    pass

def __unused():  # [unused-private-function]
    pass

class _UnusedClass():  # [unused-private-class]
    pass

# No messages when private/protected functions and classes are used
def _used_fn():
    pass

def _used_fn2():
    pass

def _used_fn3():
    pass

def __used_fn():
    pass

class _UsedClass():
    pass

class _UsedClass2():
    pass

_used_fn()
__used_fn()
obj = _UsedClass()

# Used inside a separate function
def other_fn():
    _used_fn2()
    obj2 = _UsedClass2()
    return _used_fn3

# Private class members used and unused won't be affected by this check
class ClassA:
    def _func_unused(self):
        pass
    def _func_used(self):
        pass
    @staticmethod
    def _func_unused_static():
        pass
    @staticmethod
    def _func_used_static():
        pass

    def do_something(self):
        ClassA._func_used_static()
        self._func_used()

# No messages for public functions and classes when used and when not
def unused_fn():
    pass
class UnusedClass():
    pass

def used_fn():
    pass
class UsedClass:
    pass
used_fn()
obj3 = UsedClass()
