import pytest
from conftest import setup

@pytest.mark.usefixtures("setup")
class Test_class:
    def test_c1(self):
        print("1st method")

    def test_c2(self):
        print("2st method")

    def test_c3(self):
        print("3st method")

@pytest.mark.usefixtures("data")
class Test_dt:
    def test_case7(self,data):
        print("name",data[2])

@pytest.mark.usefixtures("data2")
class Test_classtest:
    def test_case8(self, data2):
        print(data2)

