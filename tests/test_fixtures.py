"""
=========================================================
PyTest Fixtures
=========================================================

What is a Fixture?
------------------
A fixture is a reusable function that provides test data,
resources, or setup code before a test executes.

Think of a fixture as common setup code that can be shared
across multiple tests.

=========================================================
How Fixtures Work
=========================================================

1. PyTest sees the fixture name in the test function
   parameters.

2. It searches for a fixture with the same name.

3. The fixture is executed.

4. The returned value is injected into the test.

Example:

    @pytest.fixture
    def browser():
        return "Chrome"

    def test_login(browser):
        assert browser == "Chrome"

=========================================================
Interview Questions
=========================================================

1. What is a fixture in PyTest?
-------------------------------
A fixture is a reusable function that provides setup data,
resources, or objects to test functions before execution.


2. Why do we use fixtures?
--------------------------
• Avoid duplicate setup code
• Improve code reusability
• Simplify test maintenance
• Make tests cleaner and easier to read
• Manage test setup and cleanup


3. How does PyTest know which fixture to use?
---------------------------------------------
PyTest matches the test function parameter name with
the fixture function name.

Example:

    @pytest.fixture
    def browser():
        return "Chrome"

    def test_login(browser):
        assert browser == "Chrome"


4. Can one test use multiple fixtures?
--------------------------------------
Yes.

Example:

    def test_login(browser, username, password):
        ...

PyTest automatically injects all requested fixtures.


5. Where have you used fixtures in a real project?
--------------------------------------------------
Interview Answer:

"In my automation framework, I used fixtures to
initialize browser instances, create API clients,
generate authentication tokens, load test data,
establish database connections, and perform common
setup and teardown activities.

Using fixtures reduced duplicate code and made the
framework easier to maintain."

6. What is the scope of a fixture?
----------------------------------
PyTest supports different fixture scopes:

• function (default)
• class
• module
• package
• session

The scope determines how often the fixture is created.
"""

import pytest


# =====================================================
# Basic Fixture Example
# =====================================================

@pytest.fixture
def browser():
    """Return the browser name."""
    return "Chrome"


def test_login(browser):
    assert browser == "Chrome"


def test_logout(browser):
    assert browser == "Chrome"


# =====================================================
# Multiple Fixtures
# =====================================================

@pytest.fixture
def username():
    return "admin"


@pytest.fixture
def password():
    return "admin123"


def test_user_login(username, password):
    assert username == "admin"
    assert password == "admin123"


# =====================================================
# Real-World API Example
# =====================================================

@pytest.fixture
def base_url():
    return "https://api.example.com"


@pytest.fixture
def auth_token():
    return "Bearer xyz123"


def test_get_users(base_url, auth_token):
    assert base_url.startswith("https://")
    assert auth_token.startswith("Bearer")


# =====================================================
# Fixture Scope Example
# =====================================================

@pytest.fixture(scope="module")
def database():
    print("\nConnecting to database...")
    yield "Database Connection"
    print("\nClosing database connection...")


def test_database_connection(database):
    assert database == "Database Connection"


def test_database_query(database):
    assert database == "Database Connection"