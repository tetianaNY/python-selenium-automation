# Created by tetyanakuzmyna at 3/13/20
Feature: select and search training


  Scenario: We can choose select category
    Given Open Amzn main page
    When Select Video Games options
    And Looking for pacman
    Then Our searching will be in Video Games category