# A Simple Calculator
## Description
The package contains a simple calculator that a user can use to perform basic mathematical actions.
## Features

The calculator is able to add or subtract a given number from the calculator's memory as well as multiply, divide and take the nth algebraic root. Multiple actions can be performed each updating the calculator's memory to the most recent result. 

## Installation
The package can be installed using the following line:

```
pip install git+https://github.com/egluma/calculator
```
## Usage
_class_ project.calculator.Calculator(memory)

### Attributes:
memory : float, default = 0

### Methods:
`add(addend)` adds a given addend to calculator's memory

`subtract(subtrahend)` subtracts a given subtrahend from calculator's memory

`multiply(multiplier)` multiplies calculator's memory by a given factor (multiplier)

`divide(divisor)` divides calculator's memory by a given divisor

`nthroot(n)` takes the nth root of calculator memory. The calculator can take the algebraic root of a number, so using this method with negative calculator memory will not return a value and calculator memory will remain unchanged.

`reset()` resets calculator memory to 0

#### Examples
```buildoutcfg
from project.calculator import Calculator

>>> example = Calculator()  # create an instance of the class
>>> example.memory
0
```
```buildoutcfg
>>> example.add(3)
>>> example.multiply(20)
>>> example.memory
60
```
