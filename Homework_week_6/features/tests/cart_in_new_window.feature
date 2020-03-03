# Created by tetyanakuzmyna at 3/1/20
Feature: Feature: User can manipulate with windows and add goods to the cart


  Scenario: User should choose a good, open the new window, and add to the cart
    Given Open Amazon page and store it
    When Click to the blog link, switch windows, and click to the amazon link
    And Open deal of the day, choose first item
    Then Add goods to the cart
    And Switch back to original
    And Check goods in he cart
