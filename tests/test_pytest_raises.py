"""
Q What is an exception
ans: an expection is an error that occur while program running
ex: 10/0 --> ZeroDivisionError

Why Do We Test Exceptions?
Imagine you're testing a login API.

If someone enters:

Username : admin
Password : (blank)

The application should return an error.

This is called negative testing.

Instead of checking successful scenarios only, we also verify that the application raises the correct error for invalid inputs.
Exception: An error that interrupts the normal execution of a Python program.
pytest.raises(): Used to verify that code raises an expected exception.
If no exception is raised: The test fails with DID NOT RAISE.
If a different exception is raised: The test fails because the exception type doesn't match.
Verify exception message: Use with pytest.raises(...) as exc: and assert str(exc.value).
Real-world use: Commonly used to test input validation, utility methods, file handling, and other error-handling scenarios to ensure the application behaves correctly with invalid input.
"""

import pytest

def divide(a,b):
    return a/b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1,0)

## ValueError Example
def convert(text):
    return int(text)

def test_invalid_int():
    with pytest.raises(ValueError):
        convert("a")


## IndexError Example

def test_index_error():
    numbers = [1,2,3,4,5]
    with pytest.raises(IndexError):
        print(numbers[10])

## KeyError Example
import pytest


def test_key_error():

    employee = {

        "name": "Viraj"

    }

    with pytest.raises(KeyError):
        print(employee["salary"])

## Type Error

def add(a,b):
    return a+ b

def test_type_error():
    with pytest.raises(TypeError):
        add(1,None)


# Verify the Exception Message
def divide1(a, b):
    return a / b

def test_exception_message():

    with pytest.raises(ZeroDivisionError) as exc_info:
        divide1(10, 0)

    assert "division by zero" in str(exc_info.value)


def validate_age(age):

    if age < 18:
        raise ValueError("Age must be at least 18")

    return True


def test_invalid_age():

    with pytest.raises(ValueError):
        validate_age(15)