*** Settings ***
Resource    ../Resources/Resources.robot

*** Keywords ***

Wait for and Click on Element
    [Arguments]    ${element}    ${element2}
    AppiumLibrary.Wait Until Element Is Visible  ${element}    ${element2}
    AppiumLibrary.Click Element    ${element}

Wait Time
    Sleep    20s

Click on Element and Wait
    [Arguments]    ${element}    ${element2}
    AppiumLibrary.Click Element    ${element}
    AppiumLibrary.Wait Until Element Is Visible    ${element2}

