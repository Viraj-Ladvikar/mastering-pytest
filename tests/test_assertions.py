"""
=========================================================
PyTest Assertions
=========================================================

Think of an assertion as a checkpoint.

Example:
--------
You log in to an application.

After clicking the Login button, what do you verify?

You verify that:
- The Dashboard page is displayed.
- The logged-in user's name is displayed.
- The URL changes to the Dashboard URL.

These verifications are called assertions.

---------------------------------------------------------
Important Interview Points
---------------------------------------------------------

• Assertion
  A statement that verifies whether the expected result
  matches the actual result.

• Purpose
  To validate application behavior and determine whether
  a test passes or fails.

• assert vs print()
  - assert validates the result and can fail the test.
  - print() only displays information for debugging.

• Failed Assertion
  - Raises an AssertionError.
  - Stops the current test execution.
  - Marks the test as Failed.

• Multiple Assertions
  Yes, one test can contain multiple assertions.
  Execution stops at the first failed assertion.

• Assertion Introspection
  PyTest automatically displays the expected and actual
  values when an assertion fails, making debugging easier.

• Custom Assertion Messages
  Used to provide meaningful, business-specific failure
  messages in test reports.
"""


class TestAssertion:
    """Examples of different types of PyTest assertions."""

    # =====================================================
    # Equality Assertion
    # =====================================================

    def test_addition(self):
        result = 2 + 2
        assert result == 4

    def test_name(self):
        name = "Viraj"
        assert name == "Viraj"

    # =====================================================
    # Boolean Assertion
    # =====================================================

    def test_boolean(self):
        is_logged_in = True
        assert is_logged_in is True

    # =====================================================
    # Not Equal Assertion
    # =====================================================

    def test_not_equal(self):
        age = 18
        assert age != 30

    # =====================================================
    # Greater Than Assertion
    # =====================================================

    def test_salary(self):
        salary = 20000
        assert salary > 10000

    # =====================================================
    # Less Than Assertion
    # =====================================================

    def test_marks(self):
        marks = 60
        assert marks < 62

    # =====================================================
    # Membership Assertion
    # =====================================================

    def test_list(self):
        fruits = ["Apple", "Banana", "Orange"]
        assert "Banana" in fruits

    # =====================================================
    # Not In Assertion
    # =====================================================

    def test_not_in(self):
        fruits = ["Apple", "Banana", "Orange"]
        assert "Kiwi" not in fruits

    # =====================================================
    # String Assertion
    # =====================================================

    def test_string(self):
        text = "Hello"
        assert text == "Hello"

    # =====================================================
    # None Assertion
    # =====================================================

    def test_none(self):
        value = None
        assert value is None

    # =====================================================
    # Identity Assertion
    # =====================================================

    def test_identity(self):
        name = "Viraj"
        another_name = name

        assert another_name is name

    # =====================================================
    # Negative Test (Expected to Fail)
    # =====================================================

    def test_age(self):
        age = 18
        assert age == 30

    # =====================================================
    # Assertion with Custom Message
    # =====================================================

    def test_message(self):
        age = 18
        assert age == 30, "Age should be 30."

    # =====================================================
    # API Response Assertions
    # =====================================================

    def test_api_response(self):
        response = {
            "status": "success",
            "code": 200,
        }

        assert response["code"] == 200
        assert response["status"] == "success"


# =========================================================
# Assignment
# =========================================================

class TestAssertionAssignment:
    """Practice assertion exercises."""

    # Check whether a number is even.

    def test_even_number(self):
        number = 8
        assert number % 2 == 0

    # Check whether a string starts with "Py".

    def test_string_starts_with(self):
        text = "Pytest"
        assert text.startswith("Py")

    # Check whether a sentence contains "framework".

    def test_contains_word(self):
        sentence = "pytest is the testing framework"
        assert "framework" in sentence

    # Check whether a list contains 100.

    def test_list_contains_value(self):
        numbers = [1, 2, 33, 445, 32, 100]
        assert 100 in numbers

    # Check whether a dictionary contains the key "username".

    def test_dictionary_key(self):
        user = {
            "username": "viraj",
            "password": "Akola@123"
        }

        assert "username" in user