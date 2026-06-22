import pytest

@pytest.fixture(scope='function')
def preparation_before_test():
    print("\n**********Start test**********")
    yield
    print("\n**********End test**********")


@pytest.fixture(scope='class')
def preparation_before_class():
    print("\n##########Start class##########")
    yield
    print("\n##########End class##########")

@pytest.fixture
def test_fixture_for_triangle_area(request):
    print("\n$$$$$$$$$$ Start test$$$$$$$$$$")
    def _wrapper(type_of_number: str):
        if type_of_number == "int":
            return 2, 3, 4, 2.9
        elif type_of_number == "float":
            return 3.3, 5.4, 3.2, 4.88
        elif type_of_number == "int and float":
            return 4, 5.5, 6, 10.7
    yield _wrapper
    print("\n$$$$$$$$$$End test$$$$$$$$$$")

@pytest.fixture
def test_fixture_for_triangle_perimetr(request):
    print("\n$$$$$$$$$$ Start test$$$$$$$$$$")
    def _wrapper(type_of_number: str):
        if type_of_number == "int":
            return 4, 5, 3, 12
        elif type_of_number == "float":
            return 5.4, 5.4, 4.4, 15.2
        elif type_of_number == "int and float":
            return 5, 5.5, 5, 15.5
    yield _wrapper
    print("\n$$$$$$$$$$End test$$$$$$$$$$")

