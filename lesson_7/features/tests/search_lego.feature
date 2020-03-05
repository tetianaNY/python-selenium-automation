# Created by tetyanakuzmyna at 2/1/20
Feature: Lego search


#  Scenario: Find header on the search result page
#    Given Open Amazon main page
#    When Search input fill lego
#    Then Assert "lego" in header on the page

  Scenario Outline: Find header on the search result page
    Examples:
    |search_word      |expected_search_result     |
    |dress            |"dress"                    |
    |toys             |"toys"                     |



    Given Open Amazon main page
    When Search input fill <search_word>
    Then Assert <expected_search_result> in header on the page

