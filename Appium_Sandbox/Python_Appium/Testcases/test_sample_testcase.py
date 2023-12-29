from Python_Appium.POM_Pages.page_basicDeails import Deails
from Python_Appium.POM_Pages.page_basicDeails import Home
from pytest import mark
@mark.usefixtures("setup_driver")
class test_sampleclass:

    def test_navigate_To_Homepage(self,setup_driver):
        obj=Deails(setup_driver)
        obj.clickNextButton()
        obj.clickbutton()


    def test_homepage(self,setup_driver):
        obj2=Home(setup_driver)
        obj2.click2ndNextElement()



