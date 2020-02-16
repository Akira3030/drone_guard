# -*- coding: utf-8 -*-

class ValidateArgumentEntityExceptioin(Exception):
    """Error raised when an entity is not found in a repository"""


class MyAppValueError(Exception):
    def __init__(self, message, *args):         
        super(MyAppValueError, self).__init__(message, *args)