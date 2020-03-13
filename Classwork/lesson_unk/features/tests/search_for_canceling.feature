# Created by tetyanakuzmyna at 2/1/20
Feature: Cancel Order search

  Scenario: User can search for Cancelling an order on Amazon
    Given Open Amazon help
    When Search input enter Cancel Order
    And Click on search
    Then Find Cancel Order on the page
