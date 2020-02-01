# Created by tetyanakuzmyna at 2/1/20
Feature: Cancel Order search
  # Enter feature description here

  Scenario: User can search for Cancelling an order on Amazon
  Given Open Amazon main page
  When Search input fill Cancel Order
  And Click on search button
  Then Assert Cancel Order in header on the page
    # Enter steps here