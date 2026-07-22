"""
=========================================================
PyTest Markers
=========================================================

What are Markers?
-----------------
Markers are labels that allow you to group and selectively
run specific tests.

Imagine your project contains:

• 500 Smoke tests
• 2,000 Regression tests
• 100 Sanity tests

Running all 2,600 tests every time would be slow.

Instead, you can run only the tests you need by assigning
markers to them.


Interview Questions
===================

1. What are markers in PyTest?
------------------------------
Markers are tags used to categorize tests so that
specific groups of tests can be executed independently.

Examples:
- Smoke
- Regression
- Sanity
- API
- Database
- UI


2. Why do we use markers?
-------------------------
Markers help us:

• Run only the required tests.
• Reduce execution time.
• Organize large test suites.
• Support CI/CD pipelines.
• Execute feature-specific tests.


3. How do you create a marker?
------------------------------
Use the @pytest.mark decorator.

Example:

    @pytest.mark.smoke
    def test_login():
        pass


4. Can a test have multiple markers?
------------------------------------
Yes.

Example:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login():
        pass


5. How do you execute marked tests?
-----------------------------------

Run Smoke tests:

    pytest -m smoke

Run Regression tests:

    pytest -m regression

Run Sanity tests:

    pytest -m sanity

Run multiple markers:

    pytest -m "smoke or regression"

Run tests having both markers:

    pytest -m "smoke and regression"

Exclude Smoke tests:

    pytest -m "not smoke"


6. Where have you used markers in real projects?
------------------------------------------------
Interview Answer:

"In my automation framework, I used Smoke markers for
critical business flows such as login, checkout, and
payment. Regression markers were applied to the complete
test suite, while Sanity markers were used to verify
major functionality after each deployment.

During CI/CD, the Smoke suite was executed after every
build, and the full Regression suite was scheduled to
run overnight."
"""

import pytest


# =====================================================
# Function-Level Markers
# =====================================================

@pytest.mark.smoke
def test_homepage():
    """Verify that the homepage loads successfully."""
    assert True


@pytest.mark.regression
def test_payment():
    """Verify payment functionality."""
    assert True


@pytest.mark.sanity
def test_profile():
    """Verify profile page functionality."""
    assert True


# =====================================================
# Multiple Markers
# =====================================================

@pytest.mark.smoke
@pytest.mark.regression
def test_login():
    """Verify login functionality."""
    assert True


# =====================================================
# Class-Level Tests with Markers
# =====================================================

class TestLogin:
    """Login-related test cases."""

    @pytest.mark.smoke
    def test_valid_login(self):
        assert True

    @pytest.mark.regression
    def test_invalid_login(self):
        assert True


class TestPayment:
    """Payment-related test cases."""

    @pytest.mark.regression
    def test_card_payment(self):
        assert True

    @pytest.mark.sanity
    def test_upi_payment(self):
        assert True