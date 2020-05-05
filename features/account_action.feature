Feature: User account operations

  Scenario: Create new account
    Given web browser is at e-shop register page
    When all required fields are filled
    And privacy policy is accepted
    When user clicks on "Continue" button
    Then user account is created


  Scenario: Login into existing account
    Given web browser is at e-shop login page
    And  all required fields are filled
    When user clicks on "Login" button
    Then user is logged in

  Scenario: Logout
    Given web browser is at e-shop site
    And user is logged in
    And "My Account" dropdown menu is opened
    When user clicks on "Logout" button
    Then user is logged out