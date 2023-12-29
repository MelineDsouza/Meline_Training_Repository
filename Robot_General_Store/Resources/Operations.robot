*** Settings ***
Resource    ../Resources/Resources.robot

*** Keywords ***

User Launches the Application
     Open Application  http://localhost:4723/wd/hub    devicename=${Device_name}  platformName=${platform_name}  appPackage=${App_package}  appActivity=${App_activity}

Enter Details and click Lets shop
     Wait Time
     AppiumLibrary.Input Text     ${Name}    ${Mac}
     Wait Time
     AppiumLibrary.Click Element    ${Female}
#     AppiumLibrary.Click Element    ${Country}
#     AppiumLibrary.Wait Until Element Is Visible    ${Afghanistan}
#     AppiumLibrary.Click Element    ${Afghanistan}
     Wait Time
#     AppiumLibrary.Click Element   ${LetsShop}
User selects country
      Wait for and Click on Element    ${country_select}      20s
      Wait Until Element Is Visible    ${antartica}
      Click Element    ${antartica}
#      Capture Page Screenshot
      Wait for and Click on Element   ${LetsShop}  20s

Swipe By Percentage Products
    ${screen_width}   Get Window Height
    ${screen_height}  Get Window Width

    # Calculate swipe coordinates based on percentages
    ${start_x}        Set Variable  ${screen_width * 0.2}
    ${start_y}        Set Variable  ${screen_height * 1}
    ${end_x}          Set Variable  ${screen_width * 0.2}
    ${end_y}          Set Variable  ${screen_height * 0.2}
    Swipe             ${start_x}  ${start_y}  ${end_x}  ${end_y}  duration=500
Add AirJordanMidSE to Cart
    Wait for and Click on Element    ${NikeBlazerMid}    10s
Check in cart
    Wait for and Click on Element   ${cart}    10s
    Wait for and Click on Element    ${Checkbox}    10s
    Wait for and Click on Element    ${websiteLink}     10s
    Wait Time


#User Enters the Email Email ID
#    Wait for and Click on Element  ${Sign_In}    30s
#    Page Should Contain Text    ${EmaiL_Text_Verification}
#    Wait for and Click on Element    ${UserName}    30s
#    Input Text  ${UserName}    ${Email_Id}
#    Wait Time
#    Wait for and Click on Element    ${Login_Button}    30s
#
#User Logs IN
#    Wait Time
#    Wait for and Click on Element    ${Password_Field}      30s
#    Input Text    ${Password_Field}    ${Password_Value}
#    Wait for and Click on Element    ${SignIn_Button}    30s
#    Wait Time
#    ${Present} =    Run Keyword And Return Status    Element Should be Visible    ${Skip_Button}
#    Run keyword If    ${Present}    Skip Pop Up
#    Wait Time
#    ${Present} =    Run Keyword And Return Status    Element Should be Visible    ${Skip_Button}
#    Run keyword If    ${Present}    User Enters Pin
#
#User Enters Pin
#    Wait Time
#    Press Keycode   16
#    Press Keycode   16
#    Press Keycode   16
#    Press Keycode   16
#    Press Keycode   16
#    Press Keycode   16
#    Wait for and Click on Element    ${Verify_Pin}    30s
#
#Skip Pop Up
#    Wait for and Click on Element    ${Skip_Button}    30s
#
#User adds cash to the Juno Wallet
#    Wait for and Click on Element    ${Add_Cash}    30s
#    Wait for and Click on Element    ${Confirm_Add_Cash}    30s
#    Wait Time
#    Click Text    ${Link Bank Account}    exact_match=True
#    Wait for and Click on Element    ${BackSpace}    30s
#    Wait for and Click on Element    ${BackSpace}    30s
#    Wait for and Click on Element    ${BackSpace}    30s
#    Wait for and Click on Element    ${Number_1}    30s
#    Wait for and Click on Element    ${Add_Next}    30s
#    Wait for and Click on Element    ${Confirm_Add}    30s
#    Wait Time
#    Wait for and Click on Element    ${Initiate_Transfer}    30s
#    Wait Time
#    Wait for and Click on Element    ${OTP_Screen}    30s
#    # ${Present} =    Run Keyword And Return Status    Page Should Contain Text    ${Confirm_Add_Money}
#    # Run keyword If    ${Present}    Enter Pin
#    Press Keycode   16
#    Press Keycode   16
#    Press Keycode   16
#    Press Keycode   16
#    Press Keycode   16
#    Press Keycode   16
#    Wait for and Click on Element    ${Confirm_OTP}    30s
#    Wait Time
#    Wait for and Click on Element    ${Dashboard}    30s
#    Wait for and Click on Element    ${But_Crypto}    30s
#    Click Text    ${Bitcoin_text}    exact_match=True
#    Wait for and Click on Element    ${Number_2}    30s
#    Wait Time
#    Wait for and Click on Element    ${Preview_buy}    30s
#    Wait Time
#    Swipe By Percent	10	95	95	95
#    Wait for and Click on Element    ${Dashboad_button}    30s
