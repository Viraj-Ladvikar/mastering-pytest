"""
=========================================================
PyTest Parameterization
=========================================================

What is @pytest.mark.parametrize?
---------------------------------
Parameterization allows the same test function to run
multiple times with different sets of input data.

Instead of writing multiple test functions with different
values, you can write one test and provide multiple inputs.

=========================================================
Interview Questions
=========================================================

1. What is @pytest.mark.parametrize?
------------------------------------
It is a PyTest decorator that executes the same test
function multiple times using different input values.

Example:

    @pytest.mark.parametrize("num", [1, 2, 3])
    def test_number(num):
        assert num > 0


2. Why do we use parameterization?
----------------------------------
• Avoid duplicate test code
• Improve readability
• Support data-driven testing
• Increase test coverage
• Reduce maintenance effort


3. Can parameterize accept multiple arguments?
----------------------------------------------
Yes.

Example:

    @pytest.mark.parametrize(
        "username, password",
        [
            ("admin", "admin123"),
            ("guest", "guest123")
        ]
    )


4. Where have you used parameterization in a real project?
----------------------------------------------------------
Interview Answer:

"In my automation framework, I used
@pytest.mark.parametrize to validate multiple login
credentials, API request payloads, HTTP status codes,
database inputs, and boundary test data without creating
separate test functions for each scenario."

5. What are the advantages of parameterization?
-----------------------------------------------
• Reusable test logic
• Less duplicate code
• Easy to maintain
• Better readability
• Higher test coverage
"""

import pytest


# =====================================================
# Single Parameter Example
# =====================================================

@pytest.mark.parametrize("success_code", [200, 201, 205])
def test_success_status(success_code):
    """Verify valid HTTP success status codes."""
    assert success_code in [200, 201, 205]


# =====================================================
# Multiple Parameters Example
# =====================================================

@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("admin", "admin123", True),
        ("admin", "wrongpass", False),
        ("guest", "guest123", True),
    ]
)
def test_login(username, password, expected):
    """Verify login with multiple credentials."""

    # Simulated login logic
    result = (password != "wrongpass")

    assert result == expected


# =====================================================
# Mathematical Example
# =====================================================

@pytest.mark.parametrize(
    "number, square",
    [
        (2, 4),
        (3, 9),
        (4, 16),
        (5, 25),
    ]
)
def test_square(number, square):
    """Verify square calculation."""
    assert number * number == square