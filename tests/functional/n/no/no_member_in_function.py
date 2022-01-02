""" Test that no-member check works inside a function. """

# pylint:disable=too-few-public-methods,missing-function-docstring

# https://github.com/PyCQA/pylint/issues/5626
class Class:
    """Empty class"""


def my_function(arg: Class) -> None:
    arg.shouldFail()  # [no-member]


obj = Class()
obj.shouldFail()  # [no-member]
