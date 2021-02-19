*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username and Password
	Input New Command
	Input Credentials  aapeli  abcd1234
	Output Should Contain  New user registered
