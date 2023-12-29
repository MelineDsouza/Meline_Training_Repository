#pytest is for unit testing//TestNG//Junit
# method-put some data in itand run
#before and after,groups,parameter,result,skip,priority
import pytest
from conftest import setup

def test_tc1(setup):
    print("meline")

@pytest.mark.sanity
def test_tc2():
    var = "sunil"
    assert var == "macline"


