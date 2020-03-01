# Created by tetyanakuzmyna at 3/1/20
Feature: Test scenario for tooltip
  # Enter feature description here

  Scenario: Check when tooltip will be hide
    Given Open Amz page
    When Sign in tooltip is clickable
    When Sign in tooltip will be hide
    Then Tooltip is not clickable


    # Enter steps here