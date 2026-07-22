"""
=========================================================
PyTest - Skipping Tests
=========================================================

What is Skipping?
-----------------
Sometimes you don't want a test to run.

Examples:
---------
• A feature is not developed yet.
• A known bug already exists.
• The QA environment is unavailable.
• The API server is down.
• The test only works on Windows or Linux.
• A third-party service is unavailable.

Instead of deleting the test, you skip it.


Interview Questions
===================

1. What is skipping in PyTest?
------------------------------
Skipping allows you to prevent a test from running while
keeping it in the test suite.

The skipped test is reported as "SKIPPED" instead of
"PASSED" or "FAILED".


2. Why do we skip tests?
------------------------
Common reasons include:

• Feature not implemented
• Known bug
• Environment unavailable
• Platform-specific functionality
• Third-party dependency unavailable
• Test is temporarily disabled


3. Difference between @pytest.mark.skip and @pytest.mark.skipif?
---------------------------------------------------------------

@pytest.mark.skip
    Always skips the test.

@pytest.mark.skipif
    Skips the test only when the specified condition
    evaluates to True.


4. Can you skip a test during execution?
----------------------------------------
Yes.

Example:

    pytest.skip("Database unavailable")

This is useful when a required dependency is not available
while the test is running.


5. Where have you used skipping in a real project?
--------------------------------------------------
Interview Answer:

"In my automation framework, I used @pytest.mark.skip
for features that were temporarily disabled and
@pytest.mark.skipif for tests that should run only
in specific environments or operating systems.

I also used pytest.skip() inside tests when a required
dependency, such as a database, API service, or test
environment, was unavailable during execution."
"""

import sys
import pytest


# =====================================================
# Skip Individual Test
# =====================================================

@pytest.mark.skip(reason="Login feature is temporarily disabled")
def test_valid_login():
    assert True


# =====================================================
# Skip Entire Test Class
# =====================================================

@pytest.mark.skip(reason="Payment module is under maintenance")
class TestPayment:
    """Tests related to payment functionality."""

    def test_card_payment(self):
        assert True

    def test_upi_payment(self):
        assert True


# =====================================================
# Skip Based on a Condition
# =====================================================

@pytest.mark.skipif(
    sys.platform == "win32",
    reason="This feature is supported only on Linux."
)
def test_linux_feature():
    assert True


# =====================================================
# Real-World Example
# =====================================================

@pytest.mark.skip(reason="Payment API is under maintenance")
def test_make_payment():
    assert True


# =====================================================
# Feature Not Yet Implemented
# =====================================================

@pytest.mark.skip(reason="Registration feature is not implemented")
def test_registration():
    assert True


# =====================================================
# Platform-Specific Test
# =====================================================

@pytest.mark.skipif(
    sys.platform == "win32",
    reason="Runs only on Linux."
)
def test_linux():
    assert True


# =====================================================
# Skip During Test Execution
# =====================================================

def test_database_connection():
    """
    Skip the test if the database is unavailable.
    """

    database_available = False

    if not database_available:
        pytest.skip("Database is unavailable.")

    assert True