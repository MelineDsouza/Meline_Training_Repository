from POM_classes.Home_Page import Home
from Test_Scripts.conftest import setup

def test_filter_i_phones(setup):
    obj = Home(setup)
    obj.selectfurniture()