import pytest

@pytest.fixture(scope="session", autouse=True)
def fixture_example():
    print("\nHere we have executed some PRE-conditions of full session")
    yield
    print("\nHere we have executed some POST-conditions of full session")

@pytest.fixture
def fixture_just_precond():
    print("\nHere we have executed some PRE-conditions")
    return

@pytest.fixture
def fixture_just_postcond():
    yield
    print("\nHere we have executed some POST-conditions")
