"""
=========================================================
PyTest Parallel Execution
=========================================================

What is Parallel Execution?
---------------------------
Parallel execution allows multiple tests to run
simultaneously using multiple worker processes or CPU
cores, significantly reducing the overall test execution
time.

PyTest supports parallel execution through the
pytest-xdist plugin.

=========================================================
How to Enable Parallel Execution
=========================================================

Install pytest-xdist:

    pip install pytest-xdist

Run tests using 4 workers:

    pytest -n 4

Automatically use all available CPU cores:

    pytest -n auto

=========================================================
Interview Questions
=========================================================

1. What is parallel execution?
------------------------------
Parallel execution runs multiple tests simultaneously
using multiple worker processes, reducing the overall
execution time.


2. Which plugin is used for parallel execution?
-----------------------------------------------
pytest-xdist


3. How do you run tests in parallel?
------------------------------------

Run with a fixed number of workers:

    pytest -n 4

Run using all available CPU cores:

    pytest -n auto


4. What does -n auto do?
------------------------
It automatically detects the available CPU cores and
creates an appropriate number of worker processes.


5. What are the advantages of parallel execution?
-------------------------------------------------
• Faster test execution
• Reduced CI/CD pipeline time
• Better CPU utilization
• Faster regression testing
• Improved developer productivity


6. What are the disadvantages?
------------------------------
• Shared resources can cause flaky tests
• Test data collisions
• Race conditions
• Harder debugging
• Tests must be independent


7. When should you avoid parallel execution?
--------------------------------------------
Avoid parallel execution when tests share resources such
as:

• Database records
• Files
• Browser sessions
• Global variables
• API test data
• Execution order dependencies

Running such tests in parallel may cause:

• Race conditions
• Data corruption
• Intermittent failures
• Unreliable test results


8. Where have you used parallel execution in a real project?
------------------------------------------------------------
Interview Answer:

"In our automation framework, we used pytest-xdist to
execute independent UI and API regression tests in
parallel within the CI/CD pipeline.

This reduced the regression execution time significantly.

Tests that shared databases, files, or common resources
were executed sequentially to prevent race conditions
and data conflicts."
"""

import time


# =====================================================
# Example Tests
# =====================================================

def test_one():
    time.sleep(2)
    assert True


def test_two():
    time.sleep(2)
    assert True


def test_three():
    time.sleep(2)
    assert True


def test_four():
    time.sleep(2)
    assert True