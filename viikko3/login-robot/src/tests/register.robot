*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username and Password
	Input New Command
	Input Credentials  aapeli  abcd1234
	Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
	Input New Command
	Input Credentials  maija  abcd1234
	Input New Command
	Input Credentials  maija  abcd1234
	Output Should Contain  User with username maija already exists
