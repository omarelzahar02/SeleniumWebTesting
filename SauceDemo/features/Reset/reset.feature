# User Story 1:  Successful Reset of App
# As a registered user, I want to be able to reset my shopping cart so that I can remove all items from it at once.

# Acceptance Criteria:
# 1. When I am logged in and I add an item to the shopping cart, a remove button should appear on that item.
# 2. When I click on the more options button, a Reset button should be visible.
# 3. When I click on the Reset button, no Remove buttons should be visible and there should be no number on the shopping cart.
# 4. When I open the shopping cart, I should see no items.


Feature: Reset

    User Story 1: Successful Reset of App
    As a registered user, 
    I want to be able to reset my shopping cart 
    so that I can remove all items from it at once.
    definition of done: no items selected in the shopping cart and empty shopping cart

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