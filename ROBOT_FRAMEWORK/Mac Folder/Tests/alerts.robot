
*** Settings ***
Resource     ../operational/alert_instruction.robot
Library      SeleniumLibrary

*** Variables ***
${browser}    chrome
${url1}     https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Managing with alerts
    Open Browser  ${url1}  ${browser}
    Sleep   5
    Maximize Browser Window
    Alerts
    Sleep   5
    Close Browser



