
*** Settings ***
Library     SeleniumLibrary

*** Keywords    ***
tabshandling
    Click Element     opentab
    @{windows}=     Get Window Handles
    Log To Console      ${windows}
    @{Titles}=      Get Window Titles
    Log To Console      ${Titles}[0]
    Switch Window       title=${Titles}[1]
    Close Browser