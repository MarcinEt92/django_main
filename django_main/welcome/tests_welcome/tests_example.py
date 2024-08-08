import pytest


@pytest.fixture(scope="session")
def fixture_1():
    print("Fixture 1")
    return 1


@pytest.fixture
def yield_fixture():
    print("start yield")
    yield 6
    print('End of yield')


def test_example(fixture_1):
    print("run ex 1")
    num = fixture_1
    assert num == 1


def test_example2(yield_fixture):
    print("run ex 1")
    assert yield_fixture == 6
