*** settings ***
Library  Screenshot

*** variables ***
${path}  /home/hmicro/RobotFramework-Screenshots

*** test cases ***
Test Case one
    Set Screenshot Directory  ${path}
    Take Screenshot  screenshot2