*** settings ***

Library  SeleniumLibrary


*** variables ***
${Browser}  Chrome
${URL}  http://www.google.com


*** test cases ***
TC_001 Browser Start
    Open Browser  ${URL}  ${Browser}
Tc_002 Browser Close
    Close Browser
