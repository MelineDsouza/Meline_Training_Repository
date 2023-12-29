
*** Settings ***
Library     SeleniumLibrary

*** Keywords    ***
Alerts
       SeleniumLibrary.Click Button  xpath://input[@id="alertbtn"]
       BuiltIn.Sleep    3
       SeleniumLibrary.Handle Alert         accept
#       SeleniumLibrary.Handle Alert         dismiss
#       SeleniumLibrary.Handle Alert         Leave
#       SeleniumLibrary.Alert Should Be Present         text here mac!
#       SeleniumLibrary.Alert Should Not Be Present         notesthere mac