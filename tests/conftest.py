"""
=========================================================
PyTest conftest.py
=========================================================

What is conftest.py?
--------------------
conftest.py is a special PyTest configuration file used
to define shared fixtures, hooks, and test configuration.

Fixtures defined in conftest.py are automatically
available to all test files in the same directory and
its subdirectories.

No import statement is required.

=========================================================
Why do we use conftest.py?
=========================================================

• Centralize reusable fixtures
• Eliminate duplicate setup code
• Improve maintainability
• Keep test files clean
• Share common configuration across multiple tests

=========================================================
Interview Questions
=========================================================

1. What is conftest.py?
-----------------------
conftest.py is a special PyTest file that stores shared
fixtures, hooks, and configuration. PyTest automatically
discovers it during test execution.


2. Why do we use conftest.py?
-----------------------------
• Reuse fixtures
• Reduce duplicate code
• Simplify maintenance
• Keep test files focused on test logic


3. Do we import fixtures from conftest.py?
------------------------------------------
No.

PyTest automatically discovers fixtures from
conftest.py and injects them into test functions.


4. Can we have multiple conftest.py files?
------------------------------------------
Yes.

Large projects often have one at the project root
and additional conftest.py files inside folders such as:

tests/
│
├── conftest.py
├── api/
│   ├── conftest.py
│   └── test_users.py
│
└── ui/
    ├── conftest.py
    └── test_login.py

Each conftest.py applies to its own directory and
its subdirectories.


5. What is usually stored inside conftest.py?
---------------------------------------------
• Browser fixtures
• API client fixtures
• Authentication tokens
• Database connections
• Test data
• Hooks (pytest_runtest_setup, etc.)
• Command-line options
• Global configuration


6. Where have you used conftest.py in a real project?
-----------------------------------------------------
Interview Answer:

"In my automation framework, I used conftest.py to
manage browser initialization, API clients,
authentication tokens, common test data, database
connections, and shared setup/teardown logic.

This reduced code duplication and made the framework
much easier to maintain."

7. Can we write test cases inside conftest.py?
----------------------------------------------
No.

conftest.py should only contain shared fixtures,
hooks, and configuration.

Test cases should always be written in test_*.py files.
"""

import pytest


# =====================================================
# Shared Browser Fixture
# =====================================================

@pytest.fixture
def browser():
    """Provide browser information."""
    return "Chrome"


# =====================================================
# Shared Base URL Fixture
# =====================================================

@pytest.fixture
def base_url():
    """Provide the application base URL."""
    return "http://127.0.0.1:8000"