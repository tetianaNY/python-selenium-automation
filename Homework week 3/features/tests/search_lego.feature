# Created by tetyanakuzmyna at 2/1/20
Feature: Lego search

  # Enter feature description here
  Scenario: Find header on the search result page
  # Enter steps here
  Given Open Amazon main page
  When Search input fill Cars
  And Click on search button
  Then Assert Cars in header on the page

