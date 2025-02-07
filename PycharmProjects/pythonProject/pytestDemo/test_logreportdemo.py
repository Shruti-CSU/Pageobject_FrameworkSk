
import pytest

from pytestDemo.BaseClass import BaseClass


class CallingClass(BaseClass):
    def test_method1(self):
        log = self.test_getlog()
        log.info("This is info")
        print("End of the test")