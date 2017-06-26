*** Settings ***
Documentation    Simple Example
Library    ../Resources/ConverterLibrary.py

*** Variables ***

*** Test Cases ***
Test case - eur to usd
    test usd
    result should be    5.6000000000000005

Test case - eur to mkd
    test mkd
    result should be    308.45

Test case - eur to chf
    test chf
    result should be    5.45

Test case - eur to dem
    test dem
    result should be    9.6

*** Keywords ***