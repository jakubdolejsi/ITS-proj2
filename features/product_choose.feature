Feature: Product choosing

  Background:
    Given "MacBook" is available

  Scenario: Choose product from search bar
    Given web browser is opened at e-shop home page
    When user types "MacBook" into "Search" bar
    Then "Not Found" error is shown

   Scenario: choose product from featured
     Given web browser is at home e-shop page
     And "MacBook" is in the "Featured" section
     When user clicks on "MacBook" product
     Then "MacBook" product page is opened

  Scenario: choose product from section
    Given e-shop has "Mac" and "Laptops & Notebooks" category
    And web browser is at e-shop's "Macs" category inside "Laptops & Notebooks"
    When user clicks on "MacBook"
    Then "MacBook" product page is opened