*** Settings ***
Resource    ../Resources/Resources.robot


*** Test Cases ***
#Test Case 1
User Opens the General Store Application and Add shoe in Cart
    [Tags]  BasicDetails
    User Launches the Application
    Enter Details and click Lets shop
    User selects country
    Swipe By Percentage Products
    Add AirJordanMidSE to Cart
    Check in cart

#Test Case 2
Add Item to Cart
    [Tags]  AddCart
    Swipe By Percentage Products
    Add AirJordanMidSE to Cart
    Check in cart







#    Given User Launches the Application
#    When User Enters the Email Email ID
#    Then User Logs IN
#
##Test Case 2
#User Adds Cash to the Juno App
#    [Tags]  Add_Cash
#    Given User adds cash to the Juno Wallet
