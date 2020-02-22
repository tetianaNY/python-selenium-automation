# Created by tetyanakuzmyna at 2/22/20
Feature: Count best sellers in the "Fantasy book" search result
  # Enter feature description here

  Scenario: Count all best sellers
    Given Open Amazon page
    When Search Fantasy book
    Then Counting best sellers
