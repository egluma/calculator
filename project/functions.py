import numpy as np

def addition(a, b):
    """This function defines a simple math addition of two numbers"""
    return a + b


def subtraction(a, b):
    """This function returns a simple math subtraction of two numbers"""
    return a - b


def multiplication(a, b):
    """This function returns a simple math multiplication of two numbers"""
    return a * b


def division(a, b):
    """This function returns a simple math division from the first argument by the second argument"""
    return a / b


def take_root(a, b):
    """This function returns a algebraic root from the first argument by the second argument"""
    return np.power(a, (1 / b))