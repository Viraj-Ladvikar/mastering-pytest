"""
=========================================================
PyTest Markers
=========================================================

What are Markers?
-----------------
Markers are labels used to group tests so that specific
sets of tests can be executed independently.

Example:
--------
Imagine your project contains:

• 500 Smoke tests
• 2,000 Regression tests
• 100 Sanity tests

Running all 2,600 tests after every code change is time-
consuming. Instead, markers allow you to execute only the
required test suite.


Interview Questions
=========================================================

1. What are PyTest markers?
---------------------------
Markers are labels (tags) used to categorize tests and
selectively execute them.

Common markers include:
• smoke
• regression
• sanity
• api
• ui
• database

You can also create your own custom markers.


2. Why do we use markers?
-------------------------
• Group related tests
• Execute only the required test suite
• Reduce execution time
• Organize large automation suites
• Support CI/CD pipelines


3. How do you create a marker?
------------------------------

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

Run Smoke OR Regression:

    pytest -m "smoke or regression"

Run tests having BOTH markers:

    pytest -m "smoke and regression"

Exclude Smoke tests:

    pytest -m "not smoke"


6. Why do we register markers in pytest.ini?
--------------------------------------------
To:
• Avoid PytestUnknownMarkWarning
• Document all custom markers
• Improve maintainability


Example:

[pytest]
markers =
    smoke: Smoke test suite
    regression: Regression test suite
    sanity: Sanity test suite


7. Where have you used markers in a real project?
-------------------------------------------------
Interview Answer:

"In my automation framework, I categorized tests using
Smoke, Regression, and Sanity markers.

• Smoke tests covered critical business flows such as
  Login, Checkout, and Payment. They ran after every build.

• Regression tests covered the complete application and
  were executed before releases or overnight.

• Sanity tests verified major functionalities after new
  deployments or hotfixes.

Using markers reduced execution time and allowed the CI/CD
pipeline to execute only the required test suite."
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
# Class-Level Markers
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