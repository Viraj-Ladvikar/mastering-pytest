"""
=========================================================
PyTest xfail (Expected Failure)
=========================================================

What is xfail?
--------------
Sometimes a test is expected to fail because:

• A known bug already exists.
• The feature has not been fixed yet.
• The development team is working on it.

Instead of skipping the test, you mark it as an
Expected Failure using @pytest.mark.xfail.

Unlike @pytest.mark.skip, the test still executes.

=========================================================
Interview Questions
=========================================================

1. What is xfail?
-----------------
xfail (Expected Failure) marks a test that is expected
to fail due to a known defect or incomplete feature.

The test still runs, but PyTest reports it as XFAIL
instead of FAILED.


2. Why do we use xfail?
-----------------------
• Known bugs
• Feature under development
• Temporary issues
• To document expected failures
• To automatically detect when bugs are fixed


3. What is the difference between skip and xfail?
-------------------------------------------------

skip
-----
• Test is NOT executed.
• Result is reported as SKIPPED.

xfail
------
• Test IS executed.
• Expected failure is reported as XFAIL.


4. What is XPASS?
-----------------
XPASS (Unexpected Pass) means a test was expected to
fail but actually passed.

This usually indicates that the underlying bug has been
fixed.


5. What does strict=True do?
----------------------------
When strict=True is enabled:

• If the test fails → XFAIL (Expected)
• If the test unexpectedly passes → FAILED (XPASS becomes FAIL)

This ensures developers remove the xfail marker after
the bug has been fixed.


6. Where have you used xfail in a real project?
-----------------------------------------------
Interview Answer:

"In my automation framework, I used xfail for tests
covering known defects. The tests continued to execute
during every regression run, allowing us to know
immediately when a bug was fixed. Once the defect was
resolved, we removed the xfail marker and treated the
test as a normal regression test."
"""

import sys
import pytest


# =====================================================
# Basic xfail Example
# =====================================================

@pytest.mark.xfail(reason="Known bug #123")
def test_login():
    assert 2 == 3


# =====================================================
# XPASS Example
# =====================================================

@pytest.mark.xfail(reason="Bug expected")
def test_addition():
    # This test passes even though it was expected to fail.
    # Result: XPASS
    assert 2 + 2 == 4


# =====================================================
# strict=True Example
# =====================================================

@pytest.mark.xfail(reason="Known bug", strict=True)
def test_strict_mode():
    # Because strict=True is enabled,
    # this unexpected pass becomes a FAILURE.
    assert 2 + 2 == 4


# =====================================================
# Conditional xfail
# =====================================================

@pytest.mark.xfail(
    sys.platform == "win32",
    reason="Known issue on Windows"
)
def test_platform_feature():
    assert True


# =====================================================
# Expected Failure Example
# =====================================================

@pytest.mark.xfail(reason="Known calculation bug")
def test_expected_failure():
    assert 10 == 20