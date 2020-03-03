# Created by tetyanakuzmyna at 3/3/20
Feature: Loops

  Scenario: Click on each top link and verify their
    Given Amazon webpage
    When Click on best sellers
    Then Click on each top link and verify that new pages open
