import project.functions as func


class Calculator:

    def __init__(self):
        """Default calculator memory is set to 0"""
        self.memory = 0

    def do_function(self, number, function):
        """This function passes the number in calculator memory as an argument in a given function.
        The other number to be passed in a function is defined by the user."""
        try:
            self.memory = function(self.memory, number)
            return self.memory
        except TypeError:
            print('Oops!  That was no valid number.  Try again...')

    def add(self, addend):
        """This function adds a provided number to the number in calculator memory"""
        return self.do_function(addend, func.addition)

    def subtract(self, subtrahend):
        """This function subtracts the number provided by the user from the number in calculator memory"""
        return self.do_function(subtrahend, func.subtraction)

    def multiply(self, multiplier):
        """This function multiplies the number in calculator memory by the number provided (multiplier)"""
        return self.do_function(multiplier, func.multiplication)

    def nthroot(self, n):
        """This function takes the root provided by the user from the number in calculator memory if the number
        provided is positive"""
        return self.do_function(n, func.take_root)

    def divide(self, divisor):
        """This function divides the number in calculator memory by the number provided (divisor)"""
        if divisor == 0:
            return 'Cannot divide by 0'
        else:
            return self.do_function(divisor, func.division)

    def reset(self):
        """This function resets calculator memory to 0"""
        self.memory = 0
        return f'Calculator memory is set to {self.memory}'
