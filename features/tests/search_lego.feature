# Created by alexeygerasimov at 1/26/20
Feature: Lego search
  # Enter feature description here

  Scenario: Find header on the search result page
  Given Open Amazon main page
  When Search input fill Cars
  And Click on search button
  Then Open goods page
  And Assert Cars in header on the page

    # Enter steps here