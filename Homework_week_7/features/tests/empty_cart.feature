# Created by tetyanakuzmyna at 3/5/20
Feature: Page Object training

Scenario: Your Shopping Cart is empty' shown if no product added
 Given Open Amzo page
 When Click on cart icon
 Then Verify Your Amazon cart is empty text present