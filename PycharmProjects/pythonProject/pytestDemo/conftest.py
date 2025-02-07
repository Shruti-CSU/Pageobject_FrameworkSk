import pytest

@pytest.fixture()
def dataload():
    print("This is from profile date")
    return ["shruti","Patel","Tester"]

@pytest.fixture()
def setup():
    print("This fixture from conftest")


@pytest.fixture(params=["chrome", "Firefox", "Edge"])
def crossbrowsers(request):
    return request.param