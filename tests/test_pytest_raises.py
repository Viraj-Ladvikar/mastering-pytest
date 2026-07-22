"""
=========================================================
PyTest - Testing Exceptions with pytest.raises()
=========================================================

What is an Exception?
---------------------
An exception is an error that occurs while a program is running.
It interrupts the normal flow of program execution.

Examples of common exceptions:
- ZeroDivisionError
- ValueError
- TypeError
- IndexError
- KeyError
- FileNotFoundError

Example:
--------
10 / 0

Output:
-------
ZeroDivisionError: division by zero


Why Do We Test Exceptions?
--------------------------
Imagine you're testing a Login API.

Input:
-------
Username : admin
Password : (blank)

Expected Result:
----------------
The application should return an error instead of logging in.

This is called Negative Testing.

Instead of testing only successful scenarios, we also verify that
the application correctly handles invalid inputs by raising the
appropriate exception.


Interview Summary
-----------------

• Exception
  An error that interrupts the normal execution of a Python program.

• pytest.raises()
  Used to verify that code raises an expected exception.

• If no exception is raised
  The test fails with:
      Failed: DID NOT RAISE

• If a different exception is raised
  The test fails because the exception type doesn't match.

• Verify Exception Message
  Store the exception using:

      with pytest.raises(...) as exc:

  Then verify the message using:

      assert str(exc.value)

• Real-World Usage
  Commonly used to test:
  - Input validation
  - Utility functions
  - API error handling
  - File handling
  - Database validations
  - Business rule validations
"""

import pytest


# =====================================================
# ZeroDivisionError Example
# =====================================================

def divide(a, b):
    return a / b


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# =====================================================
# ValueError Example
# =====================================================

def convert(text):
    return int(text)


def test_invalid_integer():
    with pytest.raises(ValueError):
        convert("abc")


# =====================================================
# IndexError Example
# =====================================================

def test_index_error():
    numbers = [1, 2, 3, 4, 5]

    with pytest.raises(IndexError):
        print(numbers[10])


# =====================================================
# KeyError Example
# =====================================================

def test_key_error():
    employee = {
        "name": "Viraj"
    }

    with pytest.raises(KeyError):
        print(employee["salary"])


# =====================================================
# TypeError Example
# =====================================================

def add(a, b):
    return a + b


def test_type_error():
    with pytest.raises(TypeError):
        add(1, None)


# =====================================================
# Verify Exception Message
# =====================================================

def divide_again(a, b):
    return a / b


def test_exception_message():

    with pytest.raises(ZeroDivisionError) as exc_info:
        divide_again(10, 0)

    assert "division by zero" in str(exc_info.value)


# =====================================================
# Custom Exception Example
# =====================================================

def validate_age(age):

    if age < 18:
        raise ValueError("Age must be at least 18")

    return True


def test_invalid_age():

    with pytest.raises(ValueError) as exc_info:
        validate_age(15)

    assert str(exc_info.value) == "Age must be at least 18"