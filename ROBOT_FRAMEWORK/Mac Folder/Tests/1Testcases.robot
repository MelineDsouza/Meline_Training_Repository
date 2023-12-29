
*** Settings ***
Resource     ../operational/1instruction.robot
Library      SeleniumLibrary

*** Variables ***
${browser}    chrome
${url}     https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
#${url1}  https://demo.nocommerce.com/

*** Test Cases ***
LoginTest
    Open Browser  ${url}  ${browser}
    Sleep   3
    Maximize Browser Window
    Sleep   2
    loginToApplication
    Sleep   2
#    Close Browser

Logout
    Click Element    css:.oxd-userdropdown-tab
    Click Element    xpath://a[text()='Logout']

#TestingInputBox
#    Open    Browser  ${{url1}  ${browser}
#    Maximize    Browser    Window
#    TesttheUserbox
#    Close   Browser

