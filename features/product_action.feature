Feature: Product actions
  Background:
    Given "MacBook" product is available on e-shop

  Scenario: add product to wish list
    Given a web browser is at e-shop "MacBook" product page
    And user is logged in
    When user clicks on the "Add to Wish List" button
    Then product is added into his wish list


  Scenario: compare product
    Given a web browser is at e-shop "MacBook" product page
    When user clicks on the "Compare this Product" button
    Then product is added into his product comparison


