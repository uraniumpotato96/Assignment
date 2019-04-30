*** settings ***
Library  SeleniumLibrary

*** variables ***
${Browser}  Chrome
${URL}  https://www.google.com

*** test cases ***
TC_001 Browser Start
    Open Browser  ${URL}  ${Browser}
TC_003 Search In Browser
    Input Text  name:q  facebook

TC_004 Close Browser
    Close Browsere