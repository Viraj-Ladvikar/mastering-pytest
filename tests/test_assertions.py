"""
Think of an assertion as a checkpoint.
Example:
You log in to an application.
After clicking Login, what do you verify?
You verify:
Dashboard is displayed
User name is displayed
URL changed

Those verifications are assertions.



Assertion: A statement that verifies whether the expected result matches the actual result.
Purpose: To validate application behavior and determine whether a test passes or fails.
assert vs print(): assert validates and can fail a test; print() only displays information.
Failed assertion: Raises AssertionError, stops the current test, and marks it as failed.
Multiple assertions: Yes, but execution stops at the first failed assertion.
Assertion introspection: PyTest automatically displays detailed expected vs. actual values when an assertion fails.
Custom assertion messages: Used to provide clearer, domain-specific information in failure reports.

"""

## First Assertion
class TestAssertion:

    def test_addition(slef):
        result = 2 + 2
        assert result == 4

    ## Equality Assertion

    def test_name(self):
        name = "Viraj"
        assert name == "Viraj"

    ## Boolean Assertion
    def test_boolean(self):
        is_login = True
        assert is_login == True

    ## Not equal

    def test_not_equal(self):
        age =18
        assert age != 30

    ## Greater Than

    def test_salary(self):
        salary = 20000

        assert salary > 10000

    ## Less Than

    def test_marks(self):
        marks = 60

        assert marks < 62

    ## Membership Assertion
    def test_list(self):
        fruits = ["Apple", "Banana", "Orange"]

        assert "Banana" in fruits

    ## Not In

    def test_not_in(self):
        fruits = ["Apple", "Banana", "Orange"]

        assert "Kiwi" not in fruits

    ## String assertion
    def test_string(self):
        text = "Hello"
        assert text == "Hello"

    ## None Assertion
    def test_none(self):
        value = None

        assert value is None

    ## Identity Assertion

    def test_identity(self):
        value = "Viraj"
        assert value == "Viraj"

    ## Negative Tes

    def test_age(self):
        age = 18
        assert age == 30

    ## Assertions with Messages

    def test_messsage(self):
        age = 18
        assert age == 30,"Age Should be 18"

    ## API response
    def test_api(self):

        resp = {
            "status":"success",
            "code":200,
        }

        assert  resp["code"] == 200
        assert resp["status"] == "success"

# ===========================================================================================
                # Assingment #
#===========================================================================================

    ## Even Number

    def test_even(self):
        num = 8

        assert num % 2 == 0

    ## String Strat with "Py"

    def test_start_with(self):
        text ="Pytest"

        assert text.startswith("Py")

    ## Check if the framework exists in the sentence

    def test_contain(self):
        sentence = "pytest is the testing framework"
        assert "framework" in sentence

    ## Check if a list contains 100.

    def test_lst_contain(self):
        lst =[1,2,33,445,32,100]

        assert 100 in lst

    ## Check if a dictionary contains the key "username"

    def test_dict(self):
        d ={"username":"viraj","password":"Akola@123"}
        assert "username" in d


