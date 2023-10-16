import pytest
from src.some_module import some_file_operation_function, some_math_function

# Pytest is used to test larger frameworks with lots of flexibility.
# Output of pytest is better formatted and contains more information that unittest.
# Pytest has plugins like pytest-randomly, pytest-django etc...
# Able to use native assert statements.
# Lets you create fixtures for reusing setups.
# You can also use conftest.py to organize your fixtures and import in multiple places.
# You can define "marks" and run tests only with or without that mark.
# It lets you inhibit certain behaviour so nothing unexpected would be implemented.

# How to run?
# To run all tests: pytest tests/test_*.py
# To run tests in a module: pytest test_mod.py
# To run tests in a directory: pytest tests/
# To run by mark: pytest -m mark or pytest -m "not mark"
# To find slowest tests: pytest --durations=5

# Generating coverage report
# pytest --cov-report html tests/test_*.py --cov=src.some_module


@pytest.fixture
def variables_fixture():
    # Fixtures can be used in multiple tests.
    return (5, 10)


# This expression is used to create a mark named "mathematical" and adds this test to it.
@pytest.mark.mathematical
# We can include fixtures by supplying them to tests
def test_some_math_function(variables_fixture):
    a, b = variables_fixture
    assert some_math_function(a, b) == 9765630


# Parametrizing is used to test different cases for a certain function or method cleanly.
@pytest.mark.parametrize(
    "a, b, expected_result",
    [
        (5, 10, 9765630),
        (5, 5, 3125),
        (1, 5, 2),
    ],
)
def test_some_function_with_parameters(a, b, expected_result):
    assert some_math_function(a, b) == expected_result
