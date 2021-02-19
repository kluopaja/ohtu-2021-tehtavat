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

Register With Too Short Username And Valid Password
	Input New Command
	Input Credentials  a  abcd1234
	Output Should Contain  Too short username

Register With Valid Username and Too Short Password
	Input New Command
	Input Credentials  maija  a
	Output Should Contain  Too short password

Register With Valid Username And Long Enough Password Containing Only Letters
	Input New Command
	Input Credentials  maija  abcdefgh
	Output Should Contain  Password should not consist of only letters
