import time

from POM_Login.LoginPage import Login
from testcases.conftest import setup
# class Test_Login_1(Login):
#     # name="Admin"
#     # pwd="admin123"

def test_Login(setup):
    obj = Login(setup)
    obj.test_Enter_username(name="Admin")
    obj.test_Enter_password(pwd="admin123")




