# Created by tetyanakuzmyna at 3/1/20
Feature: User can manipulate with windows and tabs


  Scenario: User can open and close Today's deal under $25
    Given Open Amzon page
    When Store original window
    And Click to blog link
    And Switch to the newly opened window
    Then Check this page has https://blog.aboutamazon.com/sustainability
    And User can close new window and switch back to original

    # Enter steps here