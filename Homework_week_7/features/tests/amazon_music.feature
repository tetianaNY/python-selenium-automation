# Created by tetyanakuzmyna at 3/5/20
Feature: Page Object training

Scenario: Amazon Music has 6 menu items
  Given Open Amzo page
  When Click on hamburger menu
  And Click on Amazon Music menu item
  Then 6 menu items are present


