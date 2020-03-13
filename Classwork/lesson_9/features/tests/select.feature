# Created by tetyanakuzmyna at 3/11/20
Feature: Test our select


  Scenario: We can choose select category
    Given Open Amzn main page
    When Select Electronics options
    And Looking for coffee pot
    Then Our searching will be in Electronics category
