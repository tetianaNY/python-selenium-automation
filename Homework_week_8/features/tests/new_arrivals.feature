# Created by tetyanakuzmyma at 3/13/20
Feature: Tests for product page

  Scenario: Size tooltip is shown upon hovering over Add to the Cart Button
    Given Open amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify user sees a deal