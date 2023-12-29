
*** Settings ***
Resource     ../operational/dropdown_instruction.robot
Library      SeleniumLibrary

*** Variables ***
${browser}    chrome
${url1}     https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
TestDropdowns
    Open Browser  ${url1}  ${browser}
    Sleep   5
    Maximize Browser Window
    Sleep   5
    ${Speed}        SeleniumLibrary.Get Selenium Speed
    Log To Console      ${Speed}
    SeleniumLibrary.Set Selenium Speed 2 seconds
    dropdown
    Close Browser