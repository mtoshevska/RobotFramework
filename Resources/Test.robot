*** Settings ***
Documentation  Simple Example
Library  ConverterLibrary

*** Variables ***

*** Test Cases ***
Test case - eur to usd
    Test usd
    Result should be  5.6000000000000005

*** Keywords ***
