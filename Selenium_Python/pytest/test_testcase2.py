import pytest

@pytest.mark.sanity
def test_tc3():
    a = 2
    b = 3
    c = a+b
    print(c)
    print("pytest is done")

@pytest.mark.xfail
def test_caseregression():
    print("pythontest done")



