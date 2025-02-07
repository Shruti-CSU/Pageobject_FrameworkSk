# any pytest file name should be start with test_ or end with _test
# pytest method name should be start with test
# Any code should be wrapped in method only
# -k use for to run specific method like -k method1
# -s use for log prints
# -m use to run smoke testcases like -m smoke @pytest.mark.smoke
# @pytest.mark.skip use to skip specific testcase
# @pytest.mark.xfail use to run testcase but it will not report pass/fail
# fixtures are used for generalize one testcases and it should be declared in conftest file
# To generate a report use command --html=report.html so for ex py.test --html=report.html -s
# You can use any name for report like --html=inventoryreport.html 

import pytest

def test_method1():
    print("Hello")


# @pytest.mark.smoke
# @pytest.mark.skip
def test_method2():
    a = 5
    b = 7
    assert a+2 == b

# fixture is used to run pre-requsite conditions

@pytest.fixture()
def prereq():
    print("I will be treated as pre-requsite and run fist")
    yield
    print("yield used to run last after pre-req then method associate to that and then yield")


def test_method3(prereq):
    print("I will be execute after pre-req steps and to add connection we need to pass fixture method as an argument")