# Created by tetyanakuzmyna at 3/5/20
Feature: HomeDepot project


#  Scenario Outline: Verify that Auto-suggestion works
#    Examples:
#    |search_word      |
#    |hammer           |
#    |plier            |
#    |pry bar          |
#    |lawn mower       |
#
#
#    Given Open HomeDepot page
#    When Enter <search_word> to the search box
#    Then Count <search_word> on the page
#
#  Scenario: User is taken to the search results page
#    Given Open HomeDepot page
#    When Insert dry vacuum in search field
#    And Click search button or click enter button
#    Then Expect to see the search results page. Check that title is relevant to "dry vacuum"

#  Scenario: Verify that Registration flow works as expected
#    Given Open HomeDepot page
#    When Click account button
#    And Click "register" button
#    And Fill all fields with fake data
#    And Click submit registration form
#    Then Expected registration will be complete successfully


#  Scenario: Verify that Sign-In with existing account works
#    Given Open HomeDepot page
#    When Click account button
#    And Fill data from prev step
#    And Click sign_in button
#    Then Expected login will be complete successfully


#  Scenario: Shopping cart - empty state
#    Given Open HomeDepot page
#    When Click HomeDepot cart button
#    Then Expected cart page will have empty in the title


  Scenario:
    Given Open HomeDepot page
    When Insert circular saw in search field
    And On search results page choose something and click it
    And Add product to shopping cart
    Then Expected product would be in cart
    And Close all pop-ups



