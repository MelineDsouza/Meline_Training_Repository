
*** Settings ***
Library     SeleniumLibrary

*** Keywords    ***
loginToApplication
#    Click Link  xpath://input[@name="username"]
    Title Should Be     OrangeHRM
    Input Text      xpath://input[@name="username"]     Admin
    Input Text      xpath://input[@name="password"]     admin123
    Click Button     xpath://button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]
    Sleep   5
    ${Search}    Set Variable    xpath://input[@class="oxd-input oxd-input--active"]
    Element Should Be Visible   ${Search}
    Element Should Be Enabled   ${Search}
    Input Text  ${Search}    time
    Sleep   5
#    Clear Element Text  ${Search}


TesttheUserbox
    Title Should Be nopCommerce demo Store
    Click Link  xpath://*[@class'ifndofn']
    ${Email}    Set Variable    xpath://*[@class'ifndofn']
    Element Should Be Visible   ${Email}
    Element Should Be Enabled   ${Email}
    Input Text  ${Email}    meline@gmail.com
    Sleep   5
    Clear Element Text  ${Email}
    Sleep   3

