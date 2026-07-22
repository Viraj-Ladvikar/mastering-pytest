"""
=========================================
PyTest Test Classes
=========================================

What is a Test Class?
---------------------
A Test Class is a Python class used to group related test methods.

Why do we use 'self'?
---------------------
Every instance method inside a Python class must have 'self' as its first parameter.
It represents the current object of the class.

PyTest Test Class Naming Conventions
------------------------------------
1. Class name should start with 'Test'
   Example:
       class TestLogin:

2. Test method names should start with 'test_'
   Example:
       def test_valid_login(self):

When Should You Use Test Classes?
---------------------------------
Use a test class when:
- Tests belong to the same feature (Login, Dashboard, Orders, etc.)
- You want to share fixtures across multiple tests
- You want better organization and cleaner test reports

Avoid using a test class when:
- You have only one or two simple tests
- Tests are unrelated
- No shared setup or fixtures are required

PyTest supports both:
- Function-based tests
- Class-based tests
"""

# =========================================
# Calculator Tests
# =========================================

class TestCalculator:
    """Tests related to calculator functionality."""

    def test_addition(self):
        assert 2 + 2 == 4

    def test_subtraction(self):
        assert 6 - 2 == 4


# =========================================
# Login Tests
# =========================================

class TestLogin:
    """Tests related to login functionality."""

    def test_valid_login(self):
        assert True

    def test_invalid_login(self):
        assert True


# =========================================
# Dashboard Tests
# =========================================

class TestDashboard:
    """Tests related to dashboard functionality."""

    def test_dashboard_loaded(self):
        assert True

    def test_logout(self):
        assert True