# Created by tetyanakuzmyna at 2/14/20
Feature: Test cart scenario


  Scenario: User get good, and check this item in the cart
    Given Open Amazon website
    When Search input and fill Iphone Xs Case
    And Click a search button
    And Choose the first item
    And Add good to cart
    When Click cart icon
    Then Check 1 item in the cart
