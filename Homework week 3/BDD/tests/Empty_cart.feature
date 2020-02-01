# Created by tetyanakuzmyna at 2/1/20
Feature: Empty cart check

  Scenario: Check shopping cart on the website
    Given Open Amazon
    When Search cart on the website and click
    Then Check Your Shopping Cart is empty on the page
