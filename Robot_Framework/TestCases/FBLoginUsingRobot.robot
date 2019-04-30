*** settings ***
Library  SeleniumLibrary
*** test cases ***
Login facebook
    Open facebook by Chrome
    Log in facebook  username  password

*** keywords ***
Open facebook by Chrome
    Open Browser  https://www.facebook.com  Chrome
    Wait Until Page Contains    Log In
Log in facebook
    [Arguments]  ${email}  ${password}
    Input Text  email  ${email}
    Input Password  pass  ${password}
    Click Button  Log In
    Wait Until Page Contains  facebookname
