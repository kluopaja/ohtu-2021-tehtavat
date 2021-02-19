*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application and Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
	Set Username  maija
	Set Password  maija123
	Set Password Confirmation  maija123
	Submit Registration
	Register Should Succeed

Register With Too Short Username And Valid Password
	Set Username  a
	Set Password  maija123
	Set Password Confirmation  maija123
	Submit Registration
	Register Should Fail With Message  Too short username

Register With Valid Username And Too Short Password
	Set Username  maija
	Set Password  maija12
	Set Password Confirmation  maija12
	Submit Registration
	Register Should Fail With Message  Too short password

Register With Nonmatching Password And Password Confirmation
	Set Username  maija
	Set Password  maija123
	Set Password Confirmation  maija132
	Submit Registration
	Register Should Fail With Message  Nonmatching password and password confirmation

Login After Successful Registration
	Set Username  maija
	Set Password  maija123
	Set Password Confirmation  maija123
	Submit Registration
	Register Should Succeed
	Go To Login Page
	Set Username  maija
	Set Password  maija123
	Submit Login
	Login Should Succeed
	
Login After Failed Registration
	Set Username  m
	Set Password  maija123
	Set Password Confirmation  maija123
	Submit Registration
	Register Should Fail With Message  Too short username
	Go To Login Page
	Set Username  maija
	Set Password  maija123
	Submit Login
	Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset Application And Go To Register Page
	Reset Application
	Go To Register Page
	Register Page Should Be Open

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registration
	Click Button  Register

Submit Login
    Click Button  Login

Register Should Succeed
	Welcome Page Should Be Open

Register Should Fail With Message
	[Arguments]  ${message}
	Register Page Should Be Open
	Page Should Contain  ${message}
