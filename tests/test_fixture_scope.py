"""
Scope	Runs
function	Before every test
class	Once per class
module	Once per Python file
session	Once for the entire test run
Interview Questions
1. What is fixture scope?

Fixture scope determines how often a fixture is created and reused during test execution.

2. What are the available fixture scopes?
function
class
module
session
3. Which scope is the default?
function
4. Which scope is used most often?

function is the most common because it provides test isolation.

5. When would you use session scope?

For expensive resources that can be shared across all tests, such as:

API clients
Database connections
Authentication setup
Configuration loading
6. Why not always use session scope?

Because shared state can cause one test to affect another, making tests less reliable.


"""

import pytest

@pytest.fixture(scope="session")
def browser():
    print("\nOpening Browser")
    return "Chrome"

def test_login(browser):
    assert browser == "Chrome"

def test_logout(browser):
    assert browser == "Chrome"