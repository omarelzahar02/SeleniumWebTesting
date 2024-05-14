Feature: Reset

    Scenario: Successful Reset
        Given I am logged in
        And I add an item to the shopping cart
        Then A remove button appears on that item
        When I click on the more options button
        Then Reset button should be visible
        When I click on the Reset button
        Then No Remove buttons are visible
        And No number on shopping cart
        When I open the shopping cart
        Then I should see no items