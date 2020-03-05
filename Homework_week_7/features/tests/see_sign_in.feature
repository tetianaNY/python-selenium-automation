# Created by tetyanakuzmyna at 3/5/20
Feature: Page Object training

Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amzo page
 When Click Amazon Orders link
 Then Verify Sign-In page is opened