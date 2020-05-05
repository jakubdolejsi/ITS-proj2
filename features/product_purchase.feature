Feature: Product buying process

  Background:
    Given "MacBook" is available in the e-shop
    And "MacBook" with quantity "1" is in the shopping cart

  Scenario: Checkout options with registration
    Given web browser is at  checkout page on step "1"
    And "Register Account" is selected
    When user clicks on the "Continue" button
    Then step "2" is shown

  Scenario: Un-successful Account & billing details - not filled fields
    Given web browser is at checkout page on step "2"
    And user is not logged
    And user selected "Register Account" in step "1"
    And all required fields are empty
    And "Privacy Policy" checkbox is checked
    When user clicks on the "Continue" button
    Then error messages are shown under each required field

  Scenario: Un-successful Account & billing details - privacy policy
    Given web browser is at checkout page on step "2"
    And user is not logged
    And user selected "Register Account" in step "1"
    And all required fields are filled
    And "Privacy Policy" checkbox is not checked
    When user clicks on the "Continue" button
    Then Error message is shown


  Scenario: Successful Account & billing details
    Given web browser is at checkout page on step "2"
    And user is not logged
    And user selected "Register Account" in step "1"
    And all required fields are filled
    And "Privacy Policy" checkbox is checked
    When user clicks on the "Continue" button
    Then step "3" is shown

  Scenario: Checkout options as guest
    Given web browser is at Checkout page on step "1"
    And Guest Checkout is selected
    When user clicks on the "Continue" button
    Then step "2" is shown

  Scenario: Un-successful Billing Details as guest
    Given web browser is at checkout page on step "2"
    And all required fields are empty
    When user clicks on the "Continue" button
    Then error messages are shown under each required field

  Scenario: Successful billing details as guest
    Given web browser is at checkout page on step "2"
    And all required fiels are filled
    When user clicks on the "Continue" button
    Then step "3" is shown

  Scenario: Un-successful payment method
    Given web browser at checkout page on step "3"
    And "Terms & Conditions" checkbox is not checked
    When user clicks on the "Continue" button
    Then error message is shown

  Scenario: Successful payment method
    Given web browser at checkout page on step "3"
    And "Terms & Conditions" checkbox is checked
    When user clicks on the "Continue" button
    Then step "4" is shown

  Scenario: Confirm order
    Given web browser is at checkout page on step "4"
    When user clicks ont he "Confirm Order" button
    Then message about successful order is shown


  Scenario: Billing details as logged user with same address
    Given web browser is at checkout page on step "2"
    And user is logged in
    And "I want to use an exisitng address" selected
    When user clicks on "Continue" button
    Then step "3" is shown

  Scenario: Un-successful billing details as logged user with different address
    Given web browser is at checkout page on step "2"
    And user is logged in
    And "I want to user a new address" is selected
    And all required fields are not filled
    When user clicks on the "Continue" button
    Then error messages are shown under each required field

  Scenario: Successful billing details as logged user with different address
    Given web browser is at checkout page on step "2"
    And user is logged in
    And "I want to user a new address" is selected
    And all required fields are filled
    When user clicks on the "Continue" button
    Then step "3" is shown
