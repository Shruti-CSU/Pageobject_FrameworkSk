import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestGetData(BaseClass):

    def test_profiledata(self,dataload):  # To load the data we have to mentioned fixure name
        log = self.getlog() # calling getlog method from baseclass here and stored in object
        log.info(dataload[0])
        log.info(dataload[2])
        log.error(dataload[1])
        print(dataload[0])

print("end of test")
