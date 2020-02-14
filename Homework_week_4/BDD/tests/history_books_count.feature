# Created by tetyanakuzmyna at 2/14/20
Feature: History book count


  Scenario: User search books and count result on search page
    Given Open Amazon website
    When Input history book
    And Search history books
    Then Count result
    And Add first book to the cart if price more than 10 dollars
