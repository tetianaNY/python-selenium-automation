# Created by tetyanakuzmyna at 2/14/20
Feature: History book count scenario


  Scenario: User search books and count result on search page
    Given Open Amazon website
    When Input history book
    And Search history books
    Then Count result