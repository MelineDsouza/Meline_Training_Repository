
*** Settings ***
Resource     ../operational/multipletabs.robot
Library      SeleniumLibrary

*** Variables ***
${browser}    chrome
${url}     https://rahulshettyacademy.com/AutomationPractice/
${Title}

*** Test Cases ***
Testmultipletabs
    Open Browser  ${url}  ${browser}
    Sleep   3
    Maximize Browser Window
    Sleep   2
    tabshandling
    Sleep   2
#    Close Browser
