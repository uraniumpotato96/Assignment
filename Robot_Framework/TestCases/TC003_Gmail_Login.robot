*** settings ***
Library  SeleniumLibrary

*** variables ***
${Browser}  Chrome
${URL}  https://www.google.com

*** test cases ***

TC_001 Open The Browser
    Open Browser  ${URL}  ${Browser}
TC_002 Click On Gmail
    Click Link  xpath://a[text()='Sign in']
TC_004 Enter The User name
    Input Text  name:identifier  risheek96bharadwaj@gmail.com
TC_005 Click On Next
    Click Element  xpath://div[@id="identifierNext"]
TC_006 Enter Password
    Wait Until Element Is Visible  name:password
    Input Password  name:password  P@s$w0RD
TC_007 Click On Next
    Click Element  xpath://*[@id="passwordNext"]/content/span